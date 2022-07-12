from flask_migrate import Migrate

#BluePrints
from routes.mail_user_bp import mail_user 

#business logic
from models.MailUser import MailUser 


from store.db_init import db
from store.app_store import app
import flask_cors

from flask import jsonify, make_response

cors=flask_cors.CORS()

app.config.from_object('config')

db.init_app(app)

cors.init_app(app)

migrate = Migrate(app, db, compare_type=True)

@app.route('/')
def index():
  return make_response(
    jsonify({"Hello": "World"}),
    200)

app.register_blueprint(mail_user, url_prefix='/api/mail_user')

if __name__ == '__main__':
    app.debug = True
    app.run()
