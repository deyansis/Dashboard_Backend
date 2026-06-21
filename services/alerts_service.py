from collections import Counter

from services.supabase_service import supabase


def obtener_alertas(
    fecha_inicio=None,
    fecha_fin=None,
    prioridad=None
):

    query = supabase.table(
        "comentarios"
    ).select("*")

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

    def construir_resumen(datos):

        if not datos:

            return {
                "cantidad": 0,
                "tema_principal": "-",
                "sentimiento_predominante": "-"
            }

        temas = Counter(
            [
                c.get("tema", "Otros")
                for c in datos
            ]
        )

        tema_principal = temas.most_common(1)[0][0]

        positivos = len([
            c for c in datos
            if c["sentimiento"].lower() == "positivo"
        ])

        negativos = len([
            c for c in datos
            if c["sentimiento"].lower() == "negativo"
        ])

        neutrales = len([
            c for c in datos
            if c["sentimiento"].lower() == "neutro"
        ])

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

            "cantidad":
                len(datos),

            "tema_principal":
                tema_principal,

            "sentimiento_predominante":
                sentimiento_predominante

        }

    return {

        "alta":
            construir_resumen(
                alta
            ),

        "media":
            construir_resumen(
                media
            ),

        "baja":
            construir_resumen(
                
                baja
            )

    }