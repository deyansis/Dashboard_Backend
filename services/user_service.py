from services.supabase_service import supabase
import bcrypt

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
    
    # Verificar si el correo ya existe
    existe = (
        supabase
        .table("usuarios")
        .select("id")
        .eq("correo", datos["correo"])
        .limit(1)
        .execute()
    )

    if existe.data:
        raise ValueError("Ya existe un usuario registrado con ese correo electrónico.")

    # Obtener el último número de registro
    ultimo = (
        supabase
        .table("usuarios")
        .select("numero_registro")
        .order("id", desc=True)
        .limit(1)
        .execute()
    )

    if ultimo.data and ultimo.data[0]["numero_registro"]:
    
        ultimo_numero = int(
        ultimo.data[0]["numero_registro"].split("-")[1]
    )

        numero_registro = f"ADM-{ultimo_numero + 1:03d}"

    else:

        numero_registro = "ADM-001"

    # Encriptar contraseña
    password_hash = bcrypt.hashpw(
        datos["password"].encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    # Registrar usuario
    response = (
        supabase
        .table("usuarios")
        .insert({
            "nombre": datos["nombre"],
            "correo": datos["correo"],
            "password": password_hash,
            "cargo": datos["cargo"],
            "estado": datos["estado"],
            "numero_registro": numero_registro
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