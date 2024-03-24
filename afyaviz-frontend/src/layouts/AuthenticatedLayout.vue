<template>
  <div class="flex h-screen bg-gray-100">
    <!-- sidebar -->
    <Sidebar />
    <!-- Main content -->
    <div class="flex flex-col flex-1 overflow-y-auto">
      <Navbar />
      <slot></slot>
      <Footer />
    </div>
  </div>
</template>
<script setup>
import Navbar from "../components/Navbar.vue";
import Sidebar from "../components/Sidebar.vue";
import Footer from "../components/Footer.vue";
</script>
