# pyAudioHTTPStreamer

I would like to create one Audio streamer to steam audio to web server so that other can listen via internet

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

```
pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl
pip install Flask
```


# Workaround
The code is not really working and I don't know why

Now I use the VLC Player to do the streaming of the audio
and read the mp3 stream

```html
<audio controls>
    <source src="http://192.168.8.234:8080/mp3" type="audio/mpeg">
</audio>
```