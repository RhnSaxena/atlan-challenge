import flask
import json
from flask import Response, request
from handler import Handler

app = flask.Flask(__name__)
app.config["DEBUG"] = True

handler = Handler()


@app.route("/status", methods=["GET"])
def status():
    data = handler.get_status()
    return Response(json.dumps({"Details": data["message"]}), status=data["code"])


@app.route("/create", methods=["POST"])
def create_process():
    data = handler.create_thread(request.files["file"])
    return Response(json.dumps({"Details": data["message"]}), status=data["code"])


@app.route("/pause", methods=["GET"])
def pause_process():
    data = handler.thread_pause()
    return Response(json.dumps({"Details": data["message"]}), status=data["code"])


@app.route("/resume", methods=["GET"])
def resume_process():
    data = handler.thread_resume()
    return Response(json.dumps({"Details": data["message"]}), status=data["code"])


@app.route("/stop", methods=["GET"])
def stop_process():
    data = handler.thread_stop()
    return Response(json.dumps({"Details": data["message"]}), status=data["code"])


app.run()