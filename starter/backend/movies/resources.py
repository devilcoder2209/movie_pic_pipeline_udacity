from flask import jsonify, abort
from flask.views import MethodView

movies = {
    "123": {"title": "Top Gun: Maverick", "description": "Fighter planes"},
    "456": {"title": "Sonic the Hedgehog", "description": "Blue Sega character"},
    "789": {"title": "A Quiet Place", "description": "Scary monsters"},
    "101": {
        "title": "Inception",
        "description": "A thief who steals corporate secrets.",
    },
    "102": {
        "title": "The Dark Knight",
        "description": "The Joker wreaks havoc and chaos on Gotham.",
    },
    "103": {
        "title": "Interstellar",
        "description": "Explorers travel through a wormhole in space.",
    },
    "104": {
        "title": "The Matrix",
        "description": "A computer hacker learns about true reality.",
    },
    "105": {
        "title": "Avengers: Endgame",
        "description": "The Avengers assemble once more.",
    },
    "106": {
        "title": "Spider-Man: Across the Spider-Verse",
        "description": "Miles Morales catapults across the Multiverse.",
    },
    "107": {
        "title": "Dune: Part Two",
        "description": "Paul Atreides unites with the Fremen.",
    },
    "108": {
        "title": "Oppenheimer",
        "description": "The story of J. Robert Oppenheimer.",
    },
    "109": {
        "title": "Gladiator",
        "description": "A Roman General sets out to exact vengeance.",
    }
}


class Movies(MethodView):
    def get(self, movie_id):
        if movie_id is None:
            movie_list = [dict({"title": m["title"]}, **{"id": i})
                          for i, m in movies.items()]
            return jsonify({"movies": movie_list})
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
