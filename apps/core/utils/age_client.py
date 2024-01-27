import os
import pandas as pd
import psycopg2


class AgeClient(object):
    def __init__(self):
        self.client = psycopg2.connect(database=os.getenv('DB_NAME'),
                                       user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'),
                                       host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))
        with self.client.cursor() as cursor:
            cursor.execute("LOAD 'age';")
            cursor.execute("SET search_path = ag_catalog, '$user', public;")

    def close(self):
        self.client.close()

    def create_graph(self, graph_name):
        if self.graph_exists(graph_name) is False:
            self.cypher_transaction(f"SELECT * FROM ag_catalog.create_graph('{graph_name}')")

    def graph_exists(self, graph_name) -> bool:
        result = self.cypher_query(f"SELECT count(*) FROM ag_graph WHERE name='{graph_name}'")
        if result['count'][0] == 0:
            return False
        else:
            return True

    def delete_graph(self, graph_name):
        self.cypher_transaction(f"SELECT * FROM ag_catalog.drop_graph('{graph_name}', true)")

    def cypher_query(self, cypher_query):
        result = pd.read_sql_query(cypher_query, self.client)
        return result

    def cypher_transaction(self, cypher_query):
        with self.client.cursor() as cursor:
            cursor.execute(cypher_query)
            self.client.commit()

    def create_entity(self, graph_name: str, name: str, props: dict):
        cypher = f"SELECT * FROM cypher('{graph_name}', $$"
        props_str = '{'
        for key, value in props.items():
            if type(value) == str:
                props_str += f"{key}:'{value}',"
            else:
                props_str += f"{key}:{value},"
        props_str = props_str[:-1]
        props_str += "}"
        cypher += f"CREATE (:{name} {props_str})"
        cypher += f"$$) AS (result agtype);"
        self.cypher_transaction(cypher)
