from apps.resource.constants import CLASSIFICATION, MODEL
from apps.resource.utils.ag import AgUtils


class ModelManage(object):

    @staticmethod
    def create_model_classification(data: dict):
        """
            创建模型分类
        """
        ag = AgUtils()
        result = ag.create_entity(CLASSIFICATION, data, "classification_name")
        ag.con.close()
        return result

    @staticmethod
    def delete_model_classification(classification_id):
        """
            删除模型分类
        """
        ag = AgUtils()
        ag.delete_entity(CLASSIFICATION, classification_id)
        ag.con.close()

    @staticmethod
    def create_model(data):
        """
            创建模型
        """
        ag = AgUtils()
        result = ag.create_entity(MODEL, data, "model_name")
        ag.con.close()
        return result

    @staticmethod
    def delete_model(model_id):
        """
            删除模型
        """
        ag = AgUtils()
        ag.delete_entity(CLASSIFICATION, model_id)
        ag.con.close()

    @staticmethod
    def create_model_attr(model_id, attr_info):
        """
            创建模型属性
        """
        ag = AgUtils()
        model_query = {"field": "model_id", "type": "str=", "value": model_id}
        models, model_count = ag.query_entity(MODEL, [model_query])
        if model_count == 0:
            raise Exception("模型不存在！")
        model_info = models[0]
        attrs = model_info["properties"].get("attrs", [])
        if attr_info["attr_id"] in {i["attr_id"] for i in attrs}:
            raise Exception("属性ID已存在！")
        attrs.append(attr_info)
        result = ag.set_entity_properties(MODEL, model_info["id"], dict(attrs=attrs))
        ag.con.close()
        return result

    @staticmethod
    def delete_model_attr(model_id, attr_id):
        """
            删除模型属性
        """
        ag = AgUtils()
        model_query = {"field": "model_id", "type": "str=", "value": model_id}
        models, model_count = ag.query_entity(MODEL, [model_query])
        if model_count == 0:
            raise Exception("模型不存在！")
        model_info = models[0]
        attrs = model_info["properties"].get("attrs", [])
        new_attrs = [attr for attr in attrs if attr["attr_id"] != attr_id]
        result = ag.set_entity_properties(MODEL, model_info["id"], dict(attrs=new_attrs))
        ag.con.close()
        return result
