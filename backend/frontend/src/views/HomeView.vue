
<template>
  <main>
    <h2>Home page!</h2>
    <button v-on:click="getComponents">load components</button>
    <div v-for="usage in usage_data" :key="usage.pk">
      <div class="hw-collapse">
        <el-collapse>
          <el-collapse-item :title="usage.name" >
            <ComponentColapse :data="usage" :calculation_id="3"/>
          </el-collapse-item>
        </el-collapse>
      </div> 
    </div>
  </main>
</template>

<script>

import { axios } from "@/common/api.service.js"
import ComponentColapse from "@/components/ComponentColapse.vue"

export default {
  name: "HomeView",
  data() {
    return {
      components_data: {
        system: [],
        user: [],
      },
      calculations_data: [],
      usage_data: [],
      current_calculation: 0

    }
  },
  propos: {

  },
  components: {
    ComponentColapse
  },
  methods: {

    async getCalculations() {
      let endpoint = "/api/calculation/";
      try {
        const response = await axios.get(endpoint);
        this.calculations_data = response.data;
        console.log(this.calculations_data);
      } catch (error) {
        alert(error.response.statusText);
      }
      this.getCalculationComponents();
    },
    getCalculationComponents() {
      this.calculations_data.forEach( async (calculation) => {
        let endpoint = "/api/calculation/" + calculation.id + "/data/";
        try {
          const response = await axios.get(endpoint);
          this.usage_data = JSON.parse(response.data); 
          console.log(calculation.id);
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
        this.components_data.system = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }

      endpoint = "/api/component/";
      try {
        const response = await axios.get(endpoint);
        this.components_data.user = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }
      //console.log(this.components_data);
    }
      
  },
  created() {
    this.getComponents()
    this.getCalculations();
  }

}
</script>
