class SubGroup:
    def __init__(self, group_id, group_list):
        self.group_id = group_id
        self.group_list = group_list

    def get_group_id_and_subgroup_id(self):
        """获取组织ID与子组ID的列表"""
        if self.group_list:
            sub_group = self.get_subgroup(self.group_list[0], self.group_id)
        else:
            sub_group = None
        group_id_list = [self.group_id]
        if not sub_group:
            return group_id_list
        self.get_all_group_id_by_subgroups(sub_group["subGroups"], group_id_list)
        return group_id_list

    def get_subgroup(self, group, id):
        """根据子组ID获取子组"""

        if group["id"] == id:
            return group

        for subgroup in group["subGroups"]:
            if subgroup["id"] == id:
                return subgroup
            elif subgroup["subGroups"]:
                for subgroup in group["subGroups"]:
                    result = self.get_subgroup(subgroup, id)
                    if result:
                        return result
        return None

    def get_all_group_id_by_subgroups(self, subgroups: list, id_list: list):
        """取出所有子组ID"""
        for subgroup in subgroups:
            id_list.append(subgroup["id"])
            if subgroup["subGroups"]:
                self.get_all_group_id_by_subgroups(subgroup["subGroups"], id_list)
