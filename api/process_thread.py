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

    def get_state(self):
        if self._running is True:
            return "running"
        elif self._running is False:
            return "paused"

    def progress(self):
        return "Completed {}%, currently on row number {}.".format(
            round((self._current_row / self._total_row) * 100, 2), self._current_row
        )

    def resume(self):
        self._running = True
        return "Process resumed. {}".format(self.progress())

    def pause(self):
        self._running = False
        return "Process paused. {}".format(self.progress())

    def terminate(self):
        self._terminate = True
        return "Process stopped at row number {}. Completed {}% processing.".format(
            self._current_row, round((self._current_row / self._total_row) * 100, 2)
        )

    def run(self, filename):

        tempfile = NamedTemporaryFile(mode="w", delete=False, newline="")
        with open(filename, "r") as csv_file, tempfile:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
            self._total_row = len(rows)
            fields = reader.fieldnames
            fields = {fields[1]: fields[1], fields[0]: fields[0]}
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            writer.writerow(fields)

            while not self._terminate:
                writer.writerow(rows[self._current_row])
                self._current_row = self._current_row + 1
                time.sleep(0.1)
                while not self._running:
                    if self._terminate:
                        break
                if self._current_row == self._total_row:
                    self.terminate()
        shutil.move(tempfile.name, filename)