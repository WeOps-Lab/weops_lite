import mimetypes
import os
import urllib.parse

from django.http import FileResponse


def download_local_file(local_path, file_name):
    """下载本地文件"""

    # 使用 mimetypes 模块来获取文件的 MIME 类型
    content_type, _ = mimetypes.guess_type(file_name)

    # 默认 MIME 类型
    if content_type is None:
        content_type = "application/octet-stream"

    # 构建文件路径
    file_path = os.path.join(local_path, file_name)

    # 构建响应对象并设置文件名和类型
    response = FileResponse(open(file_path, "rb"), content_type=content_type)

    # 文件名进行URL编码
    encoded_file_name = urllib.parse.quote(file_name)
    response["Content-Disposition"] = f'attachment; filename="{encoded_file_name}"'

    return response
