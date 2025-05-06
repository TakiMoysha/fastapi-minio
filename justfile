set dotenv-load

default_env := "production"
alembic_config := "app/database/migrations/alembic.ini"

setup_db:
  uv run tooling/setup_db.py -q --target fastapiminio_user:fastapiminio_db:fastapiminio

# example: just alembic revision --autogenerate
alembic *ARGS:
  uv run -m alembic -c {{ alembic_config }} {{ ARGS }}

# example: just test tests -v -s --log-cli-level=INFO
test target="tests" *ARGS:
  uv run pytest {{ target }} {{ ARGS }}

