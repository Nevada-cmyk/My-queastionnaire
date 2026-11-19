from flask import Flask, render_template,request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def questionnaire():
    if request.method == "POST":
        answers = {
            "name": request.form.get("name"),
            "country": request.form.get("country"),
            "food": request.form.get("food"),
            "activity": request.form.get("actvity"),
            "artist": request.form.get("artist"),
            "song": request.form.get("song"),
            "color": request.form.get("color"),
            "movie": request.form.get("movie"),
            "language": request.form.get("language"),
            "guilty_pleasure": request.form.get("guilty_pleasure")
        }
        return render_template("index.html", answers=answers)

    return render_template("index.html", answers=None)

if __name__  == "__main__":
    app.run(debug=True)