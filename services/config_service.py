from services.supabase_service import supabase

def obtener_configuracion():

    response = (
        supabase
        .table("configuracion")
        .select("*")
        .limit(1)
        .execute()
    )

    if len(response.data) > 0:
        return response.data[0]

    return {}


def actualizar_configuracion(
    idioma,
    tema,
    comentarios_maximos
):

    response = (
        supabase
        .table("configuracion")
        .update({

            "idioma": idioma,

            "tema": tema,

            "comentarios_maximos":
                comentarios_maximos

        })
        .eq("id", 1)
        .execute()
    )

    return response.data