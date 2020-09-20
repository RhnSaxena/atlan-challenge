import flask
import json
from flask import Response, request
from handler import Handler
import uuid

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

handler = Handler()


@app.route("/status", methods=["GET"])
def status():
    data = handler.get_status()
    return Response(json.dumps({"Details": data["message"]}), status=data["code"])


@app.route("/create", methods=["POST"])
def create_process():

    if request.files["file"]:
        filename = str(uuid.uuid4()) + ".csv"
        request.files["file"].save(filename)
        data = handler.create_thread(filename)
        return Response(json.dumps({"Details": data["message"]}), status=data["code"])
    else:
        return Response(
            json.dumps(
                {"Details": "Please attach a file. Ensure that the key is 'file'"}
            ),
            status=403,
        )


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