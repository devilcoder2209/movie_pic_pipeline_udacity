import React from 'react';
import PropTypes from 'prop-types';

function Navbar({ search, onSearchChange, isDarkMode, toggleTheme }) {
  return (
    <nav className="navbar">
      <div className="nav-brand">ReveurFlix</div>

      <div className="search-wrapper">
        <span className="search-icon">🔍</span>
        <input
          type="text"
          className="search-input"
          placeholder="Titles, people, genres"
          value={search}
          onChange={(e) => onSearchChange(e.target.value)}
        />
      </div>

      <button className="theme-toggle" onClick={toggleTheme}>
        {isDarkMode ? 'Light Mode' : 'Dark Mode'}
      </button>
    </nav>
  );
}

Navbar.propTypes = {
  search: PropTypes.string.isRequired,
  onSearchChange: PropTypes.func.isRequired,
  isDarkMode: PropTypes.bool.isRequired,
  toggleTheme: PropTypes.func.isRequired,
};

export default Navbar;
