
<template>
  <main>
  
    <h2>Home page!</h2>
    <button v-on:click="getComponents">load components</button>
    <div v-for="component_data in components_data" :key="component_data.pk">
      <div class="hw-collapse">
        <el-collapse>
          <el-collapse-item :title="component_data.name" >
            <HWComponent :data="component_data" />
          </el-collapse-item>
        </el-collapse>
      </div> 
    </div>
  </main>
</template>

<script>

import { axios } from "@/common/api.service.js"
import HWComponent from "@/components/HWComponent.vue"

export default {
  name: "HomeView",
  data() {
    return {
      components_data: [],
      calculations_data: [],
      usage_data: [],
      jsonData: []

    }
  },
  propos: {

  },
  components: {
    HWComponent
  },
  methods: {

    async getCalculations() {
      this.jsonData = {};
      let endpoint = "/api/calculation/";
      try {
        const response = await axios.get(endpoint);
        this. calculations_data = response.data;
      } catch (error) {
        //console.log(error.response);
        alert(error.response.statusText);
      }


      //poner try catch
      this.calculations_data.forEach( async (calculation) => {
        
        
        //console.log(calculation);
        let endpoint = "/api/calculation/" + calculation.id + "/usage/";
        const response = await axios.get(endpoint);
        //console.log(endpoint)
        //console.log(response.data);
        
        let data = response.data;
        this.jsonData[calculation.id] = {
          id: calculation.id,
          name: calculation.name,
          owner: calculation.owner,
          usage: data,
        }  
      });

      console.log(this.jsonData);
    }
      
  },
  created() {
    this.getCalculations();
  }

}
</script>
