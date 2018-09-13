from flask import Blueprint, request
from response import ApiResponse
from exception import ApiException

bp = Blueprint('calculator', __name__)


@bp.route('/add', methods=['GET'])
def add():
    num1 = request.args.get('a', type=int)
    num2 = request.args.get('b', type=int)
    if num1 is None or num2 is None:
        raise ApiException('Two integers are expected')
    return ApiResponse({'sum': num1 + num2})