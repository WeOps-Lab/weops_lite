import json

from apps.cmdb_mgmt.constants import MODEL, MODEL_ASSOCIATION, INSTANCE, INST_NAME_INFO, CREATE_MODEL_CHECK_ATTR, \
    UPDATE_MODEL_CHECK_ATTR_MAP
from apps.cmdb_mgmt.messages import EDGE_REPETITION, MODEL_EDGE_REPETITION
from apps.cmdb_mgmt.utils.ag import AgUtils
from apps.core.exceptions.base_app_exception import BaseAppException


class ModelManage(object):
    @staticmethod
    def create_model(data: dict):
        """
            创建模型
        """
        # 对模型初始化默认属性实例名称
        data.update(attrs=json.dumps([INST_NAME_INFO]))

        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(MODEL, [])
            result = ag.create_entity(MODEL, data, CREATE_MODEL_CHECK_ATTR, exist_items)
        return result

    @staticmethod
    def delete_model(id: int):
        """
            删除模型
        """

        # TODO 校验是否存在模型关联
        # TODO 校验是否存在模型实例

        with AgUtils() as ag:
            ag.delete_entity(MODEL, id)

    @staticmethod
    def update_model(id: int, data: dict):
        """
            更新模型
        """
        data.pop("model_id", "")    # 不能更新model_id
        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(MODEL, [])
            model = ag.set_entity_properties(MODEL, id, data, UPDATE_MODEL_CHECK_ATTR_MAP, exist_items)
        return model

    @staticmethod
    def search_model():
        """
            查询模型分类
        """
        with AgUtils() as ag:
            models, _ = ag.query_entity(MODEL, [])
        return models

    @staticmethod
    def parse_attrs(attrs: str):
        return json.loads(attrs.replace('\\"', '"'))

    @staticmethod
    def create_model_attr(model_id, attr_info):
        """
            创建模型属性
        """
        with AgUtils() as ag:
            model_query = {"field": "model_id", "type": "str=", "value": model_id}
            models, model_count = ag.query_entity(MODEL, [model_query])
            if model_count == 0:
                raise BaseAppException("模型不存在！")
            model_info = models[0]
            attrs = ModelManage.parse_attrs(model_info.get("attrs", "[]"))
            if attr_info["attr_id"] in {i["attr_id"] for i in attrs}:
                raise BaseAppException("属性ID已存在！")
            attrs.append(attr_info)
            result = ag.set_entity_properties(MODEL, model_info["_id"], dict(attrs=json.dumps(attrs)))

        attrs = ModelManage.parse_attrs(result.get("attrs", "[]"))

        attr = None
        for attr in attrs:
            if attr["attr_id"] != attr_info["attr_id"]:
                continue
            attr = attr

        return attr

    @staticmethod
    def update_model_attr(model_id, attr_info):
        """
            创建模型属性
        """
        with AgUtils() as ag:
            model_query = {"field": "model_id", "type": "str=", "value": model_id}
            models, model_count = ag.query_entity(MODEL, [model_query])
            if model_count == 0:
                raise BaseAppException("模型不存在！")
            model_info = models[0]
            attrs = ModelManage.parse_attrs(model_info.get("attrs", "[]"))
            if attr_info["attr_id"] not in {i["attr_id"] for i in attrs}:
                raise BaseAppException("属性不存在！")
            for attr in attrs:
                if attr_info["attr_id"] != attr["attr_id"]:
                    continue
                attr.update(
                    attr_group=attr_info["attr_group"],
                    attr_name=attr_info["attr_name"],
                    is_required=attr_info["is_required"],
                    editable=attr_info["editable"],
                    option=attr_info["option"],
                )

            result = ag.set_entity_properties(MODEL, model_info["_id"], dict(attrs=json.dumps(attrs)))

        attrs = ModelManage.parse_attrs(result.get("attrs", "[]"))

        attr = None
        for attr in attrs:
            if attr["attr_id"] != attr_info["attr_id"]:
                continue
            attr = attr

        return attr

    @staticmethod
    def delete_model_attr(model_id: str, attr_id: str):
        """
            删除模型属性
        """
        with AgUtils() as ag:
            model_query = {"field": "model_id", "type": "str=", "value": model_id}
            models, model_count = ag.query_entity(MODEL, [model_query])
            if model_count == 0:
                raise BaseAppException("模型不存在！")
            model_info = models[0]
            attrs = ModelManage.parse_attrs(model_info.get("attrs", "[]"))
            new_attrs = [attr for attr in attrs if attr["attr_id"] != attr_id]
            result = ag.set_entity_properties(MODEL, model_info["_id"], dict(attrs=json.dumps(new_attrs)))

            # 模型属性删除后，要删除对应模型实例的属性
            model_params = [{"field": "model_id", "type": "str=", "value": model_id}]
            ag.remove_entitys_properties(INSTANCE, model_params, [attr_id])

        return ModelManage.parse_attrs(result.get("attrs", "[]"))

    @staticmethod
    def search_model_info(model_id: str):
        """
            查询模型详情
        """
        query_data = {"field": "model_id", "type": "str=", "value": model_id}
        with AgUtils() as ag:
            models, _ = ag.query_entity(MODEL, [query_data])
        if len(models) == 0:
            return {}
        return models[0]

    @staticmethod
    def search_model_attr(model_id: str):
        """
            查询模型属性
        """
        model_info = ModelManage.search_model_info(model_id)
        return ModelManage.parse_attrs(model_info.get("attrs", "[]"))

    @staticmethod
    def model_association_create(**data):
        """
            创建模型关联
        """
        with AgUtils() as ag:
            try:
                edge = ag.create_edge(MODEL_ASSOCIATION, data["src_id"], MODEL, data["dst_id"], MODEL, data, "model_asst_id")
            except BaseAppException as e:
                if e.message == EDGE_REPETITION:
                    raise BaseAppException(MODEL_EDGE_REPETITION)
        return edge

    @staticmethod
    def model_association_delete(id: int):
        """
            删除模型关联
        """
        with AgUtils() as ag:
            ag.delete_edge(MODEL_ASSOCIATION, id)

    @staticmethod
    def model_association_info_search(model_asst_id: str):
        """
            查询模型关联详情
        """
        with AgUtils() as ag:
            query_data = {"field": "model_asst_id", "type": "str=", "value": model_asst_id}
            edges, _ = ag.query_edge(MODEL_ASSOCIATION, MODEL, MODEL, [query_data])
        if len(edges) == 0:
            return {}
        return edges[0]

    @staticmethod
    def model_association_search(model_id: str):
        """
            查询模型所有的关联
        """
        with AgUtils() as ag:
            # 作为源模型
            src_query_data = {"field": "src_model_id", "type": "str=", "value": model_id}
            src_edge, _ = ag.query_edge(MODEL_ASSOCIATION, MODEL, MODEL, [src_query_data])

            # 作为目标模型
            dst_query_data = {"field": "dst_model_id", "type": "str=", "value": model_id}
            dst_edge, _ = ag.query_edge(MODEL_ASSOCIATION, MODEL, MODEL, [dst_query_data])
        return src_edge + dst_edge
