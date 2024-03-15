from apps.core.exceptions.base_app_exception import BaseAppException
from apps.core.utils.ag_client import AgClient
from apps.cmdb_mgmt.utils.format_type import FORMAT_TYPE


class AgUtils(object):
    def __init__(self):
        self.con = AgClient().get_con()

    def close(self):
        """关闭连接"""
        self.con.close()

    @staticmethod
    def entity_to_list(data: iter):
        """将使用fetchall查询的结果转换成列表类型"""
        return [dict(id=i[0].id, label=i[0].label, properties=i[0].properties) for i in data]

    @staticmethod
    def entity_to_dict(data: tuple):
        """将使用fetchone查询的结果转换成字典类型"""
        return dict(id=data[0].id, label=data[0].label, properties=data[0].properties)

    @staticmethod
    def edge_to_list(data: iter):
        """将使用fetchall查询的结果转换成列表类型"""
        return [dict(id=i[0].id, label=i[0].label, properties=i[0].properties, start_id=i[0].start_id, end_id=i[0].end_id) for i in data]

    @staticmethod
    def edge_to_dict(data: tuple):
        """将使用fetchone查询的结果转换成字典类型"""
        return dict(id=data[0].id, label=data[0].label, properties=data[0].properties, start_id=data[0].start_id, end_id=data[0].end_id)

    @staticmethod
    def format_properties(properties: dict):
        """将属性格式化为sql中的字符串格式"""
        properties_str = '{'
        for key, value in properties.items():
            if type(value) == str:
                properties_str += f"{key}:'{value}',"
            else:
                properties_str += f"{key}:{value},"
        properties_str = properties_str[:-1]
        properties_str += "}"
        return properties_str

    def create_entity(self, label: str, properties: dict, check_unique_attr: str):
        """
            快速创建一个实体
        """
        result = self._create_entity(label, properties, check_unique_attr)
        # 提交事务, 持久化到库
        self.con.commit()
        return result

    def _create_entity(self, label: str, properties: dict, check_unique_attr: str):

        # 校验必填项标签非空
        if not label:
            raise BaseAppException("标签为空！")

        # 校验必填项实体名非空
        check_unique_attr_val = properties.get(check_unique_attr)
        if not check_unique_attr_val:
            raise BaseAppException("实体名为空！")

        # 校验实体名称的唯一性
        _, counts = self.query_entity(label, [{"field": check_unique_attr, "type": "str=", "value": check_unique_attr_val}])
        if counts > 0:
            raise BaseAppException("实体重复！")

        # 创建实体
        properties_str = self.format_properties(properties)
        entity = self.con.execCypher(f"CREATE (n:{label} {properties_str}) RETURN n").fetchone()

        return self.entity_to_dict(entity)

    def create_edge(self, label: str, a_id: int, a_label: str, b_id: int, b_label: str, properties: dict):
        """
            快速创建一条边
        """
        result = self._create_edge(label, a_id, a_label, b_id, b_label, properties)
        # 提交事务, 持久化到库
        self.con.commit()
        return result

    def _create_edge(self, label: str, a_id: int, a_label: str, b_id: int, b_label: str, properties: dict):

        # 校验必填项标签非空
        if not label:
            raise BaseAppException("标签为空！")

        # 校验边是否已经存在
        edge_count = self.con.execCypher(f"MATCH (a:{a_label})-[e]-(b:{b_label}) WHERE id(a) = {a_id} AND id(b) = {b_id} RETURN e").rowcount
        if edge_count > 0:
            raise BaseAppException("边已存在！")

        # 创建边
        properties_str = self.format_properties(properties)
        edge = self.con.execCypher(
            f"MATCH (a:{a_label}), (b:{b_label}) WHERE id(a) = {a_id} AND id(b) = {b_id} CREATE (a)-[e:{label} {properties_str}]->(b) RETURN e").fetchone()

        # 提交事务
        self.con.commit()

        return self.entity_to_dict(edge)

    def batch_create_entity(self, label: str, properties_list: list, check_unique_attr: str):
        """批量创建实体"""
        results = []
        for properties in properties_list:
            result = {}
            try:
                entity = self._create_entity(label, properties, check_unique_attr)
                result.update(data=entity, success=True)
            except Exception as e:
                result.update(message=e, success=False)
            results.append(result)
        self.con.commit()

    def batch_create_edge(self, label: str, edge_list: list):
        """批量创建边"""
        results = []
        for edge_info in edge_list:
            result = {}
            try:
                a_id, a_label = edge_info["start_id"], edge_info["start_label"]
                b_id, b_label = edge_info["end_id"], edge_info["end_label"]
                properties = edge_info["properties"]
                edge = self._create_edge(label, a_id, a_label, b_id, b_label, properties)
                result.update(data=edge, success=True)
            except Exception as e:
                result.update(message=e, success=False)
            results.append(result)
        self.con.commit()

    @staticmethod
    def format_params(params: list):
        """
            查询参数格式化:
            bool: {"field": "is_host", "type": "bool", "value": True} -> "n.is_host = True"

            time: {"field": "create_time", "type": "time", "start": "", "end": ""} -> "n.time >= '2022-01-01 08:00:00' AND n.time <= '2022-01-02 08:00:00'"

            str=: {"field": "name", "type": "str=", "value": "host"} -> "n.name = 'host'"
            str<>: {"field": "name", "type": "str<>", "value": "host"} -> "n.name <> 'host'"
            str*: {"field": "name", "type": "str*", "value": "host"} -> "n.name =~ '.*host.*'"
            str[]: {"field": "name", "type": "str[]", "value": ["host"]} -> "n.name IN ["host"]"

            int=: {"field": "mem", "type": "int=", "value": 200} -> "n.mem = 200"
            int>: {"field": "mem", "type": "int>", "value": 200} -> "n.mem > 200"
            int<: {"field": "mem", "type": "int<", "value": 200} -> "n.mem < 200"
            int<>: {"field": "mem", "type": "int<>", "value": 200} -> "n.mem <> 200"
            int[]: {"field": "mem", "type": "int[]", "value": [200]} -> "n.mem IN [200]"
        """

        params_str = ""
        for param in params:
            method = FORMAT_TYPE.get(param["type"])
            if not method:
                continue

            params_str += method(param)
            params_str += " AND "

        if params_str == "":
            return params_str
        else:
            return f"WHERE {params_str[:-5]}"

    def query_entity(self, label: str, params: list, page: dict = None, order: str = None):
        """
            查询实体
        """
        label_str = f":{label}" if label else ""
        params_str = AgUtils.format_params(params)
        sql_str = f"MATCH (n{label_str}) {params_str} RETURN n"

        if page:
            sql_str += f" SKIP {page['skip']} LIMIT {page['limit']}"

        if order:
            sql_str += f" ORDER BY n.{order}"

        objs = self.con.execCypher(sql_str)
        return self.entity_to_list(objs), objs.rowcount

    def query_edge(self, label: str, a_label: str, b_label: str, params: list):
        """
            查询边
        """
        label_str = f":{label}" if label else ""
        a_label_str = f":{a_label}" if a_label else ""
        b_label_str = f":{b_label}" if b_label else ""
        params_str = AgUtils.format_params(params)
        objs = self.con.execCypher(f"MATCH (a{a_label_str})-[n{label_str}]-(b{b_label_str}) {params_str} RETURN DISTINCT n")
        return self.edge_to_list(objs), objs.rowcount

    @staticmethod
    def format_properties_set(properties: dict):
        """格式化properties的set数据"""
        properties_str = ""
        for key, value in properties.items():
            if type(value) == str:
                properties_str += f"n.{key}='{value}',"
            else:
                properties_str += f"n.{key}={value},"
        return properties_str if properties_str == "" else properties_str[:-1]

    def set_entity_properties(self, label: str, entity_id: int, properties: dict):
        """
            设置实体属性
        """
        label_str = f":{label}" if label else ""
        properties_str = self.format_properties_set(properties)
        entity = self.con.execCypher(f"MATCH (n{label_str}) WHERE id(n) = {entity_id} SET {properties_str} RETURN n").fetchone()
        self.con.commit()
        return self.entity_to_dict(entity)

    @staticmethod
    def format_properties_remove(attrs: list):
        """格式化properties的remove数据"""
        properties_str = ""
        for attr in attrs:
            properties_str += f"n.{attr},"
        return properties_str if properties_str == "" else properties_str[:-1]

    def remove_entity_properties(self, label: str, entity_id: int, attrs: list):
        """移除实体属性"""
        label_str = f":{label}" if label else ""
        properties_str = self.format_properties_remove(attrs)
        entity = self.con.execCypher(f"MATCH (n{label_str}) WHERE id(n) = {entity_id} REMOVE {properties_str} RETURN n").fetchone()
        self.con.commit()
        return self.entity_to_dict(entity)

    def _delete_entity(self, label: str, entity_id: int):
        """删除实体"""
        label_str = f":{label}" if label else ""
        self.con.execCypher(f"MATCH (n{label_str}) WHERE id(n) = {entity_id} DELETE n")

    def delete_entity(self, label: str, entity_id: int):
        """删除实体"""
        self._delete_entity(label, entity_id)
        self.con.commit()

    def batch_delete_entity(self, label: str, entity_ids: list):
        """批量删除实体"""
        for entity_id in entity_ids:
            self._delete_entity(label, entity_id)
        self.con.commit()

    def delete_edge(self, label: str, edge_id: int):
        """删除边"""
        label_str = f":{label}" if label else ""
        self.con.execCypher(f"MATCH ()-[n{label_str}]->() WHERE id(n) = {edge_id} DELETE n")
        self.con.commit()
