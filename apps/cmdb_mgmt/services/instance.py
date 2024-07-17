from apps.cmdb_mgmt.constants import INSTANCE, INSTANCE_ASSOCIATION, ORGANIZATION, ENCRYPTION, ENUM, USER, BASE, \
    CREDENTIAL, CREDENTIAL_INSTANCE, CREDENTIAL_INSTANCE_ASSOCIATION
from apps.cmdb_mgmt.messages import EDGE_REPETITION, INSTANCE_EDGE_REPETITION
from apps.cmdb_mgmt.models.Instance_permission import MANAGE, QUERY
from apps.cmdb_mgmt.models.change_record import DELETE_INST_ASST, CREATE_INST_ASST, CREATE_INST, UPDATE_INST, \
    DELETE_INST
from apps.cmdb_mgmt.models.show_field import ShowField
from apps.cmdb_mgmt.services.model import ModelManage
from apps.cmdb_mgmt.utils.ag import AgUtils
from apps.cmdb_mgmt.utils.change_record import create_change_record, create_change_record_by_asso, \
    batch_create_change_record
from apps.cmdb_mgmt.utils.credential import Credential
from apps.cmdb_mgmt.utils.export import Export
from apps.cmdb_mgmt.utils.Import import Import
from apps.cmdb_mgmt.utils.permission import PermissionManage, RolePermissionManage, CredentialPermissionManage
from apps.cmdb_mgmt.utils.subgroup import SubGroup
from apps.core.exceptions.base_app_exception import BaseAppException
from apps.system_mgmt.services.group_manage import GroupManage
from apps.system_mgmt.services.user_manage import UserManage


