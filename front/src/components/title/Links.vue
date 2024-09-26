<template>
	<SubSectionLayout>
		<CardTitle>Liens</CardTitle>
		<UrlInput
			label="LinkedIn"
			placeholder="https://linkedin.com/in/coachmania"
			name="linkedin_url"
			:value="titleStore.data.linkedin_url"
			@update:value="updateValue"
		/>
		<div class="grid grid-cols-2 gap-md">
			<UrlInput
				label="Autre site"
				placeholder="https://github.com/"
				name="other_url"
				:value="titleStore.data.other_url"
				@update:value="updateValue"
			/>
			<UrlInput
				label="Trimoji"
				placeholder="https://trimoji.fr/"
				name="trimoji_url"
				:value="titleStore.data.trimoji_url"
				@update:value="updateValue"
			/>
		</div>
	</SubSectionLayout>
</template>

<script setup>
import { useTitleStore } from '@/store/useTitleStore';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import UrlInput from '../input/UrlInput.vue';

const titleStore = useTitleStore();
const updateValue = async ({name, value}) => {
	await titleStore.updateValue({name, value});
};
</script>