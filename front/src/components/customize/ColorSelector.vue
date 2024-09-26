<template>
	<h2>{{ names[props.name] }}</h2>
	<div class="grid grid-cols-8 gap-2">
		<div v-for="color in colors" :key="color">
			<button
				class="btn btn-ghost btn-block h-12 border border-base-content/15"
				:style="{ backgroundColor: color }"
				@click="updateValue(color)"
			></button>
			<p class="text-center" v-if="color === settingsStore.data[props.name + '_color']">•</p>
		</div>
	</div>
</template>

<script setup>
import { useSettingsStore } from '@/store/useSettingsStore';

const props = defineProps({
	colors: Object,
	name: String,
});

const names = {
	primary: 'Principale',
	secondary: 'Secondaire',
	third: 'Tertiaire',
	dark: 'Contenu sombre',
	light: 'Contenu clair',
};

const settingsStore = useSettingsStore();
const updateValue = (color) => {
	settingsStore.updateValue({name: props.name + '_color', value: color});
};
</script>