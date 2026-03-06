import apiClient from './client';

export const getCollections = async () => {
  const response = await apiClient.get('/collections');
  return response.data;
};

export const createCollection = async (data) => {
  const response = await apiClient.post('/collections', data);
  return response.data;
};

export const deleteCollection = async (id) => {
  await apiClient.delete(`/collections/${id}`);
};
