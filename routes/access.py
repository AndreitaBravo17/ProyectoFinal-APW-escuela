from flask import request, jsonify, Response
from bson import json_util
from bson.objectid import ObjectId

def get_aulas(mongo):
    if request.method == "GET":
        # Verificamos si ya existe esa cedula
        students = mongo.db.aulas.find({})
        data = {
            "status": True,
            "data": students
        }
        result = json_util.dumps(data)
        return Response(result, mimetype="application/json")

    else:
        return jsonify({"error": "404"})

def get_students(mongo):

    if request.method == "POST":
        idAula = ObjectId(request.form["id"])
        # Verificamos si ya existe esa cedula
        students = mongo.db.usuarios.aggregate([
            {
                "$match": {
                    "aula":idAula
                }
            },
            {
                "$lookup":  {
                    "from": "aulas",
                    "foreignField": "_id",
                    "localField": "aula",
                    "as": "aula"
                }
            }
        ])
        data = {
            "status": True,
            "data": students
        }
        result = json_util.dumps(data)
        return Response(result, mimetype="application/json")
    else:
        return jsonify({
            "result": False,
            "error": "No hay cupos Disponibles"
        })