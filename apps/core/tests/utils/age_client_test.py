import logging

from apps.core.utils.age_client import AgeClient


class TestAgeClient:
    def setup_method(self):
        self.age_client = AgeClient()
        self.logger = logging.getLogger(__name__)

    def teardown_method(self):
        self.age_client.close()

    def testAgeClient(self):
        self.age_client.create_graph('test_graph')
        assert self.age_client.graph_exists('test_graph') is True

        self.logger.info(f'创建实体')
        self.age_client.cypher_transaction(
            """
            SELECT * from cypher('test_graph', $$ 
                CREATE (n:Person {name: 'Joe', title: 'Developer'}) 
            $$) as (v agtype); 
            """)
        self.age_client.cypher_transaction(
            """
            SELECT * from cypher('test_graph', $$ 
                CREATE (n:Person {name: 'Smith', title: 'Developer'}) 
            $$) as (v agtype); 
            """)
        self.age_client.cypher_transaction(
            """
            SELECT * from cypher('test_graph', $$ 
                CREATE (n:Person {name: 'Tom', title: 'Manager'}) 
                RETURN n
             $$) as (v agtype); 
            """)

        self.age_client.cypher_transaction(
            """
            SELECT * from cypher('test_graph', $$ 
                MATCH (a:Person {name: 'Joe'}), (b:Person {name: 'Smith'}) 
                CREATE (a)-[r:workWith {weight: 5}]->(b)
             $$) as (v agtype); 
            """)
        self.age_client.cypher_transaction(
            """
            SELECT * from cypher('test_graph', $$ 
                MATCH (a:Person {name: 'Smith'}), (b:Person {name: 'Tom'}) 
                CREATE (a)-[r:workWith {weight: 3}]->(b)
             $$) as (v agtype); 
            """)

        result = self.age_client.cypher_query("""
            SELECT * from cypher('test_graph', $$
                MATCH (n) RETURN n
            $$) as (v agtype); 
        """)
        logging.info(result)

        result = self.age_client.cypher_query("""
            SELECT * from cypher('test_graph', $$
                MATCH p=()-[]->() RETURN p LIMIT 10
            $$) as (v agtype); 
        """)
        logging.info(result)

        result = self.age_client.cypher_query("""
            SELECT * from cypher('test_graph', $$
                 MATCH p=(a)-[b]->(c) RETURN a.name, label(b), c.name 
            $$) as (a agtype, b agtype, c agtype); 
        """)
        logging.info(result)

        self.age_client.cypher_query("""
                  SELECT * from cypher('test_graph', $$
                      MATCH (n) 
                      DETACH DELETE n
                  $$) as (v agtype); 
              """)
        self.age_client.delete_graph('test_graph')
        assert self.age_client.graph_exists('test_graph') is False
