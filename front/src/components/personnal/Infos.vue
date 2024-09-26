<template>
	<SubSectionLayout>
		<CardTitle>Informations personnelles</CardTitle>
		<div class="grid grid-cols-2 gap-md">
			<TextInput
				label="Prénom"
				placeholder="Jean"
				name="first_name"
				:value="personnalStore.data.first_name"
				@update:value="updateValue"
			/>
			<TextInput
				label="Nom"
				placeholder="Dupont"
				name="name"
				:value="personnalStore.data.name"
				@update:value="updateValue"
			/>
		</div>
		<div class="grid grid-cols-3 gap-md">
			<TextInput
				label="Téléphone"
				placeholder="06 12 34 56 78"
				name="phone"
				:value="personnalStore.data.phone"
				@update:value="updateValue"
			/>
			<TextInput
				class="col-span-2"	
				label="Email"
				placeholder="jean@jobmania.fr"
				name="email"
				:value="personnalStore.data.email"
				@update:value="updateValue"
			/>
			<NumberInput
				label="Âge"
				placeholder="20"
				name="age"
				:value="Number(personnalStore.data.age)"
				@update:value="updateValue"
				:min=0
				:max=150
			/>
			<!-- TODO replace by dateInput -->
			<TextInput
				class="col-span-2"
				label="Date de naissance"
				placeholder="01/01/2000"
				name="birthdate"
				:value="personnalStore.data.birthdate"
				@update:value="updateValue"
			/>
		</div>
	</SubSectionLayout>
</template>

<script setup>
import { usePersonnalStore } from '@/store/usePersonnalStore';
import CardTitle from '../global/CardTitle.vue';
import TextInput from '../input/TextInput.vue';
import NumberInput from '../input/NumberInput.vue';
import SubSectionLayout from '../layout/SubSectionLayout.vue';

const personnalStore = usePersonnalStore();
const updateValue = async ({name, value}) => {
	await personnalStore.updateValue({name, value});
};
</script>