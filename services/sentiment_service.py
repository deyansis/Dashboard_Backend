import joblib

from utils.text_utils import limpiar_texto

modelo, vectorizer = joblib.load(
    "models/modelo.pkl"
)

def analizar_sentimiento(texto):

    texto_limpio = limpiar_texto(
        texto
    )

    texto_vec = vectorizer.transform(
        [texto_limpio]
    )

    prediccion = modelo.predict(
        texto_vec
    )[0]

    return prediccion