from services.supabase_service import supabase


def obtener_comentarios_extraidos(
    fecha_inicio=None,
    fecha_fin=None,
    tema=None,
    cantidad=50,
    sentimiento=None,
    pagina=1,
):

    query = (
        supabase
        .table("comentarios")
        .select(
            """
            id,
            usuario,
            comentario,
            sentimiento,
            prioridad,
            confianza,
            tema,
            publicacion_id,
            fecha_registro
            """,
            count="exact"
        )
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

    if tema:

        query = query.ilike(
            "tema",
            f"%{tema}%"
        )

    if sentimiento and sentimiento != "todos":

        query = query.eq(
            "sentimiento",
            sentimiento
        )

    limite = int(cantidad)

    desde = (int(pagina) - 1) * limite

    hasta = desde + limite - 1

    response = (
        query
        .order(
            "fecha_registro",
            desc=True
        )
        .range(
            desde,
            hasta
        )
        .execute()
    )

    return {
        "comentarios": response.data,
        "total": response.count
    }