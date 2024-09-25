<template>
	<button @click="handleAuthAction" class="btn btn-ghost">
		{{ isLogged ? 'Se déconnecter' : 'Se connecter' }}
	</button>
</template>

<script setup>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/store/authStore';

const authStore = useAuthStore();
const isLogged = computed(() => authStore.isLogged);
const router = useRouter();

function handleAuthAction() {
	if (isLogged.value) {
		authStore.logout();
	}
	router.push('/login');
}
</script>