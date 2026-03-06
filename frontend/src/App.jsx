import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import PromptList from './components/PromptList';
import PromptDetail from './components/PromptDetail';
import PromptForm from './components/PromptForm';
import CollectionList from './components/CollectionList';
import CollectionForm from './components/CollectionForm';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorMessage from './components/ErrorMessage';
import { getPrompts, createPrompt, updatePrompt, deletePrompt } from './api/prompts';
import { getCollections, createCollection } from './api/collections';

function App() {
  const [prompts, setPrompts] = useState([]);
  const [collections, setCollections] = useState([]);
  const [selectedCollection, setSelectedCollection] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch all data on component mount
    fetchAllData();
  }, []);

  const fetchAllData = async () => {
    setLoading(true);
    setError(null);
    try {
      const [promptsData, collectionsData] = await Promise.all([
        getPrompts(),
        getCollections(),
      ]);
      setPrompts(promptsData.prompts);
      setCollections(collectionsData.collections);
    } catch (err) {
      setError("Failed to load data, please try again later.");
    } finally {
      setLoading(false);
    }
  };

  const handleCreatePrompt = async (prompt) => {
    try {
      await createPrompt(prompt);
      fetchPrompts();  // Refresh prompts list
    } catch (err) {
      setError("Failed to create prompt. Please try again.");
    }
  };

  const handleUpdatePrompt = async (id, updatedPrompt) => {
    try {
      await updatePrompt(id, updatedPrompt);
      fetchPrompts();  // Refresh prompts list
    } catch (err) {
      setError("Failed to update prompt. Please try again.");
    }
  };

  const handleDeletePrompt = async (id) => {
    if (window.confirm('Are you sure you want to delete this prompt?')) {
      try {
        await deletePrompt(id);
        fetchPrompts();  // Refresh prompts list
      } catch (err) {
        setError("Failed to delete prompt. Please try again.");
      }
    }
  };

  const handleCreateCollection = async (collection) => {
    try {
      await createCollection(collection);
      fetchCollections();  // Refresh collections list
    } catch (err) {
      setError("Failed to create collection. Please try again.");
    }
  };

  const handleSelectCollection = (id) => {
    setSelectedCollection(id);
  };

  const filteredPrompts = selectedCollection
    ? prompts.filter(prompt => prompt.collection_id === selectedCollection)
    : prompts;

  return (
    <Router>
      <Layout>
        {loading && <LoadingSpinner />}
        {error && <ErrorMessage message={error} />}
        
        <Routes>
          <Route path="/" element={
            <>
              <CollectionForm onSubmit={handleCreateCollection} />
              <CollectionList collections={collections} onSelect={handleSelectCollection} />
              {filteredPrompts.length === 0 ? (
                <p>No prompts available.</p>
              ) : (
                <PromptList prompts={filteredPrompts} onDelete={handleDeletePrompt} />
              )}
            </>
          } />
          <Route path="/prompts/new" element={<PromptForm onSubmit={handleCreatePrompt} />} />
          <Route path="/prompts/:id" element={<PromptDetail />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;