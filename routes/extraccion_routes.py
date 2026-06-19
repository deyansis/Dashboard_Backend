from flask import Blueprint
from flask import request
from flask import jsonify

from services.extraction_results_service import (
    obtener_comentarios_extraidos
)

from services.comment_service import (
    eliminar_comentario,
    actualizar_comentario
)

extraccion_bp = Blueprint(
    "extraccion",
    __name__
)

@extraccion_bp.route(
    "/extraer-facebook",
    methods=["POST"]
)
def extraer_facebook():

    data = request.get_json()

    url = data.get("url")

    fecha_inicio = data.get(
        "fecha_inicio"
    )

    fecha_fin = data.get(
        "fecha_fin"
    )

    tema = data.get(
        "tema"
    )

    cantidad = data.get(
        "cantidad",
        100
    )

    sentimiento = data.get(
        "sentimiento"
    )

    print(
        "URL recibida:",
        url
    )

    print(
        "Sentimiento:",
        sentimiento
    )

    comentarios = (
        obtener_comentarios_extraidos(
            fecha_inicio,
            fecha_fin,
            tema,
            cantidad,
            sentimiento
        )
    )

    return jsonify({

        "comentarios":
        comentarios

    })


@extraccion_bp.route(
    "/comentarios/<int:id>",
    methods=["DELETE"]
)
def eliminar(id):

    eliminar_comentario(id)

    return jsonify({

        "success": True

    })


@extraccion_bp.route(
    "/comentarios/<int:id>",
    methods=["PUT"]
)
def actualizar(id):

    data = request.get_json()

    sentimiento = data.get(
        "sentimiento"
    )

    prioridad = data.get(
        "prioridad"
    )

    actualizar_comentario(
        id,
        sentimiento,
        prioridad
    )

    return jsonify({

        "success": True

    })

@extraccion_bp.route(
    "/comentarios",
    methods=["GET"]
)
def obtener_comentarios():

    comentarios = (
        obtener_comentarios_extraidos()
    )

    return jsonify({
        "comentarios":
        comentarios
    })