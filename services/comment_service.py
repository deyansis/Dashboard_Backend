from services.supabase_service import supabase

def eliminar_comentario(id):

    response = (
        supabase
        .table("comentarios")
        .delete()
        .eq("id", id)
        .execute()
    )

    return response.data


def actualizar_comentario(
    id,
    sentimiento,
    prioridad
):

    response = (
        supabase
        .table("comentarios")
        .update({
            "sentimiento": sentimiento,
            "prioridad": prioridad
        })
        .eq("id", id)
        .execute()
    )

    return response.data