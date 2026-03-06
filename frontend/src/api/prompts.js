import apiClient from './client';

export const getPrompts = async () => {
  const response = await apiClient.get('/prompts');
  return response.data;
};

export const getPrompt = async (id) => {
  const response = await apiClient.get(`/prompts/${id}`);
  return response.data;
};

export const createPrompt = async (data) => {
  const response = await apiClient.post('/prompts', data);
  return response.data;
};

export const updatePrompt = async (id, data) => {
  const response = await apiClient.put(`/prompts/${id}`, data);
  return response.data;
};

export const deletePrompt = async (id) => {
  await apiClient.delete(`/prompts/${id}`);
};
