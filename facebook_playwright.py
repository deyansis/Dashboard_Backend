from playwright.sync_api import sync_playwright
from urllib.parse import urlparse, parse_qs

from services.facebook_service import (
    guardar_comentario_facebook,
)


def extraer_comentarios(url):

    query = parse_qs(
        urlparse(url).query
    )

    publicacion_id = query.get(
        "fbid",
        ["facebook"]
    )[0]

    print("URL:", url)
    print("QUERY:", query)
    print("PUBLICACION_ID:", publicacion_id)

    comentarios = []

    with sync_playwright() as p:
        print("===== INICIANDO PLAYWRIGHT =====")

        browser = p.chromium.launch(

            headless=True,

            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
            ]

        )

        context = browser.new_context(

            viewport={
                "width": 1366,
                "height": 768,
            }

        )

        page = context.new_page()

        print("\nAbriendo publicación...")

        page.goto(

            url,

            wait_until="domcontentloaded",

            timeout=60000

        )
        print("===== PAGINA CARGADA =====")
        print("Esperando que carguen los comentarios...")

        page.wait_for_timeout(
            10000
        )

        for _ in range(2):

            page.mouse.wheel(
                0,
                3000,
            )

            page.wait_for_timeout(
                1500
            )

        print("Comentarios cargados.")

        try:

            page.keyboard.press(
                "Escape"
            )

        except Exception:

            pass

        print("\nCapturando contenido...")

        texto = page.locator(
            "body"
        ).inner_text()

        print(f"===== TEXTO OBTENIDO: {len(texto)} caracteres =====")
        lineas = [

            x.strip()

            for x in texto.split("\n")

            if x.strip()

        ]

        inicio = 0

        for i, linea in enumerate(lineas):

            if linea.lower() == "más relevantes":

                inicio = i + 1

                break

        ignorar = {

            "Me gusta",
            "Comentar",
            "Compartir",
            "Responder",
            "Ver más comentarios",
            "Comentarios",
            "Todas las reacciones",
            "Público",
            "Seguir",
            "Enviar",

        }

        i = inicio

        while i < len(lineas) - 2:

            usuario = lineas[i]
            comentario = lineas[i + 1]
            tiempo = lineas[i + 2]

            if not tiempo.endswith("sem"):

                i += 1
                continue

            if usuario in ignorar:

                i += 1
                continue

            if len(comentario) < 5:

                i += 3
                continue

            try:

                resultado = guardar_comentario_facebook(

                    usuario,

                    comentario,

                    publicacion_id,

                )

                if resultado:

                    if isinstance(resultado, list):

                        comentarios.append(
                            resultado[0]
                        )

                    else:

                        comentarios.append(
                            resultado
                        )

                print(f"Usuario: {usuario}")
                print(f"Comentario: {comentario}")
                print("-" * 60)

            except Exception as e:

                print("Error guardando comentario:")
                print(e)

            i += 3

        print(
            f"\nTotal encontrados: {len(comentarios)}"
        )

        context.close()
        browser.close()
        print(f"===== TOTAL COMENTARIOS: {len(comentarios)} =====")
        return comentarios


if __name__ == "__main__":

    url = input(
        "Ingrese URL Facebook: "
    )

    extraer_comentarios(
        url
    )