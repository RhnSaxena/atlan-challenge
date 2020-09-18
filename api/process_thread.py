class Process:
    def __init__(self):
        self._running = True
        self._terminate = False
        self._current_row = 0
        self._total_row = 0

    def pause(self):
        self._running = False
        return "Process paused."

    def resume(self):
        self._running = True
        return "Process resumed."

    def terminate(self):
        self._terminate = True
        return "Process stopped."

    def get_state(self):
        if self._running is True:
            return "running"
        elif self._running is False:
            return "paused"

    def run(self, file):
        self._current_row = 0
        self._total_row = 100000
        while not self._terminate:
            print(self._current_row)
            self._current_row = self._current_row + 1
            while not self._running:
                if self._terminate:
                    break
            if self._current_row > self._total_row:
                self.terminate()
        print("stopped")
