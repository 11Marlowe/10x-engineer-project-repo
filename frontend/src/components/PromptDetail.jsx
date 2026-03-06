import React from 'react';

const PromptDetail = ({ prompt }) => {
  return (
    <div className="prompt-detail">
      <h2>{prompt.title}</h2>
      <p>{prompt.content}</p>
    </div>
  );
};

export default PromptDetail;
