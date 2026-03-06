import React from 'react';

const Header = () => {
  return (
    <header style={{ backgroundColor: '#6200ea', color: 'white', padding: '1rem' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1>PromptLab</h1>
        <nav>
          <a href="#" style={{ color: 'white', marginLeft: '1rem', textDecoration: 'none' }}>Home</a>
          <a href="#" style={{ color: 'white', marginLeft: '1rem', textDecoration: 'none' }}>About</a>
          <a href="#" style={{ color: 'white', marginLeft: '1rem', textDecoration: 'none' }}>Contact</a>
        </nav>
      </div>
    </header>
  );
};

export default Header;
