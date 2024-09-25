import { defineStore } from 'pinia';
import apiClient from '@/services/api.js';

export const useAuthStore = defineStore('auth', {
	state: () => ({
		username: '',
        accessToken: localStorage.getItem('accessToken') || '',
	}),
	getters: {
		isLogged: (state) => !!state.accessToken,
	},
	actions: {
        async login(username, password) {
            try {
                const response = await apiClient.post('/auth/login/', {
                    username,
                    password
                });

                const { access } = response.data;
                this.username = username;
                this.accessToken = access;
                localStorage.setItem('accessToken', access);
                apiClient.defaults.headers.common['Authorization'] = `Bearer ${this.accessToken}`;
                console.log('Login:', response.data);
            } catch (error) {
                throw error;
            }
        },
        async tokenRefresh() {
            try {
                this.accessToken = '';
                const response = await apiClient.post('/auth/refresh/');

                const { access } = response.data;
                this.accessToken = access;
                localStorage.setItem('accessToken', access);
                apiClient.defaults.headers.common['Authorization'] = `Bearer ${this.accessToken}`;
            } catch (error) {
                throw error;
            }
        },
        async profile() {
            try {
                const response = await apiClient.get('/auth/profile/');
                console.log('Profile:', response.data);
            } catch (error) {
				throw error;
			}
        },
        async logout() {
            try {
                const response = await apiClient.post('/auth/logout/');
                this.username = '';
                this.accessToken = '';
                localStorage.removeItem('accessToken');
                apiClient.defaults.headers.common['Authorization'] = '';
                console.log('Logout:', response.data);
            } catch (error) {
                throw error;
            }
        },  
    },
});