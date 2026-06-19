from flask import Blueprint
from flask import jsonify

from services.supabase_service import supabase

test_bp = Blueprint(
    "test",
    __name__
)

@test_bp.route(
    "/test-supabase",
    methods=["GET"]
)
def test_supabase():

    response = supabase.table(
        "comentarios"
    ).select("*").limit(5).execute()

    return jsonify(
        response.data
    )