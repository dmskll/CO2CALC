
<template>
  <main>
    <el-dropdown>
    <span class="el-dropdown-link">
      Seleccionar Calculos
    </span>
    <template #dropdown>
      <el-dropdown-menu >
        <div v-for="calculation in this.calculations_data" :key="calculation.pk" >
          <el-dropdown-item @click="changeCalculation(calculation.id)"> {{ calculation.name }}</el-dropdown-item>
        </div>
      </el-dropdown-menu>
    </template>
  </el-dropdown>



    <h1>Calculadora: {{ calculation_data.name }}</h1>
    <div v-for="(used_component, index) in calculation_data" :key="used_component.pk">
      <div class="hw-collapse">
        <el-collapse>
          <el-collapse-item>
            <template #title>
              <el-dropdown>
                  <el-button class="button" text>
                   ⚙️
                  </el-button>
                  <template #dropdown>
                    <el-dropdown-menu>
                      <el-dropdown-item >Cambiar componente</el-dropdown-item>
                      <el-dropdown-item @click="router.push('/components')">Editar componente</el-dropdown-item>
                      <el-dropdown-item @click="removeUsedComponent(index)" divided>Eliminar uso</el-dropdown-item>
                    </el-dropdown-menu>
                  </template>
              </el-dropdown>
              {{ this.getComponentName(used_component.system_component, used_component.id) }}
            </template>
            <ComponentColapse 
              :user="user" 
              :data="used_component" 
              :calculation_id="this.current_calculation"
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

    <el-dialog v-model="dialogComponentVisible"  title="Add component" width="40%">
      <el-scrollbar height="400px" style="width: auto;">
        <div v-for="(component, index) in components.system" :key="component.pk">
          <el-card @click="addComponent(component.system_component, index)" class="box-card" el-card shadow="hover">
            <div class="text item"><b>{{ component.name }}</b></div>
            <div class="text item">{{ component.description }}</div>
          </el-card>
        </div>
        <div v-for="(component, index) in components.user" :key="component.pk" style="width: auto;">
          <el-card @click="addComponent(component.system_component, index)" class="box-card" el-card shadow="hover">
            <div class="text item"><b>{{ component.name }}</b></div>
            <div class="text item">{{ component.description }}</div>
          </el-card>
        </div>
      </el-scrollbar>
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
  props: ["user", "calculation_data", "calculations_data", "components", "current_calculation" ],
  emits: ["updateCalculation", "addComponent", "changeCalculation", "removeUsedComponent"],
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
        console.log("sistema");
        const component = this.components.system.filter((item) => item.id === id);
        return component[0].name;
      }
      console.log("no sistema");
      const component = this.components.user.filter((item) => item.id === id)
      return component[0].name;
    },
    addComponent(index, system){
      console.log("añadido!");
      this.$emit('addComponent', index, system);
      this.dialogComponentVisible = false;
    },
    changeCalculation(id){
      this.$emit('changeCalculation', id)
    },
    removeUsedComponent(index){
      this.$emit('removeUsedComponent', index);
    }
  },

}
</script>

<style>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: left;
}

.text {
  font-size: 14px;
  text-align: left;
}

.item {
  margin-bottom: 0px;
}

.box-card {
  width: auto;
  margin-bottom: 2px;
}



.example-showcase .el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}


</style>