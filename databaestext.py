import os
import dj_database_url

# Get DATABASE_URL from environment variables
DATABASE_URL = os.getenv('DATABASE_URL')

# Parse the DATABASE_URL
db_config = dj_database_url.parse(DATABASE_URL)

# Extract components
DATABASE_NAME = db_config['NAME']
DATABASE_USER = db_config['USER']
DATABASE_PASSWORD = db_config['PASSWORD']
DATABASE_HOST = db_config['HOST']
DATABASE_PORT = db_config['PORT']

# Print or use these variables as needed
print(f"DATABASE_NAME: {DATABASE_NAME}")
print(f"DATABASE_USER: {DATABASE_USER}")
print(f"DATABASE_PASSWORD: {DATABASE_PASSWORD}")
print(f"DATABASE_HOST: {DATABASE_HOST}")
print(f"DATABASE_PORT: {DATABASE_PORT}")

# Alternatively, you can write these values directly to a .env file
with open('.env', 'w') as f:
    f.write(f"DATABASE_NAME={DATABASE_NAME}\n")
    f.write(f"DATABASE_USER={DATABASE_USER}\n")
    f.write(f"DATABASE_PASSWORD={DATABASE_PASSWORD}\n")
    f.write(f"DATABASE_HOST={DATABASE_HOST}\n")
    f.write(f"DATABASE_PORT={DATABASE_PORT}\n")
