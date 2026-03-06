import React from 'react';

const SearchBar = ({ value, onChange, placeholder = 'Search...' }) => {
  return (
    <input
      type="text"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder={placeholder}
      style={{ padding: '0.5rem', width: '100%', borderRadius: '4px', border: '1px solid #ccc' }}
    />
  );
};

export default SearchBar;
