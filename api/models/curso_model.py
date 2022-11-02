from api import db

class Curso(db.Model):
    __tablename__ = "curso"
    ip = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    data_publicacao = db.Column(db.Date, nullable=False)