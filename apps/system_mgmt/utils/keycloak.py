import json

from keycloak import urls_patterns, KeycloakGetError
from keycloak.exceptions import raise_error_from_response

from apps.system_mgmt.constants import BUILT_IN_ROLES
from weops_lite.components.keycloak import KEYCLOAK_CLIENT_ID


def get_first_and_max(params):
    """格式化page参数, 获取first与max"""
    page, page_size = int(params.get('page', 1)), int(params.get('page_size', 20))
    _first = (page - 1) * page_size
    _max = page_size
    return _first, _max


def get_client_id(realm_client):
    """获取客户端的id"""
    # TODO 考虑放入缓存
    clients = realm_client.get_clients()
    for client in clients:
        if client["clientId"] == KEYCLOAK_CLIENT_ID:
            return client["id"]


def get_realm_roles(realm_client):
    """获取域角色，并过滤掉内置角色"""
    result = realm_client.get_realm_roles()
    return [i for i in result if i.get("name") not in BUILT_IN_ROLES]


def get_realm_roles_of_user(realm_client, user_id):
    """获取用户关联的角色，并过滤掉内置角色"""
    result = realm_client.get_realm_roles_of_user(user_id)
    return [i for i in result if i.get("name") not in BUILT_IN_ROLES]


# python-keycloak库缺少的api, 在此处补充
class SupplementApi(object):
    def __init__(self, connection):
        self.connection = connection

    def get_permission_by_policy_id(self, client_id, policy_id):
        """根据策略查询权限"""
        url = urls_patterns.URL_ADMIN_CLIENT_AUTHZ_POLICY + "/dependentPolicies"
        params_path = {
            "realm-name": self.connection.realm_name,
            "id": client_id,
            "policy-id": policy_id,
        }
        data_raw = self.connection.raw_get(url.format(**params_path))
        return raise_error_from_response(data_raw, KeycloakGetError)

    def update_permission(self, client_id, permission_id, permission):
        """设置权限"""
        url = urls_patterns.URL_ADMIN_CLIENT_AUTHZ + "/permission/resource/{permission_id}"
        params_path = {
            "realm-name": self.connection.realm_name,
            "id": client_id,
            "permission_id": permission_id
        }
        data_raw = self.connection.raw_put(url.format(**params_path), json.dumps(permission))
        return raise_error_from_response(data_raw, KeycloakGetError)

    def get_policies_by_permission_id(self, client_id, permission_id):
        """根据权限ID查询策略"""
        url = urls_patterns.URL_ADMIN_CLIENT_AUTHZ + "/policy/{permission_id}/associatedPolicies"
        params_path = {
            "realm-name": self.connection.realm_name,
            "id": client_id,
            "permission_id": permission_id,
        }
        data_raw = self.connection.raw_get(url.format(**params_path))
        return raise_error_from_response(data_raw, KeycloakGetError)

