import React from 'react';
import Header from '../Header';
import Sidebar from '../Sidebar';

const Layout = ({ children }) => {
  return (
    <div style={{ display: 'flex', minHeight: '100vh' }}>
      <Sidebar />
      <div style={{ flexGrow: 1 }}>
        <Header />
        <main>{children}</main>
      </div>
    </div>
  );
};

export default Layout;
