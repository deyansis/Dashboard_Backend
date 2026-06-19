from flask import Blueprint
from flask import jsonify

from services.user_service import (
    obtener_usuario
)

user_bp = Blueprint(
    "usuarios",
    __name__
)

@user_bp.route(
    "/usuario",
    methods=["GET"]
)
def usuario():

    return jsonify(
        obtener_usuario()
    )