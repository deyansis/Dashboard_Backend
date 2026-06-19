from flask import Blueprint
from flask import jsonify
from flask import request
from flask import send_file

from services.report_service import (
    obtener_reportes,
    guardar_reporte
)

from services.supabase_service import (
    supabase
)

report_bp = Blueprint(
    "reportes",
    __name__
)


@report_bp.route(
    "/reportes",
    methods=["GET"]
)
def listar_reportes():

    return jsonify({
        "reportes":
        obtener_reportes()
    })


@report_bp.route(
    "/reportes",
    methods=["POST"]
)
def crear_reporte():

    data = request.get_json()

    nombre = data.get(
        "nombre"
    )

    formato = data.get(
        "formato"
    )

    guardar_reporte(
        nombre,
        formato
    )

    return jsonify({
        "success": True
    })


@report_bp.route(
    "/descargar-reporte/<int:id>",
    methods=["GET"]
)
def descargar_reporte(id):

    response = (
        supabase
        .table("reportes")
        .select("*")
        .eq("id", id)
        .single()
        .execute()
    )

    reporte = response.data

    if not reporte:

        return jsonify({
            "error":
            "Reporte no encontrado"
        }), 404

    return send_file(
        reporte["archivo_url"],
        as_attachment=True
    )