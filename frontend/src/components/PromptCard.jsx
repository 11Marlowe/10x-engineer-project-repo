import React from 'react';

const PromptCard = ({ prompt }) => {
  return (
    <div className="prompt-card" style={{ border: '1px solid #ddd', padding: '1rem', marginBottom: '1rem' }}>
      <h3>{prompt.title}</h3>
      <p>{prompt.content}</p>
      <button>View Details</button>
    </div>
  );
};

export default PromptCard;
