import json

from apps.cmdb_mgmt.constants import MODEL, MODEL_ASSOCIATION, INSTANCE
from apps.cmdb_mgmt.utils.ag import AgUtils
from apps.core.exceptions.base_app_exception import BaseAppException


class ModelManage(object):
    @staticmethod
    def create_model(data: dict):
        """
            创建模型
        """
        ag = AgUtils()
        result = ag.create_entity(MODEL, data, "model_name")
        ag.con.close()
        return result

    @staticmethod
    def delete_model(id: int):
        """
            删除模型
        """
        ag = AgUtils()
        ag.delete_entity(MODEL, id)
        ag.con.close()

    @staticmethod
    def search_model():
        """
            查询模型分类
        """
        ag = AgUtils()
        models, _ = ag.query_entity(MODEL, [])
        ag.con.close()
        return models

    @staticmethod
    def parse_attrs(attrs: str):
        return json.loads(attrs.replace('\\"', '"'))

    @staticmethod
    def create_model_attr(model_id, attr_info):
        """
            创建模型属性
        """
        ag = AgUtils()
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
        ag.con.close()

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
        ag = AgUtils()
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

        ag.con.close()
        return ModelManage.parse_attrs(result.get("attrs", "[]"))

    @staticmethod
    def search_model_info(model_id: str):
        """
            查询模型详情
        """
        query_data = {"field": "model_id", "type": "str=", "value": model_id}
        ag = AgUtils()
        models, _ = ag.query_entity(MODEL, [query_data])
        ag.con.close()
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
        ag = AgUtils()
        edge = ag.create_edge(MODEL_ASSOCIATION, data["src_id"], MODEL, data["dst_id"], MODEL, data)
        return edge

    @staticmethod
    def model_association_delete(id: int):
        """
            删除模型关联
        """
        ag = AgUtils()
        ag.delete_edge(MODEL_ASSOCIATION, id)
        ag.con.close()

    @staticmethod
    def model_association_info_search(model_asst_id: str):
        """
            查询模型关联详情
        """
        ag = AgUtils()
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
        ag = AgUtils()
        # 作为源模型
        src_query_data = {"field": "src_model_id", "type": "str=", "value": model_id}
        src_edge, _ = ag.query_edge(MODEL_ASSOCIATION, MODEL, MODEL, [src_query_data])

        # 作为目标模型
        dst_query_data = {"field": "dst_model_id", "type": "str=", "value": model_id}
        dst_edge, _ = ag.query_edge(MODEL_ASSOCIATION, MODEL, MODEL, [dst_query_data])
        return src_edge + dst_edge
