import threading

class ClassBetweenhreads:
    def __init__(self):
        self.client =''
        self.received = []
        self.lock = threading.RLock()
