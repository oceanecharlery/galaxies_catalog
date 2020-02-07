from flask import Flask, render_template, jsonify
from flask_restplus import Api, Resource

#from initialization import Objects 
from initialization import engine
from initialization import Messier, db_session

app = Flask(__name__)
api = Api(app=app)
messier = Messier()


##DEBUT CREATION DES ROUTES 

@api.route("/")
class Test(Resource):
    def get(self):
        res = messier.all()
        print(res)
        return render_template('index.html')



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


@api.route("/galaxies/constellation/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByConstellation(category)
        print(res)
        return jsonify(res)

@api.route("/galaxies/constellation_en/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByConstellationEn(category)
        print(res)
        return jsonify(res)

@api.route("/galaxies/constellation_fr/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByConstellationFr(category)
        print(res)
        return jsonify(res)


@api.route("/galaxies/constellation_latin/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByConstellationLatin(category)
        print(res)
        return jsonify(res)

@api.route("/galaxies/discoverer/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByDiscoverer(category)
        print(res)
        return jsonify(res)


@api.route("/galaxies/ngc/<category>")
class Test(Resource):
    def get(self,category):
        res = messier.getByNGC(category)
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
    #category = request.args.get('username')
    def get(self,category):
        res = messier.getBySeason(category)
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



app.run(host="0.0.0.0", port=80, debug=True)
