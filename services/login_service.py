from datetime import datetime, timedelta, timezone
import random
import bcrypt
from services.supabase_service import supabase
from services.email_service import enviar_correo_codigo


def iniciar_sesion(
    correo,
    password
):

    response = (
        supabase
        .table("usuarios")
        .select("*")
        .eq("correo", correo)
        .eq("estado", "Activo")
        .limit(1)
        .execute()
    )

    if len(response.data) == 0:
        return None

    usuario = response.data[0]

    password_hash = usuario["password"]

    if not bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8")
    ):
        return None

    return usuario


def generar_codigo(correo):

    response = (
        supabase
        .table("usuarios")
        .select("*")
        .eq("correo", correo.strip())
        .limit(1)
        .execute()
    )

    if len(response.data) == 0:
        return None

    (
        supabase
        .table("codigos_recuperacion")
        .delete()
        .eq("correo", correo)
        .execute()
    )

    codigo = str(random.randint(100000, 999999))

    fecha_expiracion = (
        datetime.utcnow() +
        timedelta(minutes=10)
    ).isoformat()

    (
        supabase
        .table("codigos_recuperacion")
        .insert({
            "correo": correo,
            "codigo": codigo,
            "fecha_expiracion": fecha_expiracion,
            "utilizado": False
        })
        .execute()
    )

    enviar_correo_codigo(
        correo,
        codigo
    )

    return codigo


def cambiar_password(
    correo,
    codigo,
    password
):

    response = (
        supabase
        .table("codigos_recuperacion")
        .select("*")
        .eq("correo", correo)
        .eq("codigo", codigo)
        .eq("utilizado", False)
        .limit(1)
        .execute()
    )

    if len(response.data) == 0:

        return {
            "success": False,
            "message": "Código incorrecto."
        }

    registro = response.data[0]

    fecha_expiracion = datetime.fromisoformat(
        registro["fecha_expiracion"]
    )

    fecha_actual = datetime.now(timezone.utc)

    if fecha_actual > fecha_expiracion:
    
        return {
            "success": False,
            "message": "El código ha expirado."
        }

    # Generar hash de la nueva contraseña

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    # Actualizar contraseña

    (
        supabase
        .table("usuarios")
        .update({

            "password": password_hash

        })
        .eq("correo", correo)
        .execute()
    )

    # Marcar código como utilizado

    (
        supabase
        .table("codigos_recuperacion")
        .update({

            "utilizado": True

        })
        .eq("id", registro["id"])
        .execute()
    )

    return {

        "success": True,

        "message": "Contraseña actualizada correctamente."

    }