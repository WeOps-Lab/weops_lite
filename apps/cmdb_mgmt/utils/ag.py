from apps.cmdb_mgmt.constants import ENTITY_TYPE, EDGE_TYPE
from apps.core.exceptions.base_app_exception import BaseAppException
from apps.core.utils.ag_client import AgClient
from apps.cmdb_mgmt.utils.format_type import FORMAT_TYPE


class AgUtils(object):
    def __init__(self):
        self.con = AgClient().get_con()

    def close(self):
        """关闭连接"""
        self.con.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def entity_to_list(self, data: iter):
        """将使用fetchall查询的结果转换成列表类型"""
        return [self.entity_to_dict(i) for i in data]

    def entity_to_dict(self, data: tuple):
        """将使用fetchone查询的结果转换成字典类型"""
        return dict(_id=data[0].id, _label=data[0].label, **data[0].properties)

    def edge_to_list(self, data: iter, return_entity: bool):
        """将使用fetchall查询的结果转换成列表类型"""
        result = [
            {
                "src": self.entity_to_dict((i[0][0],)),
                "edge": self.edge_to_dict((i[0][1],)),
                "dst": self.entity_to_dict((i[0][2],)),
            }
            for i in data
        ]
        return result if return_entity else [i["edge"] for i in result]

    def edge_to_dict(self, data: tuple):
        """将使用fetchone查询的结果转换成字典类型"""
        return dict(_id=data[0].id, _label=data[0].label, **data[0].properties)

    def format_properties(self, properties: dict):
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

    def create_entity(self, label: str, properties: dict, check_attr_map: dict, exist_items: list, operator: str = None):
        """
            快速创建一个实体
        """
        result = self._create_entity(label, properties, check_attr_map, exist_items, operator)
        # 提交事务, 持久化到库
        self.con.commit()
        return result

    def check_unique_attr(self, item, check_attr_map, exist_items, is_update=False):
        """校验唯一属性"""
        not_only_attr = set()

        check_attrs = [i for i in check_attr_map.keys() if i in item] if is_update else check_attr_map.keys()

        for exist_item in exist_items:
            for attr in check_attrs:
                if exist_item[attr] == item[attr]:
                    not_only_attr.add(attr)

        if not not_only_attr:
            return

        message = ""
        for attr in not_only_attr:
            message += f"{check_attr_map[attr]}重复；"

        raise BaseAppException(message)

    def check_required_attr(self, item, check_attr_map, is_update=False):
        """校验必填属性"""
        not_required_attr = set()

        check_attrs = [i for i in check_attr_map.keys() if i in item] if is_update else check_attr_map.keys()

        for attr in check_attrs:
            if not item.get(attr):
                not_required_attr.add(attr)

        if not not_required_attr:
            return

        message = ""
        for attr in not_required_attr:
            message += f"必填项{check_attr_map[attr]}为空；"

        raise BaseAppException(message)

    def get_editable_attr(self, item, check_attr_map):
        """取可编辑属性"""
        return {k: v for k, v in item.items() if k in check_attr_map}

    def _create_entity(self, label: str, properties: dict, check_attr_map: dict, exist_items: list, operator: str = None):

        # 校验必填项标签非空
        if not label:
            raise BaseAppException("标签为空！")

        # 校验唯一属性
        self.check_unique_attr(properties, check_attr_map.get("is_only", {}), exist_items)

        # 校验必填项
        self.check_required_attr(properties, check_attr_map.get("is_required", {}))

        # 补充创建人
        if operator:
            properties.update(_creator=operator)

        # 创建实体
        properties_str = self.format_properties(properties)
        entity = self.con.execCypher(f"CREATE (n:{label} {properties_str}) RETURN n").fetchone()

        return self.entity_to_dict(entity)

    def create_edge(self, label: str, a_id: int, a_label: str, b_id: int, b_label: str, properties: dict,
                    check_asst_key: str):
        """
            快速创建一条边
        """
        result = self._create_edge(label, a_id, a_label, b_id, b_label, properties, check_asst_key)
        # 提交事务, 持久化到库
        self.con.commit()
        return result

    def _create_edge(self, label: str, a_id: int, a_label: str, b_id: int, b_label: str, properties: dict,
                     check_asst_key: str = "model_asst_id"):

        # 校验必填项标签非空
        if not label:
            raise BaseAppException("标签为空！")

        # 校验边是否已经存在
        check_asst_val = properties.get(check_asst_key)
        edge_count = self.con.execCypher(
            f"MATCH (a:{a_label})-[e]-(b:{b_label}) WHERE id(a) = {a_id} AND id(b) = {b_id} AND e.{check_asst_key} = '{check_asst_val}' RETURN e").rowcount
        if edge_count > 0:
            raise BaseAppException("边已存在！")

        # 创建边
        properties_str = self.format_properties(properties)
        edge = self.con.execCypher(
            f"MATCH (a:{a_label}), (b:{b_label}) WHERE id(a) = {a_id} AND id(b) = {b_id} CREATE (a)-[e:{label} {properties_str}]->(b) RETURN e").fetchone()

        # 提交事务
        self.con.commit()

        return self.edge_to_dict(edge)

    def batch_create_entity(self, label: str, properties_list: list, check_attr_map: dict, exist_items: list, operator: str = None):
        """批量创建实体"""
        results = []
        for index, properties in enumerate(properties_list):
            result = {}
            try:
                entity = self._create_entity(label, properties, check_attr_map, exist_items, operator)
                result.update(data=entity, success=True)
                exist_items.append(entity)
            except BaseAppException as e:
                message = f"第{index + 1}条数据，{e.message}"
                result.update(message=message, success=False)
            results.append(result)
        self.con.commit()
        return results

    def batch_create_edge(self, label: str, a_label: str, b_label: str, edge_list: list, check_asst_key: str):
        """批量创建边"""
        results = []
        for index, edge_info in enumerate(edge_list):
            result = {}
            try:
                a_id = edge_info["src_id"]
                b_id = edge_info["dst_id"]
                edge = self._create_edge(label, a_id, a_label, b_id, b_label, edge_info, check_asst_key)
                result.update(data=edge, success=True)
            except BaseAppException as e:
                message = f"第{index + 1}条数据，{e.message}"
                result.update(message=message, success=False)
            results.append(result)
        self.con.commit()
        return results

    def format_search_params(self, params: list, param_type: str = "AND"):
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

            list[]: {"field": "test", "type": "list[]", "value": [1,2]} -> "n.test @> ARRAY [1,2]"
        """

        params_str = ""
        param_type = f" {param_type} "
        for param in params:
            method = FORMAT_TYPE.get(param["type"])
            if not method:
                continue

            params_str += method(param)
            params_str += param_type

        return f"({params_str[:-len(param_type)]})" if params_str else params_str

    def format_final_params(self, search_params: list, search_param_type: str = "AND", permission_params=""):
        search_params_str = self.format_search_params(search_params, search_param_type)

        if not search_params_str:
            return permission_params

        if not permission_params:
            return search_params_str

        return f"{search_params_str} AND {permission_params}"

    def query_entity(self, label: str, params: list, page: dict = None, order: str = None, param_type="AND", permission_params: str = ""):
        """
            查询实体
        """
        label_str = f":{label}" if label else ""
        params_str = self.format_final_params(params, search_param_type=param_type, permission_params=permission_params)
        params_str = f"WHERE {params_str}" if params_str else params_str

        sql_str = f"MATCH (n{label_str}) {params_str} RETURN n"

        if order:
            sql_str += f" ORDER BY n.{order}"

        count = 0
        if page:
            count = self.con.execCypher(sql_str).rowcount
            sql_str += f" SKIP {page['skip']} LIMIT {page['limit']}"

        objs = self.con.execCypher(sql_str)
        return self.entity_to_list(objs), count or objs.rowcount

    def query_entity_by_id(self, label: str, id: int):
        """
            查询实体详情
        """
        label_str = f":{label}" if label else ""
        obj = self.con.execCypher(f"MATCH (n{label_str}) WHERE id(n) = {id} RETURN n").fetchone()
        return self.entity_to_dict(obj)

    def query_entity_by_ids(self, label: str, ids: list):
        """
            查询实体列表
        """
        label_str = f":{label}" if label else ""
        objs = self.con.execCypher(f"MATCH (n{label_str}) WHERE id(n) IN {ids} RETURN n")
        return self.entity_to_list(objs)

    def query_edge(self, label: str, a_label: str, b_label: str, params: list, param_type: str = "AND",
                   return_entity: bool = False):
        """
            查询边
        """
        label_str = f":{label}" if label else ""
        a_label_str = f":{a_label}" if a_label else ""
        b_label_str = f":{b_label}" if b_label else ""
        params_str = self.format_search_params(params, param_type)
        params_str = f"WHERE {params_str}" if params_str else params_str

        objs = self.con.execCypher(f"MATCH p=((a{a_label_str})-[n{label_str}]->(b{b_label_str})) {params_str} RETURN p")
        return self.edge_to_list(objs, return_entity), objs.rowcount

    def query_edge_by_id(self, label: str, id: int, return_entity: bool = False):
        """
            查询边详情
        """
        label_str = f":{label}" if label else ""
        objs = self.con.execCypher(f"MATCH p=((a)-[n{label_str}]->(b)) WHERE id(n) = {id} RETURN p")
        edges = self.edge_to_list(objs, return_entity)
        return edges[0]

    def format_properties_set(self, properties: dict):
        """格式化properties的set数据"""
        properties_str = ""
        for key, value in properties.items():
            if type(value) == str:
                properties_str += f"n.{key}='{value}',"
            else:
                properties_str += f"n.{key}={value},"
        return properties_str if properties_str == "" else properties_str[:-1]

    def set_entity_properties(self, label: str, entity_id: int, properties: dict, check_attr_map: dict,
                              exist_items: list, check: bool = True):
        """
            设置实体属性
        """
        if check:
            # 校验唯一属性
            self.check_unique_attr(properties, check_attr_map.get("is_only", {}), exist_items, is_update=True)

            # 校验必填项
            self.check_required_attr(properties, check_attr_map.get("is_required", {}), is_update=True)

            # 取出可编辑属性
            properties = self.get_editable_attr(properties, check_attr_map.get("editable", {}))

        label_str = f":{label}" if label else ""
        properties_str = self.format_properties_set(properties)
        if not properties_str:
            raise BaseAppException("无可更新属性！")
        entity = self.con.execCypher(
            f"MATCH (n{label_str}) WHERE id(n) = {entity_id} SET {properties_str} RETURN n").fetchone()
        self.con.commit()
        return self.entity_to_dict(entity)

    def format_properties_remove(self, attrs: list):
        """格式化properties的remove数据"""
        properties_str = ""
        for attr in attrs:
            properties_str += f"n.{attr},"
        return properties_str if properties_str == "" else properties_str[:-1]

    def remove_entitys_properties(self, label: str, params: list, attrs: list):
        """移除某些实体的某些属性"""
        label_str = f":{label}" if label else ""
        properties_str = self.format_properties_remove(attrs)
        params_str = self.format_search_params(params)
        params_str = f"WHERE {params_str}" if params_str else params_str

        self.con.execCypher(f"MATCH (n{label_str}) {params_str} REMOVE {properties_str} RETURN n")
        self.con.commit()

    def batch_delete_entity(self, label: str, entity_ids: list):
        """批量删除实体"""
        label_str = f":{label}" if label else ""
        self.con.execCypher(f"MATCH (n{label_str}) WHERE id(n) IN {entity_ids} DELETE n")
        self.con.commit()

    def delete_edge(self, label: str, edge_id: int):
        """删除边"""
        label_str = f":{label}" if label else ""
        self.con.execCypher(f"MATCH ()-[n{label_str}]->() WHERE id(n) = {edge_id} DELETE n")
        self.con.commit()

    def entity_fulltext_search(self, label: str, search: str, params: list, permission_params: str = ""):
        """实体全网检索"""

        label_str = f":{label}" if label else ""
        params_str = self.format_final_params(params, permission_params=permission_params)
        params_str = f"WHERE {params_str}" if params_str else params_str

        sql_str = f"MATCH (n{label_str}) {params_str} RETURN n"

        inst_objs = self.con.execCypher(sql_str)

        result = [
            {
                '_id': inst[0].id,
                '_label': inst[0].label,
                **inst[0].properties
            }
            for inst in inst_objs
            if search in " ".join(map(str, inst[0].properties.values()))
        ]

        return result

    def query_topo(self, label: str, params: list):
        """查询实例拓扑"""

        label_str = f":{label}" if label else ""
        params_str = self.format_search_params(params)
        params_str = f"WHERE {params_str}" if params_str else params_str
        objs = self.con.execCypher(f"MATCH p=(n{label_str})-[*]-() {params_str} RETURN p")

        return self.format_topo(objs)

    def format_topo(self, objs):
        """格式化拓扑数据"""

        if objs.rowcount == 0:
            return dict(src_result={}, dst_result={})

        edge_map = {}
        entity_map = {}

        for obj in objs:
            for topo in obj:
                for data in topo:
                    data_json = dict(_id=data.id, _label=data.label, **data.properties)
                    if data.gtype == ENTITY_TYPE:
                        entity_map[data_json["_id"]] = data_json
                    elif data.gtype == EDGE_TYPE:
                        edge_map[data_json["_id"]] = data_json

        edges = list(edge_map.values())
        entities = list(entity_map.values())

        src_result = self.create_node(entities[0], edges, entities, True)
        dst_result = self.create_node(entities[0], edges, entities, False)

        return dict(src_result=src_result, dst_result=dst_result)

    def create_node(self, entity, edges, entities, entity_is_src=True):
        """entity作为目标"""
        node = {
            '_id': entity['_id'],
            'model_id': entity['model_id'],
            'inst_name': entity['inst_name'],
            'children': []
        }

        if entity_is_src:
            entity_key, child_entity_key = "src", "dst"
        else:
            entity_key, child_entity_key = "dst", "src"

        for edge in edges:
            if edge[f'{entity_key}_inst_id'] == entity['_id']:
                child_entity = self.find_entity_by_id(edge[f'{child_entity_key}_inst_id'], entities)
                if child_entity:
                    child_node = self.create_node(child_entity, edges, entities, entity_is_src)
                    child_node['model_asst_id'] = edge['model_asst_id']
                    child_node['asst_id'] = edge['asst_id']
                    node['children'].append(child_node)
        return node

    def find_entity_by_id(self, entity_id, entities):
        """根据ID找实体"""
        for entity in entities:
            if entity['_id'] == entity_id:
                return entity
        return None
