from flask import Blueprint, jsonify, request

from services.user_service import (
    obtener_usuario,
    obtener_usuarios,
    crear_usuario,
    editar_usuario,
    eliminar_usuario
)

user_bp = Blueprint(
    "usuarios",
    __name__
)


# ==========================
# PERFIL
# ==========================

@user_bp.route(
    "/usuario",
    methods=["GET"]
)
def usuario():

    return jsonify(
        obtener_usuario()
    )


# ==========================
# LISTAR USUARIOS
# ==========================

@user_bp.route(
    "/usuarios",
    methods=["GET"]
)
def usuarios():

    return jsonify(
        obtener_usuarios()
    )


# ==========================
# CREAR USUARIO
# ==========================

@user_bp.route(
    "/usuarios",
    methods=["POST"]
)
def crear():

    datos = request.json

    try:

        usuario = crear_usuario(datos)

        return jsonify(usuario), 201

    except ValueError as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 400

    except Exception:

        return jsonify({
            "success": False,
            "message": "Ocurrió un error al registrar el usuario."
        }), 500

# ==========================
# EDITAR USUARIO
# ==========================

@user_bp.route(
    "/usuarios/<int:id_usuario>",
    methods=["PUT"]
)
def editar(id_usuario):

    datos = request.json

    return jsonify(
        editar_usuario(
            id_usuario,
            datos
        )
    )


# ==========================
# ELIMINAR USUARIO
# ==========================

@user_bp.route(
    "/usuarios/<int:id_usuario>",
    methods=["DELETE"]
)
def eliminar(id_usuario):

    return jsonify(
        eliminar_usuario(
            id_usuario
        )
    )