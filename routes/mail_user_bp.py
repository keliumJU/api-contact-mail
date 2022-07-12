from flask import Blueprint

from controllers.MailUserController import store,send_all_mail 

mail_user = Blueprint('mail_user', __name__)

mail_user.route('/create', methods=['POST'])(store)
mail_user.route('/send_all_mail', methods=['POST'])(send_all_mail)

