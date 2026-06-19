from services.supabase_service import supabase

def obtener_resumen_dashboard(
    fecha_inicio=None,
    fecha_fin=None,
    prioridad=None
):

    query = supabase.table(
        "comentarios"
    ).select(
        "id,fecha_registro,prioridad"
    )

    if fecha_inicio:

        query = query.gte(
            "fecha_registro",
            fecha_inicio
        )

    if fecha_fin:

        query = query.lte(
            "fecha_registro",
            fecha_fin
        )

    if prioridad and prioridad != "todas":

        query = query.eq(
            "prioridad",
            prioridad
        )

    response = query.execute()

    comentarios = response.data

    total = len(comentarios)

    ultima_fecha = "-"

    if total > 0:

        fechas = [
            c["fecha_registro"]
            for c in comentarios
            if c["fecha_registro"]
        ]

        if fechas:

            ultima_fecha = max(fechas)

    return {

        "total_comentarios": total,

        "comentarios_analizados": total,

        "porcentaje_analizado": 100,

        "ultima_fecha": ultima_fecha

    }