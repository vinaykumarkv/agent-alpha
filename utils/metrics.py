import time
import psutil

class MetricsTracker:
    def __init__(self):
        self.start_time = time.time()
        self.token_usage = 0

    def add_tokens(self, tokens):
        self.token_usage += tokens

    def end(self):
        self.end_time = time.time()

    def get_latency(self):
        return round(self.end_time - self.start_time, 2)

    def get_system_metrics(self):
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent

        return {
            "cpu_usage": cpu,
            "memory_usage": memory
        }