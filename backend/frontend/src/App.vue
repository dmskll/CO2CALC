<template>
  <div id="nav">
    <NavBar :user="user_info" />
  </div>
  <el-row :gutter="20">
    <el-col :span="18" :offset="3">
      <div class="content" v-if="loaded">


        <router-view
          :user="user_info" 
          :calculation_data="calculation_data"
          :calculations_data="calculation"
          :components="components"
          @updateCalculation="updateCalculationData"
          @updateComponents="updateComponentsData"
        />
        <!-- <router-view
          v-if="this.$route.name === Components"
          :user="user_info" 
          :components="components"
          @update="updateComponentsData"
        />

        <router-view
          v-if="this.$route.name === Info"
          :user="user_info" 
        />

        <router-view
          v-if="this.$route.name === Home"
          :user="user_info" 
          :calculation_data="calculation_data"
          :calculations_data="calculation"
          :components="components"
          @update="updateCalculationData"
        /> -->
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
      loaded: false,
      calculations: [],
      current_calculation: [],
      calculation_data: [],
      components: {
        system: [],
        user: [],
      },
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
      

      this.getComponents();
      this.getCalculations();
      this.loaded = true;
    },
    async getCalculations() {
      if(!this.user_info.authenticated){
        console.log("no calculos")
        this.calculation_data = {
          "5": {
              "bad_case_idle_power": "3.00",
              "bad_case_max_power": "3.00",
              "cfp": "3.00",
              "cfp_deviation_standard": "3.00",
              "cfp_use_phase": "3.00",
              "description": "hehe",
              "good_case_idle_power": "3.00",
              "good_case_max_power": "3.00",
              "id": 5,
              "idle_power": "3.00",
              "max_power": "3.00",
              "name": "pc dani",
              "owner": "dani",
              "system_component": "false",
              "usage": [
                  {
                      "Description": "programación backend",
                      "calculation": "3",
                      "component": "5",
                      "hours": "150",
                      "id": "-1",
                      "use": "50"
                  }
              ]
          }
        }
        return
      }
        
      let endpoint = "/api/calculation/";
      try {
        const response = await axios.get(endpoint);
        this.calculations = response.data;
        console.log(this.calculations);
      } catch (error) {
        alert(error.response.statusText);
      }
      this.getCalculationComponents();
    },
    getCalculationComponents() {
      this.calculations.forEach( async (calculation) => {
        let endpoint = "/api/calculation/" + calculation.id + "/data/";
        try {
          const response = await axios.get(endpoint);
          this.calculation_data = JSON.parse(response.data); 
          console.log(response.data);
        } catch (error) {
          console.log("error")
          alert(error.response.statusText);
        }
      });
    },
    async getComponents() {

      let endpoint = "/api/component/system/";
      try {
        const response = await axios.get(endpoint);
        this.components.system = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }

      if(!this.user_info.authenticated)
        return
        
      endpoint = "/api/component/";
      try {
        const response = await axios.get(endpoint);
        this.components.user = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }
    },
    updateCalculationData(data){
      this.calculation_data[data.id] = data
    },
    updateComponentsData(data){
      this.components.user = data;
      console.log("editado!")
      console.log(this.components.user)
    }
  },
  created() {
    this.getUser();

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
