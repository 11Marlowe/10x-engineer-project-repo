import React from 'react';

const Button = ({ children, onClick, type = 'button', style = {} }) => {
  return (
    <button type={type} onClick={onClick} style={{ padding: '0.5rem 1rem', backgroundColor: '#6200ea', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', ...style }}>
      {children}
    </button>
  );
};

export default Button;
