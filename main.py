import json

from flask import Flask
from flask_restful import Api,Resource
import pymysql
import chardet
from config import host,user, password, db_name

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True
api = Api()


class getAllClass(Resource):
    def get(self):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor,
                charset='utf8'
            )
            print("Доступ есть")
            try:
                with connection.cursor() as cursor:
                    select_query = "SELECT class_number FROM `class`"
                    cursor.execute(select_query)
                    data = cursor.fetchall()
                    return data
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
            print("Проблема с подключением")

class getSubjects(Resource):
    def get(self,idClasse):
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Доступ есть")
            try:
                with connection.cursor() as cursor:
                    select_query = f"SELECT disciplines.name_discipline FROM x JOIN class ON x.id_class = class.id_class JOIN disciplines ON x.id_discipline = disciplines.id_discipline WHERE class_number={idClasse}"
                    cursor.execute(select_query)
                    data = cursor.fetchall()
                    # data = json.dumps(data, ensure_ascii=False,)
                    print(data)
                    return data
            finally:
                connection.close()
        except Exception as ex:
            print(ex)
            print("Проблема с подключением")

class getStudents(Resource):
    def get(self,idClasse,subjects):
        return 3
class getExercise(Resource):
    def get(self, codeSubjects, exNum):
        return 4

api.add_resource(getAllClass, '/api/classes')
api.add_resource(getSubjects, '/api/subjects/<int:idClasse>')
api.add_resource(getStudents, '/api/subjects/<int:idClasse>/<string:subjects>')
api.add_resource(getExercise, '/api/students/<string:codeSubjects>/<int:exNum>')
api.init_app(app)

if __name__ == '__main__':
    app.run(port=3000, host="127.0.0.1")



