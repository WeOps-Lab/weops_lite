from django.http import JsonResponse
from rest_framework import status


class WebUtils:
    @staticmethod
    def response_success(response_data={}):
        return JsonResponse({
            'result': response_data,
            'success': True,
            'messages': ''
        }, status=status.HTTP_200_OK)

    @staticmethod
    def response_error(response_data={}, error_message='', status=status.HTTP_400_BAD_REQUEST):
        return JsonResponse({
            'result': response_data,
            'success': False,
            'messages': error_message
        }, status=status)
