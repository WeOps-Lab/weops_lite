from apps.cmdb_mgmt.constants import CLASSIFICATION
from apps.cmdb_mgmt.utils.ag import AgUtils


class ClassificationManage(object):

    @staticmethod
    def create_model_classification(data: dict):
        """
            创建模型分类
        """
        ag = AgUtils()
        result = ag.create_entity(CLASSIFICATION, data, "classification_name")
        ag.con.close()
        return result.get("properties", {})

    @staticmethod
    def search_model_classification_info(classification_id: str):
        """
            查询模型分类属性
        """
        query_data = {"field": "classification_id", "type": "str=", "value": classification_id}
        ag = AgUtils()
        models, _ = ag.query_entity(CLASSIFICATION, [query_data])
        ag.con.close()
        if len(models) == 0:
            return {}
        return models[0]

    @staticmethod
    def delete_model_classification(id: int):
        """
            删除模型分类
        """
        ag = AgUtils()
        ag.delete_entity(CLASSIFICATION, id)
        ag.con.close()

    @staticmethod
    def search_model_classification():
        """
            查询模型分类
        """
        ag = AgUtils()
        classifications, _ = ag.query_entity(CLASSIFICATION, [])
        ag.con.close()
        return [i.get("properties", {}) for i in classifications]
