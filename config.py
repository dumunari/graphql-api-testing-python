from os import environ
DOGOPHQL_URI = environ.get("DOGOPHQL_URI", "http://localhost:8080")
DOGOPHQL_PATH = environ.get("DOGOPHQL_PATH", "/dogophql")