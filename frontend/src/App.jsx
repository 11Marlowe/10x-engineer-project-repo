import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Layout from './components/Layout';
import PromptList from './components/PromptList';
import PromptDetail from './components/PromptDetail';
import PromptForm from './components/PromptForm';
import CollectionList from './components/CollectionList';
import CollectionForm from './components/CollectionForm';
import { getPrompts, createPrompt, updatePrompt, deletePrompt } from './api/prompts';
import { getCollections, createCollection } from './api/collections';

function App() {
  const [prompts, setPrompts] = useState([]);
  const [collections, setCollections] = useState([]);
  const [selectedCollection, setSelectedCollection] = useState(null);

  useEffect(() => {
    fetchPrompts();
    fetchCollections();
  }, []);

  const fetchPrompts = async () => {
    const data = await getPrompts();
    setPrompts(data.prompts);
  };

  const fetchCollections = async () => {
    const data = await getCollections();
    setCollections(data.collections);
  };

  const handleCreatePrompt = async (prompt) => {
    await createPrompt(prompt);
    fetchPrompts();
  };

  const handleUpdatePrompt = async (id, updatedPrompt) => {
    await updatePrompt(id, updatedPrompt);
    fetchPrompts();
  };

  const handleDeletePrompt = async (id) => {
    if (window.confirm('Are you sure you want to delete this prompt?')) {
      await deletePrompt(id);
      fetchPrompts();
    }
  };

  const handleCreateCollection = async (collection) => {
    await createCollection(collection);
    fetchCollections();
  };

  const handleSelectCollection = (id) => {
    setSelectedCollection(id);
  };

  const filteredPrompts = selectedCollection
    ? prompts.filter((prompt) => prompt.collection_id === selectedCollection)
    : prompts;

  return (
    <Router>
      <Layout>
        <Switch>
          <Route path="/" exact>
            <CollectionForm onSubmit={handleCreateCollection} />
            <CollectionList collections={collections} onSelect={handleSelectCollection} />
            <PromptList prompts={filteredPrompts} onDelete={handleDeletePrompt} />
          </Route>
          <Route path="/prompts/new" exact>
            <PromptForm onSubmit={handleCreatePrompt} />
          </Route>
          <Route path="/prompts/:id" exact>
            <PromptDetail />
          </Route>
        </Switch>
      </Layout>
    </Router>
  );
}

export default App;