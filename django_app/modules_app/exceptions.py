from rest_framework.exceptions import APIException, status


class WrongJsonFormatApiException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'JSON file should contain fields: module, function'


class ModuleApiException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
