<template>
	<SubSectionLayout>
		<CardTitle>Mobilité</CardTitle>
		<div class="col-span-full grid grid-cols-2 gap-md">
			<SelectInput
				label="Permis de conduire"
				name="license"
				:value="personnalStore.data.license"
				:items="personnalStore.data.license_choices"
				@update:value="emitUpdate"
			/>
			<CheckBoxInput
				v-if="personnalStore.data.license !== 'Aucun'"
				label="Véhicule"
				name="has_vehicle"
				:checked="personnalStore.data.has_vehicle"
				@update:value="emitUpdate"
			/>
		</div>
		<div class="max-w-[400px] grid gap-md">
			<TextInput
				v-if="personnalStore.data.license === 'Autre'"
				label="Autre permis"
				placeholder="Permis"
				name="other_license"
				:value="personnalStore.data.other_license"
				@update:value="emitUpdate"
			/>
			<TextInput
				label="Champ de mobilité"
				placeholder="Départemental, régional, national, etc."
				name="range"
				:value="personnalStore.data.range"
				@update:value="emitUpdate"
			/>
		</div>
		<AlertBox classColor="alert-info">
			Le champ de mobilité indique votre rayon de déplacement (ex : département, région, etc.).
		</AlertBox>
	</SubSectionLayout>
</template>

<script setup>
import { usePersonnalStore } from '@/store/usePersonnalStore';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
import TextInput from '../input/TextInput.vue';
import SelectInput from '../input/SelectInput.vue';
import CheckBoxInput from '../input/CheckBoxInput.vue';

const personnalStore = usePersonnalStore();
const emit = defineEmits(['update:value']);
const emitUpdate = ({name, value}) => {
	emit('update:value', {name, value});
};
</script>