<template>
	<SubSectionLayout>
		<CardTitle>Type de poste recherché</CardTitle>
		<MultiButton 
			colsClass="grid-cols-4"
			:items="titleStore.data.type_choices"
			:selectedItem="titleStore.data.type"
			@clicked="updateValue"
		/>
	</SubSectionLayout>
</template>

<script setup>
import { useTitleStore } from '@/store/useTitleStore';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import MultiButton from '../button/MultiButton.vue';

const titleStore = useTitleStore();
const updateValue = async (selectedType) => {
	await titleStore.updateValue({name: 'type', value: selectedType});
};
</script>