# The Handler class handles the processes to be performed.
# It connects the app routes in api module with their respective processes.

from process_thread import Process
import threading


class Handler:
    def __init__(self):
        self.__current_process = None

    def getState(self):
        if not self.__current_process:
            return False
        elif self.__current_process._terminate:
            return False
        else:
            return True

    # To start a new process, handles the route POST '/'
    def create_thread(self, file):

        if not self.getState():
            self.__current_process = Process()
            process_thread = threading.Thread(
                target=self.__current_process.run, kwargs=dict(file=file)
            )
            process_thread.start()
            return {"message": "Process started successfully.", "code": 201}
        else:
            return {
                "message": "A file already in process. Wait till the process gets completed or try stopping the current process.",
                "code": 403,
            }

    # To get the status of the process, handles the route GET '/'
    def get_status(self):

        if not self.getState():
            return {"message": "No active process.", "code": 200}
        else:
            return {
                "message": "An active process, currently {state} ".format(
                    state=self.__current_process.getState()
                ),
                "code": 200,
            }

    # To pause the process, handles the route GET '/pause'
    def thread_pause(self):
        if not self.getState():
            return {"message": "No active process.", "code": 403}
        else:
            return {"message": self.__current_process.pause(), "code": 200}

    # To resume the process, handles the route GET '/resume'
    def thread_resume(self):
        if not self.getState():
            return {"message": "No active process.", "code": 403}
        else:
            return {"message": self.__current_process.resume(), "code": 200}

    # To stop the process, handles the route GET '/stop'
    def thread_stop(self):

        if not self.getState():
            return {"message": "No active process.", "code": 403}
        else:
            message = self.__current_process.terminate()
            del self.__current_process
            self.__current_process = None
            return {"message": message, "code": 200}
