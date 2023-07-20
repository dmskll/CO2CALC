<template>
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      :ellipsis="false"
      @select="handleSelect"
    >
    <el-menu-item index="1" >Calculadora</el-menu-item>
    <el-menu-item index="2" href="/info">Información</el-menu-item>
    <div class="flex-grow" />
    <el-menu-item index="3" href="/info">Login</el-menu-item>
    </el-menu>
</template>
  
<script setup>
import { ref } from 'vue';
import router from '../router';

const activeIndex = ref('1');
const handleSelect = (key, keyPath) => {
  console.log(key, keyPath);
  if (key == 1){
    router.push("/");
  }
  else if (key == 2) {
    router.push("/info");
  } 
};
</script>


<script>
  export default {
    name: "NavBar"
  }
</script>

<style>
.flex-grow {
flex-grow: 1;
}
.flex-shrink {
flex-shrink: 1;
}
</style>
  