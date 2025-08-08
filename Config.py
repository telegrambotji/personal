import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 27194475))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', b9eaaeead349eb9c593bfe9ae04ded7d)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', 8199466118:AAG4qKhzLP-kw8MFXBpXDhQpvPG3JHbVB0g)
    DATABASE_URL = os.environ.get('DATABASE_URL', mongodb+srv://tutorialmaster22103:tutorialmaster22103@cluster0.pahxkfp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@mrdesktops"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""
    DATABASE_URL = ""
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "StarkBots"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]

DEVS = [1744109441, 1946995626]
