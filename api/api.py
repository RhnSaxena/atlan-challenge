import flask

# import process_thread
from handler import Handler

app = flask.Flask(__name__)
app.config["DEBUG"] = True

handler = Handler()


# def handler(request):

#     if request["method"] is "main":
#         return globals()[request["method"]](request)
#     elif request["method"] is "thread_stop":
#         message = globals()[request["method"]]()
#         del current_object
#         return message
#     else:
#         return globals()[request["method"]]()


@app.route("/", methods=["GET"])
def status():
    # request = {}
    # request["method"] = "get_status"
    return handler.get_status()


@app.route("/", methods=["POST"])
def create_process():
    # request = {}
    # request["method"] = "main"
    return handler.create_thread("request")


@app.route("/pause", methods=["GET"])
def pause_process():
    # request = {}
    # request["method"] = "thread_pause"
    return handler.thread_pause()
    # return thread_pause()


@app.route("/resume", methods=["GET"])
def resume_process():
    # request = {}
    # request["method"] = "thread_resume"
    return handler.thread_resume()
    # return thread_resume()


@app.route("/stop", methods=["GET"])
def stop_process():
    # request = {}
    # request["method"] = "thread_stop"
    return handler.thread_stop()
    # return thread_stop()


app.run()