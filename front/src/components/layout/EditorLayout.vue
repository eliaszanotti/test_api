<template>
    <main class="grid grid-cols-[5rem,4fr,5fr] overflow-hidden">
        <Sidebar/>
        <slot></slot>
        <PreviewContainer/>
    </main>
</template>

<script setup>
import Sidebar from '@/components/sidebar/Sidebar.vue';
import PreviewContainer from '@/components/global/PreviewContainer.vue';
</script>