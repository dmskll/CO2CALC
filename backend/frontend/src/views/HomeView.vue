
<template>
  <main>
    
    <div v-if="store.calculations.length == 0">
      Venga genera un calculo es divertido!
      <el-button @click="addCalculation" class="button" text>
        <font-awesome-icon icon="fa-solid fa-file-circle-plus" size="lg" />   
      </el-button>
    </div>
    <div v-else>
      <el-button @click="addCalculation" class="button" text>
        <font-awesome-icon icon="fa-solid fa-file-circle-plus" size="lg" />   
      </el-button>
      
      <el-dropdown>
        <el-button  class="button" text>
          <font-awesome-icon icon="fa-regular fa-folder-open" size="lg" /> 
        </el-button>
        <template #dropdown>
          <el-dropdown-menu >
            <div v-for="(calculation, index) in this.store.calculations" :key="calculation.pk" >
              <el-dropdown-item @click="changeCalculation(index)"> {{ calculation.name }}</el-dropdown-item>
            </div>
            <el-dropdown-item @click="addCalculation" divided> 
              <font-awesome-icon icon="fa-solid fa-file-circle-plus" size="lg" />   
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
      
      <h1>
        Calculadora: {{ this.store.current_calculation.name }}
      
        
        <el-dropdown>
        <el-button class="button" text>
          ⚙️
        </el-button>
        <template #dropdown>
          <el-dropdown-menu >
            <el-dropdown-item @click="editCalculation()"> Edit </el-dropdown-item>
            <el-dropdown-item @click="removeCalculation()" divided> Remove </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
      </h1>
      
      
      <div v-for="(used_component, index) in this.store.components_use" :key="used_component.pk">
        <div class="use-card">
          <el-card>
            <div style=" float: right;">
              <el-dropdown>
                <el-button class="button" text>
                  ⚙️
                </el-button>
                <template #dropdown>
                  <el-dropdown-menu>
                    <el-dropdown-item @click="changeComponent(index)">Cambiar componente</el-dropdown-item>
                    <el-dropdown-item @click="$router.push('/components')">Editar componente</el-dropdown-item>
                    <el-dropdown-item @click="removeUsedComponent(index)" divided>Eliminar uso</el-dropdown-item>
                  </el-dropdown-menu>
                </template>
              </el-dropdown>
            </div>
            <br>
                <ComponentData
                  :dialog="false"
                  :data="getComponent(used_component.component, used_component.system_component)"
                  :use="used_component"
                  :show_use = "true"
                  @saveUse="updateData"
                  />
                </el-card>
              </div> 
            </div>
            <el-button text @click="dialogComponentVisible = true; usage_to_edit=new_usage;">
              +
            </el-button>
            
        <el-button type="primary" @click="generateReport">
          Generate Report
        </el-button>
      </div>
      <el-dialog v-model="dialogComponentVisible"  title="Add component" width="600px">
        <el-scrollbar height="400px" style="width: auto;">
          <div v-for="(component, index) in this.store.components.system" :key="component.pk">
            <div v-if="store.components_is_used.system[index]">
              <el-tooltip
                class="box-item"
                effect="dark"
                content="Ya tiene uso"
                placement="top-start"
              >
                <el-card disabled="" class="box-card used-component-card" el-card>
                  <div class="text item"><b>{{ component.name }}</b></div>
                  <div class="text item">{{ component.description }}</div>
                </el-card>
              </el-tooltip>
            </div>
            <div v-if="!store.components_is_used.system[index]">
              <el-card @click="saveComponent(component.system_component, index)" disabled="" class="box-card" el-card shadow="hover" >
                <div class="text item"><b>{{ component.name }}</b></div>
                <div class="text item">{{ component.description }}</div>
              </el-card>
            </div>
          </div>
          <div v-for="(component, index) in this.store.components.user" :key="component.pk" style="width: auto;">
            <div v-if="store.components_is_used.user[index]">
              <el-tooltip class="box-item" effect="dark" content="Ya tiene uso" placement="top-start">
                <el-card disabled="" class="box-card used-component-card" el-card>
                  <div class="text item"><b>{{ component.name }}</b></div>
                  <div class="text item">{{ component.description }}</div>
                </el-card>
              </el-tooltip>
            </div>
            <div v-if="!store.components_is_used.user[index]">
              <el-card @click="saveComponent(component.system_component, index)" disabled="" class="box-card" el-card shadow="hover" >
                <div class="text item"><b>{{ component.name }}</b></div>
                <div class="text item">{{ component.description }}</div>
              </el-card>
            </div>
          </div>
        </el-scrollbar>
        <span class="dialog-footer">
        <el-button @click="dialogComponentVisible = false">Cancel</el-button>
        <el-button type="primary" @click="dialogComponentVisible = false">
          Confirm
        </el-button>
      
      </span>
      
      </el-dialog>
      
      
      <el-dialog v-model="dialogCalculationVisible"  title="Add Calculation" width="600px">
      <el-form
        :model="dialog_calculation"
        style="max-width: 300px"
      >
        <el-input
          v-model="this.dialog_calculation.name"
          type="textarea"
          autosize
          placeholder="Nombre"
          style="margin-top: 10px;"
          />
        </el-form>
        <span class="dialog-footer">
          <el-button @click="dialogCalculationVisible = false">Cancel</el-button>
          <el-button type="primary" @click="saveCalculation">
            Confirm
          </el-button>
      </span>
      </el-dialog>
    </main>


    
  </template>

