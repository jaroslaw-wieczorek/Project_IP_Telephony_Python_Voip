import threading

class ClassBetweenThreads:
    def __init__(self):
        self.users = ''
        self.received = []
        self.lock = threading.RLock()

