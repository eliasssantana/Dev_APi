from flask_restful import Resource
from flask import request
import json
skills = ["Java","Python","C#","JavaScript"]

class Error(Exception):
    pass

class JaContemError(Error):
    def __init__(self,mensagem):
        self.mensagem = mensagem

class Habilidades(Resource):
    def get(self,id):
        return skills
    def put(self, id):
        try:
            new_skill= json.loads(request.data)
            for skill in skills:
                if new_skill == skill:
                    raise JaContemError("Erro! habilidade já foi registrada.")
            else:
                skills[id] = new_skill
                response = {"status":"sucesso","mensagem":"registro alterado na origem."}
        except IndexError:
            response = {"status":"erro","mensagem":"index inválido."}
        except Exception:
            response = {"status":"erro","mensagem":"tente novamente."}
        finally:
            return response

    def post(self,id):
        try:
            new_skill = json.loads(request.data)
            for skill in skills:
                if new_skill == skill:
                    raise JaContemError("Erro, habilidade já foi registrada.")
            else:
                skills.append(new_skill)
                response = {"status":"sucesso","mensagem":"registro adicionado."}
        except Exception:
            response = {"status":"erro","mensagem":"erro desconhecido"}
        finally:
            return response
    def delete(self,id):
        try:
            skills.pop(id)
            response = {"status": "sucesso","mensagem":"registro deletado."}
        except IndexError:
            response = {"status": "erro","mensagem":"indice não encontrado"}
        finally:
            return response