<script>

//import ComponentColapse from "@/components/ComponentColapse.vue"
import ComponentData from "@/components/ComponentData.vue"
import { useComponentsData } from "@/stores/ComponentsData"
import { useNoAuthID } from "@/stores/NoAuthID"
import { useState } from "@/stores/State"

import { axios } from "@/common/api.service.js"
import router from '../router';


export default {
  name: "HomeView",
  setup(){
    const store = useComponentsData();
    const max_id = useNoAuthID();
    const state = useState();
    return {
      store: store,
      state: state,
      max_id: max_id,
    }

  },
  data() {
    return {
      dialogComponentVisible: false,
      dialogCalculationVisible: false,
      use_index: -1,
      dialog_calculation: null,
      new_calculation: {
        "name": null,
      }
    }
  },
  props: ["user", "calculation_data", "calculations_data", "components", "current_calculation" ],
  emits: ["updateCalculation", "changeCalculation", "removeUsedComponent"],
  components: {
    ComponentData
  },
  methods: {
    updateData(data){
      const index = this.store.components_use.findIndex((use) => use.id === data.id);
      this.store.components_use[index] = data;

      if(!this.store.user_info.authenticated)
        return

      const body = {
        "component": data.component,
        "hours": data.hours,
        "server_years": data.server_years,
      }
      let endpoint = "/api/usage/" + data.id
            axios.put(endpoint, body)
            .then(response => {
              console.log(response.data);
            })
            .catch(error => {
              this.errorMessage = error.message;
              console.error("There was an error!", error);
            });
    },
    addCalculation(){
      this.state.add_use = true;
      router.push('/components')

    },
    editCalculation()
    {
      this.dialogCalculationVisible = true;
      this.dialog_calculation = JSON.parse(JSON.stringify(this.store.current_calculation));
    },
    removeCalculation(){
      const index = this.store.calculations.findIndex(obj => obj.id === this.store.current_calculation.id);
      this.store.calculations.splice(index, 1);
      const calculation = this.store.current_calculation
      this.changeCalculation(0);

      if(!this.store.user_info.authenticated)
        return

      let endpoint = "/api/calculation/" + calculation.id + "/";
        axios.delete(endpoint)
          .then(response => {
            console.log(response);
          })
          .catch(error => {
            this.errorMessage = error.message;
            console.error("There was an error!", error);
          });
    },
    saveCalculation(){
      this.dialogCalculationVisible = false;
      const body = {
        "name": this.dialog_calculation.name
      } 
      if(this.dialog_calculation.id){
        // el componente existe
        this.store.current_calculation.name = body.name;
        if(!this.store.user_info.authenticated)
          return

        let endpoint = "/api/calculation/"+ this.dialog_calculation.id + "/"
          axios.put(endpoint, body)
            .then(response => {
              console.log(response.data);
            })
            .catch(error => {
              this.errorMessage = error.message;
              console.error("There was an error!", error);
            });
      }
      else{
        // el componente NO existe
        if(!this.store.user_info.authenticated){
          this.store.calculations.push({
            "id": this.max_id.calculation,
            "owner": null,
            "name": body.name,
           })
           this.max_id.calculation++;
           this.changeCalculation(this.store.calculations.length - 1);
           return
        } 

        let endpoint = "/api/calculation/"
        axios.post(endpoint, body)
          .then(response => {
            this.store.calculations.push(response.data);
            this.changeCalculation(this.store.calculations.length - 1);
          })
          .catch(error => {
            this.errorMessage = error.message;
            console.error("There was an error!", error);
          });
      }
    },
    getComponent(id, system){
      let component = null
      if (!this.store.user_info.authenticated){
        let type = system ?  "system" : "user"
        component = this.store.components[type].filter((item) => item.id === id);
        return component[0];
      }

      component = this.store.components.system.filter((item) => item.id === id);
      if(component.length == 0)
        component = this.store.components.user.filter((item) => item.id === id)
      return component[0];
  
    },
    getComponentName(id, system){
      return this.getComponent(id, system).name;
    },
    generateReport(){
      router.push('/report')
    },
    async newComponentUse(component){
      let time = component.is_server ? 6 : 0;
      if(!this.store.user_info.authenticated){
        this.store.components_use.push({
          "id": this.max_id.use,
          "system_component": component.system_component,
          "component": component.id,
          "hours": time,
          "server_years": 6,
        })
        this.max_id.use++;
        this.store.updateComponentsIsUsed();
        return
      } 
        const body = {
          "component": component.id,
          "hours": time,
          "server_years": 6,
        }
        let endpoint = "/api/calculation/"+ this.store.current_calculation.id +"/usage/"
        await axios.post(endpoint, body)
        .then(response => {
          response.data["system_component"] = component.system_component;
          this.store.components_use.push(response.data);
          this.store.updateComponentsIsUsed();
        })
        .catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
    },
    updateTime(component){
      let old_component = this.getComponent(this.store.components_use[this.use_index].component, this.store.components_use[this.use_index].system_component)
      if(old_component.is_server == component.is_server)
        return  
      if(old_component.is_server){
        this.store.components_use[this.use_index].hours = 0
        return
      }
      this.store.components_use[this.use_index].server_years = 6;
    },
    async updateComponentUse(component){
      this.updateTime(component);
      this.store.components_use[this.use_index].component = component.id;
      this.store.components_use[this.use_index].system_component = component.system_component;
      this.store.updateComponentsIsUsed();
      if(this.store.user_info.authenticated){
        const body = {
          "component": component.id,
          "hours": this.store.components_use[this.use_index].hours,
        }
        let endpoint = "/api/usage/"+ this.store.components_use[this.use_index].id
        await axios.put(endpoint, body)
        .catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
      }
    },
    async saveComponent(system, index){
      const component = system ? this.store.components.system[index] : this.store.components.user[index];
      if(this.use_index == -1){
        this.newComponentUse(component);
      }
      else{
        this.updateComponentUse(component)
      }
      this.use_index = -1;
      this.dialogComponentVisible = false;
    },
    changeComponent(index)
    {
      this.use_index = index;
      this.dialogComponentVisible = true;

    },
    changeCalculation(index){
      this.$emit('changeCalculation', index)
    },
    removeUsedComponent(index){
      this.store.components_use.splice(index, 1);
      this.store.updateComponentsIsUsed();

      if(!this.store.user_info.authenticated)
        return

      let endpoint = "/api/usage/" + this.store.components_use[index].id;
        axios.delete(endpoint)
          .then(response => {
            console.log(response);
          })
          .catch(error => {
            this.errorMessage = error.message;
            console.error("There was an error!", error);
          });
    },
    
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
  margin-bottom: 5px;
}
.use-card{
  margin-bottom: 15px;
}
.used-component-card{
 filter: brightness(85%);
}



.example-showcase .el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}


</style>