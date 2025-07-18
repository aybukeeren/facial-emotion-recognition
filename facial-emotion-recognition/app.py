from flask import Flask, request, render_template
from deepface import DeepFace

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        img = request.files["image"]
        img_path = "uploaded.jpg"
        img.save(img_path)

        try:
            analysis = DeepFace.analyze(img_path, actions=["emotion"])
            emotion = analysis[0]['dominant_emotion']
            return render_template("index.html", result=emotion)
        except Exception as e:
            return f"Hata: {str(e)}"

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
    app.run(debug=True)
