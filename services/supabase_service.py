from supabase import create_client

SUPABASE_URL = "https://esxrfpvfqdkvcvriwwzp.supabase.co"

SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVzeHJmcHZmcWRrdmN2cml3d3pwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MDIzMzczOCwiZXhwIjoyMDk1ODA5NzM4fQ.eIm6hV1kTiWq56vMvPAYlASFPmhJtAZUuzlvkF2EjIg"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)