from flask_restful import Resource

skills = ["Java","Python","C#","JavaScript"]
class Habilidades(Resource):
    def get(self):
        return skills
