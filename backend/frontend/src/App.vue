<template>
  <div id="nav">
    <NavBar :user="user_info" />
  </div>
  <el-row v-if="loaded" :gutter="20">
    <el-col :span="18" :offset="3">
      <div class="content" >
        <router-view :user="user_info"/>
      </div>
    </el-col>
  </el-row>
  
</template>

<script>
import NavBar from "@/components/Navbar.vue"
import { axios } from "@/common/api.service.js"

export default {
  name: 'App',
  data() {
    return {
      user_info: {
        authenticated: false,
      },
      loaded: false 
    }
  },
  components: {
    NavBar
  },
  methods:{
    async getUser() {
      let endpoint = "/api/user/";
      try {
        const response = await axios.get(endpoint);
        this.user_info = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }
      console.log("end")
      this.loaded = true;
    }
  },
  created() {
    this.getUser()
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
