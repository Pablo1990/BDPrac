chmod a+x scripts/*

mkdir temp

echo localhost:5432:masterdb:masteruser:masterpass > ~/.pgpass

chmod 0600 ~/.pgpass

psql -h localhost masterdb masteruser -f source/sqlFiles/tablas.sql 
