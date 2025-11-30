from flask import Blueprint
from flask import make_response
from flask import jsonify

BP_NAME = "user"

bp = Blueprint(BP_NAME, __name__, url_prefix=f"/api/users")

USERS_TABLE = {
    'rob': {
        'fav-color': 'red',
        'fav-ice-cream': 'vanilla'
    },
    'mandy': {
        'fav-color': 'blue',
        'fav-ice-cream': 'caramel'
    }
}

@bp.route("", methods=["GET"])
def get_users():
    return make_response(jsonify(data=list(USERS_TABLE.keys())),
    200
)


@bp.route("<user_id>", methods=["GET"])
def get_user(user_id: str):
    if user_id in USERS_TABLE:
        return make_response(jsonify(data=USERS_TABLE[user_id]), 200)
    return make_response(jsonify(error_msg="User not found"), 401)