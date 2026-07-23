from services.supabase_service import supabase


def obtener_distribucion_sentimientos(
    fecha_inicio=None,
    fecha_fin=None,
    prioridad=None
):

    query = supabase.table(
        "comentarios"
    ).select(
        "sentimiento, prioridad, fecha_registro"
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

    comentarios = []

    inicio = 0
    tamano = 1000

    while True:

        response = (
            query
            .range(inicio, inicio + tamano - 1)
            .execute()
        )

        if not response.data:
            break

        comentarios.extend(response.data)

        if len(response.data) < tamano:
            break

        inicio += tamano

    positivos = 0
    negativos = 0
    neutrales = 0

    for comentario in comentarios:

        sentimiento = comentario[
            "sentimiento"
        ].lower()

        if sentimiento == "positivo":

            positivos += 1

        elif sentimiento == "negativo":

            negativos += 1

        else:

            neutrales += 1

    return [

        {
            "name": "Positivos",
            "value": positivos
        },

        {
            "name": "Negativos",
            "value": negativos
        },

        {
            "name": "Neutrales",
            "value": neutrales
        }

    ]