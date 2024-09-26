<template>
	<RouterLink
		:to="url || '/'"
		class="tooltip tooltip-right"
		:data-tip="name"
	>
		<SquareButton :ghost="!currentPage">
			<slot></slot>
		</SquareButton>
	</RouterLink>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import SquareButton from '../button/SquareButton.vue';

const props = defineProps({
	url: String,
	name: String,
});

const currentPage = ref(false);
const route = useRoute();

const checkCurrentPage = () => {
	currentPage.value = route.path.startsWith(props.url);
};

onMounted(checkCurrentPage);
</script>