
<template>
  <main>
    
    <div v-if="store.calculations.length == 0" style="padding: 0 5em 0 5em;">
      <h1 style="margin: 0;">CO2Calc</h1>
      <h3 style="margin: 0;">Calcula las emisiones de tu proyecto</h3>

      <p style="text-align: justify;">

        Con esta herramienta podrás estimar las emisiones asociadas a tu proyecto,
        según los componentes usados y el consumo electrico.

      </p>
      <!-- <p style="text-align: justify;">

        CO2Calc te da una serie de componentes pre-hechos que puedes consultar en la sección de componentes.
        Puedes modificarlos o incluso crear los tuyos propios.

      </p>

      <p style="text-align: justify;">

        Para más detalle de como se realizan los calculos o donde conseguir información para hacer tus componentes
        ve a la sección de información

      </p> -->
      <el-alert type="info" :closable="false" style="margin-bottom: 1.3em;">
        <p style="font-size: 1.15em; text-align: justify;">
          Si eres un estudiante de la UPC y te gustaria guardar tus calculos, inicia sesión 
          con tus credenciales de la universidad antes de empezar.
        </p>
      </el-alert>

      <el-button @click="addCalculation" class="button">
        Empezemos!  
      </el-button>
    </div>
    <div v-else>
      <div class="header-container">
        <h1>
          Proyecto: {{ this.store.current_calculation.name }}
        
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
        
        <div class="right-content">
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
          </div>
      </div>
      
      
      
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
                    <el-dropdown-item @click="editComponent(used_component, index)">Editar componente</el-dropdown-item>
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
            <el-button text @click="addComponents();">
              <font-awesome-icon icon="fa-solid fa-plus-square" size="xl" />
            </el-button>
        <br>
        <div style="text-align: right;" >
          <el-button  @click="generateReport" plain>
            CALCULAR
            <font-awesome-icon style="margin-left: 0.6em;" icon="fa-solid fa-calculator" size="xl"/>
  
          </el-button>
        </div>
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

      <el-dialog 
        v-model="dialog_component.visible"
        style="width: 35em;"
        :show-close="false" 
        :close-on-click-modal="false" 
        title="Create Component"
        >
        <el-alert 
          v-if="this.dialog_component.component.id"
          type="info alert" 
          title="Los cambios del componente se aplicarán a todos los usos del mismo componente" 
        />
        <el-alert 
          v-else
          type="info alert" 
        >
          Este componente no puede editarse directamente, cuando guardes se creará una copia en el apartado <b>tus componentes</b> 
        </el-alert>
      
      <ComponentData 
        v-if="dialog_component.visible" 
        :data="this.dialog_component.component"
        :use="this.dialog_component.component" 
        :dialog="true"
        :show_use="false"
        @close="dialog_component.visible = false" 
        @save="saveComponentData"
      />
      </el-dialog>
    </main>
  </template>

<script>

//import ComponentColapse from "@/components/ComponentColapse.vue"
// import ComponentData from "@/components/ComponentData.vue"
import { useComponentsData } from "@/stores/ComponentsData"
import { useNoAuthID } from "@/stores/NoAuthID"
import { useState } from "@/stores/State"
import { useOperations } from "@/stores/operations"
import { ElMessage } from 'element-plus'

import LoadingC from "@/components/loadingC.vue"
import { defineAsyncComponent } from 'vue'

import { axios } from "@/common/api.service.js"
import router from '../router';

const ComponentData = defineAsyncComponent({
  // the loader function
  loader: () => import('@/components/ComponentData.vue'),

  // A component to use while the async component is loading
  loadingComponent: LoadingC,
  // Delay before showing the loading component. Default: 200ms.
  delay: 0,

  // A component to use if the load fails
  // errorComponent: ErrorComponent,
  // The error component will be displayed if a timeout is
  // provided and exceeded. Default: Infinity.
  timeout: 3000
})

