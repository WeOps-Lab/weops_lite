from apps.cmdb_mgmt.models.credential import RoleCredentialPermission, UserCredentialPermission


class CredentialManage(object):
    @staticmethod
    def role_authorisation(model_id, inst_id, roles):
        """角色授权"""
        old_data = RoleCredentialPermission.objects.filter(model_id=model_id, inst_id=inst_id)
        old_roles_set = {i.role for i in old_data}
        new_roles_set = set(roles)
        add_roles = new_roles_set - old_roles_set
        del_roles = old_roles_set - new_roles_set
        create_obj = [RoleCredentialPermission(model_id=model_id, inst_id=inst_id, role=i) for i in add_roles]
        if create_obj:
            RoleCredentialPermission.objects.bulk_create(create_obj, batch_size=100)
        RoleCredentialPermission.objects.filter(model_id=model_id, inst_id=inst_id, role__in=del_roles).delete()

    @staticmethod
    def user_authorisation(model_id, inst_id, users):
        """用户授权"""
        old_data = UserCredentialPermission.objects.filter(model_id=model_id, inst_id=inst_id)
        old_users_set = {i.user for i in old_data}
        new_users_set = set(users)
        add_users = new_users_set - old_users_set
        del_users = old_users_set - new_users_set
        create_obj = [UserCredentialPermission(model_id=model_id, inst_id=inst_id, user=i) for i in add_users]
        if create_obj:
            UserCredentialPermission.objects.bulk_create(create_obj, batch_size=100)
        UserCredentialPermission.objects.filter(model_id=model_id, inst_id=inst_id, user__in=del_users).delete()

    @staticmethod
    def get_roles(model_id, inst_id):
        """获取已授权角色"""
        objs = RoleCredentialPermission.objects.filter(model_id=model_id, inst_id=inst_id)
        return list({i.role for i in objs}) if objs else []

    @staticmethod
    def get_users(model_id, inst_id):
        """获取已授权用户"""
        objs = UserCredentialPermission.objects.filter(model_id=model_id, inst_id=inst_id)
        return list({i.user for i in objs}) if objs else []
