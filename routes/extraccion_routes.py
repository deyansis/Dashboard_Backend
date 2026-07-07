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

from facebook_playwright import (
    extraer_comentarios
)

extraccion_bp = Blueprint(
    "extraccion",
    __name__
)

# ============================
# EXTRAER FACEBOOK
# ============================

@extraccion_bp.route(
    "/extraer-facebook",
    methods=["POST"]
)
def extraer_facebook():

    data = request.get_json()

    url = data.get("url")

    if not url:

        return jsonify({
            "error": "Debe enviar una URL."
        }), 400

    # Extrae comentarios y los guarda en Supabase
    comentarios = extraer_comentarios(url)

    return jsonify({

        "comentarios": comentarios

    })


# ============================
# CONSULTAR COMENTARIOS
# ============================

@extraccion_bp.route(
    "/comentarios",
    methods=["GET"]
)
def obtener_comentarios():

    fecha_inicio = request.args.get(
        "fecha_inicio"
    )

    fecha_fin = request.args.get(
        "fecha_fin"
    )

    cantidad = request.args.get(
        "cantidad",
        50
    )

    sentimiento = request.args.get(
        "sentimiento"
    )

    pagina = request.args.get(
        "pagina",
        1
    )

    resultado = obtener_comentarios_extraidos(

        fecha_inicio=fecha_inicio,

        fecha_fin=fecha_fin,

        tema=None,

        cantidad=cantidad,

        sentimiento=sentimiento,

        pagina=pagina

    )

    return jsonify(resultado)


# ============================
# ELIMINAR
# ============================

@extraccion_bp.route(
    "/comentarios/<int:id>",
    methods=["DELETE"]
)
def eliminar(id):

    eliminar_comentario(id)

    return jsonify({

        "success": True

    })


# ============================
# ACTUALIZAR
# ============================

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