from configs.flask_config import db, ma


class Candidato(db.Model):
    __table_args__ = {"schema": "evaluationroom"}
    __tablename__ = 'candidato'

    idcandidato = db.Column(db.Integer, primary_key=True)
    correoelectronico = db.Column(db.String())
    selfregistration = db.Column(db.Boolean())


class CandidatoSchema(ma.Schema):
    class Meta:
        fields = ('idcandidato', 'selfregistration')
