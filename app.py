from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        n = int(request.form["number"])
        c = 0
        for i in range(2, n // 2):
            if n % i == 0:
                c = 1
                break
        if c == 0:
            result = f"{n} is a Prime Number"
        else:
            result = f"{n} is Not a Prime Number"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
