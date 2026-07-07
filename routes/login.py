from flask import Blueprint
from flask import request
from flask import jsonify
from services.login_service import (
    iniciar_sesion,
    generar_codigo,
    cambiar_password
)


login_bp = Blueprint(
    "login",
    __name__
)


@login_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.get_json()

    usuario = iniciar_sesion(

        data["correo"],

        data["password"]

    )

    if usuario is None:

        return jsonify({

            "success": False,

            "message": "Correo o contraseña incorrectos."

        }), 401

    usuario.pop("password", None)

    return jsonify({

        "success": True,

        "usuario": usuario

    })
@login_bp.route(
    "/enviar-codigo",
    methods=["POST"]
)
def enviar_codigo():

    data = request.get_json()

    codigo = generar_codigo(

        data["correo"]

    )

    if codigo is None:

        return jsonify({

            "success": False,

            "message": "El correo no existe."

        }), 404

    return jsonify({

        "success": True,

        "codigo": codigo

    })
@login_bp.route(
    "/cambiar-password",
    methods=["POST"]
)
def actualizar_password():

    data = request.get_json()

    print("====================================")
    print("Correo:", repr(data["correo"]))
    print("Código:", repr(data["codigo"]))
    print("Password:", repr(data["password"]))

    respuesta = cambiar_password(
        data["correo"],
        data["codigo"],
        data["password"]
    )

    print("Respuesta:", respuesta)

    if not respuesta["success"]:
        return jsonify(respuesta), 400

    return jsonify(respuesta)