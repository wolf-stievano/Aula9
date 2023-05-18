from flask import json, request, jsonify
import flask
from bson import json_util
from app import app
from app import db
from bson.objectid import ObjectId

@app.route('/')
@app.route('/index')
def index():
    return flask.jsonify(json.loads(json_util.dumps(db.livro.find({}).sort("_id", 1))))

@app.route('/create', methods=['POST',])
def create():
    json_data = request.json
    if json_data is not None:
        db.livro.insert_one(json_data)
        return jsonify(mensagem='livro criado')
    else:
        return jsonify(mensagem='livro não criado')

@app.route('/update', methods=['POST'])
def update():
    json_data = request.json
    if json_data is not None and db.livro.find_one({"_id": ObjectId(json_data["id"])}) is not None:
        db.livro.update_one({'_id': ObjectId(json_data["id"])}, {"$set": {'Titulo': json_data["Titulo"], 'Autores': json_data["Autores"], 'Editora':json_data["Editora"],'Ano':json_data["Ano"],'ISBN':json_data["ISBN"], "Preco":json_data["Preco"]}})
        return jsonify(mensagem='livro atualizado')
    else:
        return jsonify(mensagem='livro não atualizado')

@app.route("/delete/<string:bookId>")
def delete(bookId):
    result = db.livro.delete_one({"_id": ObjectId(bookId)})
    if(result.deleted_count > 0):
        return jsonify(mensagem='livro removido')
    else:
        return jsonify(mensagem='livro não removido')

@app.route("/getid/<string:bookId>")
def getid(bookId):
    livro = db.livro.find_one({"_id": ObjectId(bookId)})
    return flask.jsonify(json.loads(json_util.dumps(livro)))
