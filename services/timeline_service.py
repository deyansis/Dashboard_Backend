from collections import defaultdict

from services.supabase_service import supabase

def obtener_timeline(
    fecha_inicio=None,
    fecha_fin=None,
    prioridad=None
):

    query = supabase.table(
        "comentarios"
    ).select(
        "sentimiento,fecha_registro,prioridad"
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

    timeline = defaultdict(
        lambda: {
            "positivos": 0,
            "negativos": 0,
            "neutrales": 0
        }
    )

    for comentario in comentarios:

        fecha = comentario[
            "fecha_registro"
        ][:10]

        sentimiento = comentario[
            "sentimiento"
        ].lower()

        if sentimiento == "positivo":

            timeline[fecha][
                "positivos"
            ] += 1

        elif sentimiento == "negativo":

            timeline[fecha][
                "negativos"
            ] += 1

        else:

            timeline[fecha][
                "neutrales"
            ] += 1

    resultado = []

    for fecha, valores in sorted(
        timeline.items()
    ):

        resultado.append({

            "fecha": fecha,

            "positivos":
                valores["positivos"],

            "negativos":
                valores["negativos"],

            "neutrales":
                valores["neutrales"]

        })

    return resultado