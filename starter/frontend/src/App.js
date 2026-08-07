import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import MovieList from './components/MovieList';
import MovieDetails from './components/MovieDetails';
import './App.css';

export default function App() {
  const [selectedMovie, setSelectedMovie] = useState(null);
  const [search, setSearch] = useState('');
  const [isDarkMode, setIsDarkMode] = useState(true);

  // Toggle theme class on body
  useEffect(() => {
    if (isDarkMode) {
      document.body.classList.remove('light-mode');
    } else {
      document.body.classList.add('light-mode');
    }
  }, [isDarkMode]);

  const handleMovieClick = (movie) => {
    setSelectedMovie(movie);
  };

  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
  };

  return (
    <>
      <Navbar search={search} onSearchChange={setSearch} isDarkMode={isDarkMode} toggleTheme={toggleTheme} />

      <div className="container">
        <h2>Popular on ReveurFlix</h2>
        <MovieList onMovieClick={handleMovieClick} search={search} />
        {selectedMovie && <MovieDetails movie={selectedMovie} onClose={() => setSelectedMovie(null)} />}
      </div>
    </>
  );
}
