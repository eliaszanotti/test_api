<template>
	<div class="grid grid-cols-[1fr,auto]">
		<CardTitle>{{ data.company || 'Nouvelle expérience' }}</CardTitle>
		<ExitDetailButton @click="handleClick"/>
	</div>
	<div class="grid grid-cols-2 gap-md">
		<TextInput
			label="Entreprise"
			placeholder="CVmania"
			name="company"
			:value="data.company"
			@update:value="updateValue"
		/>
		<TextInput
			label="Titre du poste"
			placeholder="Business Developper"
			name="title"
			:value="data.title"
			@update:value="updateValue"
		/>
		<TextInput
			label="Ville"
			placeholder="Lyon"
			name="city"
			:value="data.city"
			@update:value="updateValue"
		/>
		<SelectInput
			label="Type de contrat"
			name="contract"
			:value="data.contract"
			:items="data.contract_choices"
			@update:value="updateValue"
		/>
	</div>
	<br>
	<CardTitle>Dates</CardTitle>
	<DateBlock
		:data="data"
		@update:value="updateValue"
	/>
	<br>
	<CardTitle>Détails</CardTitle>
	<div class="grid grid-cols-2 gap-md">
		<QuillEditor
			label="Détails de l'expérience"
			name="details"
			:value="data.details"
			@update:value="updateValue"
		/>
	</div>
	<AlertBox classColor="alert-info">
		<p>Les détails de vos expériences doivent être obligatoirement à l'indicatif</p>
	</AlertBox>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api.js';
import CardTitle from '../global/CardTitle.vue';
import TextInput from '../input/TextInput.vue';
import AlertBox from '../global/AlertBox.vue';
import ExitDetailButton from '../button/ExitDetailButton.vue';
import SelectInput from '../input/SelectInput.vue';
import QuillEditor from '../input/QuillEditor.vue';
import DateBlock from '../global/DateBlock.vue';

const data = reactive({});

const props = defineProps({
	item_id: Number
});

const emit = defineEmits(['close']);
const handleClick = () => {
	emit('close');
};

const updateValue = async ({name, value}) => {
	try {
		let sendData = {[name]: value,}
		if (name === 'company') {
			data.company = value;
		}
		await apiClient.put(`/cv_experience/update/${props.item_id}/`, sendData);
	} catch (error) {
		console.error('Error updating language data:', error);
	}
};

const fetchLangData = async () => {
	try {
		const response = await apiClient.get(`/cv_experience/item/${props.item_id}/`);
		Object.assign(data, response.data);
	} catch (error) {
		console.error('Error fetching language data:', error);
	}
};

onMounted(() => {
	fetchLangData();
});
</script>