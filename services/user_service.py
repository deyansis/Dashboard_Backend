from services.supabase_service import supabase

def obtener_usuario():

    response = (
        supabase
        .table("usuarios")
        .select("*")
        .limit(1)
        .execute()
    )

    if len(response.data) > 0:

        return response.data[0]

    return {}