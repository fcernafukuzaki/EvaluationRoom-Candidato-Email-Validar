from flask import request
from flask_restful import Resource
from configs.flask_config import app
from service.candidatoemailvalidar_service import CandidatoEmailValidarService
from service.autorizador_service import AutorizadorService

candidatoemailvalidar_service = CandidatoEmailValidarService()
autorizador_service = AutorizadorService()

class CandidatoEmailValidarController(Resource):

    def get(self, email_candidato):
        token = request.headers['Authorization']
        valido = autorizador_service.validar_token(token)
        if valido:
            return candidatoemailvalidar_service.valida_email(email_candidato)
        return {'mensaje': 'Operación no valida.'}, 403