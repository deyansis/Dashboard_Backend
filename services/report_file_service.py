from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from openpyxl import Workbook

import os


def generar_pdf(
    nombre,
    comentarios,
    total,
    positivos,
    negativos,
    neutrales
):

    carpeta = "reports"

    os.makedirs(
        carpeta,
        exist_ok=True
    )

    ruta = f"{carpeta}/{nombre}.pdf"

    pdf = SimpleDocTemplate(
        ruta
    )

    estilos = getSampleStyleSheet()

    contenido = []

    contenido.append(

        Paragraph(
            "REPORTE SENTIGOB",
            estilos["Title"]
        )

    )

    contenido.append(
        Spacer(1, 20)
    )

    contenido.append(

        Paragraph(
            f"Nombre del reporte: {nombre}",
            estilos["Heading2"]
        )

    )

    contenido.append(
        Spacer(1, 10)
    )

    contenido.append(

        Paragraph(
            f"Total comentarios: {total}",
            estilos["Normal"]
        )

    )

    contenido.append(

        Paragraph(
            f"Comentarios positivos: {positivos}",
            estilos["Normal"]
        )

    )

    contenido.append(

        Paragraph(
            f"Comentarios negativos: {negativos}",
            estilos["Normal"]
        )

    )

    contenido.append(

        Paragraph(
            f"Comentarios neutrales: {neutrales}",
            estilos["Normal"]
        )

    )

    contenido.append(
        Spacer(1, 20)
    )

    contenido.append(

        Paragraph(
            "Comentarios recientes",
            estilos["Heading2"]
        )

    )

    contenido.append(
        Spacer(1, 10)
    )

    for comentario in comentarios[:20]:

        texto = f"""
        <b>Sentimiento:</b>
        {comentario['sentimiento']}
        <br/>

        <b>Prioridad:</b>
        {comentario['prioridad']}
        <br/>

        <b>Comentario:</b>
        {comentario['comentario']}
        """

        contenido.append(

            Paragraph(
                texto,
                estilos["BodyText"]
            )

        )

        contenido.append(
            Spacer(1, 10)
        )

    pdf.build(
        contenido
    )

    return ruta


def generar_excel(
    nombre
):

    carpeta = "reports"

    os.makedirs(
        carpeta,
        exist_ok=True
    )

    ruta = f"{carpeta}/{nombre}.xlsx"

    wb = Workbook()

    ws = wb.active

    ws.title = "Reporte"

    ws["A1"] = "Nombre del reporte"
    ws["B1"] = nombre

    wb.save(
        ruta
    )

    return ruta