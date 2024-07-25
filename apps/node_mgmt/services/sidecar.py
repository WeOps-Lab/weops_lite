from apps.node_mgmt.constants import L_INSTALL_DOWNLOAD_URL, L_SIDECAR_DOWNLOAD_URL, W_SIDECAR_DOWNLOAD_URL, LOCAL_HOST, \
    LINUX_OS, WINDOWS_OS
from apps.node_mgmt.models.node import Node


class Sidecar(object):
    def __init__(self, id=None):
        self.id = id
        self.node = self.get_node_obj()

    def get_node_obj(self):
        """获取节点操作系统类型"""
        if not self.id:
            return None
        obj = Node.objects.filter(id=self.id).first()
        return obj

    def get_version(self):
        """获取版本信息"""
        return

    def sync_sidecar_config(self):
        """同步sidecar的配置"""
        return

    def get_collectors(self):
        """获取采集器列表"""
        return

    def get_collector_config(self):
        """获取采集器配置"""
        return

    def get_installation_steps(self):
        """获取安装步骤"""
        local_host = LOCAL_HOST
        local_api_token = ""

        if self.node.os_type == LINUX_OS:
            return self.linux_step(self.node.node_id, local_api_token, local_host)
        elif self.node.os_type == WINDOWS_OS:
            return self.windows_step(self.node.node_id, local_api_token, local_host)

    def windows_step(self, node_id, gl_token, gl_host):
        """windows安装步骤"""

        return [
            {
                "title": "下载安装包",
                "content": "下载安装包",
                "download_url": W_SIDECAR_DOWNLOAD_URL,
            },
            {
                "title": "创建以下目录",
                "content": "c:/gse",
            },
            {
                "title": "执行安装脚本，在指定目录下安装控制器和探针",
                "content": r'.\install_sidecar.bat "{}" "{}" "{}"'.format(node_id, gl_token, gl_host),
            },
        ]

    def linux_step(self, node_id, gl_token, gl_host):
        """linux安装步骤"""

        params = [L_INSTALL_DOWNLOAD_URL, node_id, gl_token, gl_host, L_SIDECAR_DOWNLOAD_URL]
        return [
            {
                "title": "下载安装包",
                "content": 'curl -sSL {}|bash -s - -n "{}" -t "{}" -s "{}" -d "{}"'.format(*params),
            },
        ]
