<template>
	<SubSectionLayout>
		<CardTitle>Couleurs</CardTitle>
		<div v-if="settingsStore.data.templates_choices && settingsStore.data.templates_choices.length > 0">
			<ColorSelector 
				v-for="(colors, name) in settingsStore.data.templates_choices[settingsStore.data.template]"
				:name="name"
				:colors="colors"
			/>
		</div>
	</SubSectionLayout>
</template>

<script setup>
import { useSettingsStore } from '@/store/useSettingsStore';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import ColorSelector from './ColorSelector.vue';

const settingsStore = useSettingsStore();
</script>