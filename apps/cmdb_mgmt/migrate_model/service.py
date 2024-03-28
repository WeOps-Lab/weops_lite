from apps.cmdb_mgmt.constants import CLASSIFICATION, MODEL, CREATE_CLASSIFICATION_CHECK_ATTR_MAP, \
    CREATE_MODEL_CHECK_ATTR, MODEL_ASSOCIATION
from apps.cmdb_mgmt.migrate_model.constants import CLASSIFICATIONS, MODELS, ASSOCIATIONS
from apps.cmdb_mgmt.utils.ag import AgUtils


class MigrateModel:
    def run(self):
        classification_resp = self.migrate_classifications()
        model_resp = self.migrate_models()
        association_resp = self.migrate_associations()
        return dict(classification=classification_resp, model=model_resp, association=association_resp)

    def migrate_classifications(self):
        """初始化模型分类"""
        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(CLASSIFICATION, [])
            result = ag.batch_create_entity(CLASSIFICATION, CLASSIFICATIONS, CREATE_CLASSIFICATION_CHECK_ATTR_MAP, exist_items)
        return result

    def migrate_models(self):
        """初始化模型"""
        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(MODEL, [])
            result = ag.batch_create_entity(MODEL, MODELS, CREATE_MODEL_CHECK_ATTR, exist_items)
        return result

    def migrate_associations(self):
        """初始模型关联"""
        with AgUtils() as ag:
            models, _ = ag.query_entity(MODEL, [])
            model_map = {i["model_id"]: i["_id"] for i in models}
            associations = [
                dict(
                    dst_id=model_map.get(i["dst_model_id"]),
                    src_id=model_map.get(i["src_model_id"]),
                    **i)
                for i in ASSOCIATIONS
            ]
            result = ag.batch_create_edge(MODEL_ASSOCIATION, MODEL, MODEL, associations)
        return result
