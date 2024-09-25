import axios from 'axios';
import { useAuthStore } from '@/store/authStore';
import router from '@/router';

const apiClient = axios.create({
    baseURL: '/api',
    withCredentials: true,
});

apiClient.interceptors.request.use(
    config => {
        const authStore = useAuthStore();
        if (authStore.accessToken) {
            config.headers['Authorization'] = `Bearer ${authStore.accessToken}`;
        }
        return config;
    },
    error => Promise.reject(error)
);

apiClient.interceptors.response.use(
    response => response,
    async error => {
        const authStore = useAuthStore();
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            try {
                const response = await axios.post('/api/auth/refresh/', {}, { withCredentials: true });
                const { access } = response.data;
                authStore.accessToken = access;
                localStorage.setItem('accessToken', access);
                originalRequest.headers['Authorization'] = `Bearer ${access}`;
                return await axios(originalRequest);
            } catch (refreshError) {
                authStore.logout();
                router.push('/login');
                return Promise.reject(refreshError);
            }
        }
        return Promise.reject(error);
    }
);

export default apiClient;