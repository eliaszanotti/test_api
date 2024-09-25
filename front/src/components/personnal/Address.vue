<template>
	<SubSectionLayout>
		<CardTitle>Adresse</CardTitle>
		<div class="grid grid-cols-3 gap-md">
			<TextInput
				class="col-span-2"
				label="Complément d'adresse"
				placeholder="Arrêt de bus, étage, etc."
				name="additional"
				:value="personnalStore.data.additional"
				@update:value="emitUpdate"
			/>
			<TextInput
				label="Code postal"
				placeholder="69006"
				name="postal_code"
				:value="personnalStore.data.postal_code"
				@update:value="emitUpdate"
			/>
		</div>
		<AlertBox classColor="alert-info">
			Dans un CV, on ne met pas l'adresse complète. Le complément d'adresse sert ici à indiquer un arrêt de bus, de métro, etc.
		</AlertBox>
		<div class="grid grid-cols-2 gap-md">
			<TextInput
				label="Ville"
				placeholder="Lyon"
				name="city"
				:value="personnalStore.data.city"
				@update:value="emitUpdate"
			/>
			<!-- TODO change to select country input champs hybrid libre ou parmis un liste (autocompletion) -->
			<TextInput
				label="Pays"
				placeholder="France"
				name="country"
				:value="personnalStore.data.country"
				@update:value="emitUpdate"
			/>
		</div>
	</SubSectionLayout>
</template>

<script setup>
import { usePersonnalStore } from '@/store/usePersonnalStore';
import { defineEmits } from 'vue';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
import TextInput from '../input/TextInput.vue';

const personnalStore = usePersonnalStore();
const emit = defineEmits(['update:value']);
const emitUpdate = ({name, value}) => {
	emit('update:value', {name, value});
};
</script>