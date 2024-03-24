<template>
  <footer class="flex flex-col space-y-10 justify-center m-10">
    <p class="text-center text-gray-700 font-medium">
      &copy; {{ getYear }} Company Ltd. All rights reservered.
    </p>
  </footer>
</template>
<script setup>
const getDate = new Date();
const getYear = getDate.getFullYear();
</script>
