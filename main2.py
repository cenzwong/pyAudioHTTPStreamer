from flask import Flask, Response
import pyaudio

p = pyaudio.PyAudio()
app = Flask(__name__)


@app.route("/wav")
def streamwav():
    def generate():
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, frames_per_buffer=1024)
        data = stream.write(1024)
        while data:
            yield data
            data = stream.write(1024)
    return Response(generate(), mimetype="audio/x-wav")


# @app.route("/audio")
# def streamwav():
#     def generate():
#         with open("sample.wav", "rb") as fwav:
#             data = fwav.read(1024)
#             while data:
#                 yield data
#                 data = fwav.read(1024)
#     return Response(generate(), mimetype="audio/x-wav")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)