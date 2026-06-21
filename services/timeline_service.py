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
        "sentimiento, fecha_registro, prioridad"
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

    timeline = defaultdict(
        lambda: {
            "positivos": 0,
            "negativos": 0,
            "neutrales": 0
        }
    )

    for comentario in comentarios:

        mes = comentario[
            "fecha_registro"
        ][:7]

        sentimiento = comentario[
            "sentimiento"
        ].lower()

        if sentimiento == "positivo":

            timeline[mes][
                "positivos"
            ] += 1

        elif sentimiento == "negativo":

            timeline[mes][
                "negativos"
            ] += 1

        else:

            timeline[mes][
                "neutrales"
            ] += 1

    resultado = []

    nombres_meses = {
        "01": "Ene",
        "02": "Feb",
        "03": "Mar",
        "04": "Abr",
        "05": "May",
        "06": "Jun",
        "07": "Jul",
        "08": "Ago",
        "09": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dic",
    }

    for mes, valores in sorted(
        timeline.items()
    ):

        numero_mes = mes.split(
            "-"
        )[1]

        resultado.append({

            "fecha":
                nombres_meses[
                    numero_mes
                ],

            "positivos":
                valores[
                    "positivos"
                ],

            "negativos":
                valores[
                    "negativos"
                ],

            "neutrales":
                valores[
                    "neutrales"
                ]

        })

    return resultado