from flask import Blueprint
from flask import jsonify
from flask import request

from services.config_service import (
    obtener_configuracion,
    actualizar_configuracion
)

config_bp = Blueprint(
    "configuracion",
    __name__
)

@config_bp.route(
    "/configuracion",
    methods=["GET"]
)
def obtener():

    return jsonify(
        obtener_configuracion()
    )


@config_bp.route(
    "/configuracion",
    methods=["PUT"]
)
def actualizar():

    data = request.get_json()

    actualizar_configuracion(

        data["idioma"],

        data["tema"],

        data["comentarios_maximos"]

    )

    return jsonify({
        "success": True
    })