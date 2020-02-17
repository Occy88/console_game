import time


class Timer:
    def __init__(self):
        self.timer_start = 0
        self.timer_end = 0
        self.elapsed = 0
        self.running = False
        self.prev_lap = 0

    def poll(self):
        if self.running:
            return time.time() - self.timer_start
        else:
            return self.elapsed

    def lap(self):
        if not self.running:
            to_return = self.timer_end - self.prev_lap
            self.prev_lap = self.timer_end
        else:
            to_return = time.time() - self.prev_lap
            self.prev_lap = time.time()
        return to_return

    def stop(self):
        self.timer_end = time.time()
        self.elapsed = self.timer_end - self.timer_start
        self.running = False

    def start(self):
        self.timer_start = time.time()
        self.prev_lap = self.timer_start
        self.running = True
