try:
    import flask
except ModuleNotFoundError:
    exit("Install flask dulu, pip install flask")

from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

# filter lebih kuat, buang tanda petik
def detect_xss(msg):
     return bool(re.search(r'[<>]',msg))

# penting untuk elak buang simbol yg mendorong kepada xss
def sanitize(text):
	return text.replace("<","").replace(">","")

# server index.html sebagai index page
@app.route("/")
def main():
	return render_template("index.html")

# endpoint terima data post
@app.route("/submit", methods=["POST"])
def send():
    data = request.get_json()  
    msg = data.get("msg", "")
    
    if detect_xss(msg):
        return "XSS DETECTED!"

    # penting kalau bersihkan respon sebelum hantar kepada client
    return sanitize(msg)


# run server.py jika dijalankan secara terus bukan import call
if __name__ == "__main__":
    app.run(port=8000, debug=True)
