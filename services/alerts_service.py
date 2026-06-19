from services.supabase_service import supabase

def obtener_alertas(
    fecha_inicio=None,
    fecha_fin=None,
    prioridad=None
):

    query = supabase.table(
        "comentarios"
    ).select(
        "*"
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

    response = query.order(
        "fecha_registro",
        desc=True
    ).execute()

    comentarios = response.data

    alta = [
        c for c in comentarios
        if c["prioridad"].lower() == "alta"
    ]

    media = [
        c for c in comentarios
        if c["prioridad"].lower() == "media"
    ]

    baja = [
        c for c in comentarios
        if c["prioridad"].lower() == "baja"
    ]

    return {

        "alta": {
            "cantidad": len(alta),
            "comentarios": alta[:2]
        },

        "media": {
            "cantidad": len(media),
            "comentarios": media[:2]
        },

        "baja": {
            "cantidad": len(baja),
            "comentarios": baja[:2]
        }

    }