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
    comentarios_maximos,
    notificaciones,
    alertas_criticas
):

    response = (
        supabase
        .table("configuracion")
        .update({

            "idioma": idioma,

            "tema": tema,

            "comentarios_maximos":
                comentarios_maximos,

            "notificaciones":
                notificaciones,

            "alertas_criticas":
                alertas_criticas

        })
        .eq("id", 1)
        .execute()
    )

def actualizar_perfil(
    nombre,
    correo,
    correo_actual
):

    response = (
        supabase
        .table("usuarios")
        .update({

            "nombre": nombre,

            "correo": correo

        })
        .eq("correo", correo_actual)
        .execute()
    )

    if len(response.data) == 0:

        return None

    return response.data[0]

    