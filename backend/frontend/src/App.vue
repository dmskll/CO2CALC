<template>
  <div id="nav">
    <NavBar :user="user_info" />
  </div>
  <el-row>
    <el-col :span="18" :offset="3">
      <div class="content" v-if="loaded">


        <!-- <router-view
          :calculation_data="calculation_data"
          :calculations_data="calculation"
          :components="components"
          @addComponent="addComponentUse"
          @updateCalculation="updateCalculationData"
          @updateComponents="updateComponentsData"
        /> -->
        <router-view
          v-if="this.$route.name === 'Components'"
          @updateComponents="updateComponentsData"
        />

        <router-view
          v-if="this.$route.name === 'Info'"
        />

        <router-view
          v-if="this.$route.name === 'Home'"
          @updateCalculation="updateCalculationData"
          @changeCalculation="changeCalculation"

        />
      </div>
    </el-col>
  </el-row>
  
</template>


<script setup>

</script>

<script>
import NavBar from "@/components/Navbar.vue"
import { axios } from "@/common/api.service.js"
import { useComponentsData } from "@/stores/ComponentsData"



export default {
  name: 'App',
  setup(){
    const store = useComponentsData();
    return {
      store: store,
    }

  },
  data() {
    return {
      loaded: false,
      calculation_data: [],
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
        this.store.user_info = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }
      console.log("end")
      

      this.getComponents();
      this.getCalculations();
      this.loaded = true;
    },
    async getCalculations() {
      if(!this.store.user_info.authenticated){
        console.log("no calculos")
        this.store.components_use = {
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
        this.store.calculations = response.data;
        console.log(this.store.calculations);
      } catch (error) {
        alert(error.response.statusText);
      }
      this.store.current_calculation = this.store.calculations[0].id
      this.getCalculationComponents();
    },
    async getCalculationComponents() {

      let endpoint = "/api/calculation/" + this.store.current_calculation + "/usage/";
      try {
        const response = await axios.get(endpoint);
        this.store.components_use = response.data; 
        console.log(response.data);
      } catch (error) {
        console.log("error")
        alert(error.response.statusText);
      }
    },
    async getComponents() {

      let endpoint = "/api/component/system/";
      try {
        const response = await axios.get(endpoint);
        this.store.components.system = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }

      if(!this.store.user_info.authenticated)
        return
        
      endpoint = "/api/component/";
      try {
        const response = await axios.get(endpoint);
        this.store.components.user = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }
    },
    getIndexByID(data){
      return this.calculation_data.findIndex(obj => obj.id === data.id);
    },
    updateCalculationData(data){
      const index = this.getIndexByID(data);
      this.calculation_data[index] = data;
    },
    updateComponentsData(data){
      this.components.user = data;
      console.log("editado!")
      console.log(this.components.user)
    },
    changeCalculation(id){
      this.current_calculation = id;
      this.getCalculationComponents();
    },
  },
  created() {
    this.getUser();
    console.log(this.store.components)

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
  padding: 100px;
  width: 21cm;
}

.demo-radius .radius {
  height: 40px;
  width: 70%;
  border: 1px solid var(--el-border-color);
  border-radius: 0;
  margin-top: 20px;
}
</style>
