<template>
  <div id="nav" class="header">
    <NavBar :user="store.user_info" />
  </div>
  <div class="box">
    <div class="view-body">
      <div :span="18" :offset="3">
        <div class="content" v-if="loaded==2">
  
  
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
          />
  
          <router-view
            v-if="this.$route.name === 'Info'"
          />
  
          <router-view
            v-if="this.$route.name === 'Report'"
          />
  
          <router-view
            v-if="this.$route.name === 'Home'"
            @updateCalculation="updateCalculationData"
            @changeCalculation="changeCalculation"
  
          />
        </div>
      </div>
    </div>

  </div>
  
</template>


<script setup>

</script>

<script>
import NavBar from "@/components/Navbar.vue"
import { axios } from "@/common/api.service.js"
import { useComponentsData } from "@/stores/ComponentsData"
import { useNoAuthID } from "@/stores/NoAuthID"
import { useOperations } from "@/stores/operations"





export default {
  name: 'App',
  setup(){
    const store = useComponentsData();
    const max_id = useNoAuthID();
    const operations = useOperations();

    return {
      store: store,
      max_id: max_id,
      operations: operations
    }

  },
  data() {
    return {
      loaded: 0,
      calculation_data: [],
    }
  },
  components: {
    NavBar
  },
  methods:{
    async getData(){

      await this.getUser()
      await Promise.all([this.getCalculations(), this.getComponents()]);
      this.store.updateComponentsIsUsed();
      
    },
    async getUser() {
      let endpoint = "/api/user/";
      try {
        const response = await axios.get(endpoint);
        this.store.user_info = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }
    },
    async getCalculations() {
      if(!this.store.user_info.authenticated){
        // this.store.calculations.push({
        //   "id": this.max_id.calculation,
        //   "owner": null,
        //   "name": "nuevo projecto"
        // })
        // this.max_id.calculation++;
        // this.store.current_calculation = this.store.calculations[0]
        this.loaded++
        return
      }
        
      let endpoint = "/api/calculation/";
      try {
        const response = await axios.get(endpoint);
        this.store.calculations = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }
      if (this.store.calculations.length == 0){
        this.loaded++;
        return
      }

      this.store.current_calculation = this.store.calculations[0]
      await this.getCalculationComponents();
    },
    async getCalculationComponents() {
      console.log(this.store.current_calculation.id)
      let endpoint = "/api/calculation/" + this.store.current_calculation.id + "/usage/";
      try {
        const response = await axios.get(endpoint);
        this.store.components_use = response.data; 
      } catch (error) {
        console.log("error")
        alert(error.response.statusText);
      }
      this.loaded++;
    },
    async getComponents() {
      let endpoint = "/api/component/system/";
      try {
        const response = await axios.get(endpoint);
        this.store.components.system = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }

      if(this.store.user_info.authenticated)
      {
        endpoint = "/api/component/";
        try {
          const response = await axios.get(endpoint);
          this.store.components.user = response.data;
        } catch (error) {
          alert(error.response.statusText);
        }
      }
      this.loaded++;
    },
    getIndexByID(data){
      return this.calculation_data.findIndex(obj => obj.id === data.id);
    },
    updateCalculationData(data){
      const index = this.getIndexByID(data);
      this.calculation_data[index] = data;
    },
    async changeCalculation(index){
      await this.operations.changeCalculation(index)
      if(this.store.user_info.authenticated){
        this.loaded--;
        this.getCalculationComponents();
      }
    },
  },
  created() {
    this.getData();
  }
}
</script>

<style>

body, html {
  margin: 0;
  padding: 0;
  height: 100%;
  display: flex;
  flex-flow: column;
}

.view-body{
  flex: 1;
  display: flex;
  min-height: 100vh;
  background-image: linear-gradient(to bottom right, #73AB95, #7CD4AC);
  align-items: top;
  justify-content: center;
  /* background-color: rgb(160, 225, 167); */
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.box {
  flex: 1;
  display: flex;
}

.content {
  border-width: 1px;
  margin-top: 5em;  
  margin-bottom: 5em;
  border-radius: 30px;
  padding: 50px 80px 50px 80px;
  width: 21cm;
  
  background-color: rgb(255, 255, 255);
  border-style: solid;
  border-color: rgb(189, 189, 189);
}


.demo-radius .radius {
  height: 40px;
  width: 70%;
  border: 1px solid var(--el-border-color);
  border-radius: 0;
  margin-top: 20px;
}
</style>
