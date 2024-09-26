<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<Picture/>
			<Infos/>
			<Address/>
			<Mobility/>
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
onMounted(async () => {
	await personnalStore.fetchData();
});
</script>