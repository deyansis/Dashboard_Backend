import joblib

modelo_filtro, vectorizer_filtro = joblib.load(
    "models/modelo_filtro.pkl"
)

def filtrar_comentario(comentario):

    prediccion = modelo_filtro.predict(

        vectorizer_filtro.transform(
            [comentario]
        )

    )[0]

    return prediccion