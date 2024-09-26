<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<Type/>
			<Title/>
			<Links/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { onMounted } from 'vue';
import { useTitleStore } from '@/store/useTitleStore';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import Type from './Type.vue';
import Title from './Title.vue';
import Links from './Links.vue';

const titleStore = useTitleStore();
onMounted(async () => {
	await titleStore.fetchData();
});
</script>