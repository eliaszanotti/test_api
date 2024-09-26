<template>
	<button class="relative rounded-btn overflow-hidden border border-base-300">
		<!-- <img class="object-cover object-center pointer-events-none" src="{% static 'mainApp/templates/' %}{{ template.name }}.png"> -->
		
		<p>ok</p>
		<div 
			v-if="template == settingsStore.data.template.id"
			class="pointer-events-none absolute inset-0 bg-primary/25">okkk
		</div>
	</button>
</template>

<script setup>
import { useSettingsStore } from '@/store/useSettingsStore';
const settingsStore = useSettingsStore();
</script>