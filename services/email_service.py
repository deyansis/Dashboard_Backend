import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL = "gamboadeyssi6@gmail.com"

PASSWORD = "rkar nfda nikb hyia"


def enviar_correo_codigo(correo_destino, codigo):

    mensaje = MIMEMultipart()

    mensaje["From"] = EMAIL

    mensaje["To"] = correo_destino

    mensaje["Subject"] = "Recuperación de contraseña - SentiGob"

    cuerpo = f"""
Hola.

Se solicitó recuperar la contraseña de su cuenta de SentiGob.

Su código de verificación es:

{codigo}

Este código expira en 10 minutos.

Si usted no realizó esta solicitud, ignore este mensaje.

SentiGob
Sistema Inteligente de Análisis de Sentimientos
"""

    mensaje.attach(
        MIMEText(cuerpo, "plain")
    )

    servidor = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    servidor.starttls()

    servidor.login(
        EMAIL,
        PASSWORD
    )

    servidor.sendmail(
        EMAIL,
        correo_destino,
        mensaje.as_string()
    )

    servidor.quit()