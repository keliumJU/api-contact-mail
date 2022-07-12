from sqlalchemy.sql.expression import desc
from store.db_init import db

class MailUser(db.Model):
    __tablename__ = 'mail_user'
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(100), unique=True);

    def json(self):
        return {
            'id':self.id, 'mail':self.mail,
		}

    @classmethod
    def get_all(self):
        mails = MailUser.query.all()
        return mails 

    @classmethod 
    def save(self, _mail):
        mail_user=MailUser(
            mail=_mail
            )
        db.session.add(mail_user)
        db.session.commit()
        return mail_user
    

    