from flask import Flask, render_template, jsonify
from flask_restplus import Resource, Api
from initialization import Messier, db_session 

app = Flask(__name__)
api = Api(app=app)

messier = Messier()

@api.route("/galaxies")
class Test(Resource):
    def get(self):
        res = messier.all()
        print(res)
        return jsonify(res)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app.run(host="0.0.0.0", port=80, debug=True)