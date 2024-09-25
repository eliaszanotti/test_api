<template>
	<SubSectionLayout>
		<CardTitle>Informations personnelles</CardTitle>
		<div class="grid grid-cols-2 gap-md">
			<TextInput
				label="Prénom"
				placeholder="Jean"
				name="first_name"
				:value="personnalStore.data.first_name"
				@update:value="emitUpdate"
			/>
			<TextInput
				label="Nom"
				placeholder="Dupont"
				name="name"
				:value="personnalStore.data.name"
				@update:value="emitUpdate"
			/>
		</div>
		<div class="grid grid-cols-3 gap-md">
			<TextInput
				label="Téléphone"
				placeholder="06 12 34 56 78"
				name="phone"
				:value="personnalStore.data.phone"
				@update:value="emitUpdate"
			/>
			<TextInput
				class="col-span-2"	
				label="Email"
				placeholder="jean@jobmania.fr"
				name="email"
				:value="personnalStore.data.email"
				@update:value="emitUpdate"
			>
				<svg class="w-icon h-icon fill-current pointer-events-none select-none" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M20 4H4c-1.103 0-2 .897-2 2v12c0 1.103.897 2 2 2h16c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2zm0 2v.511l-8 6.223-8-6.222V6h16zM4 18V9.044l7.386 5.745a.994.994 0 0 0 1.228 0L20 9.044 20.002 18H4z"></path></svg>
			</TextInput>
			<NumberInput
				label="Âge"
				placeholder="20"
				name="age"
				:value="personnalStore.data.age"
				@update:value="emitUpdate"
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
				@update:value="emitUpdate"
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
const emit = defineEmits(['update:value']);
const emitUpdate = ({name, value}) => {
	emit('update:value', {name, value});
};
</script>