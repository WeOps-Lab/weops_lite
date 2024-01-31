from drf_yasg.utils import swagger_auto_schema
from rest_framework import views

from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.web_utils import WebUtils
from apps.system_mgmt.services.login_info import LoginInfo


class LoginInfoView(views.APIView):

    @swagger_auto_schema(
        operation_id="login_info",
        operation_description="用户登录之后，获取基本信息"
    )
    def get(self, request):
        data = LoginInfo().get_user_login_info(request)
        return WebUtils.response_success(data)
