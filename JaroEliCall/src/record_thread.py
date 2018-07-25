import queue
import os
import time
import wave
from datetime import datetime
from datetime import timedelta
from threading import Thread

import pyaudio
from pydub import AudioSegment
from pydub.playback import play


class Recorder:
    _recording = False
    _frames = queue.Queue()
    _p = ''
    _stream = ''
    _output = ''
    _audio_writer = ''
    _audio_recorder = ''
    _exit = False
    _config = None

    CHANNELS = 1
    WIDTH = pyaudio.paInt16
    RATE = 44100

    def __init__(self, filename):

        self._p = pyaudio.PyAudio()
        self._stream = self._p.open(format=self.WIDTH,
                                    channels=self.CHANNELS,
                                    rate=self.RATE,
                                    input=True,
                                    stream_callback=self._callback)

        self._output = wave.open(filename, 'wb')
        self._output.setnchannels(int(audio_config['channels']))
        self._output.setsampwidth(int(audio_config['width']))
        self._output.setframerate(int(audio_config['rate']))


        self._audio_writer = Thread(target=self._write_queue_to_file)
        self._audio_writer.daemon = True
        self._audio_writer.start()


    def start(self):
        """
        Start the recording process, which will include the disk writer
        :return:
        """
        self._recording = True
        self._audio_recorder = Thread(target=self._async_record)
        self._audio_recorder.start()


    def stop(self):
        """
        Stop the recording process, which will flush buffers and spin down started threads
        :return:
        """
        self._recording = False
        self._frames.join()
        self._exit = True


    def _async_record(self):
        """
        Starts recording from stream asynchronously
        """
        self._stream.start_stream()

        while self._stream.is_active():
            time.sleep(0.05)

        self._stream.stop_stream()
        self._stream.close()

        self._p.terminate()


    def _callback(self, in_data, frame_count, time_info, status):
        """
        Callback function for continuous_record
        Checks global var recording
           If true, put frames into the queue - another thread will pop from the queue and write to disk
           If false, shut down the recorder (we don't want silence or sudden time shifts in one recording file)
        """
        if self._recording:
            self._frames.put(in_data)
            callback_flag = pyaudio.paContinue
        else:
            callback_flag = pyaudio.paComplete

            return in_data, callback_flag


    def _write_queue_to_file(self):
        """
        Write data from a queue to a file object
        """
        while not self._exit:
            data = self._frames.get()
            self._output.writeframes(b''.join(data))
            self._frames.task_done()

#####################
def get_audio_from_filename(filename, length, lowquals):
    """
    Figures out what LQ
    :param filename: The name of the file (direct from sync chat)
    :param length: The length of the file specified in filename (direct from sync chat)
    :param lowquals: An array of finalized low quality recordings
    :return: A file name and relative time index
    """
    # All of these must be absolute paths on the local machine
    # Lowquals will be fully qualified due to stop_start_recording
    # However, filename wont be fully qualified because the file doesn't exist locally yet

    time = datetime.strptime(filename, constants.DATETIME_HQ)  # Auto strips 'HQ_' and '.wav'
    for lowqual in lowquals:
        original = lowqual
        lowqual = os.path.basename(lowqual)
        lq_time = datetime.strptime(lowqual[2:], constants.DATETIME_LQ)  # 2: to cut off the index and underscore
        if lq_time <= time:  # Check if the LQ recording started before the HQ recording
            # Check if the end of the LQ recording is after the end of the HQ recording
            time_end = time + timedelta(0, length, 0)
            lq_length = get_length(original)
            lq_time_end = lq_time + timedelta(0, lq_length, 0)
            if lq_time_end > time_end:
                time_index = time - lq_time
                return {'filename': original,
                        'start_time': time_index.total_seconds(),
                        'end_time': time_index.total_seconds() + length}
    print("Bad file: {} with length {}".format(filename, length))
# Any calling functions should check if value is not None before processing


def playback(filename, start, end=None, playback_time=None):
    print("Trying to play back {}").format(filename)
    Thread(target=_playback, args=(filename, start, end, playback_time))


def _playback(filename, start, end=None, playback_time=None):
    """
    Plays back a wav file from the start point (in seconds) to the end point (in seconds)
    :param filename: filename to playback
    :param start: start time, in seconds.  No more than 3 places after decimal or loss of precision
    :param end: end time, in seconds.  Same as above
    :param playback_time: time to play back.  use instead of end
    """

    file_name, file_extension = os.path.splitext(filename)
    # This method will play back filetypes whose extension matches the coded
    # This includes wav and mp3 so we should be good
    audio = AudioSegment.from_file(filename, format=file_extension[1:])

    if end is None and playback_time is not None:
        # Play the track starting from start for playback_time seconds
        segment = audio[int(start):int(start + playback_time)]
        play(segment)
    elif end is not None and playback_time is None:
        # Play the track starting from start and ending at end
        segment = audio[int(start):int(end)]
        play(segment)
    else:
        # Play the whole thing
        play(audio)



if __name__ == '__main__':
    length = 2.154
    results = get_audio_from_filename(file, length, lowquals)
    if results is not None:
        print("Play file {} at index {} until {} (total length {})".format(results['filename'],
                                                                               results['start_time'],
                                                                               results['end_time'],
                                                                               get_length(results['filename'])))
    else:
        print("No match found for {} with length {}".format(file, length))
