import { defineStore } from 'pinia';
import { reactive } from 'vue';
import apiClient from '@/services/api';

export const useSettingsStore = defineStore('settings', () => {
    const data = reactive({});

    const fetchData = async () => {
        try {
            const response = await apiClient.get('/settings/get/');
            Object.assign(data, response.data);
        } catch (error) {
            console.error('Erreur lors de la récupération des données de settings :', error);
        }
    };

    const updateValue = async ({name, value}) => {
        try {
            let sendData = {[name]: value};
            await apiClient.put('/settings/update/', sendData);
            data[name] = value;
        } catch (error) {
            console.error('Erreur lors de la mise à jour des données de settings :', error);
        }
    };

    return { data, fetchData, updateValue };
});
