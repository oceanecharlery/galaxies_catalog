from flask import Flask, render_template, jsonify
from flask_restplus import Resource, Api
from initialization import Objects 

app = Flask(__name__)
api = Api(app=app)

messier = Objects()

@api.route("/galaxies")
class Test(Resource):
    def get(self):
        res = messier.all()
        print(res)
        return jsonify(res)

app.run(host="0.0.0.0", port=80, debug=True)