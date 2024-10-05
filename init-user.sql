-- Create a user with specific privileges
CREATE ROLE newt WITH LOGIN ENCRYPTED PASSWORD 'tragef5072';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON ALL TABLES TO newt;