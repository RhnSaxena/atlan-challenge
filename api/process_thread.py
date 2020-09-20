from tempfile import NamedTemporaryFile
import shutil
import csv
import time


class Process:
    def __init__(self):
        self._running = True
        self._terminate = False
        self._current_row = 0
        self._total_row = 0

    def pause(self):
        self._running = False
        return "Process paused. Completed {} on line no {}".format(
            (self._current_row / self._total_row) * 100, self._current_row
        )

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

        tempfile = NamedTemporaryFile(mode="w", delete=False, newline="")
        with file.read(), tempfile:
            reader = csv.DictReader(file.stream)
            self._current_row = 1
            # self._total_row = 20000
            self._total_row = len(reader)
            fields = reader.fieldnames
            fields = {fields[1]: fields[1], fields[0]: fields[0], fields[2]: fields[2]}
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            writer.writerow(fields)

            while not self._terminate:
                print(reader[self._current_row])
                writer.writerow(reader[self._current_row])
                self._current_row = self._current_row + 1
                time.sleep(0.10)
                # self._current_row = self._current_row + 1
                while not self._running:
                    if self._terminate:
                        break
                if self._current_row >= self._total_row - 1:
                    self.terminate()
            print("stopped")

        # filename = "employee_birthday.csv"

        shutil.move(tempfile.name, file)