from apps.system_mgmt.models.graded_role import GradedRole


def get_role_all_child_role(role: str):
    """获取某个角色下的全部子角色"""
    role_objs = GradedRole.objects.all()
    role_dict = {i.role: i.superior_role for i in role_objs}
    all_child_roles = set()
    get_child_role(role_dict, role, all_child_roles)
    return all_child_roles


def get_child_role(role_dict: dict, role: str, all_child_roles: set):
    """获取角色的子角色"""
    child_roles = set()
    for k, v in role_dict.items():
        if role != v:
            continue
        child_roles.add(k)

    for child_role in child_roles:
        all_child_roles.add(child_role)
        get_child_role(role_dict, child_role, all_child_roles)
