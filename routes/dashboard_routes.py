from flask import Blueprint
from flask import jsonify
from flask import request

from services.dashboard_service import (
    obtener_kpis_dashboard
)

from services.timeline_service import (
    obtener_timeline
)

from services.sentiment_donut_service import (
    obtener_distribucion_sentimientos
)

from services.summary_service import (
    obtener_resumen_dashboard
)
from services.alerts_service import (
    obtener_alertas
)

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)

@dashboard_bp.route(
    "/dashboard",
    methods=["GET"]
)
def dashboard():

    fecha_inicio = request.args.get(
        "fecha_inicio"
    )

    fecha_fin = request.args.get(
        "fecha_fin"
    )

    prioridad = request.args.get(
        "prioridad"
    )

    return jsonify(

        obtener_kpis_dashboard(
            fecha_inicio,
            fecha_fin,
            prioridad
        )

    )
@dashboard_bp.route(
    "/dashboard/timeline",
    methods=["GET"]
)
def timeline():
    
    fecha_inicio = request.args.get(
        "fecha_inicio"
    )

    fecha_fin = request.args.get(
        "fecha_fin"
    )

    prioridad = request.args.get(
        "prioridad"
    )

    return jsonify(

        obtener_timeline(
            fecha_inicio,
            fecha_fin,
            prioridad
        )

    )

@dashboard_bp.route(
    "/dashboard/sentiments",
    methods=["GET"]
)
def sentiments():

    fecha_inicio = request.args.get(
        "fecha_inicio"
    )

    fecha_fin = request.args.get(
        "fecha_fin"
    )

    prioridad = request.args.get(
        "prioridad"
    )

    return jsonify(

        obtener_distribucion_sentimientos(
            fecha_inicio,
            fecha_fin,
            prioridad
        )

    )

@dashboard_bp.route(
    "/dashboard/summary",
    methods=["GET"]
)
def summary():

    fecha_inicio = request.args.get(
        "fecha_inicio"
    )

    fecha_fin = request.args.get(
        "fecha_fin"
    )

    prioridad = request.args.get(
        "prioridad"
    )

    return jsonify(

        obtener_resumen_dashboard(
            fecha_inicio,
            fecha_fin,
            prioridad
        )

    )
@dashboard_bp.route(
    "/dashboard/alerts",
    methods=["GET"]
)
def alerts():

    fecha_inicio = request.args.get(
        "fecha_inicio"
    )

    fecha_fin = request.args.get(
        "fecha_fin"
    )

    prioridad = request.args.get(
        "prioridad"
    )

    return jsonify(

        obtener_alertas(
            fecha_inicio,
            fecha_fin,
            prioridad
        )

    )

