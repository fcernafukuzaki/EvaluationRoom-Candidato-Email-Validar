from configs.flask_config import db
from object.candidato import Candidato, CandidatoSchema

candidato_schema = CandidatoSchema()


class CandidatoEmailValidarService():

    def valida_email(self, email):
        email_valido, mensaje, candidato = self.valida_email_candidato(email)
        
        if not email_valido:
            return {'mensaje': mensaje}, 404
        return candidato_schema.jsonify(candidato)

    def valida_email_candidato(self, email):
        candidato = db.session.query(Candidato).filter(Candidato.correoelectronico==email)
        if candidato.count():
            print('Se encontró candidato con el correo electronico {}'.format(email))
            return True, 'Existe candidato', candidato.one()
        print('No existe candidato con el correo electronico {}'.format(email))
        return False, 'No existe candidato.', None