class InstanceManage(object):

    @staticmethod
    def get_permission_params(token, model_id, permission_type: str = None):
        """获取用户实例权限查询参数，用户用户查询实例"""
        obj = PermissionManage(token, model_id, permission_type)
        permission_params = obj.get_permission_params()
        return permission_params

    @staticmethod
    def get_permission_params_cre(token, model_id, permission_type: str = None):
        """获取用户实例权限查询参数，用户用户查询实例"""
        obj = CredentialPermissionManage(token, model_id, permission_type)
        permission_params = obj.get_permission_params()
        return permission_params

    @staticmethod
    def check_instances_permission(token: str, instances: list, model_id: str, permission_type: str = MANAGE):
        """实例权限校验，用于操作之前"""
        permission_params = InstanceManage.get_permission_params(token, model_id, permission_type)
        with AgUtils() as ag:
            inst_list, count = ag.query_entity(INSTANCE, [], permission_params=permission_params)

        permission_map = {i["_id"]: i for i in inst_list}
        instances_map = {i["_id"]: i for i in instances}

        non_permission_set = set(instances_map.keys()) - set(permission_map.keys())

        if not non_permission_set:
            return
        message = f"实例：{'、'.join([instances_map[i]['inst_name'] for i in non_permission_set])}，无权限！"
        raise BaseAppException(message)

    @staticmethod
    def check_instances_permission_cre(token: str, instances: list, model_id: str, permission_type: str = MANAGE):
        """实例权限校验，用于操作之前"""
        permission_params = InstanceManage.get_permission_params_cre(token, model_id, permission_type)
        with AgUtils() as ag:
            inst_list, count = ag.query_entity(CREDENTIAL_INSTANCE, [], permission_params=permission_params)

        permission_map = {i["_id"]: i for i in inst_list}
        instances_map = {i["_id"]: i for i in instances}

        non_permission_set = set(instances_map.keys()) - set(permission_map.keys())

        if not non_permission_set:
            return
        message = f"实例：{'、'.join([instances_map[i]['inst_name'] for i in non_permission_set])}，无权限！"
        raise BaseAppException(message)

    @staticmethod
    def supplementary_subgroups(params: list):
        """对组织补充子组, 并将类型改为str[]"""
        for param in params:
            if param["field"] == ORGANIZATION and param["value"]:
                group_list = GroupManage().group_list()
                param["value"] = SubGroup(param["value"], group_list).get_group_id_and_subgroup_id()
                param["type"] = "str[]"

    @staticmethod
    def instance_list(token: str, model_id: str, params: list, page: int, page_size: int, order: str):
        """实例列表"""

        inst_label = InstanceManage.get_inst_label_by_model_id(model_id)

        InstanceManage.supplementary_subgroups(params)
        params.append({"field": "model_id", "type": "str=", "value": model_id})
        _page = dict(skip=(page - 1) * page_size, limit=page_size)
        if order and order.startswith("-"):
            order = f"{order.replace('-', '')} DESC"

        # 区分凭据类鉴权与非凭据类鉴权
        if inst_label == CREDENTIAL_INSTANCE:
            permission_params = InstanceManage.get_permission_params_cre(token, model_id)

        else:
            permission_params = InstanceManage.get_permission_params(token, model_id)

        with AgUtils() as ag:
            inst_list, count = ag.query_entity(inst_label, params, page=_page, order=order, permission_params=permission_params)

        return inst_list, count

    @staticmethod
    def instance_list_by_role(roles: list, model_id: str, params: list, page: int, page_size: int, order: str):
        """实例列表，根据角色查询，用于分级管理员授权"""
        InstanceManage.supplementary_subgroups(params)
        params.append({"field": "model_id", "type": "str=", "value": model_id})
        _page = dict(skip=(page - 1) * page_size, limit=page_size)
        if order and order.startswith("-"):
            order = f"{order.replace('-', '')} DESC"

        permission_params = RolePermissionManage(roles, model_id).get_permission_params()

        with AgUtils() as ag:
            inst_list, count = ag.query_entity(INSTANCE, params, page=_page, order=order, permission_params=permission_params)
        return inst_list, count

    @staticmethod
    def get_inst_label_by_model_id(model_id: str):
        """获取模型实例标签"""
        model_info = ModelManage.search_model_info(model_id)
        return CREDENTIAL_INSTANCE if model_info.get("model_type", BASE) == CREDENTIAL else INSTANCE

    @staticmethod
    def instance_create(model_id: str, instance_info: dict, operator: str):
        """创建实例"""
        instance_info.update(model_id=model_id)
        attrs = ModelManage.search_model_attr(model_id)
        check_attr_map = dict(is_only={}, is_required={})
        encryption_set = set()
        for attr in attrs:
            if attr["is_only"]:
                check_attr_map["is_only"][attr["attr_id"]] = attr["attr_name"]
            if attr["is_required"]:
                check_attr_map["is_required"][attr["attr_id"]] = attr["attr_name"]
            if attr["attr_type"] == ENCRYPTION:
                encryption_set.add(attr["attr_id"])

        # 密钥类属性加密
        for k, v in instance_info.items():
            if k in encryption_set:
                instance_info[k] = Credential().encrypt_data(v)

        inst_label = InstanceManage.get_inst_label_by_model_id(model_id)

        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(inst_label, [{"field": "model_id", "type": "str=", "value": model_id}])
            result = ag.create_entity(inst_label, instance_info, check_attr_map, exist_items, operator)

        create_change_record(
            result["_id"],
            result["model_id"],
            inst_label,
            CREATE_INST,
            after_data=result,
            operator=operator,
        )
        return result

    @staticmethod
    def instance_update(token: str, inst_id: int, update_attr: dict, operator: str):
        """修改实例属性"""
        inst_info = InstanceManage.query_entity_by_id(inst_id)

        if not inst_info:
            raise BaseAppException("实例不存在！")

        model_info = ModelManage.search_model_info(inst_info["model_id"])
        inst_label = CREDENTIAL_INSTANCE if model_info.get("model_type", BASE) == CREDENTIAL else INSTANCE

        # 区分凭据类鉴权与非凭据类鉴权
        if inst_label == CREDENTIAL_INSTANCE:
            InstanceManage.check_instances_permission_cre(token, [inst_info], inst_info["model_id"])
        else:
            InstanceManage.check_instances_permission(token, [inst_info], inst_info["model_id"])

        attrs = ModelManage.parse_attrs(model_info.get("attrs", "[]"))
        check_attr_map = dict(is_only={}, is_required={}, editable={})
        encryption_set = set()
        for attr in attrs:
            if attr["is_only"]:
                check_attr_map["is_only"][attr["attr_id"]] = attr["attr_name"]
            if attr["is_required"]:
                check_attr_map["is_required"][attr["attr_id"]] = attr["attr_name"]
            if attr["editable"]:
                check_attr_map["editable"][attr["attr_id"]] = attr["attr_name"]
            if attr["attr_type"] == ENCRYPTION:
                encryption_set.add(attr["attr_id"])

        for k, v in update_attr.items():

            # 属性值一致的排查避免密码重复加密
            if v == inst_info.get(k):
                continue
            # 密钥类属性加密
            if k in encryption_set:
                update_attr[k] = Credential().encrypt_data(v)

        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(inst_label, [{"field": "model_id", "type": "str=", "value": inst_info["model_id"]}])
            exist_items = [i for i in exist_items if i["_id"] != inst_id]
            result = ag.set_entity_properties(inst_label, [inst_id], update_attr, check_attr_map, exist_items)

        create_change_record(
            inst_info["_id"],
            inst_info["model_id"],
            inst_label,
            UPDATE_INST,
            before_data=inst_info,
            after_data=result[0],
            operator=operator
        )

        return result[0]

    @staticmethod
    def batch_instance_update(token: str, inst_ids: list, update_attr: dict, operator: str):
        """批量修改实例属性"""

        inst_list = InstanceManage.query_entity_by_ids(inst_ids)

        if not inst_list:
            raise BaseAppException("实例不存在！")

        model_info = ModelManage.search_model_info(inst_list[0]["model_id"])
        inst_label = CREDENTIAL_INSTANCE if model_info.get("model_type", BASE) == CREDENTIAL else INSTANCE

        # 区分凭据类鉴权与非凭据类鉴权
        if inst_label == CREDENTIAL_INSTANCE:
            InstanceManage.check_instances_permission_cre(token, inst_list, inst_list[0]["model_id"])
        else:
            InstanceManage.check_instances_permission(token, inst_list, inst_list[0]["model_id"])

        attrs = ModelManage.parse_attrs(model_info.get("attrs", "[]"))
        check_attr_map = dict(is_only={}, is_required={}, editable={})
        encryption_set = set()
        for attr in attrs:
            if attr["is_only"]:
                check_attr_map["is_only"][attr["attr_id"]] = attr["attr_name"]
            if attr["is_required"]:
                check_attr_map["is_required"][attr["attr_id"]] = attr["attr_name"]
            if attr["editable"]:
                check_attr_map["editable"][attr["attr_id"]] = attr["attr_name"]
            if attr["attr_type"] == ENCRYPTION:
                encryption_set.add(attr["attr_id"])

        is_one_inst = len(inst_list) == 1

        for k, v in update_attr.items():

            # 当单实例更新是，属性值一致的避免密码重复加密
            if is_one_inst and v == inst_list[0].get(k):
                continue

            # 密钥类属性加密
            if k in encryption_set:
                update_attr[k] = Credential().encrypt_data(v)

        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(inst_label, [{"field": "model_id", "type": "str=", "value": inst_list[0]["model_id"]}])
            exist_items = [i for i in exist_items if i["_id"] not in inst_ids]
            result = ag.set_entity_properties(inst_label, inst_ids, update_attr, check_attr_map, exist_items)

        after_dict = {i["_id"]: i for i in result}
        change_records = [dict(inst_id=i["_id"], model_id=i["model_id"], before_data=i, after_data=after_dict.get(i["_id"])) for i in inst_list]
        batch_create_change_record(inst_label, UPDATE_INST, change_records, operator=operator)

        return result

    @staticmethod
    def instance_batch_delete(token: str, inst_ids: list, operator: str):
        """批量删除实例"""
        inst_list = InstanceManage.query_entity_by_ids(inst_ids)

        if not inst_list:
            raise BaseAppException("实例不存在！")

        inst_label = InstanceManage.get_inst_label_by_model_id(inst_list[0]["model_id"])

        # 区分凭据类鉴权与非凭据类鉴权
        if inst_label == CREDENTIAL_INSTANCE:
            InstanceManage.check_instances_permission_cre(token, inst_list, inst_list[0]["model_id"])
        else:
            InstanceManage.check_instances_permission(token, inst_list, inst_list[0]["model_id"])

        with AgUtils() as ag:
            ag.batch_delete_entity(inst_label, inst_ids)

        change_records = [dict(inst_id=i["_id"], model_id=i["model_id"], before_data=i) for i in inst_list]
        batch_create_change_record(inst_label, DELETE_INST, change_records, operator=operator)

    @staticmethod
    def instance_association_instance_list(model_id: str, inst_id: int, model_type=None):
        """查询模型实例关联的实例列表"""

        edge_label = CREDENTIAL_INSTANCE_ASSOCIATION if model_type == CREDENTIAL else INSTANCE_ASSOCIATION

        with AgUtils() as ag:

            # 作为源模型实例
            src_query_data = [
                {"field": "src_inst_id", "type": "int=", "value": inst_id},
                {"field": "src_model_id", "type": "str=", "value": model_id},
            ]
            src_edge, _ = ag.query_edge(edge_label, src_query_data, return_entity=True)

            # 作为目标模型实例
            dst_query_data = [
                {"field": "dst_inst_id", "type": "int=", "value": inst_id},
                {"field": "dst_model_id", "type": "str=", "value": model_id},
            ]
            dst_edge, _ = ag.query_edge(edge_label, dst_query_data, return_entity=True)

        result = {}
        for item in src_edge + dst_edge:
            model_asst_id = item["edge"]["model_asst_id"]
            item_key = "src" if model_id == item["edge"]["dst_model_id"] else "dst"
            if model_asst_id not in result:
                result[model_asst_id] = {
                    "src_model_id": item["edge"]["src_model_id"],
                    "dst_model_id": item["edge"]["dst_model_id"],
                    "model_asst_id": item["edge"]["model_asst_id"],
                    "asst_id": item["edge"].get("asst_id"),
                    "inst_list": [],
                }
            item[item_key].update(inst_asst_id=item["edge"]["_id"])
            result[model_asst_id]["inst_list"].append(item[item_key])

        return list(result.values())

    @staticmethod
    def instance_association(model_id: str, inst_id: int, model_type=None):
        """查询模型实例关联的实例列表"""

        edge_label = CREDENTIAL_INSTANCE_ASSOCIATION if model_type == CREDENTIAL else INSTANCE_ASSOCIATION

        with AgUtils() as ag:

            # 作为源模型实例
            src_query_data = [
                {"field": "src_inst_id", "type": "int=", "value": inst_id},
                {"field": "src_model_id", "type": "str=", "value": model_id},
            ]
            src_edge, _ = ag.query_edge(edge_label, src_query_data)

            # 作为目标模型实例
            dst_query_data = [
                {"field": "dst_inst_id", "type": "int=", "value": inst_id},
                {"field": "dst_model_id", "type": "str=", "value": model_id},
            ]
            dst_edge, _ = ag.query_edge(edge_label, dst_query_data)

        return src_edge + dst_edge

    @staticmethod
    def instance_association_create(data: dict, operator: str):
        """创建实例关联"""

        models = ModelManage.search_model(CREDENTIAL)
        models_set = {i["model_id"] for i in models}

        src_label = CREDENTIAL_INSTANCE if data["src_model_id"] in models_set else INSTANCE
        dst_label = CREDENTIAL_INSTANCE if data["dst_model_id"] in models_set else INSTANCE

        edge_label = CREDENTIAL_INSTANCE_ASSOCIATION if CREDENTIAL_INSTANCE in {src_label, dst_label} else INSTANCE_ASSOCIATION

        with AgUtils() as ag:
            try:
                edge = ag.create_edge(edge_label, data["src_inst_id"], src_label, data["dst_inst_id"], dst_label, data, "model_asst_id")
            except BaseAppException as e:
                if e.message == EDGE_REPETITION:
                    raise BaseAppException(INSTANCE_EDGE_REPETITION)

        asso_info = InstanceManage.instance_association_by_asso_id(edge["_id"])

        create_change_record_by_asso(edge_label, CREATE_INST_ASST, asso_info, operator=operator)

        return edge

    @staticmethod
    def instance_association_delete(asso_id: int, operator: str):
        """删除实例关联"""

        asso_info = InstanceManage.instance_association_by_asso_id(asso_id)

        with AgUtils() as ag:
            ag.delete_edge(asso_id)

        create_change_record_by_asso(INSTANCE_ASSOCIATION, DELETE_INST_ASST, asso_info, operator=operator)

    @staticmethod
    def instance_association_by_asso_id(asso_id: int):
        """根据关联ID查询实例关联"""
        with AgUtils() as ag:
            edge = ag.query_edge_by_id(asso_id, return_entity=True)
        return edge

    @staticmethod
    def query_entity_by_id(inst_id: int):
        """根据实例ID查询实例详情"""
        with AgUtils() as ag:
            entity = ag.query_entity_by_id(inst_id)
        return entity

    @staticmethod
    def query_entity_by_ids(inst_ids: list):
        """根据实例ID查询实例详情"""
        with AgUtils() as ag:
            entity_list = ag.query_entity_by_ids(inst_ids)
        return entity_list

    @staticmethod
    def download_import_template(model_id: str):
        """下载导入模板"""
        attrs = ModelManage.search_model_attr_v2(model_id)
        return Export(attrs).export_template()

    @staticmethod
    def inst_import(model_id: str, file_stream: bytes, operator: str):
        """实例导入"""
        attrs = ModelManage.search_model_attr_v2(model_id)
        with AgUtils() as ag:
            exist_items, _ = ag.query_entity(INSTANCE, [{"field": "model_id", "type": "str=", "value": model_id}])
        results = Import(model_id, attrs, exist_items, operator).import_inst_list(file_stream)

        change_records = [
            dict(inst_id=i["data"]["_id"], model_id=i["data"]["model_id"], before_data=i["data"])
            for i in results
            if i["success"]
        ]
        batch_create_change_record(INSTANCE, CREATE_INST, change_records, operator=operator)

        return results

    @staticmethod
    def inst_export(model_id: str, ids: list):
        """实例导出"""
        attrs = ModelManage.search_model_attr_v2(model_id)
        with AgUtils() as ag:
            if ids:
                inst_list = ag.query_entity_by_ids(INSTANCE, ids)
            else:
                inst_list, _ = ag.query_entity(INSTANCE, [{"field": "model_id", "type": "str=", "value": model_id}])
        return Export(attrs).export_inst_list(inst_list)

    @staticmethod
    def topo_search(inst_id: int):
        """拓扑查询"""
        with AgUtils() as ag:
            result = ag.query_topo(INSTANCE, [{"field": "id", "type": "id=", "value": inst_id}])
        return result

    @staticmethod
    def create_or_update(data: dict):
        if not data["show_fields"]:
            raise BaseAppException("展示字段不能为空！")
        ShowField.objects.update_or_create(
            defaults=data,
            model_id=data["model_id"],
            created_by=data["created_by"],
        )
        return data

    @staticmethod
    def get_info(model_id: str, created_by: str):
        obj = ShowField.objects.filter(created_by=created_by, model_id=model_id).first()
        result = dict(model_id=obj.model_id, show_fields=obj.show_fields) if obj else None
        return result

    @staticmethod
    def decrypt_data(data: str):
        """数据解密"""
        return Credential().decrypt_data(data)

    @staticmethod
    def model_inst_count(token):
        permission_params = InstanceManage.get_permission_params(token, None)
        model_inst_count = {}
        with AgUtils() as ag:
            inst_objs = ag.entity_objs(INSTANCE, [], permission_params=permission_params)
            for inst_obj in inst_objs:
                model_id = inst_obj[0].properties.get("model_id")
                if not model_id:
                    continue
                if model_id not in model_inst_count:
                    model_inst_count[model_id] = 0
                model_inst_count[model_id] += 1
        return model_inst_count


