from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html", active_page="home")

@app.route("/Features")
def features():
    return render_template("features.html", active_page="features")

@app.route("/About")
def about():
    return render_template("about.html", active_page="about")

if __name__ == "__main__":
    app.run(debug=True)



import jwt
import time

@app.route("/dashboard")
def dashboard():
    METABASE_SITE_URL = "http://localhost:3000"
    METABASE_SECRET_KEY = "4d50ef39e0169eacb2e3c224e8cb48ffea909961bc7a056dcf317a1ee0c0d727"

    payload = {
        "resource": {"dashboard": 2},
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiry
    }

    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
    iframeUrl = f"{METABASE_SITE_URL}/embed/dashboard/{token}#bordered=true&titled=true"

    return render_template("dashboard.html", iframeUrl=iframeUrl)