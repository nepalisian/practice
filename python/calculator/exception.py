from response import ApiResponse


class ApiException(Exception):

    def __init__(self, message, status=400):
        self.message = message
        self.status = status

    def to_response(self):
        return ApiResponse({'message': self.message },
                             status=self.status)