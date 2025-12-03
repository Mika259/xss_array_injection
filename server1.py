try:
    import flask
except ModuleNotFoundError:
    exit("Install flask dulu, pip install flask")

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# filter lemah
def detect_xss(msg):
    payloads = ["<",">"]
	for x in msg:
        if x in payloads:
            return True
        else:
            return False

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

    # kembalikan respon tanpa dibersihkan
    return msg


# run server.py jika dijalankan secara terus bukan import call
if __name__ == "__main__":
    app.run(port=8000, debug=True)
