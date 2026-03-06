import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000', // Adjust this URL as needed for your backend
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiClient;
