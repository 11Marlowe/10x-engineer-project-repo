import React from 'react';

const LoadingSpinner = () => {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      <div className="loading-spinner" style={{ border: '4px solid rgba(0, 0, 0, 0.1)', borderRadius: '50%', width: '36px', height: '36px', borderTopColor: '#6200ea', animation: 'spin 1s ease-in-out infinite' }}>
        <style>
          {`
            @keyframes spin {
              to { transform: rotate(360deg); }
            }
          `}
        </style>
      </div>
    </div>
  );
};

export default LoadingSpinner;
