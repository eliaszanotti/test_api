import { defineStore } from 'pinia';
import { reactive } from 'vue';
import apiClient from '@/services/api';

export const usePersonnalStore = defineStore('personnal', () => {
	const data = reactive({});

	const fetchData = async () => {
		try {
			const response = await apiClient.get('/personnal/get/');
			Object.assign(data, response.data);
		} catch (error) {
			console.error('Erreur lors de la récupération des données personnelles :', error);
		}
	};

	const updateValue = async ({name, value}) => {
		try {
			let sendData = {[name]: value};
			await apiClient.put('/personnal/update/', sendData);
			data[name] = value;
		} catch (error) {
			console.error('Erreur lors de la mise à jour des données personnelles :', error);
		}
	};

	const updatePicture = async (file) => {
		try {
			let formData = new FormData();
			formData.append('picture', file);
			await apiClient.put('/personnal/picture/update/', formData);
			fetchData();
		} catch (error) {
			console.error('Erreur lors de la mise à jour de la photo :', error);
		}
	};

	return { data, fetchData, updateValue, updatePicture };
});
