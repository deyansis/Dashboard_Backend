from services.supabase_service import supabase
from services.sentiment_service import analizar_sentimiento
from services.topic_service import detectar_tema


def obtener_prioridad(sentimiento):

    if sentimiento == "negativo":
        return "alta"

    elif sentimiento == "neutral":
        return "media"

    return "baja"


def guardar_comentario_facebook(
    usuario,
    comentario,
    publicacion_id,
):

    # ==========================
    # Verificar si ya existe
    # ==========================

    if publicacion_id is not None:

        existe = (
            supabase
            .table("comentarios")
            .select("*")
            .eq(
                "comentario",
                comentario,
            )
            .eq(
                "publicacion_id",
                publicacion_id,
            )
            .execute()
        )

    else:

        existe = (
            supabase
            .table("comentarios")
            .select("*")
            .eq(
                "comentario",
                comentario,
            )
            .execute()
        )

    if existe.data:

        print(
            f"Comentario duplicado omitido: {comentario[:40]}"
        )

        return existe.data[0]

    # ==========================
    # Analizar comentario
    # ==========================

    sentimiento = analizar_sentimiento(
        comentario
    )

    prioridad = obtener_prioridad(
        sentimiento
    )

    tema = detectar_tema(
        comentario
    )

    # ==========================
    # Guardar en Supabase
    # ==========================

    response = (
        supabase
        .table("comentarios")
        .insert(
            {
                "usuario": usuario,
                "comentario": comentario,
                "sentimiento": sentimiento,
                "prioridad": prioridad,
                "confianza": 0.95,
                "tema": tema,
                "publicacion_id": (
                    publicacion_id
                    if publicacion_id
                    else None
                ),
            }
        )
        .execute()
    )

    print(
        f"Comentario guardado: {comentario[:40]}"
    )

    # ==========================
    # Obtener registro completo
    # ==========================

    nuevo = (
        supabase
        .table("comentarios")
        .select("*")
        .eq(
            "id",
            response.data[0]["id"]
        )
        .single()
        .execute()
    )

    return nuevo.data