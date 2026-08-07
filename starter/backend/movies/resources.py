from flask import jsonify, abort
from flask.views import MethodView

movies = {
    "123": {"title": "Top Gun: Maverick", "description": "Fighter planes"},
    "456": {"title": "Sonic the Hedgehog", "description": "Blue Sega character"},
    "789": {"title": "A Quiet Place", "description": "Scary monsters"},
    "101": {"title": "Inception", "description": "A thief who steals corporate secrets through the use of dream-sharing technology."},
    "102": {"title": "The Dark Knight", "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham."},
    "103": {"title": "Interstellar", "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."},
    "104": {"title": "The Matrix", "description": "A computer hacker learns from mysterious rebels about the true nature of his reality."},
    "105": {"title": "Avengers: Endgame", "description": "After the devastating events of Infinity War, the Avengers assemble once more."},
    "106": {"title": "Spider-Man: Across the Spider-Verse", "description": "Miles Morales catapults across the Multiverse, where he encounters a team of Spider-People."},
    "107": {"title": "Dune: Part Two", "description": "Paul Atreides unites with Chani and the Fremen while on a warpath of revenge against the conspirators who destroyed his family."},
    "108": {"title": "Oppenheimer", "description": "The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb."},
    "109": {"title": "Gladiator", "description": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family."}
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
