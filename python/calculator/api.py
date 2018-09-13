from flask import Flask
from response import ApiResponse


class ApiFlask(Flask):
    def make_response(self, rv):
        if isinstance(rv, ApiResponse):
            return rv.to_response()
        else:
            return Flask.make_response(self, rv)
