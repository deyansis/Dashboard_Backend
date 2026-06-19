from flask import Blueprint
from flask import request
from flask import jsonify

from services.sentiment_service import (
    analizar_sentimiento
)
from services.timeline_service import (
    obtener_timeline
)

analisis_bp = Blueprint(
    "analisis",
    __name__
)

@analisis_bp.route(
    "/analizar",
    methods=["POST"]
)
def analizar():

    data = request.get_json()

    comentario = data["comentario"]

    sentimiento = analizar_sentimiento(
        comentario
    )

    return jsonify({
        "sentimiento": sentimiento
    })

@analisis_bp.route(
    "/timeline",
    methods=["GET"]
)
def timeline():

    data = obtener_timeline()

    return jsonify(data)