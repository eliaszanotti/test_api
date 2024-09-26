<template>
	<SubSectionLayout>
		<CardTitle>Couleurs</CardTitle>
		<ColorSelector 
			v-for="(colors, name) in schemes"
			:name="name"
			:colors="colors"
		/>
	</SubSectionLayout>
</template>

<script setup>
import { useSettingsStore } from '@/store/useSettingsStore';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import ColorSelector from './ColorSelector.vue';

const settingsStore = useSettingsStore();
</script>