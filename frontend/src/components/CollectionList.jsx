import React from 'react';

const CollectionList = ({ collections, onSelect }) => {
  return (
    <div className="collection-list" style={{ padding: '1rem' }}>
      <h3>Collections</h3>
      <ul style={{ listStyleType: 'none', paddingLeft: '0' }}>
        {collections.map(collection => (
          <li key={collection.id} style={{ margin: '0.5rem 0' }}>
            <a href="#" onClick={() => onSelect(collection.id)} style={{ textDecoration: 'none', color: '#6200ea' }}>
              {collection.name}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CollectionList;
