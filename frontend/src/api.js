import axios from "axios";

// Determine the API base URL based on environment
const getApiBaseUrl = () => {
  // Use environment variable in production (Vercel/Render/Cyclic)
  if (import.meta.env.VITE_API_URL) {
    return import.meta.env.VITE_API_URL;
  }
  // Default to localhost for development
  // For Cyclic use port 3000, for local use 8000
  if (window.location.hostname !== 'localhost') {
    return ""; // Use relative URL in production
  }
  return "http://127.0.0.1:8000";
};

const API = axios.create({
  baseURL: getApiBaseUrl(),
});

export const analyzeReport = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await API.post("/analyze-report", formData);

  return response.data;
};
