import time

class Timer:
    time: int
    remaining_time: int

    def __init__(self, time):
        self.time = time

    def countdown(self):
        self.remaining_time = self.time
        while self.remaining_time > 0:
            print(self.remaining_time)
            self.remaining_time -= 1
            time.sleep(1)