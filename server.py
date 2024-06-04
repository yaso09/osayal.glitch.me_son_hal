from flask import *
from getTickets import *

app = Flask(__name__)

@app.route("/")
def master():
    return render_template("bilet.html")

@app.route("/bilet")
def bilet():
    return render_template("bilet.html")

@app.route("/api", methods=["POST"])
def api():
    ticket = request.form["ticket"]
    aday = request.form["aday"]
    if isTicketUsed(ticket): return "Bu bilet kullanılmış"
    else:
        oyver(ticket, aday)
        return "Oyunuz başarıyla verildi"

if __name__ == "__main__":
    app.run(port=3000, debug=True)


