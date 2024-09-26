<template>
	<SubSectionLayout>
		<CardTitle>Titre du CV</CardTitle>
		<TextInput
			label="Titre du poste recherché"
			placeholder="Ex: Développeur Web"
			name="title"
			:value="titleStore.data.title"
			@update:value="updateValue"
		/>
		<QuillEditor
			label="Accroche"
			name="details"
			:value="titleStore.data.details"
			@update:value="updateValue"
		/>
		<AlertBox
			v-if="titleStore.data.type === 'Emploi'"
			classColor="alert-info"
		>
			Pour un emploi, utilisez le titre de l'offre si vous répondez à une annonce. Pour une candidature spontanée, indiquez clairement le poste que vous visez.
		</AlertBox>
		<AlertBox 
			v-else-if="titleStore.data.type === 'Alternance'"
			classColor="alert-info"
		>
			Pour une alternance, mentionnez le poste ainsi que le rythme et la durée de l'alternance. Par exemple : 'Alternant Développeur Web - 3 jours école / 2 jours entreprise - 12 mois'.
		</AlertBox>
		<AlertBox
			v-else-if="titleStore.data.type === 'Stage'"
			classColor="alert-info"
		>
			Pour un stage, précisez le titre du poste et, si possible, la durée du stage. Exemple : 'Stage en Marketing Digital - 6 mois'.
		</AlertBox>
	</SubSectionLayout>
</template>

<script setup>
import { useTitleStore } from '@/store/useTitleStore';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import TextInput from '../input/TextInput.vue';
import QuillEditor from '../input/QuillEditor.vue';
import AlertBox from '../global/AlertBox.vue';

const titleStore = useTitleStore();
const updateValue = async ({name, value}) => {
	await titleStore.updateValue({name, value});
};
</script>