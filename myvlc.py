# pip install python-vlc
# wiki.videolan.org/Python_bindings/

import vlc

sout=":sout=#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:8080/mp3} :sout-all :sout-keep"

myInstance = vlc.Instance()
Media = myInstance.vlm_add_broadcast(psz_name="psz_name", psz_input='dshow:\\', psz_output=sout, i_options=0, ppsz_options=None, b_enabled=True, b_loop=False)
Media.get_mrl()