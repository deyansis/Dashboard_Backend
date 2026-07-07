from flask import Blueprint
from flask import jsonify
from flask import request

from services.config_service import (
    obtener_configuracion,
    actualizar_configuracion,
    actualizar_perfil
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

        data["comentarios_maximos"],

        data["notificaciones"],

        data["alertas_criticas"]

    )

    return jsonify({
        "success": True
    })

@config_bp.route(
    "/perfil",
    methods=["PUT"]
)
def actualizar_datos_perfil():

    data = request.get_json()

    usuario = actualizar_perfil(

        data["nombre"],

        data["correo"],

        data["correo_actual"]

    )

    if usuario is None:

        return jsonify({

            "success": False,

            "message": "No se pudo actualizar el perfil."

        }), 400

    usuario.pop("password", None)

    return jsonify({

        "success": True,

        "usuario": usuario

    })