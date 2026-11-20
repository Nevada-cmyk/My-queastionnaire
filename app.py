from flask import Flask, render_template,request
import os
import resend
from dotenv import load_dotenv

load_dotenv()
resend.api_key = os.getenv("RESEND_API_KEY")
print("Resend key loaded:", bool(os.getenv("RESEND_API_KEY")))
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
        email_body = f"""
New questionnaire response!
Name: {answers['name']}
country: {answers['country']}
favorite food: {answers['food']}
free-time activities: {answers['activity']}
favorite artist: {answers['artist']}
favorite song: {answers['song']}
favorite color: {answers['color']}
favorite movie: {answers['movie']}
programming language: {answers['language']}
Guilty pleasure: {answers['guilty_pleasure']}
"""
        params ={
            "from" : "My Questionnaire <onboarding@resend.dev>",
            "to": ["ngosaodette@gmail.com"],
            "subject": "New Questionnaire Response",
             "text": email_body
         }

        resend.Emails.send(params)
        return render_template("index.html", answers=answers)

    return render_template("index.html", answers=None)

if __name__  == "__main__":
    app.run(debug=True)