import os
import age
from apps.core.constants import GRAPH_NAME


class AgClient(object):
    def __init__(self, graph_name=GRAPH_NAME):
        self.graph_name = graph_name
        self.dsn = "host={} port={} dbname={} user={} password={}".format(
            os.getenv('DB_HOST'),
            os.getenv('DB_PORT'),
            os.getenv('DB_NAME'),
            os.getenv('DB_USER'),
            os.getenv('DB_PASSWORD'),
        )

    def get_con(self):
        """获取图库的连接"""
        return age.connect(graph=self.graph_name, dsn=self.dsn)

    def set_graph(self):
        """创建图"""
        con = self.get_con()
        con.setGraph(self.graph_name)
        con.close()

    def del_graph(self):
        """删除图"""
        con = self.get_con()
        age.deleteGraph(con.connection, self.graph_name)
        con.close()

    @staticmethod
    def to_list(data: iter):
        """将使用fetchall查询的结果转换成列表类型"""
        return [dict(id=i[0].id, label=i[0].label, properties=i[0].properties) for i in data]

    @staticmethod
    def to_dict(data: tuple):
        """将使用fetchone查询的结果转换成字典类型"""
        return dict(id=data[0].id, label=data[0].label, properties=data[0].properties)

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

    @staticmethod
    def create_entity(con: age.Age, label: str, properties: dict):
        """
            快速创建一个实体
        """

        # 校验必填项标签非空
        if not label:
            raise Exception("标签为空！")

        # 校验必填项实体名非空
        entity_name = properties.get("entity_name")
        if not entity_name:
            raise Exception("实体名为空！")

        # 校验实体名称的唯一性
        entity_name_str = "{entity_name:'" + entity_name + "'}"
        entity_count = con.execCypher(f"MATCH (n:{label} {entity_name_str}) RETURN n").rowcount
        if entity_count > 0:
            raise Exception("实体名称重复！")

        # 创建实体
        properties_str = AgClient.format_properties(properties)
        entity = con.execCypher(f"CREATE (n:{label} {properties_str}) RETURN n").fetchone()

        # 提交事务关闭连接
        con.commit()
        con.close()

        return AgClient.to_dict(entity)

    @staticmethod
    def create_edge(con: age.Age, label: str, a_id: int, a_label: str, b_id: int, b_label: str, properties: dict):
        """
            快速创建一条边
        """

        # 校验必填项标签非空
        if not label:
            raise Exception("标签为空！")

        # 校验边是否已经存在
        edge_count = con.execCypher(f"MATCH (a:{a_label})-[e]-(b:{b_label}) WHERE id(a) = {a_id} AND id(b) = {b_id} RETURN e").rowcount
        if edge_count > 0:
            raise Exception("边已存在！")

        # 创建边
        properties_str = AgClient.format_properties(properties)
        edge = con.execCypher(
            f"MATCH (a:{a_label}), (b:{b_label}) WHERE id(a) = {a_id} AND id(b) = {b_id} CREATE (a)-[e:{label} {properties_str}]->(b) RETURN e").fetchone()

        # 提交事务关闭连接
        con.commit()
        con.close()

        return AgClient.to_dict(edge)
