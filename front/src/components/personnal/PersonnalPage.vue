<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<!-- <Picture/> -->
			<Infos @update:value="updateValue"/>
			<Address @update:value="updateValue"/>
			<!-- <Mobility/> -->
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { onMounted } from 'vue';
import { usePersonnalStore } from '@/store/usePersonnalStore';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import Picture from './Picture.vue';
import Infos from './Infos.vue';
import Address from './Address.vue';
import Mobility from './Mobility.vue';

const personnalStore = usePersonnalStore();

const updateValue = async ({name, value}) => {
	await personnalStore.updateValue({name, value});
};

onMounted(async () => {
	await personnalStore.fetchData();
	console.log(personnalStore.data);
});
</script>