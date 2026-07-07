from flask import Blueprint
from flask import jsonify
from flask import request
from flask import send_file
import os

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

    fecha_inicio = data.get(
    "fecha_inicio"
)

    fecha_fin = data.get(
    "fecha_fin"
)

    reporte = guardar_reporte(
    nombre,
    formato,
    fecha_inicio,
    fecha_fin
)

    return jsonify({
    "success": True,
    "reporte": reporte[0]
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
@report_bp.route(
    "/reportes/<int:id>",
    methods=["DELETE"]
)
def eliminar_reporte(id):

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
            "success": False,
            "message": "Reporte no encontrado"
        }), 404

    archivo = reporte["archivo_url"]

    if os.path.exists(archivo):

        os.remove(archivo)

    (
        supabase
        .table("reportes")
        .delete()
        .eq("id", id)
        .execute()
    )

    return jsonify({
        "success": True,
        "message": "Reporte eliminado correctamente"
    })