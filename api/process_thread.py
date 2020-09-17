class Process:
    def __init__(self):
        self._running = True
        self._terminate = False

    def pause(self):
        self._running = False
        return {"Message": "Process paused."}

    def resume(self):
        self._running = True
        return {"Message": "Process resumed."}

    def terminate(self):
        self._terminate = True
        return {"Message": "Process stopped."}

    def run(self):
        i = 0
        while not self._terminate:
            print(str(i) + "\n")
            i = i + 1
            while not self._running:
                print("paused")
                if self._terminate:
                    break
        print("stopped")


# def create_thread(request):

#     if not current_object:
#         process = Process()
#         current_object = process
#         process_thread = threading.Thread(target=current_object.run)
#         process_thread.start()
#         return {"Message": "Process started successfully."}
#     else:
#         return {
#             "Message": "A file already in process. Wait till the process gets completed or try stopping the current process."
#         }


# def thread_pause():
#     return current_object.pause()


# def thread_resume():
#     return current_object.resume()


# def thread_stop():
#     return current_object.terminate()


# def get_status():

#     if not current_object:
#         return {"Message": "No active process."}
#     else:
#         return {"Message": "An active process."}
