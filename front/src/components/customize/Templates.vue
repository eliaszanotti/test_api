<template>
	<SubSectionLayout>
		<CardTitle>Modèles</CardTitle>
		<div class="grid grid-cols-4 gap-md">
			<TemplateCard 
				v-for="(template, index) in settingsStore.data.templates_choices"
				:key="index" 
				:index="index"
			/>
        </div>
	</SubSectionLayout>
</template>

<script setup>
import { useSettingsStore } from '@/store/useSettingsStore';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import TemplateCard from './TemplateCard.vue';

const settingsStore = useSettingsStore();
</script>