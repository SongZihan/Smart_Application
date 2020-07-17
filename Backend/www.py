from application import app
from pages.auth_pages import auth
from pages.api import api

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(api, url_prefix="/api")
