import os

NORMAL = "normal"
ABNORMAL = "abnormal"
NOT_INSTALLED = "not_installed"

SIDECAR_STATUS_ENUM = {
    NORMAL: "正常",
    ABNORMAL: "异常",
    NOT_INSTALLED: "未安装",
}

# 本服务的地址
LOCAL_HOST = os.getenv("WEB_SERVER_URL")

LINUX_OS = "linux"
WINDOWS_OS = "windows"

W_SIDECAR_DOWNLOAD_URL = f"{LOCAL_HOST}/openapi/sidecar/download_file/?file_name=sidecar_windows.zip"
L_SIDECAR_DOWNLOAD_URL = f"{LOCAL_HOST}/openapi/sidecar/download_file/?file_name=sidecar_linux.tar.gz"
L_INSTALL_DOWNLOAD_URL = f"{LOCAL_HOST}/openapi/sidecar/download_file/?file_name=install_sidecar.sh"
