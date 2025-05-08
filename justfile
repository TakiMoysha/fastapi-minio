set dotenv-load

default_env := "production"
alembic_config := "app/database/migrations/alembic.ini"


# example: just server --port 8000 --host 0.0.0.0 
server *ARGS:
  uv run fastapi dev --reload {{ ARGS }}

setup_db:
  uv run tooling/setup_db.py -q --target fastapiminio:fastapiminio:fastapiminio

# example: just alembic revision --autogenerate
alembic *ARGS:
  uv run -m alembic -c {{ alembic_config }} {{ ARGS }}

# example: just test tests -v -s --log-cli-level=INFO
test target="tests" *ARGS:
  export SERVER_TESTING=true
  export DB_URL="sqlite+aiosqlite:///:memory:"
  uv run pytest {{ target }} {{ ARGS }}

