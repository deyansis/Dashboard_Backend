from services.supabase_service import supabase


def obtener_kpis_dashboard(
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

    response = query.execute()

    comentarios = response.data

    total = len(comentarios)

    if total == 0:
        return {
            "tasa_positiva": 0,
            "tasa_negativa": 0,
            "indice_sentimiento": 0,
            "nivel_percepcion": 0
        }

    positivos = len([
        c for c in comentarios
        if c["sentimiento"] == "positivo"
    ])

    negativos = len([
        c for c in comentarios
        if c["sentimiento"] == "negativo"
    ])

    tasa_positiva = round(
        (positivos / total) * 100,
        1
    )

    tasa_negativa = round(
        (negativos / total) * 100,
        1
    )

    indice_sentimiento = round(
        tasa_positiva - tasa_negativa,
        1
    )

    nivel_percepcion = round(
        max(0, min(100, 50 + indice_sentimiento)),
        1
    )

    return {
        "tasa_positiva": tasa_positiva,
        "tasa_negativa": tasa_negativa,
        "indice_sentimiento": indice_sentimiento,
        "nivel_percepcion": nivel_percepcion
    }