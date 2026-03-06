import React from 'react';

const ErrorMessage = ({ message }) => {
  return (
    <div style={{ color: 'red', padding: '1rem', backgroundColor: '#fdd', border: '1px solid #fbb', borderRadius: '4px', marginBottom: '1rem' }}>
      {message}
    </div>
  );
};

export default ErrorMessage;
