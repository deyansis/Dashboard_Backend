from playwright.sync_api import sync_playwright
import time


def extraer_comentarios(url):

    comentarios = []

    with sync_playwright() as p:

        context = p.chromium.launch_persistent_context(
            user_data_dir="./facebook_profile",
            headless=False
        )

        page = context.new_page()

        print(
            "Abriendo publicación..."
        )

        page.goto(
            url,
            wait_until="networkidle"
        )

        print(
            "\nINSTRUCCIONES:"
        )

        print(
            "1. Si Facebook pide login, inicia sesión."
        )

        print(
            "2. Espera hasta ver la publicación."
        )

        print(
            "3. Desplázate manualmente hasta los comentarios."
        )

        input(
            "\nCuando veas los comentarios, presiona ENTER aquí..."
        )

        print(
            "\nURL ACTUAL:"
        )

        print(page.url)

        print(
            "\nTÍTULO:"
        )

        print(page.title())

        time.sleep(3)

        texto = page.locator(
            "body"
        ).inner_text()

        print(
            "\n=============================="
        )

        print(
            "TEXTO CAPTURADO POR PLAYWRIGHT"
        )

        print(
            "==============================\n"
        )

        print(
            texto[:5000]
        )

        print(
            "\n=============================="
        )

        print(
            "FIN DEL TEXTO"
        )

        print(
            "==============================\n"
        )

        context.close()

    return comentarios


if __name__ == "__main__":

    url = input(
        "Ingrese URL Facebook: "
    )

    extraer_comentarios(
        url
    )