from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
  return (
      "Hello, World! Welcome to my Code-to-Cloud Pipeline (Clean Baseline)."
  )


if __name__ == "__main__":
  # Run on port 8080 to match standard cloud container expectations
  app.run(host="0.0.0.0", port=8080)