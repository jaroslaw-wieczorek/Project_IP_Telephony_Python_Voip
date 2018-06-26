import threading

class ClassBetweenhreads:
    def __init__(self):
        self.received = []
        self.lock = threading.RLock()
