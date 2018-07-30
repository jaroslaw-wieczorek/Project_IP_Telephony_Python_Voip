from PyQt5 import QtCore
from collections import deque

class Key(QtCore.QObject):

    POOL_COUNT = 3

    def __init__(self, soundFile, parent=None):
        super(Key, self).__init__(parent)
        self.soundFile = soundFile

        self.resourcePool = deque()

        mediaSource = Phonon.MediaSource(soundFile)

        for i in xrange(self.POOL_COUNT):
            mediaObject = Phonon.MediaObject(self)
            audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
            Phonon.createPath(mediaObject, audioOutput)
            mediaObject.setCurrentSource(mediaSource)
            self.resourcePool.append(mediaObject)

    def play(self):
        self.resourcePool.rotate(1)
        m = self.resourcePool[0]
        m.stop()
        m.seek(0)
        m.play()

key=Key("440_sine.wav")
