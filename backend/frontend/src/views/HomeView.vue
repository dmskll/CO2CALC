
<template>
  <main>
    <h2>Home page!</h2>
    <button v-on:click="getComponents">load components</button>
    <div v-for="usage in usage_data" :key="usage.pk">
      <div class="hw-collapse">
        <el-collapse>
          <el-collapse-item :title="usage.name" >
            <ComponentColapse :user="user" :data="usage" :calculation_id="3"/>
          </el-collapse-item>
        </el-collapse>
      </div> 
    </div>
    <el-button text @click="dialogComponentVisible = true; usage_to_edit=new_usage;">
      +
    </el-button>

    <el-dialog v-model="dialogComponentVisible"  title="Add component">

      <span class="dialog-footer">
      <el-button @click="dialogComponentVisible = false">Cancel</el-button>
      <el-button type="primary" @click="dialogComponentVisible = false">
        Confirm
      </el-button>
    </span>

  </el-dialog>
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
      current_calculation: 0,
      dialogComponentVisible:false
    }
  },
  props: ["user"],
  components: {
    ComponentColapse
  },
  methods: {

    async getCalculations() {
      if(!this.user.authenticated){
        console.log("no calculos")
        this.usage_data = {
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
        this.components_data.system = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }

      if(!this.user.authenticated)
        return
        
      endpoint = "/api/component/";
      try {
        const response = await axios.get(endpoint);
        this.components_data.user = response.data;
      } catch (error) {
        alert(error.response.statusText);
      }
    }
      
  },
  created() {
    this.getComponents();
    this.getCalculations();
  }

}
</script>
