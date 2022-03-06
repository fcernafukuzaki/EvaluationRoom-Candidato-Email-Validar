from .flask_config import api
from controller.candidatoemailvalidar_controller import *

api.add_resource(CandidatoEmailValidarController,
    '/candidato_email_validar')
