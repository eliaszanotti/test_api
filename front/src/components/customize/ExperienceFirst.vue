<template>
	<SubSectionLayout>
		<CardTitle>Afficher en premier</CardTitle>
		<MultiButton
			colsClass="grid-cols-3"
			:items="['Expérience', 'Formation']"
			:selectedItem="settingsStore.data.experience_first ? 'Expérience' : 'Formation'"
			@clicked="updateValue"
		/>
		<AlertBox class-color="alert-info">
			<p>Ici, vous pouvez changer l'ordre selon l'importance : placez en premier les expériences ou les formations, selon ce qui valorise le mieux votre profil.</p>
		</AlertBox>
	</SubSectionLayout>
</template>

<script setup>
import { useSettingsStore } from '@/store/useSettingsStore.js';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
import MultiButton from '../button/MultiButton.vue';

const settingsStore = useSettingsStore();
const updateValue = (value) => {
	settingsStore.updateValue({name: 'experience_first', value: !settingsStore.data.experience_first});
};
</script>