from services.supabase_service import supabase
from services.topic_service import detectar_tema

response = (
    supabase
    .table("comentarios")
    .select(
        "id, comentario"
    )
    .execute()
)

comentarios = response.data

for item in comentarios:

    tema = detectar_tema(
        item["comentario"]
    )

    (
        supabase
        .table("comentarios")
        .update({
            "tema": tema
        })
        .eq(
            "id",
            item["id"]
        )
        .execute()
    )

    print(
        item["id"],
        tema
    )

print(
    "Temas actualizados correctamente"
)