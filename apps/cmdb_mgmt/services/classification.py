from apps.cmdb_mgmt.constants import CLASSIFICATION, MODEL, CREATE_CLASSIFICATION_CHECK_ATTR_MAP, \
    UPDATE_CLASSIFICATION_check_attr_map
from apps.cmdb_mgmt.utils.ag import AgUtils
from apps.core.exceptions.base_app_exception import BaseAppException


class ClassificationManage(object):

    @staticmethod
    def create_model_classification(data: dict):
        """
            创建模型分类
        """
        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(CLASSIFICATION, [])
            result = ag.create_entity(CLASSIFICATION, data, CREATE_CLASSIFICATION_CHECK_ATTR_MAP, exist_items)
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
    def check_classification_is_used(classification_id):
        """校验模型分类是否已经使用"""
        with AgUtils() as ag:
            model_query = {"field": "classification_id", "type": "str=", "value": classification_id}
            _, model_count = ag.query_entity(MODEL, [model_query])
            if model_count > 0:
                raise BaseAppException("模型分类已使用！")

    @staticmethod
    def delete_model_classification(id: int):
        """
            删除模型分类
        """
        with AgUtils() as ag:
            ag.delete_entity(CLASSIFICATION, id)

    @staticmethod
    def update_model_classification(id: int, data: dict):
        """
            更新模型分类
        """
        # 不能更新classification_id
        data.pop("classification_id", "")
        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(CLASSIFICATION, [])
            exist_items = [i for i in exist_items if i["_id"] != id]
            model = ag.set_entity_properties(CLASSIFICATION, id, data, UPDATE_CLASSIFICATION_check_attr_map, exist_items)
        return model

    @staticmethod
    def search_model_classification():
        """
            查询模型分类
        """
        with AgUtils() as ag:
            classifications, _ = ag.query_entity(CLASSIFICATION, [])
        return classifications
