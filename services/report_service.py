from services.supabase_service import supabase

from services.report_file_service import (
    generar_pdf,
    generar_excel
)

from services.extraction_results_service import (
    obtener_comentarios_extraidos
)


def obtener_reportes():

    response = (
        supabase
        .table("reportes")
        .select("*")
        .order(
            "fecha_generacion",
            desc=True
        )
        .execute()
    )

    return response.data


def guardar_reporte(
    nombre,
    formato
):

    comentarios = (
        obtener_comentarios_extraidos(
            cantidad=50
        )
    )

    total = len(
        comentarios
    )

    positivos = len([
        c for c in comentarios
        if c["sentimiento"] == "positivo"
    ])

    negativos = len([
        c for c in comentarios
        if c["sentimiento"] == "negativo"
    ])

    neutrales = len([
        c for c in comentarios
        if c["sentimiento"] == "neutral"
    ])

    if formato == "PDF":

        archivo = generar_pdf(
            nombre,
            comentarios,
            total,
            positivos,
            negativos,
            neutrales
        )

    else:

        archivo = generar_excel(
            nombre
        )

    response = (
        supabase
        .table("reportes")
        .insert({

            "nombre": nombre,

            "formato": formato,

            "estado": "Disponible",

            "archivo_url": archivo

        })
        .execute()
    )

    return response.data