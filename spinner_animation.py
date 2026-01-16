import sys
import time
import threading

class Spinner:
    def __init__(self):
        self.spinner = ["(●    )", "( ●   )", "(  ●  )", "(   ● )", "(    ●)"]
        self.stop_running = False

    def _animate(self):
        while not self.stop_running:
            for char in self.spinner:
                if self.stop_running:
                    break
                # moves the cursor back to the start of the line
                sys.stdout.write(f"\r{char}")
                sys.stdout.flush()
                time.sleep(0.5)
        # Clear the line
        sys.stdout.write("\r" + " " * 8 + "\r")

    def __enter__(self):
        self.stop_running = False
        self.thread = threading.Thread(target=self._animate)
        self.thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_running = True
        self.thread.join()