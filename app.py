from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/todo"

mongo = PyMongo(app)

@app.route("/ping")
def index():
    return jsonify("pong!")

# Task Related APIs
@app.route("/api/tasks", methods=["GET"])
def list_tasks():
    result = []
    all_tasks = mongo.db.tasks.find()
    for task in all_tasks:
        result.append(
            {"_id": str(task["_id"]), "title": task["title"]}
            )
    return jsonify(result)

@app.route("/api/tasks", methods=["POST"])
def add_task():
    request_body = request.get_json()
    task_title = request_body["title"]
    
    task_id = mongo.db.tasks.insert({"title": task_title})

    return jsonify(str(task_id))

@app.route("/api/tasks/:id", methods=["PUT"])
def update_task():
    pass

@app.route("/api/tasks/:id", methods=["DELETE"])
def delete_task():
    pass

@app.route("/api/tasks/:id/complete", methods=["POST"])
def complete_task():
    pass

# User Related APIs
@app.route("/api/signup", methods=["POST"])
def create_user():
    pass

@app.route("/api/login", methods=["POST"])
def login_user():
    pass

@app.route("/api/user", methods=["GET"])
def get_user():
    pass

@app.route("/api/user", methods=["PUT"])
def modify_user():
    pass

@app.route("/api/user", methods=["DELETE"])
def delete_user():
    pass

@app.route("/api/user/clear", methods=["POST"])
def clear_user_data():
    pass

@app.route("/api/logout", methods=["POST"])
def logout_user():
    pass