import unittest
from unittest.mock import MagicMock
from apps.core.utils.ag_client import AgClient


class TestAgClient(unittest.TestCase):
    def setUp(self):
        # 创建测试图
        print("***创建测试图***")
        self.ag = AgClient("test")
        self.ag.set_graph()

    def tearDown(self):
        # 删除测试图
        print("***删除测试图***")
        self.ag.del_graph()

    def test_create_entity_success(self):

        # set测试数据
        test_data = {"label": "Model", "properties": {"entity_name": "host"}}

        # 调用被测试的方法
        result = self.ag.create_entity(self.ag.get_con(), test_data["label"], test_data["properties"])

        # 断言返回值是否符合预期
        self.assertEqual(result["label"], test_data["label"])
        self.assertEqual(result["properties"], test_data["properties"])

    def test_create_entity_duplicate_entity_name(self):
        # set测试数据
        test_data = {"label": "Model", "properties": {"entity_name": "host"}}

        # 先创建一次测试数据
        self.ag.create_entity(self.ag.get_con(), test_data["label"], test_data["properties"])

        # 调用被测试的方法，断言抛出异常
        with self.assertRaises(Exception) as context:
            self.ag.create_entity(self.ag.get_con(), test_data["label"], test_data["properties"])

        # 断言抛出的异常是否为预期异常
        self.assertEqual(str(context.exception), "实体名称重复！")

    def test_create_entity_missing_label(self):
        # set测试数据
        test_data = {"label": "", "properties": {"entity_name": "host"}}

        # 调用被测试的方法，断言抛出异常
        with self.assertRaises(Exception) as context:
            self.ag.create_entity(self.ag.get_con(), test_data["label"], test_data["properties"])

        # 断言抛出的异常是否为预期异常
        self.assertEqual(str(context.exception), "标签为空！")

    def test_create_edge_success(self):
        # set测试数据, 实体a、b, 边e
        a_data = {"label": "Model", "properties": {"entity_name": "mysql"}}
        a_result = self.ag.create_entity(self.ag.get_con(), a_data["label"], a_data["properties"])
        b_data = {"label": "Model", "properties": {"entity_name": "host"}}
        b_result = self.ag.create_entity(self.ag.get_con(), b_data["label"], b_data["properties"])

        e_data = {
            "a_id": a_result["id"],
            "a_label": a_result["label"],
            "b_id": b_result["id"],
            "b_label": b_result["label"],
            "label": "install_on",
            "properties": {"bk_obj_asst_id": "mysql_install_on_host"},
        }

        # 调用被测试的方法
        e_result = self.ag.create_edge(
            self.ag.get_con(),
            e_data["label"],
            e_data["a_id"],
            e_data["a_label"],
            e_data["b_id"],
            e_data["b_label"],
            e_data["properties"],
        )
        # 断言返回值是否符合预期
        self.assertEqual(e_result["label"], e_result["label"])
        self.assertEqual(e_result["properties"], e_result["properties"])

    def test_create_edge_edge_exists(self):
        # set测试数据, 实体a、b, 边e
        a_data = {"label": "Model", "properties": {"entity_name": "mysql"}}
        a_result = self.ag.create_entity(self.ag.get_con(), a_data["label"], a_data["properties"])
        b_data = {"label": "Model", "properties": {"entity_name": "host"}}
        b_result = self.ag.create_entity(self.ag.get_con(), b_data["label"], b_data["properties"])

        e_data = {
            "a_id": a_result["id"],
            "a_label": a_result["label"],
            "b_id": b_result["id"],
            "b_label": b_result["label"],
            "label": "install_on",
            "properties": {"bk_obj_asst_id": "mysql_install_on_host"},
        }

        # 生成测试数据
        self.ag.create_edge(
            self.ag.get_con(),
            e_data["label"],
            e_data["a_id"],
            e_data["a_label"],
            e_data["b_id"],
            e_data["b_label"],
            e_data["properties"],
        )

        # 调用被测试的方法，断言抛出异常
        with self.assertRaises(Exception) as context:
            self.ag.create_edge(
                self.ag.get_con(),
                e_data["label"],
                e_data["a_id"],
                e_data["a_label"],
                e_data["b_id"],
                e_data["b_label"],
                e_data["properties"],
            )

        # 断言抛出的异常是否为预期异常
        self.assertEqual(str(context.exception), "边已存在！")

    def test_create_edge_missing_label(self):
        # 调用被测试的方法，断言抛出异常
        with self.assertRaises(Exception) as context:
            self.ag.create_edge(self.ag.get_con(), "", 1, "Person", 2, "Person", {"strength": 5})

        # 断言抛出的异常是否为预期异常
        self.assertEqual(str(context.exception), "标签为空！")
