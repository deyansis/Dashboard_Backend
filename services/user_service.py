from services.supabase_service import supabase


# ==========================
# PERFIL
# ==========================

def obtener_usuario():

    response = (
        supabase
        .table("usuarios")
        .select("*")
        .limit(1)
        .execute()
    )

    if response.data:
        return response.data[0]

    return {}


# ==========================
# LISTAR USUARIOS
# ==========================

def obtener_usuarios():

    response = (
        supabase
        .table("usuarios")
        .select("*")
        .order("id")
        .execute()
    )

    return response.data


# ==========================
# CREAR USUARIO
# ==========================

def crear_usuario(datos):

    response = (
        supabase
        .table("usuarios")
        .insert({
            "nombre": datos["nombre"],
            "correo": datos["correo"],
            "password": datos["password"],
            "cargo": datos["cargo"],
            "estado": datos["estado"],
            "numero_registro": datos["numero_registro"]
        })
        .execute()
    )

    return response.data


# ==========================
# EDITAR USUARIO
# ==========================

def editar_usuario(id_usuario, datos):

    response = (
        supabase
        .table("usuarios")
        .update({
            "nombre": datos["nombre"],
            "correo": datos["correo"],
            "cargo": datos["cargo"],
            "estado": datos["estado"],
        })
        .eq("id", id_usuario)
        .execute()
    )

    return response.data


# ==========================
# ELIMINAR USUARIO
# ==========================

def eliminar_usuario(id_usuario):

    response = (
        supabase
        .table("usuarios")
        .delete()
        .eq("id", id_usuario)
        .execute()
    )

    return response.data