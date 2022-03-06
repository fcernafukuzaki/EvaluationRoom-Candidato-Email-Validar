class AutorizadorService:

    @staticmethod
    def validar_token(token):
        if token:
            return True
        return False
