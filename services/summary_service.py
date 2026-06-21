from services.supabase_service import supabase

def obtener_resumen_dashboard(
    fecha_inicio=None,
    fecha_fin=None,
    prioridad=None
):

    query = supabase.table(
        "comentarios"
    ).select(
        "id,fecha_registro,prioridad,sentimiento"
    )

    if fecha_inicio:

        query = query.gte(
            "fecha_registro",
            fecha_inicio
        )

    if fecha_fin:

        query = query.lte(
            "fecha_registro",
            f"{fecha_fin} 23:59:59"
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

    positivos = len([
        c for c in comentarios
        if c["sentimiento"].lower() == "positivo"
    ])

    negativos = len([
        c for c in comentarios
        if c["sentimiento"].lower() == "negativo"
    ])

    neutrales = len([
        c for c in comentarios
        if c["sentimiento"].lower() in [
            "neutral",
            "neutro"
        ]
    ])

    sentimiento_predominante = "-"

    if total > 0:

        sentimiento_predominante = max(
            {
                "Positivo": positivos,
                "Negativo": negativos,
                "Neutral": neutrales
            },
            key=lambda x: {
                "Positivo": positivos,
                "Negativo": negativos,
                "Neutral": neutrales
            }[x]
        )

    return {

        "total_comentarios":
            total,

        "ultima_fecha":
            ultima_fecha,

        "sentimiento_predominante":
            sentimiento_predominante

    }