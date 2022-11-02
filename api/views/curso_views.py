from flask_restful import Resource
#import de __init__.py
from api import api

class CursoList(Resource):
    def get(self):
        return 'olá mundo'

api.add_resource(CursoList, '/cursos')