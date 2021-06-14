from habilidades import Habilidades
import json
from flask import Flask,request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

desenvolvedores = [{"ID": 0,"nome": "Elias", "habilidades":['Python', 'Flask']},{"ID": 1,"nome":"joãozinho","habilidades":['Python','Django']}]
# Devolve um desenvolvedor pelo ID, também deleta e altera um desenvolvedor
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f"Desenvolvedor de ID {id:2d} não encontrado"
            response = {'status':'erro','mensagem':mensagem}
        except Exception:
            mensagem = "Erro desconhecido. Por favor, procure o administrador da API."
            response = {'status':'erro','mensagem':mensagem}
        finally:
            return response
    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self,id):
        info = desenvolvedores.pop(id)
        return {'status':"sucesso","mensagem":"registro excluído com sucesso."}
    def post(self,id):
        dados = json.loads(request.data)
        indice = len(desenvolvedores)
        desenvolvedores.append(dados)
        desenvolvedores[indice]['id'] = indice
        return dados
# Lista todos os desenvolvedores e permite registrar um novo
class Lista_de_desenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        indice = len(desenvolvedores)
        desenvolvedores.append(dados)
        desenvolvedores[indice]['id'] = indice
        return desenvolvedores
        
        
api.add_resource(Desenvolvedor, "/dev/<int:id>")
api.add_resource(Lista_de_desenvolvedores,"/dev")
api.add_resource(Habilidades, "/skills")

if __name__ == "__main__":
    app.run(debug=True)