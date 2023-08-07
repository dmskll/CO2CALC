
<template>
  <main>
    <h2>Home page!</h2>
    <button v-on:click="getComponents">load components</button>
    <div v-for="used_component in calculation_data" :key="used_component.pk">
      <div class="hw-collapse">
        <el-collapse>
          <el-collapse-item :title="getComponentName(used_component.system_component, used_component.id)">
            <ComponentColapse 
              :user="user" 
              :data="used_component" 
              :calculation_id="3"
              :component="getComponent(used_component.system_component, used_component.id)" 
              @update="updateData"
            />
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

import ComponentColapse from "@/components/ComponentColapse.vue"

export default {
  name: "HomeView",
  data() {
    return {
      dialogComponentVisible: false,
    }
  },
  props: ["user", "calculation_data", "calculations_data", "components" ],
  emits: ["updateCalculation"],
  components: {
    ComponentColapse
  },
  methods: {
    updateData(data){
      this.$emit('updateCalculation', data)
    },
    getComponent(system, id){
      if(system){
        const component = this.components.system.filter((item) => item.id === id);
        return component[0];
      }
      const component = this.components.user.filter((item) => item.id === id)
      return component[0];
    },
    getComponentName(system, id){
      if(system){
        const component = this.components.system.filter((item) => item.id === id);
        return component[0].name;
      }
      const component = this.components.user.filter((item) => item.id === id)
      return component[0].name;
    }
  },

}
</script>
