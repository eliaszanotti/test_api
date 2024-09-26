<template>
	<SubSectionLayout>
		<CardTitle>Taille de police</CardTitle>
		<MultiButton
			colsClass="grid-cols-4"
			:items="settingsStore.data.sizes_choices"
			:selectedItem="settingsStore.data.size"
			@clicked="updateValue"
		/>
	</SubSectionLayout>
</template>

<script setup>
import { useSettingsStore } from '@/store/useSettingsStore';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import MultiButton from '../button/MultiButton.vue';

const settingsStore = useSettingsStore();
const updateValue = async (value) => {
	await settingsStore.updateValue({name: 'size', value});
};
</script>