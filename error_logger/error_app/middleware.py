import json

from django.conf import settings

from error_app.models import ErrorLog


class ErrorLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code in settings.ERROR_CODES:
            error_log = ErrorLog(
                status_code=response.status_code, error=response.content.decode()
            )
            error_log.save()

            response.status_code = 200
            response_content = {"status_code": 200, "error": response.content.decode()}
            response.content = json.dumps(response_content).encode()

        return response
