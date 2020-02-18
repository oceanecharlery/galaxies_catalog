from flask import Flask, render_template, jsonify, make_response, request 
from flask_restplus import Api, Resource

#from initialization import Objects 
from initialization import engine
from initialization import Messier, db_session

app = Flask(__name__)
api = Api(app=app)
messier = Messier()


##DEBUT CREATION DES ROUTES 

@api.route("/index")
class Test(Resource):
    def get(self):
        headers = {'content-type': 'text/html'}
        return make_response(render_template('index.html'), 200,headers)



@api.route("/galaxies")
class Test(Resource):
    def get(self):
        res = messier.all()
        print(res)
        return jsonify(res)

@api.route("/galaxies/messier/<id>")
class Test(Resource):
    def get(self,id):
        res = messier.getByMessier(id)
        print(res)
        return jsonify(res)


@api.route("/galaxies/ngc/<ngc>")
class Test(Resource):
    def get(self,ngc):
        res = messier.getByNGC(ngc)
        print(res)
        return jsonify(res)

@api.route("/galaxies/constellation/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByConstellation(category)
        print(res)
        return jsonify(res)

@api.route("/galaxies/constellation_en/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByConstellationEN(category)
        print(res)
        return jsonify(res)

@api.route("/galaxies/constellation_fr/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByConstellationFR(category)
        print(res)
        return jsonify(res)


@api.route("/galaxies/constellation_latin/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByConstellationLATIN(category)
        print(res)
        return jsonify(res)

@api.route("/galaxies/right_ascension/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByRightAscension(category)
        print(res)
        return jsonify(res)

@api.route("/galaxies/declinaison/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByDeclinaison(category)
        print(res)
        return jsonify(res)

@api.route("/galaxies/discoverer/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByDiscoverer(category)
        print(res)
        return jsonify(res)


@api.route("/galaxies/object_type/<path:category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByObjectType(category)
        print(res)
        return jsonify(res)


@api.route("/galaxies/season/<path:category>")
class Test(Resource):
    def get(self,category):
        res = messier.getBySeason(category)
        print(res)
        return jsonify(res)

@api.route("/galaxies/magnitude/<path:min>/<path:max>")
class Test(Resource):
    def get(self,min, max):
        res = messier.getByMagnitude(min, max)
        print(res)
        return jsonify(res)

        
### FIN DES ROUTES









##Test def

    def post(self):
        """
        Add a new galaxy to the list
        """
        data = messier.get_json()
        if not data:
            data = {"response": "ERROR"}
            return data, 404
        else:
            name = data.get('name')
            if name:
                if engine.galaxies.find_one({"name": name}):
                    return {"response": "galaxy already exists."}, 403
                else:
                    engine.insert(data)





@api.route("/galaxies/<string:name>")
class galaxy(Resource):
    def put(self, name):
        """
        Edits a selected galaxy
        """
        data = messier.get_json()
        mydb.galaxies.update({'Name': name}, {'set': data})
    def delete(self, name):
        """
    Delete a selected galaxy
    """

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# comment
app.run(host="0.0.0.0", port=80, debug=True)
