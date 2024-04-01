import os
import libs.age as age
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
        ag = age.Age()
        ag.connect(graph=self.graph_name, dsn=self.dsn)
        return ag

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
