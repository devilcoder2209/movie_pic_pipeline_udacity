import React, { useState, useEffect } from 'react';
import axios from 'axios';

function MovieDetail({ movie, onClose }) {
  const [details, setDetails] = useState(null);

  useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_MOVIE_API_URL || 'http://127.0.0.1:5000'}/movies/${movie.id}`)
      .then((response) => {
        setDetails(response.data);
      });
  }, [movie]);

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="close-button" onClick={onClose}>
          ✕
        </button>
        <div className="modal-poster-placeholder">{/* In a real app, this would be an img tag */}</div>
        <div className="modal-text-content">
          <h2 className="modal-title">{details?.movie?.title || 'Loading...'}</h2>
          <p className="movie-details-text">{details?.movie?.description || 'Loading details...'}</p>
        </div>
      </div>
    </div>
  );
}

export default MovieDetail;
