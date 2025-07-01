#!/bin/bash

# Load environment variables (edit these if needed)
export $(grep -v '^#' .env | xargs)

# Drop all tables in the database
psql "host=$POSTGRES_HOST port=$POSTGRES_PORT dbname=$POSTGRES_DB user=$POSTGRES_USER password=$POSTGRES_PASSWORD" <<EOF
DO
\$do\$
BEGIN
   EXECUTE
   (SELECT string_agg('DROP TABLE IF EXISTS "' || tablename || '" CASCADE;', ' ')
    FROM pg_tables
    WHERE schemaname = 'public'
   );
END
\$do\$;
EOF