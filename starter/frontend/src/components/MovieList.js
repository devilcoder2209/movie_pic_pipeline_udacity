import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

function MovieList({ onMovieClick, search }) {
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_MOVIE_API_URL}/movies`)
      .then((response) => {
        setMovies(response.data.movies);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  const filteredMovies = movies.filter((movie) => movie.title.toLowerCase().includes(search.toLowerCase()));

  return (
    <>
      {loading ? (
        <div className="loading">Loading movies...</div>
      ) : (
        <div className="movie-grid">
          {filteredMovies.map((movie) => (
            <div className="movie-card" key={movie.id} onClick={() => onMovieClick(movie)}>
              <div className="movie-poster">🎬</div>
              <div className="movie-info">{movie.title}</div>
            </div>
          ))}
          {filteredMovies.length === 0 && !loading && (
            <div style={{ gridColumn: '1 / -1', textAlign: 'center', fontSize: '1.2rem', marginTop: '20px' }}>
              No movies found.
            </div>
          )}
        </div>
      )}
    </>
  );
}

MovieList.propTypes = {
  onMovieClick: PropTypes.func.isRequired,
  search: PropTypes.string.isRequired,
};

export default MovieList;
