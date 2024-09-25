<template>
	<div class="form-control">
		<span class="label label-text">{{ label }}</span>
		<div 
			class="input grid grid-cols-[1fr,auto] items-center gap-3 shadow-sm bg-base-200"
			:class="customClass"
		>
			<input 
				type="text"
				:placeholder="placeholder" 
				:name="name" 
				:value="value"
				@input="updateValue($event)"
			>
			<slot></slot>
		</div>
	</div>
</template>

<script setup>
import { handleInput } from './handleInput';

const props = defineProps({
    label: String,
    placeholder: String,
    value: String,
	name: String,
	customClass: String,
});

const emit = defineEmits(['update:value']);
const updateValue = (event) => {
    handleInput(event.target.value, emit, props.name);
};
</script>