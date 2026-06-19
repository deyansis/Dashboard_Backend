from supabase import create_client

SUPABASE_URL = "https://esxrfpvfqdkvcvriwwzp.supabase.co"

SUPABASE_KEY = "sb_publishable_DwHaM8YCLzcsz68zNvqslw_zkyq5-J9"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)