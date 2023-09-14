<template>
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      :ellipsis="false"
      @select="handleSelect"
    >
    <el-menu-item index="1" >Calculadora</el-menu-item>
    <el-menu-item index="3" >Componentes</el-menu-item>
    <el-menu-item index="2" >Información</el-menu-item>
    <div class="flex-grow" />
    <el-menu-item index="4" >Login</el-menu-item>
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
  else if (key == 3) {
    router.push("/components");
  } 
  else if (key == 4) {
    window.open("http://127.0.0.1:8000/api-auth/login/");
  } 
};
</script>


<script>
  export default {
    name: "NavBar",
    props: ["user"]
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
  