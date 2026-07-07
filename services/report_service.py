from services.supabase_service import supabase

from services.report_file_service import (
    generar_pdf_completo,
    generar_pdf_ejecutivo,
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
    formato,
    fecha_inicio,
    fecha_fin
):

    resultado = obtener_comentarios_extraidos(
    fecha_inicio=fecha_inicio,
    fecha_fin=fecha_fin,
    cantidad=100000
)

    comentarios = resultado["comentarios"]

    total = len(comentarios)

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
        if c["sentimiento"] == "neutro"
    ])

    # 👇 DESDE AQUÍ TODO VA CON 4 ESPACIOS

    if formato == "PDF":

        if nombre == "Reporte de análisis completo":

           archivo = generar_pdf_completo(
    nombre,
    comentarios,
    total,
    positivos,
    negativos,
    neutrales,
    fecha_inicio,
    fecha_fin
)

        elif nombre == "Reporte ejecutivo":

            archivo = generar_pdf_ejecutivo(
    nombre,
    comentarios,
    total,
    positivos,
    negativos,
    neutrales,
    fecha_inicio,
    fecha_fin
)


        else:

            archivo = generar_pdf_completo(
    nombre,
    comentarios,
    total,
    positivos,
    negativos,
    neutrales,
    fecha_inicio,
    fecha_fin
)

    else:

        archivo = generar_excel(
    nombre,
    comentarios,
    total,
    positivos,
    negativos,
    neutrales,
    fecha_inicio,
    fecha_fin
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