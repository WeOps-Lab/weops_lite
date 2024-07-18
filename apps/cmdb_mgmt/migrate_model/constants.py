CLASSIFICATIONS = [
    {
        "classification_id": "biz_manage",
        "classification_name": "应用管理",
    },
    {
        "classification_id": "host_manage",
        "classification_name": "主机管理",
    },
    {
        "classification_id": "database",
        "classification_name": "数据库",
    },
    {
        "classification_id": "middleware",
        "classification_name": "中间件",
    },
    {
        "classification_id": "device",
        "classification_name": "网络设备",
    },
    {
        "classification_id": "k8s",
        "classification_name": "K8S",
    },
    {
        "classification_id": "qcloud",
        "classification_name": "腾讯云",
    },
    {
        "classification_id": "vmware",
        "classification_name": "VMware",
    },
    {
        "classification_id": "aliyun",
        "classification_name": "阿里云",
    },
    {
        "classification_id": "huaweicloud",
        "classification_name": "华为云",
    },
    {
        "classification_id": "system_service",
        "classification_name": "系统服务",
    },
    {
        "classification_id": "docker",
        "classification_name": "Docker",
    },
    {
        "classification_id": "credential_manage",
        "classification_name": "凭据管理",
    }
]

MODELS = [
    {
        "icn": "cc-mongodb_MongoDB",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"数据库名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"mongodb\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mongodb\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mongodb\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mongodb\\\", \\\"attr_id\\\": \\\"database_role\\\", \\\"attr_name\\\": \\\"数据库角色\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "mongodb",
        "model_name": "MongoDB",
        "classification_id": "database"
    },
    {
        "icn": "cc-host_主机",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\"}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"内网IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"host_outerip\\\", \\\"attr_name\\\": \\\"外网IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"host_name\\\", \\\"attr_name\\\": \\\"主机名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"os_type\\\", \\\"attr_name\\\": \\\"操作系统类型\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"os_version\\\", \\\"attr_name\\\": \\\"操作系统版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"os_bit\\\", \\\"attr_name\\\": \\\"操作系统位数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"cpu\\\", \\\"attr_name\\\": \\\"CPU逻辑核心数\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"cpu_module\\\", \\\"attr_name\\\": \\\"CPU型号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"cpu_architecture\\\", \\\"attr_name\\\": \\\"CPU架构\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"disk\\\", \\\"attr_name\\\": \\\"磁盘容量\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"mem\\\", \\\"attr_name\\\": \\\"内存容量\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"mac\\\", \\\"attr_name\\\": \\\"内网MAC地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"outer_mac\\\", \\\"attr_name\\\": \\\"外网MAC\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"operator\\\", \\\"attr_name\\\": \\\"维护人\\\", \\\"attr_type\\\": \\\"user\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}, {\\\"id\\\": \\\"host\\\", \\\"attr_id\\\": \\\"comment\\\", \\\"attr_name\\\": \\\"备注\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "host",
        "model_name": "主机",
        "classification_id": "host_manage"
    },
    {
        "icn": "cc-router_路由器",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\"}, {\\\"id\\\": \\\"router\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"管理IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"router\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"管理端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"router\\\", \\\"attr_id\\\": \\\"snmp_version\\\", \\\"attr_name\\\": \\\"SNMP版本\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": [{\\\"id\\\": \\\"1\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"v1\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"2\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v2c\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"3\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v3\\\", \\\"type\\\": \\\"text\\\"}]}, {\\\"id\\\": \\\"router\\\", \\\"attr_id\\\": \\\"model\\\", \\\"attr_name\\\": \\\"型号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"router\\\", \\\"attr_id\\\": \\\"brand\\\", \\\"attr_name\\\": \\\"品牌\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "router",
        "model_name": "路由器",
        "classification_id": "device"
    },
    {
        "icn": "cc-pod_Pod",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"Pod名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"pod\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"pod\\\", \\\"attr_id\\\": \\\"Limit_CPU\\\", \\\"attr_name\\\": \\\"CPU（limit）\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"pod\\\", \\\"attr_id\\\": \\\"Limit_Memory\\\", \\\"attr_name\\\": \\\"内存（limit）\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"pod\\\", \\\"attr_id\\\": \\\"Request_CPU\\\", \\\"attr_name\\\": \\\"CPU （request）\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"pod\\\", \\\"attr_id\\\": \\\"Request_Memory\\\", \\\"attr_name\\\": \\\"内存（request）\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}]",
        "model_id": "pod",
        "model_name": "Pod",
        "classification_id": "k8s"
    },
    {
        "icn": "cc-k8s-workload_K8S工作负载",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"工作负载名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"workload\\\", \\\"attr_id\\\": \\\"workload_type\\\", \\\"attr_name\\\": \\\"工作负载类型\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": [{\\\"id\\\": \\\"deployment\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"Deployment\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"statefulset\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"StatefulSet\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"daemonset\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"DaemonSet\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"job\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"Job\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"cronjob\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"Cronjob\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"replicaset\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"ReplicaSet\\\", \\\"type\\\": \\\"text\\\"}]}]",
        "model_id": "workload",
        "model_name": "K8S工作负载",
        "classification_id": "k8s"
    },
    {
        "icn": "cc-business_业务",
        "attrs": "[{\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"应用名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": true, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"status\\\", \\\"attr_name\\\": \\\"应用状态\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": [{\\\"id\\\": \\\"1\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"测试中\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"2\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"已上线\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"3\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"停运\\\", \\\"type\\\": \\\"text\\\"}]}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"maintainer\\\", \\\"attr_name\\\": \\\"运维人员\\\", \\\"attr_type\\\": \\\"user\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"developer\\\", \\\"attr_name\\\": \\\"开发人员\\\", \\\"attr_type\\\": \\\"user\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"productor\\\", \\\"attr_name\\\": \\\"产品人员\\\", \\\"attr_type\\\": \\\"user\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"tester\\\", \\\"attr_name\\\": \\\"测试人员\\\", \\\"attr_type\\\": \\\"user\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}, {\\\"id\\\": \\\"biz\\\", \\\"attr_id\\\": \\\"description\\\", \\\"attr_name\\\": \\\"应用描述\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "biz",
        "model_name": "应用",
        "classification_id": "biz_manage"
    },
    {
        "icn": "cc-mysql_Mysql",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"数据库名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"数据库版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"enable_binlog\\\", \\\"attr_name\\\": \\\"是否开启binlog\\\", \\\"attr_type\\\": \\\"bool\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": false}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"max_conn\\\", \\\"attr_name\\\": \\\"最大连接数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"max_mem\\\", \\\"attr_name\\\": \\\"最大内存\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql\\\", \\\"attr_id\\\": \\\"database_role\\\", \\\"attr_name\\\": \\\"数据库角色\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "mysql",
        "model_name": "MySQL",
        "classification_id": "database"
    },
    {
        "icn": "cc-nginx_nginx",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\"}, {\\\"id\\\": \\\"nginx\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"nginx\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"监听端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"nginx\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"nginx\\\", \\\"attr_id\\\": \\\"bin_path\\\", \\\"attr_name\\\": \\\"bin路径\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"nginx\\\", \\\"attr_id\\\": \\\"server_name\\\", \\\"attr_name\\\": \\\"域名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"nginx\\\", \\\"attr_id\\\": \\\"ssl_version\\\", \\\"attr_name\\\": \\\"ssl版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "nginx",
        "model_name": "Nginx",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-balance_负载均衡",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\"}, {\\\"id\\\": \\\"loadbalance\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"管理IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"loadbalance\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"管理端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"loadbalance\\\", \\\"attr_id\\\": \\\"snmp_version\\\", \\\"attr_name\\\": \\\"SNMP版本\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": [{\\\"id\\\": \\\"1\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"v1\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"2\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v2c\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"3\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v3\\\", \\\"type\\\": \\\"text\\\"}]}, {\\\"id\\\": \\\"loadbalance\\\", \\\"attr_id\\\": \\\"model\\\", \\\"attr_name\\\": \\\"型号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"loadbalance\\\", \\\"attr_id\\\": \\\"brand\\\", \\\"attr_name\\\": \\\"品牌\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "loadbalance",
        "model_name": "负载均衡",
        "classification_id": "device"
    },
    {
        "icn": "cc-k8s-namespace_K8S命名空间",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "namespace",
        "model_name": "K8S命名空间",
        "classification_id": "k8s"
    },
    {
        "icn": "cc-k8s-cluster_K8S集群",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "k8s_cluster",
        "model_name": "K8S集群",
        "classification_id": "k8s"
    },
    {
        "icn": "cc-switch2_交换机",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\"}, {\\\"id\\\": \\\"switch\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"管理IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"switch\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"管理端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"switch\\\", \\\"attr_id\\\": \\\"model\\\", \\\"attr_name\\\": \\\"型号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"switch\\\", \\\"attr_id\\\": \\\"snmp_version\\\", \\\"attr_name\\\": \\\"SNMP版本\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": [{\\\"id\\\": \\\"1\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v1\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"2\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"v2c\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"3\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v3\\\", \\\"type\\\": \\\"text\\\"}]}, {\\\"id\\\": \\\"switch\\\", \\\"attr_id\\\": \\\"brand\\\", \\\"attr_name\\\": \\\"品牌\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "switch",
        "model_name": "交换机",
        "classification_id": "device"
    },
    {
        "icn": "cc-node_Node",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"node\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"node\\\", \\\"attr_id\\\": \\\"role\\\", \\\"attr_name\\\": \\\"角色\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"node\\\", \\\"attr_id\\\": \\\"CPU\\\", \\\"attr_name\\\": \\\"CPU总容量\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"node\\\", \\\"attr_id\\\": \\\"Memory\\\", \\\"attr_name\\\": \\\"内存总容量\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"node\\\", \\\"attr_id\\\": \\\"os_version\\\", \\\"attr_name\\\": \\\"操作系统版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"node\\\", \\\"attr_id\\\": \\\"kubelet_version\\\", \\\"attr_name\\\": \\\"kubelet版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"node\\\", \\\"attr_id\\\": \\\"Storage\\\", \\\"attr_name\\\": \\\"存储总容量\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"node\\\", \\\"attr_id\\\": \\\"kernel_version\\\", \\\"attr_name\\\": \\\"内核版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"node\\\", \\\"attr_id\\\": \\\"container_runtime_version\\\", \\\"attr_name\\\": \\\"容器运行时版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"node\\\", \\\"attr_id\\\": \\\"pod_cidr\\\", \\\"attr_name\\\": \\\"Pod IP地址段\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "node",
        "model_name": "Node",
        "classification_id": "k8s"
    },
    {
        "icn": "cc-oracle_oracle",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"数据库名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"sid\\\", \\\"attr_name\\\": \\\"SID\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"max_mem\\\", \\\"attr_name\\\": \\\"最大内存\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"max_conn\\\", \\\"attr_name\\\": \\\"最大连接数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"数据库版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle\\\", \\\"attr_id\\\": \\\"database_role\\\", \\\"attr_name\\\": \\\"数据库角色\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": false, \\\"option\\\": \\\"\\\"}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "oracle",
        "model_name": "Oracle",
        "classification_id": "database"
    },
    {
        "icn": "cc-module_模块",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"模块名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"module\\\", \\\"attr_id\\\": \\\"module_type\\\", \\\"attr_name\\\": \\\"模块类型\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"module\\\", \\\"attr_id\\\": \\\"operator\\\", \\\"attr_name\\\": \\\"主要维护人\\\", \\\"attr_type\\\": \\\"user\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}, {\\\"id\\\": \\\"module\\\", \\\"attr_id\\\": \\\"bak_operator\\\", \\\"attr_name\\\": \\\"备份维护人\\\", \\\"attr_type\\\": \\\"user\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}]",
        "model_id": "module",
        "model_name": "模块",
        "classification_id": "biz_manage"
    },
    {
        "icn": "cc-cloud-plat_云平台",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "qcloud_account",
        "model_name": "腾讯云账号",
        "classification_id": "qcloud"
    },
    {
        "icn": "cc-host_主机",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"资源名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"resource_id\\\", \\\"attr_name\\\": \\\"资源ID\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"内网IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"public_ip\\\", \\\"attr_name\\\": \\\"公网IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"region\\\", \\\"attr_name\\\": \\\"地域\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"zone\\\", \\\"attr_name\\\": \\\"可用区\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"vpc\\\", \\\"attr_name\\\": \\\"VPC\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"status\\\", \\\"attr_name\\\": \\\"状态\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"instance_type\\\", \\\"attr_name\\\": \\\"规格\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"os_name\\\", \\\"attr_name\\\": \\\"操作系统名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"vcpus\\\", \\\"attr_name\\\": \\\"vCPU数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"memory\\\", \\\"attr_name\\\": \\\"内存容量\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"charge_type\\\", \\\"attr_name\\\": \\\"付费类型\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"create_time\\\", \\\"attr_name\\\": \\\"创建时间\\\", \\\"attr_type\\\": \\\"time\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}, {\\\"id\\\": \\\"qcloud_cvm\\\", \\\"attr_id\\\": \\\"expired_time\\\", \\\"attr_name\\\": \\\"到期时间\\\", \\\"attr_type\\\": \\\"time\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}]",
        "model_id": "qcloud_cvm",
        "model_name": "腾讯云CVM",
        "classification_id": "qcloud"
    },
    {
        "icn": "cc-vmware_VMware",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"vmware_vc\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_vc\\\", \\\"attr_id\\\": \\\"vc_version\\\", \\\"attr_name\\\": \\\"VC版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "vmware_vc",
        "model_name": "vCenter",
        "classification_id": "vmware"
    },
    {
        "icn": "cc-host_主机",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"资源名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"resource_id\\\", \\\"attr_name\\\": \\\"资源ID\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"内网IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"public_ip\\\", \\\"attr_name\\\": \\\"公网IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"region\\\", \\\"attr_name\\\": \\\"地域\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"zone\\\", \\\"attr_name\\\": \\\"可用区\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"vpc\\\", \\\"attr_name\\\": \\\"VPC\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"status\\\", \\\"attr_name\\\": \\\"状态\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"instance_type\\\", \\\"attr_name\\\": \\\"规格\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"os_name\\\", \\\"attr_name\\\": \\\"操作系统名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"vcpus\\\", \\\"attr_name\\\": \\\"vCPU数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"memory\\\", \\\"attr_name\\\": \\\"内存容量\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"charge_type\\\", \\\"attr_name\\\": \\\"付费类型\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"create_time\\\", \\\"attr_name\\\": \\\"创建时间\\\", \\\"attr_type\\\": \\\"time\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}, {\\\"id\\\": \\\"aliyun_ecs\\\", \\\"attr_id\\\": \\\"expired_time\\\", \\\"attr_name\\\": \\\"到期时间\\\", \\\"attr_type\\\": \\\"time\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}]",
        "model_id": "aliyun_ecs",
        "model_name": "阿里云ECS",
        "classification_id": "aliyun"
    },
    {
        "icn": "cc-host_主机",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"虚拟机名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"vmware_vm\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_vm\\\", \\\"attr_id\\\": \\\"resource_id\\\", \\\"attr_name\\\": \\\"资源ID\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_vm\\\", \\\"attr_id\\\": \\\"os_name\\\", \\\"attr_name\\\": \\\"操作系统名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_vm\\\", \\\"attr_id\\\": \\\"vcpus\\\", \\\"attr_name\\\": \\\"vCPU数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_vm\\\", \\\"attr_id\\\": \\\"memory\\\", \\\"attr_name\\\": \\\"内存容量\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "vmware_vm",
        "model_name": "VMware虚拟机",
        "classification_id": "vmware"
    },
    {
        "icn": "cc-cloud-plat_云平台",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "aliyun_account",
        "model_name": "阿里云账号",
        "classification_id": "aliyun"
    },
    {
        "icn": "cc-esxi-host_ESXI",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"vmware_esxi\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_esxi\\\", \\\"attr_id\\\": \\\"resource_id\\\", \\\"attr_name\\\": \\\"资源ID\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_esxi\\\", \\\"attr_id\\\": \\\"cpu_model\\\", \\\"attr_name\\\": \\\"CPU型号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_esxi\\\", \\\"attr_id\\\": \\\"cpu_cores\\\", \\\"attr_name\\\": \\\"CPU核数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_esxi\\\", \\\"attr_id\\\": \\\"vcpus\\\", \\\"attr_name\\\": \\\"vCPU数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_esxi\\\", \\\"attr_id\\\": \\\"memory\\\", \\\"attr_name\\\": \\\"内存容量\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_esxi\\\", \\\"attr_id\\\": \\\"esxi_version\\\", \\\"attr_name\\\": \\\"ESXi版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "vmware_esxi",
        "model_name": "ESXi",
        "classification_id": "vmware"
    },
    {
        "icn": "cc-cloud-plat_云平台",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "huaweicloud_account",
        "model_name": "华为云账号",
        "classification_id": "huaweicloud"
    },
    {
        "icn": "cc-storage_存储设备",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"资源名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"vmware_ds\\\", \\\"attr_id\\\": \\\"resource_id\\\", \\\"attr_name\\\": \\\"资源ID\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_ds\\\", \\\"attr_id\\\": \\\"system_type\\\", \\\"attr_name\\\": \\\"文件系统类型\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_ds\\\", \\\"attr_id\\\": \\\"storage\\\", \\\"attr_name\\\": \\\"总容量\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"vmware_ds\\\", \\\"attr_id\\\": \\\"url\\\", \\\"attr_name\\\": \\\"URL\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "vmware_ds",
        "model_name": "VMware数据存储",
        "classification_id": "vmware"
    },
    {
        "icn": "cc-sql-server_SQL server",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"数据库名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"数据库版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"max_conn\\\", \\\"attr_name\\\": \\\"最大连接数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"max_mem\\\", \\\"attr_name\\\": \\\"最大内存\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"order_rule\\\", \\\"attr_name\\\": \\\"排序规则\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql\\\", \\\"attr_id\\\": \\\"ha_mode\\\", \\\"attr_name\\\": \\\"高可用模式\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "mssql",
        "model_name": "MSSQL",
        "classification_id": "database"
    },
    {
        "icn": "cc-tomcat_Tomcat",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\"}, {\\\"id\\\": \\\"tomcat\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"tomcat\\\", \\\"attr_id\\\": \\\"catalina_path\\\", \\\"attr_name\\\": \\\"catalina路径\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"tomcat\\\", \\\"attr_id\\\": \\\"version_path\\\", \\\"attr_name\\\": \\\"version路径\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"tomcat\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"tomcat\\\", \\\"attr_id\\\": \\\"java_version\\\", \\\"attr_name\\\": \\\"jdk版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"tomcat\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "tomcat",
        "model_name": "Tomcat",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-apache_Apache",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\"}, {\\\"id\\\": \\\"apache\\\", \\\"attr_id\\\": \\\"httpd_path\\\", \\\"attr_name\\\": \\\"httpd路径\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"apache\\\", \\\"attr_id\\\": \\\"httpd_conf_path\\\", \\\"attr_name\\\": \\\"httpd配置文件路径\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"apache\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"apache\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"apache\\\", \\\"attr_id\\\": \\\"doc_root\\\", \\\"attr_name\\\": \\\"文档根路径\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"apache\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "apache",
        "model_name": "Apache",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-host_主机",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"资源名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"resource_id\\\", \\\"attr_name\\\": \\\"资源ID\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"内网IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"public_ip\\\", \\\"attr_name\\\": \\\"公网IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"region\\\", \\\"attr_name\\\": \\\"地域\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"zone\\\", \\\"attr_name\\\": \\\"可用区\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"vpc\\\", \\\"attr_name\\\": \\\"VPC\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"status\\\", \\\"attr_name\\\": \\\"状态\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"instance_type\\\", \\\"attr_name\\\": \\\"规格\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"os_name\\\", \\\"attr_name\\\": \\\"操作系统名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"vcpus\\\", \\\"attr_name\\\": \\\"vCPU数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"memory\\\", \\\"attr_name\\\": \\\"内存容量\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"charge_type\\\", \\\"attr_name\\\": \\\"付费类型\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"create_time\\\", \\\"attr_name\\\": \\\"创建时间\\\", \\\"attr_type\\\": \\\"time\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}, {\\\"id\\\": \\\"huaweicloud_ecs\\\", \\\"attr_id\\\": \\\"expired_time\\\", \\\"attr_name\\\": \\\"到期时间\\\", \\\"attr_type\\\": \\\"time\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}]",
        "model_id": "huaweicloud_ecs",
        "model_name": "华为云ECS",
        "classification_id": "huaweicloud"
    },
    {
        "icn": "cc-network-manage_网关",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"域名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"domain\\\", \\\"attr_id\\\": \\\"registration_date\\\", \\\"attr_name\\\": \\\"注册时间\\\", \\\"attr_type\\\": \\\"time\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}, {\\\"id\\\": \\\"domain\\\", \\\"attr_id\\\": \\\"expiration_time\\\", \\\"attr_name\\\": \\\"到期时间\\\", \\\"attr_type\\\": \\\"time\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}, {\\\"id\\\": \\\"domain\\\", \\\"attr_id\\\": \\\"owner\\\", \\\"attr_name\\\": \\\"负责人\\\", \\\"attr_type\\\": \\\"user\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}]",
        "model_id": "domain",
        "model_name": "域名",
        "classification_id": "system_service"
    },
    {
        "icn": "cc-firewall_防火墙",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\"}, {\\\"id\\\": \\\"firewall\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"管理IP\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"firewall\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"管理端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"firewall\\\", \\\"attr_id\\\": \\\"model\\\", \\\"attr_name\\\": \\\"型号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"firewall\\\", \\\"attr_id\\\": \\\"snmp_version\\\", \\\"attr_name\\\": \\\"SNMP版本\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": [{\\\"id\\\": \\\"1\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"v1\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"2\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v2c\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"3\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"v3\\\", \\\"type\\\": \\\"text\\\"}]}, {\\\"id\\\": \\\"firewall\\\", \\\"attr_id\\\": \\\"brand\\\", \\\"attr_name\\\": \\\"品牌\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "firewall",
        "model_name": "防火墙",
        "classification_id": "device"
    },
    {
        "icn": "cc-redis_redis",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"redis\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"redis\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"redis\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"redis\\\", \\\"attr_id\\\": \\\"max_conn\\\", \\\"attr_name\\\": \\\"最大连接数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"redis\\\", \\\"attr_id\\\": \\\"max_mem\\\", \\\"attr_name\\\": \\\"最大内存\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"redis\\\", \\\"attr_id\\\": \\\"database_role\\\", \\\"attr_name\\\": \\\"数据库角色\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "redis",
        "model_name": "REDIS",
        "classification_id": "database"
    },
    {
        "icn": "cc-db-cluster_数据库集群",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"db_cluster\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"db_cluster\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"db_cluster\\\", \\\"attr_id\\\": \\\"type\\\", \\\"attr_name\\\": \\\"集群类型\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": [{\\\"id\\\": \\\"1\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"Oracle 集群\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"2\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"MSSQL集群\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"3\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"MySQL集群\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"4\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"Redis集群\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"5\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"Mongodb集群\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"6\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"ElasticSearch集群\\\", \\\"type\\\": \\\"text\\\"}, {\\\"id\\\": \\\"7\\\", \\\"is_default\\\": false, \\\"name\\\": \\\"PostgreSQL集群\\\", \\\"type\\\": \\\"text\\\"}]}]",
        "model_id": "db_cluster",
        "model_name": "数据库集群",
        "classification_id": "database"
    },
    {
        "icn": "cc-default_默认",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"db2\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"db2\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"db2\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"db2\\\", \\\"attr_id\\\": \\\"database_role\\\", \\\"attr_name\\\": \\\"数据库角色\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "db2",
        "model_name": "DB2",
        "classification_id": "database"
    },
    {
        "icn": "cc-postgresql_PostgreSQL",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"postgresql\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"postgresql\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"postgresql\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "postgresql",
        "model_name": "PostgreSQL",
        "classification_id": "database"
    },
    {
        "icn": "cc-default_默认",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"elasticsearch\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"elasticsearch\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"elasticsearch\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"elasticsearch\\\", \\\"attr_id\\\": \\\"database_role\\\", \\\"attr_name\\\": \\\"数据库角色\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "elasticsearch",
        "model_name": "ElasticSearch",
        "classification_id": "database"
    },
    {
        "icn": "cc-iis_IIS",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"iis\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"iis\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "iis",
        "model_name": "IIS",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-default_默认",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"rabbitmq\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"rabbitmq\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"rabbitmq\\\", \\\"attr_id\\\": \\\"allport\\\", \\\"attr_name\\\": \\\"所有端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"rabbitmq\\\", \\\"attr_id\\\": \\\"node_name\\\", \\\"attr_name\\\": \\\"节点名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"rabbitmq\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"rabbitmq\\\", \\\"attr_id\\\": \\\"erlang_version\\\", \\\"attr_name\\\": \\\"erlange版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"rabbitmq\\\", \\\"attr_id\\\": \\\"java_version\\\", \\\"attr_name\\\": \\\"java版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "rabbitmq",
        "model_name": "RabbitMQ",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-weblogic_weblogic",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}]",
        "model_id": "weblogic",
        "model_name": "WebLogic",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-default_默认",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"ibmmq\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "ibmmq",
        "model_name": "IBM MQ",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-default_默认",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"zookeeper\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "zookeeper",
        "model_name": "ZooKeeper",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-default_默认",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"nacos\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "nacos",
        "model_name": "Nacos",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-default_默认",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"实例名\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"minio\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "minio",
        "model_name": "Minio",
        "classification_id": "middleware"
    },
    {
        "icn": "cc-node_Node",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"容器名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"dockercontainer\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"dockercontainer\\\", \\\"attr_id\\\": \\\"Image\\\", \\\"attr_name\\\": \\\"容器镜像\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"dockercontainer\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"容器版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"dockercontainer\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"dockercontainer\\\", \\\"attr_id\\\": \\\"cpu_limit\\\", \\\"attr_name\\\": \\\"CPU限制\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}, {\\\"id\\\": \\\"dockercontainer\\\", \\\"attr_id\\\": \\\"memory_limit\\\", \\\"attr_name\\\": \\\"内存限制\\\", \\\"attr_type\\\": \\\"int\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": {\\\"min\\\": 0, \\\"max\\\": 0}}]",
        "model_id": "dockercontainer",
        "model_name": "Docker容器",
        "classification_id": "docker"
    },
    {
        "icn": "cc-default_默认",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"凭据名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"mysql_credential\\\", \\\"attr_id\\\": \\\"account\\\", \\\"attr_name\\\": \\\"账号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql_credential\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mysql_credential\\\", \\\"attr_id\\\": \\\"password\\\", \\\"attr_name\\\": \\\"密码\\\", \\\"attr_type\\\": \\\"pwd\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}]",
        "model_id": "mysql_credential",
        "model_name": "MySQL凭据",
        "model_type": "credential",
        "classification_id": "credential_manage"
    },
    {
        "icn": "cc-default_默认",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"凭据名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"oracle_credential\\\", \\\"attr_id\\\": \\\"server_name\\\", \\\"attr_name\\\": \\\"服务名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle_credential\\\", \\\"attr_id\\\": \\\"account\\\", \\\"attr_name\\\": \\\"账号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle_credential\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"oracle_credential\\\", \\\"attr_id\\\": \\\"password\\\", \\\"attr_name\\\": \\\"密码\\\", \\\"attr_type\\\": \\\"pwd\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}]",
        "model_id": "oracle_credential",
        "model_name": "Oracle凭据",
        "model_type": "credential",
        "classification_id": "credential_manage"
    },
    {
        "icn": "cc-default_默认",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"凭据名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"mssql_credential\\\", \\\"attr_id\\\": \\\"server_name\\\", \\\"attr_name\\\": \\\"服务名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql_credential\\\", \\\"attr_id\\\": \\\"account\\\", \\\"attr_name\\\": \\\"账号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql_credential\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"mssql_credential\\\", \\\"attr_id\\\": \\\"password\\\", \\\"attr_name\\\": \\\"密码\\\", \\\"attr_type\\\": \\\"pwd\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}]",
        "model_id": "mssql_credential",
        "model_name": "MSSQL凭据",
        "model_type": "credential",
        "classification_id": "credential_manage"
    },
    {
        "icn": "cc-default_默认",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"凭据名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"redis_credential\\\", \\\"attr_id\\\": \\\"account\\\", \\\"attr_name\\\": \\\"账号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"redis_credential\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"redis_credential\\\", \\\"attr_id\\\": \\\"password\\\", \\\"attr_name\\\": \\\"密码\\\", \\\"attr_type\\\": \\\"pwd\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}]",
        "model_id": "redis_credential",
        "model_name": "Redis凭据",
        "model_type": "credential",
        "classification_id": "credential_manage"
    },
    {
        "icn": "cc-default_默认",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"凭据名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"host_credential\\\", \\\"attr_id\\\": \\\"account\\\", \\\"attr_name\\\": \\\"账号\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host_credential\\\", \\\"attr_id\\\": \\\"protocol\\\", \\\"attr_name\\\": \\\"协议\\\", \\\"attr_type\\\": \\\"enum\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": [{\\\"id\\\": \\\"1\\\", \\\"is_default\\\": true, \\\"name\\\": \\\"SSH\\\", \\\"type\\\": \\\"text\\\"}]}, {\\\"id\\\": \\\"host_credential\\\", \\\"attr_id\\\": \\\"port\\\", \\\"attr_name\\\": \\\"端口\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"host_credential\\\", \\\"attr_id\\\": \\\"password\\\", \\\"attr_name\\\": \\\"密码\\\", \\\"attr_type\\\": \\\"pwd\\\", \\\"is_required\\\": true, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true}]",
        "model_id": "host_credential",
        "model_name": "主机凭据",
        "model_type": "credential",
        "classification_id": "credential_manage"
    },
    {
        "icn": "cc-node_Node",
        "attrs": "[{\\\"attr_id\\\": \\\"inst_name\\\", \\\"attr_name\\\": \\\"Docker名称\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_only\\\": true, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": {}, \\\"attr_group\\\": \\\"\\\", \\\"is_pre\\\": true}, {\\\"attr_id\\\": \\\"organization\\\", \\\"attr_name\\\": \\\"所属组织\\\", \\\"attr_type\\\": \\\"organization\\\", \\\"is_only\\\": false, \\\"is_required\\\": true, \\\"editable\\\": true, \\\"option\\\": [], \\\"attr_group\\\": \\\"default\\\", \\\"is_pre\\\": true}, {\\\"id\\\": \\\"docker\\\", \\\"attr_id\\\": \\\"ip_addr\\\", \\\"attr_name\\\": \\\"IP地址\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"docker\\\", \\\"attr_id\\\": \\\"version\\\", \\\"attr_name\\\": \\\"版本\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"docker\\\", \\\"attr_id\\\": \\\"memory\\\", \\\"attr_name\\\": \\\"内存\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}, {\\\"id\\\": \\\"docker\\\", \\\"attr_id\\\": \\\"cpu\\\", \\\"attr_name\\\": \\\"CPU核数\\\", \\\"attr_type\\\": \\\"str\\\", \\\"is_required\\\": false, \\\"attr_group\\\": \\\"\\\", \\\"is_only\\\": false, \\\"editable\\\": true, \\\"option\\\": \\\"\\\"}]",
        "model_id": "docker",
        "model_name": "Docker",
        "model_type": "base",
        "classification_id": "docker"
    }
]

ASSOCIATIONS = [
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'db_cluster',
        'src_model_id': 'mongodb',
        'model_asst_id': 'mongodb_belong_db_cluster'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'mongodb',
        'model_asst_id': 'mongodb_install_on_host'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'module',
        'src_model_id': 'router',
        'model_asst_id': 'router_belong_module'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'biz',
        'src_model_id': 'router',
        'model_asst_id': 'router_belong_biz'
    },
    {
        'asst_id': 'group',
        'mapping': 'n:n',
        'dst_model_id': 'namespace',
        'src_model_id': 'workload',
        'model_asst_id': 'workload_group_namespace'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'namespace',
        'src_model_id': 'workload',
        'model_asst_id': 'workload_belong_namespace'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'db_cluster',
        'src_model_id': 'mysql',
        'model_asst_id': 'mysql_belong_db_cluster'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'mysql',
        'model_asst_id': 'mysql_install_on_host'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'nginx',
        'model_asst_id': 'nginx_install_on_host'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'module',
        'src_model_id': 'loadbalance',
        'model_asst_id': 'loadbalance_belong_module'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'biz',
        'src_model_id': 'loadbalance',
        'model_asst_id': 'loadbalance_belong_biz'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'k8s_cluster',
        'src_model_id': 'namespace',
        'model_asst_id': 'namespace_belong_k8s_cluster'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'biz',
        'src_model_id': 'namespace',
        'model_asst_id': 'namespace_belong_biz'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'biz',
        'src_model_id': 'k8s_cluster',
        'model_asst_id': 'k8s_cluster_belong_biz'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'module',
        'src_model_id': 'switch',
        'model_asst_id': 'switch_belong_module'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'biz',
        'src_model_id': 'switch',
        'model_asst_id': 'switch_belong_biz'
    },
    {
        'asst_id': 'group',
        'mapping': 'n:n',
        'dst_model_id': 'k8s_cluster',
        'src_model_id': 'node',
        'model_asst_id': 'node_group_k8s_cluster'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'db_cluster',
        'src_model_id': 'oracle',
        'model_asst_id': 'oracle_belong_db_cluster'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'oracle',
        'model_asst_id': 'oracle_install_on_host'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'qcloud_account',
        'src_model_id': 'qcloud_cvm',
        'model_asst_id': 'qcloud_cvm_belong_qcloud_account'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'aliyun_account',
        'src_model_id': 'aliyun_ecs',
        'model_asst_id': 'aliyun_ecs_belong_aliyun_account'
    },
    {
        'asst_id': 'default',
        'mapping': 'n:n',
        'dst_model_id': 'vmware_ds',
        'src_model_id': 'vmware_vm',
        'model_asst_id': 'vmware_vm_default_vmware_ds'
    },
    {
        'asst_id': 'run',
        'mapping': 'n:n',
        'dst_model_id': 'vmware_esxi',
        'src_model_id': 'vmware_vm',
        'model_asst_id': 'vmware_vm_run_vmware_esxi'
    },
    {
        'asst_id': 'group',
        'mapping': 'n:n',
        'dst_model_id': 'vmware_vc',
        'src_model_id': 'vmware_esxi',
        'model_asst_id': 'vmware_esxi_group_vmware_vc'
    },
    {
        'asst_id': 'default',
        'mapping': 'n:n',
        'dst_model_id': 'vmware_esxi',
        'src_model_id': 'vmware_ds',
        'model_asst_id': 'vmware_ds_default_vmware_esxi'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'db_cluster',
        'src_model_id': 'mssql',
        'model_asst_id': 'mssql_belong_db_cluster'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'mssql',
        'model_asst_id': 'mssql_install_on_host'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'tomcat',
        'model_asst_id': 'tomcat_install_on_host'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'apache',
        'model_asst_id': 'apache_install_on_host'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'huaweicloud_account',
        'src_model_id': 'huaweicloud_ecs',
        'model_asst_id': 'huaweicloud_ecs_belong_huaweicloud_account'
    },
    {
        'asst_id': 'default',
        'mapping': 'n:n',
        'dst_model_id': 'biz',
        'src_model_id': 'domain',
        'model_asst_id': 'domain_default_biz'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'module',
        'src_model_id': 'firewall',
        'model_asst_id': 'firewall_belong_module'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'biz',
        'src_model_id': 'firewall',
        'model_asst_id': 'firewall_belong_biz'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'iis',
        'model_asst_id': 'iis_install_on_host'
    },
    {
        'asst_id': 'default',
        'mapping': 'n:n',
        'dst_model_id': 'redis',
        'src_model_id': 'redis_credential',
        'model_asst_id': 'redis_credential_default_redis'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'biz',
        'src_model_id': 'module',
        'model_asst_id': 'module_belong_biz'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'db2',
        'model_asst_id': 'db2_install_on_host'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'db_cluster',
        'src_model_id': 'db2',
        'model_asst_id': 'db2_belong_db_cluster'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'db_cluster',
        'src_model_id': 'postgresql',
        'model_asst_id': 'postgresql_belong_db_cluster'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'postgresql',
        'model_asst_id': 'postgresql_install_on_host'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'db_cluster',
        'src_model_id': 'elasticsearch',
        'model_asst_id': 'elasticsearch_belong_db_cluster'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'elasticsearch',
        'model_asst_id': 'elasticsearch_install_on_host'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'rabbitmq',
        'model_asst_id': 'rabbitmq_install_on_host'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'ibmmq',
        'model_asst_id': 'ibmmq_install_on_host'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'zookeeper',
        'model_asst_id': 'zookeeper_install_on_host'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'nacos',
        'model_asst_id': 'nacos_install_on_host'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'minio',
        'model_asst_id': 'minio_install_on_host'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'db_cluster',
        'src_model_id': 'redis',
        'model_asst_id': 'redis_belong_db_cluster'
    },
    {
        'asst_id': 'install_on',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'redis',
        'model_asst_id': 'redis_install_on_host'
    },
    {
        'asst_id': 'default',
        'mapping': 'n:n',
        'dst_model_id': 'mysql',
        'src_model_id': 'mysql_credential',
        'model_asst_id': 'mysql_credential_default_mysql'
    },
    {
        'asst_id': 'run',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'dockercontainer',
        'model_asst_id': 'dockercontainer_run_host'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'biz',
        'src_model_id': 'dockercontainer',
        'model_asst_id': 'dockercontainer_belong_biz'
    },
    {
        'asst_id': 'default',
        'mapping': 'n:n',
        'dst_model_id': 'mssql',
        'src_model_id': 'mssql_credential',
        'model_asst_id': 'mssql_credential_default_mssql'
    },
    {
        'asst_id': 'default',
        'mapping': 'n:n',
        'dst_model_id': 'oracle',
        'src_model_id': 'oracle_credential',
        'model_asst_id': 'oracle_credential_default_oracle'
    },
    {
        'asst_id': 'contains',
        'mapping': 'n:n',
        'dst_model_id': 'dockercontainer',
        'src_model_id': 'docker',
        'model_asst_id': 'docker_contains_dockercontainer'
    },
    {
        'asst_id': 'default',
        'mapping': 'n:n',
        'dst_model_id': 'host',
        'src_model_id': 'host_credential',
        'model_asst_id': 'host_credential_default_host'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'module',
        'src_model_id': 'host',
        'model_asst_id': 'host_belong_module'
    },
    {
        'asst_id': 'belong',
        'mapping': 'n:n',
        'dst_model_id': 'biz',
        'src_model_id': 'host',
        'model_asst_id': 'host_belong_biz'
    },
    {
        'asst_id': 'group',
        'mapping': 'n:n',
        'dst_model_id': 'workload',
        'src_model_id': 'pod',
        'model_asst_id': 'pod_group_workload'
    },
    {
        'asst_id': 'group',
        'mapping': 'n:n',
        'dst_model_id': 'namespace',
        'src_model_id': 'pod',
        'model_asst_id': 'pod_group_namespace'
    },
    {
        'asst_id': 'run',
        'mapping': 'n:n',
        'dst_model_id': 'node',
        'src_model_id': 'pod',
        'model_asst_id': 'pod_run_node'
    }
]
