<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<CardTitle>Téléchargement</CardTitle>
			<CorrectText/>
			<Download/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import CorrectText from './CorrectText.vue';
import Download from './Download.vue';
</script>