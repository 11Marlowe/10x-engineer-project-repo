import React from 'react';

const Sidebar = () => {
  return (
    <aside style={{ width: '250px', backgroundColor: '#f4f4f9', padding: '1rem' }}>
      <nav>
        <h2>Collections</h2>
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          <li><a href="#" style={{ textDecoration: 'none', color: '#6200ea' }}>Collection 1</a></li>
          <li><a href="#" style={{ textDecoration: 'none', color: '#6200ea' }}>Collection 2</a></li>
          <li><a href="#" style={{ textDecoration: 'none', color: '#6200ea' }}>Collection 3</a></li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
