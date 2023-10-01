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
    <el-menu-item v-if="store.user_info.authenticated" index="4" > {{  this.store.user_info.username }} </el-menu-item>
    <el-menu-item v-else index="5" >  Login UPC </el-menu-item>
    </el-menu>
</template>
  



<script>
  import router from '../router';

  import { useComponentsData } from "@/stores/ComponentsData"

  export default {
    name: "NavBar",
    props: ["user"],
    setup(){
      const store = useComponentsData();

      return {
        store: store,
      }

    },
    data(){
      return{
        activeIndex: 1,
      }
    },
    methods: {
      handleSelect(key, keyPath){
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
          window.location.replace("https://dev.fib.upc.edu/");
          window.location.replace("https://dev.fib.upc.edu/logout");
        }
        else if (key == 5) {
          window.open("https://dev.fib.upc.edu/login");
        } 
      },
    }
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
  