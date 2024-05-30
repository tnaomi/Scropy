CREATE DATABASE scropy;
CREATE USER tada WITH PASSWORD 'xxxxx';
-- DJANGO recommended settings below
ALTER ROLE tada SET client_encoding TO 'utf8';
ALTER ROLE tada SET default_transaction_isolation TO 'read committed';
ALTER ROLE tada SET timezone to 'UTC';
-- Give admin privs to tada
GRANT ALL PRIVILEGES ON DATABASE scropy TO tada;
\q