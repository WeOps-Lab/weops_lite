import pytest

from apps.system_mgmt.models.syssetting import SysSetting


class TestSysSetting:
    @pytest.fixture
    def sys_setting(self, mocker):
        sys_setting = SysSetting()
        sys_setting._meta = mocker.Mock()
        sys_setting._meta.verbose_name = "测试"
        sys_setting.desc = "描述"
        sys_setting.value = "测试值"
        return sys_setting

    @pytest.mark.parametrize(
        "vtype",
        [
            "string",
            "integer",
            "float",
            "datetime",
            "time",
            "date",
            "json",
            "bool",
            "default",
        ],
    )
    def test_real_value(self, sys_setting, vtype):
        sys_setting.vtype = vtype
        result = sys_setting.real_value
        assert result == "测试值"

    def test_get_ins_summary(self, sys_setting):
        result = sys_setting.get_ins_summary()
        assert result == "测试[系统设置: 描述]"

    @pytest.mark.parametrize("vtype", ["nonexistent_type"])
    def test_real_value_with_exception(self, sys_setting, vtype):
        sys_setting.vtype = vtype
        result = sys_setting.real_value
        assert result == "测试值"