export default {
  name: "HomeView",
  setup(){
    const store = useComponentsData();
    const max_id = useNoAuthID();
    const state = useState();
    const operations = useOperations();
    return {
      store: store,
      state: state,
      max_id: max_id,
      operations: operations
    }

  },
  data() {
    return {
      dialogComponentVisible: false,
      dialogCalculationVisible: false,
      use_index: -1,
      dialog_calculation: null,
      dialog_component:{
        visible: false,
        component: null,
        index: null,
      },
      new_calculation: {
        "name": null,
      },
      var_error: false,
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
        "emissions": parseInt(data.emissions),
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
    editComponent(use, index){
      this.state.use_index = index;
      const component = this.getComponent(use.component, use.system_component);
      if (component.system_component){
        this.dialog_component.component = JSON.parse(JSON.stringify(component));
        //borramos el elemento id para que cuando se cree uno nuevo al guardar
        delete this.dialog_component.component["id"];
        this.dialog_component.component.name = "New Copy";
      }
      else{
        this.dialog_component.component = component;
        this.dialog_component.index = this.store.components.user.indexOf(component);
      }
      this.dialog_component.visible = true;
    },
    validateComponent(c){
      if(c.name === "" || c.name == null || c.cfp_build_phase == null || 
        c.cfp_deviation_standard == null || c.middle_case == null || 
        c.worst_case == null || c.best_case == null || c.hosted_apps == null){
          return false;
      }
      return true;
    },      
    async saveComponentData(component){
      if(this.validateComponent(component)){
        this.dialog_component.visible = false;
        await this.operations.saveComponentData(component, this.dialog_component.index);
        if(!component.id){       
          //REVISAR 
          this.updateComponentUse(this.store.components.user[this.store.components.user.length -1])
        }
        this.dialog_component.index = null;
      }
      else{
        ElMessage.error({
            duration: 8000,
            message: 'Has introducido valores invalidos',
          })
      }
    },
    addComponents(){
      this.state.add_use = true;
      router.push('/components')
    },
    addCalculation(){
      this.state.add_calc = true;
      router.push('/components')
    },
    changeComponent(index)
    {
      // this.use_index = index;
      // this.dialogComponentVisible = true;
      this.state.change_use = true;
      this.state.use_index = index;
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
      this.operations.saveCalculation(this.dialog_calculation)
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
      this.var_error = false;
      for (const index in this.store.components_use){
        var use = this.store.components_use[index];
        if (use.hours == null || use.server_years == null || use.emissions === ""){
          console.log(use);
          this.var_error = true;
          ElMessage.error({
            duration: 8000,
            message: 'Has introducido valores invalidos en el tiempo de uso o en las emisiones',
          })
          return
        }
      }
      router.push('/report')
    },
    newComponentUse(component){
      this.operations.newComponentUse(component)
    },
    updateTime(component){
        let old_component = this.getComponent(this.store.components_use[this.state.use_index].component, this.store.components_use[this.state.use_index].system_component)
        if(old_component.is_server == component.is_server)
          return  
        if(old_component.is_server){
          this.store.components_use[this.state.use_index].hours = 0
          return
        }
        this.store.components_use[this.state.use_index].server_years = 6;
      },
      async updateComponentUse(component){
        this.updateTime(component);
        this.store.components_use[this.state.use_index].component = component.id;
        this.store.components_use[this.state.use_index].system_component = component.system_component;
        this.store.updateComponentsIsUsed();
        if(this.store.user_info.authenticated){
          const body = {
            "component": component.id,
            "hours": this.store.components_use[this.state.use_index].hours,
            "server_years": this.store.components_use[this.state.use_index].server_years,
            "emissions": parseInt(this.store.components_use[this.state.use_index].emissions),
          }
          let endpoint = "/api/usage/"+ this.store.components_use[this.state.use_index].id
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
    changeCalculation(index){
      this.$emit('changeCalculation', index)
    },
    removeUsedComponent(index){


      if(!this.store.user_info.authenticated){
        this.store.components_use.splice(index, 1);
        this.store.updateComponentsIsUsed();
        return
      }

      let endpoint = "/api/usage/" + this.store.components_use[index].id;
      axios.delete(endpoint)
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
      this.store.components_use.splice(index, 1);
      this.store.updateComponentsIsUsed();  
    },
    
  },
  created(){
    this.state.resetState();
  }

}
</script>

<style>

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px; /* Ajusta el espaciado según tus necesidades */
}

.right-content {
  display: flex;
  gap: 10px; /* Espaciado entre el botón y el menú desplegable */
}

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