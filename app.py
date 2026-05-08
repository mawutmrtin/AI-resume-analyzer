from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_resume(text):
    blob = TextBlob(text)

    sentiment = blob.sentiment.polarity

    keywords = [
        "python",
        "machine learning",
        "data analysis",
        "artificial intelligence",
        "ai",
        "communication",
        "leadership",
        "teamwork",
        "problem solving",
        "flask",
        "django",
        "sql",
        "data science"
    ]

    found_keywords = []

    for word in keywords:
        if word.lower() in text.lower():
            found_keywords.append(word)

    score = len(found_keywords) * 10

    if sentiment > 0:
        score += 10

    score = min(score, 100)

    return {
        "score": score,
        "keywords": found_keywords,
        "sentiment": round(sentiment, 2)
    }

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":
        resume_text = request.form["resume"]
        result = analyze_resume(resume_text)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)