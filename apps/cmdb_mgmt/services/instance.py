from apps.cmdb_mgmt.constants import INSTANCE, INSTANCE_ASSOCIATION
from apps.cmdb_mgmt.services.model import ModelManage
from apps.cmdb_mgmt.utils.ag import AgUtils
from apps.core.exceptions.base_app_exception import BaseAppException


class InstanceManage(object):

    @staticmethod
    def instance_list(model_id: str, params: list, page: int, page_size: int, order: str):
        """实例列表"""
        _page = dict(skip=(page - 1) * page_size, limit=page_size)
        if order and order.startswith("-"):
            order = f"{order.replace('-', '')} DESC"
        params.append({"field": "model_id", "type": "str=", "value": model_id})
        with AgUtils() as ag:
            inst_list, count = ag.query_entity(INSTANCE, params, page=_page, order=order)
        return inst_list, count

    @staticmethod
    def instance_create(model_id: str, instance_info: dict):
        """创建实例"""
        instance_info.update(model_id=model_id)
        attrs = ModelManage.search_model_attr(model_id)
        check_attr_map = dict(is_only={}, is_required={})
        for attr in attrs:
            if attr["is_only"]:
                check_attr_map["is_only"][attr["attr_id"]] = attr["attr_name"]
            if attr["is_required"]:
                check_attr_map["is_required"][attr["attr_id"]] = attr["attr_name"]

        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(INSTANCE, [{"field": "model_id", "type": "str=", "value": model_id}])
            result = ag.create_entity(INSTANCE, instance_info, check_attr_map, exist_items)
        return result

    @staticmethod
    def instance_update(inst_id: int, update_attr: dict):
        """修改实例属性"""
        inst_info = InstanceManage.query_entity_by_id(inst_id)
        attrs = ModelManage.search_model_attr(inst_info["model_id"])
        check_attr_map = dict(is_only={}, is_required={}, editable={})
        for attr in attrs:
            if attr["is_only"]:
                check_attr_map["is_only"][attr["attr_id"]] = attr["attr_name"]
            if attr["is_required"]:
                check_attr_map["is_required"][attr["attr_id"]] = attr["attr_name"]
            if attr["editable"]:
                check_attr_map["editable"][attr["attr_id"]] = attr["attr_name"]

        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(INSTANCE, [{"field": "model_id", "type": "str=", "value": inst_info["model_id"]}])
            exist_items = [i for i in exist_items if i["_id"] != inst_id]
            result = ag.set_entity_properties(INSTANCE, inst_id, update_attr, check_attr_map, exist_items)
        return result

    @staticmethod
    def instance_batch_delete(inst_ids: list):
        """批量删除实例"""
        with AgUtils() as ag:
            ag.batch_delete_entity(INSTANCE, inst_ids)

    @staticmethod
    def instance_association_instance_list(model_id: str, inst_id: int):
        """查询模型实例关联的实例列表"""
        with AgUtils() as ag:

            # 作为源模型实例
            src_query_data = [
                {"field": "src_inst_id", "type": "int=", "value": inst_id},
                {"field": "src_model_id", "type": "str=", "value": model_id},
            ]
            src_edge, _ = ag.query_edge(INSTANCE_ASSOCIATION, INSTANCE, INSTANCE, src_query_data, return_entity=True)

            # 作为目标模型实例
            dst_query_data = [
                {"field": "dst_inst_id", "type": "int=", "value": inst_id},
                {"field": "dst_model_id", "type": "str=", "value": model_id},
            ]
            dst_edge, _ = ag.query_edge(INSTANCE_ASSOCIATION, INSTANCE, INSTANCE, dst_query_data, return_entity=True)

        result = {}
        for item in src_edge + dst_edge:
            model_asst_id = item["edge"]["model_asst_id"]
            item_key = "src" if model_id == item["edge"]["dst_model_id"] else "dst"
            if model_asst_id not in result:
                result[model_asst_id] = {
                    "src_model_id": item["edge"]["src_model_id"],
                    "dst_model_id": item["edge"]["dst_model_id"],
                    "model_asst_id": item["edge"]["model_asst_id"],
                    "inst_list": [],
                }
            result[model_asst_id]["inst_list"].append(item[item_key])

        return list(result.values())

    @staticmethod
    def instance_association_list(params: dict):
        """查询实例与某个模型的关联"""
        if not params:
            raise BaseAppException("缺少查询条件！")

        query_list = []
        for k, v in params.items():
            _type = "int=" if k in {"src_inst_id", "dst_inst_id"} else "str="
            query_list.append({"field": k, "type": _type, "value": v})

        with AgUtils() as ag:
            edges, _ = ag.query_edge(INSTANCE_ASSOCIATION, INSTANCE, INSTANCE, query_list)

        return edges

    @staticmethod
    def instance_association_create(data: dict):
        """创建实例关联"""
        with AgUtils() as ag:
            edge = ag.create_edge(INSTANCE_ASSOCIATION, data["src_inst_id"], INSTANCE, data["dst_inst_id"], INSTANCE, data)
        return edge

    @staticmethod
    def instance_association_delete(asso_id: int):
        """删除实例关联"""
        with AgUtils() as ag:
            ag.delete_edge(INSTANCE_ASSOCIATION, asso_id)

    @staticmethod
    def instance_association_by_asso_id(asso_id: int):
        """根据关联ID查询实例关联"""
        with AgUtils() as ag:
            edge = ag.query_edge_by_id(INSTANCE_ASSOCIATION, asso_id, return_entity=True)
        return edge

    @staticmethod
    def query_entity_by_id(inst_id: int):
        """根据实例ID查询实例详情"""
        with AgUtils() as ag:
            entity = ag.query_entity_by_id(INSTANCE, inst_id)
        return entity
