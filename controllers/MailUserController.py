from flask import json, request, make_response, jsonify
from sqlalchemy.sql.expression import desc
from models.MailUser import MailUser 
from helper.mail_service import *

#MAIL SERVICE CONFIG
FROM_ADMIN = 'exilesoft.servico@gmail.com'
KEY_MAIL = 'oixzbucncdukgjio'

def store():
    req=request.get_json(force=True)
    _mail=req.get('mail',None)
    print("this is mail")
    print(_mail)
    if(_mail): 
        mail_user = MailUser.save(
            _mail=_mail
            )
        if(mail_user):
            return make_response(jsonify({"msg":"Correo agregado satisfactoriamente"}), 200)
        else:
            return make_response(jsonify({"error":"Se produjo un error al agregar el correo"}), 400)
    else:
        return make_response(jsonify({"error":"Se produjo un error al agregar el correo"}), 400)

def send_all_mail():
    req=request.get_json(force=True)
    message=req.get('message',None)
    subject=req.get('subject',None)
    mails_obj=MailUser.get_all()
    list_mails=[]

    for item in mails_obj:
        list_mails.append(item.mail)

    send_message(FROM_ADMIN,list_mails,subject,message,KEY_MAIL)

    return make_response(jsonify({"msg":"Mensaje enviado a todos los subscriptores via mail"}), 200)
    
