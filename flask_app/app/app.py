from routes import keys_router
from flask import Flask


app = Flask(__name__)
app.register_blueprint(keys_router)

if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run(port=8080, threaded=True)
