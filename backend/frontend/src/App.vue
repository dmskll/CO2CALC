<template>
  <div id="nav">
    <NavBar :user="user_info" />
  </div>
  <el-row>
    <el-col :span="18" :offset="3">
      <div class="content" v-if="loaded">


        <!-- <router-view
          :user="user_info" 
          :calculation_data="calculation_data"
          :calculations_data="calculation"
          :components="components"
          @addComponent="addComponentUse"
          @updateCalculation="updateCalculationData"
          @updateComponents="updateComponentsData"
        /> -->
        <router-view
          v-if="this.$route.name === 'Components'"
          :user="user_info" 
          :components="components"
          @updateComponents="updateComponentsData"
        />

        <router-view
          v-if="this.$route.name === 'Info'"
          :user="user_info" 
        />

        <router-view
          v-if="this.$route.name === 'Home'"
          :user="user_info" 
          :calculation_data="calculation_data"
          :calculations_data="calculations"
          :components="components"
          :current_calculation="current_calculation"
          @updateCalculation="updateCalculationData"
          @addComponent="addComponentUse"
          @changeCalculation="changeCalculation"
          @removeUsedComponent="removeUsedComponent"

        />
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
      this.current_calculation = this.calculations[0].id
      this.getCalculationComponents();
    },
    async getCalculationComponents() {

      let endpoint = "/api/calculation/" + this.current_calculation + "/data/";
      try {
        const response = await axios.get(endpoint);
        this.calculation_data = JSON.parse(response.data); 
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
    addComponentUse(system, index){
      console.log("recivido");
      const component = system ? this.components.system[index] : this.components.user[index];
      component["usage"] = [];
      //const calc_index = this.getIndexByID(component);
      this.calculation_data.push(component);
    },
    changeCalculation(id){
      this.current_calculation = id;
      this.getCalculationComponents();
    },
    async removeUsedComponent(index){

      this.calculation_data[index].usage.forEach(use => {
        let endpoint = "/api/usage/" + use.id;
          axios.delete(endpoint)
            .then(response => {
              console.log(response);
            })
            .catch(error => {
              this.errorMessage = error.message;
              console.error("There was an error!", error);
            });
      });
      this.calculation_data.splice(index, 1)
      // this.local_data.usage.splice(index, 1);
      //   this.$emit("update", this.local_data);
      //   if(!this.user.authenticated)
      //     return

      //     let endpoint = "/api/usage/" + id;
      //     axios.delete(endpoint,)
      //       .then(response => {
      //         console.log(response);
      //       })
      //       .catch(error => {
      //         this.errorMessage = error.message;
      //         console.error("There was an error!", error);
      //       });
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
