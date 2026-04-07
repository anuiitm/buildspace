import axios from 'axios';

const API_BASE = 'http://127.0.0.1:5000/api';

const api = axios.create({
  baseURL: API_BASE,
  headers: { 'Content-Type': 'application/json' },
});

export default {
  // Feed
  getFeed: () => api.get('/feed'),
  createPost: (data) => api.post('/feed', data),
  toggleLike: (postId) => api.post(`/feed/${postId}/like`),

  // Projects
  getProjects: (params) => api.get('/projects', { params }),
  createProject: (data) => api.post('/projects', data),

  // Opportunities
  getOpportunities: (params) => api.get('/opportunities', { params }),
  createOpportunity: (data) => api.post('/opportunities', data),

  // Profile
  getProfile: () => api.get('/profile'),
  updateProfile: (data) => api.put('/profile', data),

  // Widgets
  getTrending: () => api.get('/trending'),
  getSuggestedUsers: () => api.get('/users/suggested'),
  getHackathons: () => api.get('/hackathons'),
};
