#!/bin/sh
set -e
cmd="$@"

# This entrypoint is used to play nicely with the current cookiecutter configuration.
# Since docker-compose relies heavily on environment variables itself for configuration, we'd have to define multiple
# environment variables just to support cookiecutter out of the box. That makes no sense, so this little entrypoint
# does all this for us.

# the official postgres image uses 'postgres' as default user if not set explictly.
if [ -z "$POSTGRES_USER" ]; then
    export POSTGRES_USER=postgres
fi


postgres_ready () {
python3 << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(dbname="$POSTGRES_NAME", user="$POSTGRES_USER",
    password="$POSTGRES_PASSWORD", host="$POSTGRES_HOST",
    port="$POSTGRES_PORT")
except psycopg2.OperationalError as e:
    print(e)
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."
exec $cmd
