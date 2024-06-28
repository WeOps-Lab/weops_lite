import json

from apps.cmdb_mgmt.constants import MODEL, MODEL_ASSOCIATION, INSTANCE, INST_NAME_INFOS, CREATE_MODEL_CHECK_ATTR, \
    UPDATE_MODEL_CHECK_ATTR_MAP, ORGANIZATION, USER, BASE, CREDENTIAL
from apps.cmdb_mgmt.messages import EDGE_REPETITION, MODEL_EDGE_REPETITION, MODEL_NOT_PRESENT, MODEL_ATTR_NOT_PRESENT, \
    MODEL_ATTR_PRESENT, EXIST_MODEL_EDGE, EXIST_MODEL_INST
from apps.cmdb_mgmt.utils.ag import AgUtils
from apps.core.exceptions.base_app_exception import BaseAppException
from apps.system_mgmt.services.group_manage import GroupManage
from apps.system_mgmt.services.user_manage import UserManage


class ModelManage(object):
    @staticmethod
    def create_model(data: dict):
        """
            创建模型
        """
        # 对模型初始化默认属性实例名称
        data.update(attrs=json.dumps(INST_NAME_INFOS))

        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(MODEL, [])
            result = ag.create_entity(MODEL, data, CREATE_MODEL_CHECK_ATTR, exist_items)
        return result

    @staticmethod
    def delete_model(id: int):
        """
            删除模型
        """
        with AgUtils() as ag:
            ag.batch_delete_entity(MODEL, [id])

    @staticmethod
    def update_model(id: int, data: dict):
        """
            更新模型
        """
        model_id = data.pop("model_id", "")    # 不能更新model_id
        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(MODEL, [{"field": "model_id", "type": "str<>", "value": model_id}])
            model = ag.set_entity_properties(MODEL, [id], data, UPDATE_MODEL_CHECK_ATTR_MAP, exist_items)
        return model[0]

    @staticmethod
    def search_model(model_type=None):
        """
            查询模型分类
        """
        with AgUtils() as ag:
            models, _ = ag.query_entity(MODEL, [])
        if model_type:
            return [i for i in models if i.get("model_type", BASE) == model_type]
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
                raise BaseAppException(MODEL_NOT_PRESENT)
            model_info = models[0]
            attrs = ModelManage.parse_attrs(model_info.get("attrs", "[]"))
            if attr_info["attr_id"] in {i["attr_id"] for i in attrs}:
                raise BaseAppException(MODEL_ATTR_PRESENT)
            attrs.append(attr_info)
            result = ag.set_entity_properties(MODEL, [model_info["_id"]], dict(attrs=json.dumps(attrs)), {}, [], False)

        attrs = ModelManage.parse_attrs(result[0].get("attrs", "[]"))

        attr = None
        for attr in attrs:
            if attr["attr_id"] != attr_info["attr_id"]:
                continue
            attr = attr

        return attr

    @staticmethod
    def update_model_attr(model_id, attr_info):
        """
            更新模型属性
        """
        with AgUtils() as ag:
            model_query = {"field": "model_id", "type": "str=", "value": model_id}
            models, model_count = ag.query_entity(MODEL, [model_query])
            if model_count == 0:
                raise BaseAppException(MODEL_NOT_PRESENT)
            model_info = models[0]
            attrs = ModelManage.parse_attrs(model_info.get("attrs", "[]"))
            if attr_info["attr_id"] not in {i["attr_id"] for i in attrs}:
                raise BaseAppException(MODEL_ATTR_NOT_PRESENT)
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

            result = ag.set_entity_properties(MODEL, [model_info["_id"]], dict(attrs=json.dumps(attrs)), {}, [], False)

        attrs = ModelManage.parse_attrs(result[0].get("attrs", "[]"))

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
                raise BaseAppException(MODEL_NOT_PRESENT)
            model_info = models[0]
            attrs = ModelManage.parse_attrs(model_info.get("attrs", "[]"))
            new_attrs = [attr for attr in attrs if attr["attr_id"] != attr_id]
            result = ag.set_entity_properties(MODEL, [model_info["_id"]], dict(attrs=json.dumps(new_attrs)), {}, [], False)

            # 模型属性删除后，要删除对应模型实例的属性
            model_params = [{"field": "model_id", "type": "str=", "value": model_id}]
            ag.remove_entitys_properties(INSTANCE, model_params, [attr_id])

        return ModelManage.parse_attrs(result[0].get("attrs", "[]"))

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
    def get_organization_option(items: list, result: list):
        for item in items:
            result.append(dict(
                id=item["id"],
                name=item["path"],
                is_default=False,
                type="str",
            ))
            if item["subGroups"]:
                ModelManage.get_organization_option(item["subGroups"], result)

    @staticmethod
    def search_model_attr(model_id: str):
        """
            查询模型属性
        """
        model_info = ModelManage.search_model_info(model_id)
        attrs = ModelManage.parse_attrs(model_info.get("attrs", "[]"))
        return attrs

    @staticmethod
    def search_model_attr_v2(model_id: str):
        """
            查询模型属性
        """
        model_info = ModelManage.search_model_info(model_id)
        attrs = ModelManage.parse_attrs(model_info.get("attrs", "[]"))
        for attr in attrs:
            if attr["attr_type"] == ORGANIZATION:
                group = GroupManage().group_list()
                option = []
                ModelManage.get_organization_option(group, option)
                attr.update(option=option)
                continue

            if attr["attr_type"] == USER:
                users = UserManage().user_all()
                option = [
                    dict(
                        id=user["username"],
                        name=user["lastName"],
                        is_default=False,
                        type="str",
                    )
                    for user in users]
                attr.update(option=option)
                continue

        return attrs

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
                else:
                    raise BaseAppException(e.message)
        return edge

    @staticmethod
    def model_association_delete(id: int):
        """
            删除模型关联
        """
        with AgUtils() as ag:
            ag.delete_edge(id)

    @staticmethod
    def model_association_info_search(model_asst_id: str):
        """
            查询模型关联详情
        """
        with AgUtils() as ag:
            query_data = {"field": "model_asst_id", "type": "str=", "value": model_asst_id}
            edges, _ = ag.query_edge(MODEL_ASSOCIATION, [query_data])
        if len(edges) == 0:
            return {}
        return edges[0]

    @staticmethod
    def model_association_search(model_id: str, model_type=None):
        """
            查询模型所有的关联
        """
        query_list = [
            {"field": "src_model_id", "type": "str=", "value": model_id},
            {"field": "dst_model_id", "type": "str=", "value": model_id}
        ]
        with AgUtils() as ag:
            edges, _ = ag.query_edge(MODEL_ASSOCIATION, query_list, param_type="OR")

        # 根据模型类型过滤模型关联
        if model_type:
            models = ModelManage.search_model(CREDENTIAL)
            models_set = {i["model_id"] for i in models}
            if model_type == CREDENTIAL:
                edges = [i for i in edges if i["src_model_id"] in models_set or i["dst_model_id"] in models_set]
            else:
                edges = [i for i in edges if i["src_model_id"] not in models_set and i["dst_model_id"] not in models_set]

        return edges

    @staticmethod
    def check_model_exist_association(model_id):
        """模型存在关联关系"""
        edges = ModelManage.model_association_search(model_id)
        if edges:
            raise BaseAppException(EXIST_MODEL_EDGE)

    @staticmethod
    def check_model_exist_inst(model_id):
        """模型存在实例"""
        params = [{"field": "model_id", "type": "str=", "value": model_id}]
        with AgUtils() as ag:
            _, count = ag.query_entity(INSTANCE, params, page=dict(skip=0, limit=1))
        if count > 0:
            raise BaseAppException(EXIST_MODEL_INST)
