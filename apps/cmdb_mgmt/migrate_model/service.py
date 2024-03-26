from apps.cmdb_mgmt.constants import CLASSIFICATION, MODEL
from apps.cmdb_mgmt.migrate_model.constants import CLASSIFICATIONS, MODELS
from apps.cmdb_mgmt.utils.ag import AgUtils


class MigrateModel:
    def run(self):
        self.migrate_classifications()
        self.migrate_models()
        self.migrate_associations()

    def migrate_classifications(self):
        """初始化模型分类"""
        with AgUtils() as ag:
            ag.batch_create_entity(CLASSIFICATION, CLASSIFICATIONS, "classification_name")

    def migrate_models(self):
        """初始化模型"""
        with AgUtils() as ag:
            ag.batch_create_entity(MODEL, MODELS, "model_name")

    def migrate_associations(self):
        """初始模型关联"""
        pass
