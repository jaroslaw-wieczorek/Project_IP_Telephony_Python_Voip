># Projekt Telefoni IP w języku Python

Overview
----------
>- Implementation of VOIP communicator.

Tools
-------
>- Pycharm / Spyder3
>- Wireshark
>- Ubuntu 18.04

Files
-------------
>- setup - file to create .exe

Attributons
-------------
MIT license

Contributors
-------------
Elżbieta Kaczmarek
Jarosław Wieczorek


Resolve problems with alsa like bottom:
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map
ALSA lib pcm_route.c:867:(find_matching_chmap) Found no matching channel map

[SETUP]
Setup app under linux: 

[install]
sudo apt install python3 
sudo apt install python3-pip
sudo apt install python3-venv

python3 -m venv env

source env/bin/active

pip3 install pip --upgrade
pip3 install -r requirements

requirements.txt

sudo apt install libasound-dev
sudo apt install portaudio19-dev 
sudo apt install libportaudio2 
sudo apt install libportaudiocpp0
sudo apt install ffmpeg 
sudo apt install libav-tools


sudo pip3 install pyaudio

[run]
python3 -m JaroEliCall



