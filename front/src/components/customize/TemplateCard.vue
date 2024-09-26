<template>
	<button class="relative rounded-btn overflow-hidden border border-base-300">
		<img 
			class="object-cover object-center pointer-events-none" 
			:src="`templates/template${index}.png`"
		>
		<div 
			v-if="index == settingsStore.data.template"
			class="pointer-events-none absolute inset-0 bg-primary/25">
		</div>
	</button>
</template>

<script setup>
import { useSettingsStore } from '@/store/useSettingsStore';
const settingsStore = useSettingsStore();

const props = defineProps({
	index: Number
});
</script>