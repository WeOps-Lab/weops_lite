CLASSIFICATIONS = [
    {
        "classification_id": "biz_manage",
        "classification_name": "应用管理"
    },
    {
        "classification_id": "host_manage",
        "classification_name": "主机管理"
    },
    {
        "classification_id": "database",
        "classification_name": "数据库"
    },
    {
        "classification_id": "middleware",
        "classification_name": "中间件"
    },
    {
        "classification_id": "device",
        "classification_name": "网络设备"
    }
]

MODELS = [
    {
        "icn": "cc-host_主机",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": false, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"host_innerip\\\", \\\"attr_name\\\": \\\"内网IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"host_outerip\\\", \\\"attr_name\\\": \\\"外网IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"host_name\\\", \\\"attr_name\\\": \\\"主机名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"os_type\\\", \\\"attr_name\\\": \\\"操作系统类型\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"os_version\\\", \\\"attr_name\\\": \\\"操作系统版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"os_bit\\\", \\\"attr_name\\\": \\\"操作系统位数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"cpu\\\", \\\"attr_name\\\": \\\"CPU逻辑核心数\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"cpu_module\\\", \\\"attr_name\\\": \\\"CPU型号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"cpu_architecture\\\", \\\"attr_name\\\": \\\"CPU架构\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"mem\\\", \\\"attr_name\\\": \\\"内存容量\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"disk\\\", \\\"attr_name\\\": \\\"磁盘容量\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"mac\\\", \\\"attr_name\\\": \\\"内网MAC地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"outer_mac\\\", \\\"attr_name\\\": \\\"外网MAC\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"operator\\\", \\\"attr_name\\\": \\\"维护人\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"comment\\\", \\\"attr_name\\\": \\\"备注\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}]",
        "model_id": "host",
        "model_name": "主机",
        "classification_id": "host_manage"
    },
    {
        "icn": "cc-balance_负载均衡",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": false, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\"}, {\\\"id\\\": \\\"loadbalance\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"管理IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"loadbalance\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"管理端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"loadbalance\\\", \\\"attr_id\\\": \\\"snmp_version\\\", \\\"attr_name\\\": \\\"SNMP版本\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": [{\\\"id\\\": \\\"1\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"v1\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"2\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v2c\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"3\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v3\\\", \\\"type\\\": \\\"text\\\"}]}, {\\\"id\\\": \\\"loadbalance\\\", \\\"attr_id\\\": \\\"model\\\", \\\"attr_name\\\": \\\"型号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"loadbalance\\\", \\\"attr_id\\\": \\\"brand\\\", \\\"attr_name\\\": \\\"品牌\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}]",
        "model_id": "loadbalance",
        "model_name": "负载均衡",
        "classification_id": "device"
    },
    {
        "icn": "cc-router_路由器",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": false, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\"}, {\\\"id\\\": \\\"router\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"管理IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"router\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"管理端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"router\\\", \\\"attr_id\\\": \\\"snmp_version\\\", \\\"attr_name\\\": \\\"SNMP版本\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": [{\\\"id\\\": \\\"1\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"v1\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"2\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v2c\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"3\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v3\\\", \\\"type\\\": \\\"text\\\"}]}, {\\\"id\\\": \\\"router\\\", \\\"attr_id\\\": \\\"model\\\", \\\"attr_name\\\": \\\"型号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"router\\\", \\\"attr_id\\\": \\\"brand\\\", \\\"attr_name\\\": \\\"品牌\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}]",
        "model_id": "router",
        "model_name": "路由器",
        "classification_id": "device"
    },
    {
        "icn": "cc-mysql_Mysql",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": false, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\"}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"数据库版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"enable_binlog\\\", \\\"attr_name\\\": \\\"是否开启binlog\\\", \\\"attr_type\\\": \\\"bool\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": false}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"max_conn\\\", \\\"attr_name\\\": \\\"最大连接数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"max_mem\\\", \\\"attr_name\\\": \\\"最大内存\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"database_role\\\", \\\"attr_name\\\": \\\"数据库角色\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}]",
        "model_id": "mysql",
        "model_name": "MySQL",
        "classification_id": "database"
    },
    {
        "icn": "cc-oracle_oracle",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": false, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"sid\\\", \\\"attr_name\\\": \\\"SID\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"max_mem\\\", \\\"attr_name\\\": \\\"最大内存\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"max_conn\\\", \\\"attr_name\\\": \\\"最大连接数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"db_name\\\", \\\"attr_name\\\": \\\"数据库名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"数据库版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"database_role\\\", \\\"attr_name\\\": \\\"数据库角色\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}]",
        "model_id": "oracle",
        "model_name": "Oracle",
        "classification_id": "database"
    },
    {
        "icn": "cc-sql-server_SQL server",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": false, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"db_name\\\", \\\"attr_name\\\": \\\"数据库名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"数据库版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"max_conn\\\", \\\"attr_name\\\": \\\"最大连接数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"max_mem\\\", \\\"attr_name\\\": \\\"最大内存\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"order_rule\\\", \\\"attr_name\\\": \\\"排序规则\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"ha_mode\\\", \\\"attr_name\\\": \\\"高可用模式\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}]",
        "model_id": "mssql",
        "model_name": "MSSQL",
        "classification_id": "database"
    },
    {
        "icn": "cc-tomcat_Tomcat",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": false, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\"}, {\\\"id\\\": \\\"tomcat\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"tomcat\\\", \\\"attr_id\\\": \\\"catalina_path\\\", \\\"attr_name\\\": \\\"catalina路径\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"tomcat\\\", \\\"attr_id\\\": \\\"version_path\\\", \\\"attr_name\\\": \\\"version路径\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"tomcat\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"tomcat\\\", \\\"attr_id\\\": \\\"java_version\\\", \\\"attr_name\\\": \\\"jdk版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"tomcat\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}]",
        "model_id": "tomcat",
        "model_name": "Tomcat",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-firewall_防火墙",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": false, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\"}, {\\\"id\\\": \\\"firewall\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"管理IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"firewall\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"管理端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"firewall\\\", \\\"attr_id\\\": \\\"model\\\", \\\"attr_name\\\": \\\"型号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"firewall\\\", \\\"attr_id\\\": \\\"snmp_version\\\", \\\"attr_name\\\": \\\"SNMP版本\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": [{\\\"id\\\": \\\"1\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"v1\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"2\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v2c\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"3\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v3\\\", \\\"type\\\": \\\"text\\\"}]}, {\\\"id\\\": \\\"firewall\\\", \\\"attr_id\\\": \\\"brand\\\", \\\"attr_name\\\": \\\"品牌\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}]",
        "model_id": "firewall",
        "model_name": "防火墙",
        "classification_id": "device"
    },
    {
        "icn": "cc-apache_Apache",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": false, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\"}, {\\\"id\\\": \\\"apache\\\", \\\"attr_id\\\": \\\"httpd_path\\\", \\\"attr_name\\\": \\\"httpd路径\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"apache\\\", \\\"attr_id\\\": \\\"httpd_conf_path\\\", \\\"attr_name\\\": \\\"httpd配置文件路径\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"apache\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"apache\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"apache\\\", \\\"attr_id\\\": \\\"doc_root\\\", \\\"attr_name\\\": \\\"文档根路径\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"apache\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}]",
        "model_id": "apache",
        "model_name": "Apache",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-nginx_nginx",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": false, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\"}, {\\\"id\\\": \\\"nginx\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"nginx\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"监听端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"nginx\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"nginx\\\", \\\"attr_id\\\": \\\"bin_path\\\", \\\"attr_name\\\": \\\"bin路径\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"nginx\\\", \\\"attr_id\\\": \\\"server_name\\\", \\\"attr_name\\\": \\\"域名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"nginx\\\", \\\"attr_id\\\": \\\"ssl_version\\\", \\\"attr_name\\\": \\\"ssl版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}]",
        "model_id": "nginx",
        "model_name": "Nginx",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-switch2_交换机",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": false, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\"}, {\\\"id\\\": \\\"switch\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"管理IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"switch\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"管理端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"switch\\\", \\\"attr_id\\\": \\\"model\\\", \\\"attr_name\\\": \\\"型号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"switch\\\", \\\"attr_id\\\": \\\"snmp_version\\\", \\\"attr_name\\\": \\\"SNMP版本\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": [{\\\"id\\\": \\\"1\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v1\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"2\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"v2c\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"3\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v3\\\", \\\"type\\\": \\\"text\\\"}]}, {\\\"id\\\": \\\"switch\\\", \\\"attr_id\\\": \\\"brand\\\", \\\"attr_name\\\": \\\"品牌\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}]",
        "model_id": "switch",
        "model_name": "交换机",
        "classification_id": "device"
    },
    {
        "icn": "cc-business_业务",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": false, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\"}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"biz_name\\\", \\\"attr_name\\\": \\\"应用名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"biz_status\\\", \\\"attr_name\\\": \\\"应用状态\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": [{\\\"id\\\": \\\"1\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"测试中\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"2\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"已上线\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"3\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"停运\\\", \\\"type\\\": \\\"text\\\"}]}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"biz_maintainer\\\", \\\"attr_name\\\": \\\"运维人员\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"biz_developer\\\", \\\"attr_name\\\": \\\"开发人员\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"biz_productor\\\", \\\"attr_name\\\": \\\"产品人员\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"biz_tester\\\", \\\"attr_name\\\": \\\"测试人员\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"biz_description\\\", \\\"attr_name\\\": \\\"应用描述\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}]",
        "model_id": "biz",
        "model_name": "应用",
        "classification_id": "biz_manage"
    }
]

ASSOCIATIONS = [
    {
        "asst_id": "belong",
        "mapping": "n:n",
        "dst_model_id": "biz",
        "src_model_id": "host",
        "model_asst_id": "host_belong_biz"
    },
    {
        "asst_id": "belong",
        "mapping": "n:n",
        "dst_model_id": "biz",
        "src_model_id": "loadbalance",
        "model_asst_id": "loadbalance_belong_biz"
    },
    {
        "asst_id": "belong",
        "mapping": "n:n",
        "dst_model_id": "biz",
        "src_model_id": "router",
        "model_asst_id": "router_belong_biz"
    },
    {
        "asst_id": "belong",
        "mapping": "n:n",
        "dst_model_id": "biz",
        "src_model_id": "firewall",
        "model_asst_id": "firewall_belong_biz"
    },
    {
        "asst_id": "belong",
        "mapping": "n:n",
        "dst_model_id": "biz",
        "src_model_id": "switch",
        "model_asst_id": "switch_belong_biz"
    },
    {
        "asst_id": "install_on",
        "mapping": "n:n",
        "dst_model_id": "host",
        "src_model_id": "oracle",
        "model_asst_id": "oracle_install_on_host"
    },
    {
        "asst_id": "install_on",
        "mapping": "n:n",
        "dst_model_id": "host",
        "src_model_id": "mysql",
        "model_asst_id": "mysql_install_on_host"
    },
    {
        "asst_id": "install_on",
        "mapping": "n:n",
        "dst_model_id": "host",
        "src_model_id": "mssql",
        "model_asst_id": "mssql_install_on_host"
    },
    {
        "asst_id": "install_on",
        "mapping": "n:n",
        "dst_model_id": "host",
        "src_model_id": "tomcat",
        "model_asst_id": "tomcat_install_on_host"
    },
    {
        "asst_id": "install_on",
        "mapping": "n:n",
        "dst_model_id": "host",
        "src_model_id": "apache",
        "model_asst_id": "apache_install_on_host"
    },
    {
        "asst_id": "install_on",
        "mapping": "n:n",
        "dst_model_id": "host",
        "src_model_id": "nginx",
        "model_asst_id": "nginx_install_on_host"
    }
]
