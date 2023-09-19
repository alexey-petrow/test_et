import importlib

from rest_framework import views, status
from rest_framework.response import Response


from config.settings import MODULES_DIR_NAME
from modules_app.exceptions import WrongJsonFormatApiException, ModuleApiException


class JsonHandlerAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        module_name = request.data.get('module')
        function_name = request.data.get('function')
        if module_name is None or function_name is None:
            raise WrongJsonFormatApiException()
        try:
            module = importlib.import_module(f'{MODULES_DIR_NAME}.{module_name}')
            function = getattr(module, function_name)

            result = function(request.data)
            return Response(data={'result': result},
                            status=status.HTTP_200_OK)

        except ImportError:
            raise ModuleApiException(detail=f'Unknown module {module_name}')
        except AttributeError:
            raise ModuleApiException(detail=f'Unknown function {function_name}')
