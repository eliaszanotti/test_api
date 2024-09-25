<template>
	<div class="grid grid-rows-[auto,1fr] h-screen">
		<Header/>
		<div class="grid place-items-center h-full">
			<LoginForm/>
		</div>
	</div>
</template>

<script setup>
import Header from '../header/Header.vue';
import LoginForm from './LoginForm.vue';
</script>