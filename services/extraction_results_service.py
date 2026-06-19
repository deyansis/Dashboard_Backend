from services.supabase_service import supabase

def obtener_comentarios_extraidos(
    fecha_inicio=None,
    fecha_fin=None,
    tema=None,
    cantidad=100,
    sentimiento=None
):

    query = supabase.table(
        "comentarios"
    ).select(
        """
        id,
        comentario,
        sentimiento,
        prioridad,
        confianza,
        fecha_registro
        """
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

    if tema:

        query = query.ilike(
            "comentario",
            f"%{tema}%"
        )

    if (
        sentimiento and
        sentimiento != "todos"
    ):

        query = query.eq(
            "sentimiento",
            sentimiento
        )

    response = (
        query
        .order(
            "fecha_registro",
            desc=True
        )
        .limit(
            int(cantidad)
        )
        .execute()
    )

    return response.data