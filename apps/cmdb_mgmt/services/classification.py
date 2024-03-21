from apps.cmdb_mgmt.constants import CLASSIFICATION
from apps.cmdb_mgmt.utils.ag import AgUtils


class ClassificationManage(object):

    @staticmethod
    def create_model_classification(data: dict):
        """
            创建模型分类
        """
        with AgUtils() as ag:
            result = ag.create_entity(CLASSIFICATION, data, "classification_name")
        return result

    @staticmethod
    def search_model_classification_info(classification_id: str):
        """
            查询模型分类属性
        """
        query_data = {"field": "classification_id", "type": "str=", "value": classification_id}
        with AgUtils() as ag:
            models, _ = ag.query_entity(CLASSIFICATION, [query_data])
        if len(models) == 0:
            return {}
        return models[0]

    @staticmethod
    def delete_model_classification(id: int):
        """
            删除模型分类
        """
        with AgUtils() as ag:
            ag.delete_entity(CLASSIFICATION, id)

    @staticmethod
    def search_model_classification():
        """
            查询模型分类
        """
        with AgUtils() as ag:
            classifications, _ = ag.query_entity(CLASSIFICATION, [])
        return classifications
