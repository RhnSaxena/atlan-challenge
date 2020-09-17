from process_thread import Process
import threading


class Handler:
    def __init__(self):
        self.__current_object = None

    def create_thread(self, request):

        if not self.__current_object:
            process = Process()
            self.__current_object = process
            process_thread = threading.Thread(target=self.__current_object.run)
            process_thread.start()
            return {"Message": "Process started successfully."}
        else:
            return {
                "Message": "A file already in process. Wait till the process gets completed or try stopping the current process."
            }

    def get_status(self):

        if not self.__current_object:
            return {"Message": "No active process."}
        else:
            return {"Message": "An active process."}

    def thread_pause(self):
        return self.__current_object.pause()

    def thread_resume(self):
        return self.__current_object.resume()

    def thread_stop(self):

        message = self.__current_object.terminate()
        del self.__current_object
        self.__current_object = None
        return message
