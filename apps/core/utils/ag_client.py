import os
from libs import age
from apps.core.constants import GRAPH_NAME
from psycopg2 import sql

from apps.core.exceptions.base_app_exception import BaseAppException


class LocalAge(age.Age):

    @staticmethod
    def _execCypher(conn, graphName, cypherStmt, cols=None, params=None):
        if conn == None or conn.closed:
            raise age.NoConnection()
        cursor = conn.cursor()
        # clean up the string for mogrification
        cypherStmt = cypherStmt.replace("\n", "")
        cypherStmt = cypherStmt.replace("\t", "")
        cypher = cursor.mogrify(cypherStmt, params).decode('utf-8')

        preparedStmt = "SELECT * FROM age_prepare_cypher({graphName},{cypherStmt})"

        cursor = conn.cursor()
        try:
            cursor.execute(
                sql.SQL(preparedStmt).format(graphName=sql.Literal(graphName), cypherStmt=sql.Literal(cypher)))
        except SyntaxError as cause:
            conn.rollback()
            raise cause
        except Exception as cause:
            conn.rollback()
            raise age.SqlExecutionError("Execution ERR[" + str(cause) + "](" + preparedStmt + ")", cause)

        stmt = age.buildCypher(graphName, cypher, cols)

        cursor = conn.cursor()
        try:
            cursor.execute(stmt)
            return cursor
        except SyntaxError as cause:
            conn.rollback()
            raise cause
        except Exception as cause:
            conn.rollback()
            raise age.SqlExecutionError("Execution ERR[" + str(cause) + "](" + stmt + ")", cause)

    def execCypher(self, cypherStmt: str, cols: list = None, params: tuple = None):
        return self._execCypher(self.connection, self.graphName, cypherStmt, cols=cols, params=params)


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
        ag = LocalAge()
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
