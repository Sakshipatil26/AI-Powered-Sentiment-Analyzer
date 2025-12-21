from flask import Flask, render_template, request
from sentiment_ai import analyze_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        result = analyze_sentiment(text)

    return render_template("index.html", result=result, text=text)

if __name__ == "__main__":
    app.run(debug=True)
