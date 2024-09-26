<template>
	<SubSectionLayout>
		<CardTitle>Photo</CardTitle>
		<div class="grid gap-md grid-cols-[auto,1fr]">
			<div class="h-full flex flex-col items-center gap-md">
				<PictureDisplay/>
				<HideButton/>
			</div>
			<DropZone/>
		</div>
	</SubSectionLayout>
</template>

<script setup>
import CardTitle from '../global/CardTitle.vue';
import PictureDisplay from './PictureDisplay.vue';
import HideButton from './HideButton.vue';
import DropZone from './DropZone.vue';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
</script>