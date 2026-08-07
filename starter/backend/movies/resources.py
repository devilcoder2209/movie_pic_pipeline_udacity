from flask import jsonify, abort
from flask.views import MethodView

movies = {
    "123": {"title": "Top Gun: Maverick", "description": "Fighter planes"},
    "456": {"title": "Sonic the Hedgehog", "description": "Blue Sega character"},
    "789": {"title": "A Quiet Place", "description": "Scary monsters"},
}


class Movies(MethodView):
    def get(self, movie_id):
        if movie_id is None:
            return jsonify({"movies": [dict({"title": movie["title"]}, **{"id": i}) for i, movie in movies.items()]})
        else:
            str_id = str(movie_id)
            if str_id not in movies:
                abort(404, description="Movie not found")
            return jsonify({"movie": movies[str_id]})
            
    def post(self):
        abort(501, description="Method not implemented yet")
        
    def put(self, movie_id):
        abort(501, description="Method not implemented yet")
        
    def delete(self, movie_id):
        abort(501, description="Method not implemented yet")
