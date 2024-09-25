<template>
	<p>Déconnexion en cours...</p>
</template>

<script setup>
import { onMounted } from 'vue';
import { useAuthStore } from '@/store/authStore';
import { useRouter } from 'vue-router';

const authStore = useAuthStore();
const router = useRouter();

onMounted(() => {
	authStore.logout();
	router.push('/login');
});
</script>