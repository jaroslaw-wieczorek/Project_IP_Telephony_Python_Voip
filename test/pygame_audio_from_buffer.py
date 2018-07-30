import pygame
import subprocess

#pygame.init()
rawdata = subprocess.check_output([
    'sox', '-n', '-b', '16', '-e', 'signed', '-r', '44100',
    '-c', '1', '-t', 'raw', '-', 'synth', '0.1', 'sin', '700'])
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1)
pygame.init()
beep = pygame.mixer.Sound(buffer=rawdata)
pygame.mixer.Sound.play(beep)
pygame.quit()