class FullText:
    def __init__(self):
        self.user_map = self.get_user_map()
        self.group_map = self.get_group_map()
        self.model_enum_map = self.get_model_enum_map()

    def get_model_enum_map(self):
        """获取所有模型的枚举"""
        model_list = ModelManage.search_model()
        model_map = {}
        for model_info in model_list:
            model_attrs = ModelManage.parse_attrs(model_info.get("attrs", "[]"))
            enum_attr_map = {}
            for attr in model_attrs:
                if attr["attr_type"] == ENUM:
                    enum_attr_map[attr["attr_id"]] = {i["id"]: i["name"] for i in attr["option"]}
                elif attr["attr_type"] == USER:
                    enum_attr_map[attr["attr_id"]] = self.user_map
                elif attr["attr_type"] == ORGANIZATION:
                    enum_attr_map[attr["attr_id"]] = self.group_map

            if not enum_attr_map:
                continue
            model_map[model_info["model_id"]] = enum_attr_map
        return model_map

    def get_user_map(self):
        users = UserManage().user_all()
        return {user["username"]: user["lastName"] for user in users}

    def get_group_map(self):
        group = GroupManage().group_list()
        option = []
        ModelManage.get_organization_option(group, option)
        return {i["id"]: i["name"] for i in option}

    def matching(self, search, data, exclude=["model_id", "_creator"]):
        model_id = data.get("model_id", "")
        values = []
        for k, v in data.items():

            # 排除某些key不进行检索
            if k in exclude:
                continue

            if k not in self.model_enum_map.get(model_id, {}):
                values.append(str(v))
            else:
                value = self.model_enum_map.get(model_id, {}).get(k, {}).get(v, "")
                values.append(str(value))

        return search in " ".join(values)

    def search(self, token: str, data: dict):

        permission_params = InstanceManage.get_permission_params(token, data.get("model_id"))
        with AgUtils() as ag:
            inst_objs = ag.entity_objs(INSTANCE, [], permission_params=permission_params)

            items = []
            for inst_obj in inst_objs:
                item = {
                    '_id': inst_obj[0].id,
                    '_label': inst_obj[0].label,
                    **inst_obj[0].properties
                }
                if self.matching(data["search"], inst_obj[0].properties):
                    items.append(item)
        return items
