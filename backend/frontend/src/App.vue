<template>
  <div id="nav">
    <NavBar />
  </div>
  <el-row :gutter="20">
    <el-col :span="18" :offset="3">
      <div class="content" >
        <router-view/>
      </div>
    </el-col>
  </el-row>
  
</template>

<script>
import NavBar from "@/components/Navbar.vue"

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.content {
  border-style: solid;
  margin-top: 25px;
  border-radius: 30px;
  padding: 50px;
}

.demo-radius .radius {
  height: 40px;
  width: 70%;
  border: 1px solid var(--el-border-color);
  border-radius: 0;
  margin-top: 20px;
}
</style>
