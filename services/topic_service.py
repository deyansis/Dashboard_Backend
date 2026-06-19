def detectar_tema(texto):
    
    texto = texto.lower()

    if any(
        palabra in texto
        for palabra in [
            "seguridad",
            "robo",
            "robos",
            "delincuencia",
            "serenazgo",
            "violencia",
            "asalto",
            "asaltos",
            "policia",
            "policía",
            "patrullaje",
            "patrulla",
            "vigilancia",
            "camara",
            "cámara",
            "camaras",
            "cámaras"
        ]
    ):
        return "Seguridad Ciudadana"

    elif any(
        palabra in texto
        for palabra in [
            "obra",
            "obras",
            "pista",
            "pistas",
            "vereda",
            "veredas",
            "puente",
            "infraestructura",
            "construcción",
            "construccion",
            "remodelación",
            "remodelacion",
            "avenida"
        ]
    ):
        return "Obras Públicas"

    elif any(
        palabra in texto
        for palabra in [
            "basura",
            "limpieza",
            "residuos",
            "contaminación",
            "contaminacion",
            "parque",
            "parques",
            "reciclaje",
            "árbol",
            "arbol",
            "medio ambiente",
            "áreas verdes",
            "areas verdes"
        ]
    ):
        return "Medio Ambiente"

    elif any(
        palabra in texto
        for palabra in [
            "atención",
            "atencion",
            "trámite",
            "tramite",
            "municipalidad",
            "funcionario",
            "ciudadano",
            "beneficio",
            "programa social",
            "reclamo",
            "servicio"
        ]
    ):
        return "Atención Ciudadana"

    elif any(
        palabra in texto
        for palabra in [
            "transporte",
            "bus",
            "buses",
            "ruta",
            "rutas",
            "paradero",
            "tráfico",
            "trafico"
        ]
    ):
        return "Transporte"

    elif any(
        palabra in texto
        for palabra in [
            "salud",
            "hospital",
            "médico",
            "medico",
            "médica",
            "medica",
            "doctor",
            "paciente",
            "medicamento",
            "vacuna",
            "centro de salud"
        ]
    ):
        return "Salud"

    elif any(
        palabra in texto
        for palabra in [
            "educación",
            "educacion",
            "colegio",
            "escuela",
            "estudiante",
            "docente",
            "profesor",
            "biblioteca",
            "universidad"
        ]
    ):
        return "Educación"

    return "Otros"