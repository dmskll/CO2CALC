<template>


  <el-form
    :model="new_calculation"
    style="max-width: 300px"
    label-position="top"
  >
    <el-form-item label="Nombre del projecto"  v-if="state.add_calc">
          <el-input v-model="this.new_calculation.name"  />
    </el-form-item>

        <el-form-item label="Emisiones" v-if="state.add_use || state.add_calc">
              <el-input style="width: 70%;" v-model="this.new_calculation.emissions"  maxlength="3" @input="handleInput">
                <template #prepend>
                  <el-dropdown>
                  <el-button style="width: 3.7em;">
                    <font-awesome-icon icon="fa-solid fa-bolt" size="lg" /> 
                  </el-button>
                  <template #dropdown>
                    <el-dropdown-menu >
                      <div v-for="mix in store.mix" :key="mix.pk" >

                      <el-dropdown-item  @click="this.new_calculation.emissions=String(mix.emissions)" > 
                        {{ mix.name }}
                      </el-dropdown-item>

                      </div>
                    </el-dropdown-menu>
                  </template>
                </el-dropdown>
                </template>
                <template #append ><div style="font-size: 0.7em;">gCO2/kWh</div></template>
              </el-input>
        </el-form-item>
          </el-form>      


    <h1 v-if="state.add_use || state.add_calc" style="text-align: left;">Selecciona los componentes utilizados</h1>
    <div v-else>
      <h1 style="text-align: left;">Lista de componentes</h1>
      <p>

      </p>
    </div>
    
    <div style="text-align: left;">
      
      <h3>Ordenadores</h3>
      <p>
        Selecciona que tipo de ordenador has utilizado para realizar el proyecto. 
      </p>
      <ComponentGroup
        :data2="this.store.components.system"
        :index_list="component_types.PC"
        :system="true"
        :selected="selected_components.system"
        type="system"
        @duplicate="duplicateComponent"
        @toggleSelect="toggleSelect"
        />
        
      <h3>Pantallas</h3>
      <p>
        Selecciona que tipo de pantallas has utilizado durante el proyecto.
      </p>
      <ComponentGroup
        :data2="this.store.components.system"
        :index_list="component_types.MO"
        :system="true"
        :selected="selected_components.system"
        type="system"
        @duplicate="duplicateComponent"
        @toggleSelect="toggleSelect"
      />

      <h3>Servidores</h3>
      <p>
        Selecciona este componente si has utilizado algún servidor en un centro de datos o alguna plataforma de cloud.
        Por ejemplo para alojar el proyecto durante o después de su desarrollo. 
      </p>
      <ComponentGroup
        :data2="this.store.components.system"
        :index_list="component_types.SE"
        :system="true"
        :selected="selected_components.system"
        type="system"
        @duplicate="duplicateComponent"
        @toggleSelect="toggleSelect"
      />


      <h3>Otros componentes</h3>
      <p>
        Algunos componentes que has podido utilizar. 
      </p>
      <ComponentGroup
        :data2="this.store.components.system"
        :index_list="component_types.MO"
        :system="true"
        :selected="selected_components.system"
        type="system"
        @duplicate="duplicateComponent"
        @toggleSelect="toggleSelect"
      />

      <h3>Tus componentes</h3>
      <p>
        Estos son los componentes que has editado o creado desde cero.
      </p>

      <ComponentGroup
        :data2="this.store.components.user"
        :system="false"
        :index_list="component_types.PC"
        :selected="selected_components.user"
        type="user"
        @duplicate="duplnumbericateComponent"
        @edit="editComponent"
        @delete="deleteComponent"
        @toggleSelect="toggleSelect"
        @addNew="addNewComponent"
      />
      

      <div style="flex: 1; padding: 1.5em; display: flex; justify-content: center;">
        <!-- <el-affix position="bottom" :offset="20">

        </el-affix> -->
        <el-button 
            v-if="state.add_use || state.add_calc" 
            @click="CreateCalculation()" 
            size="large"
        >
          Guardar usos
        </el-button>

      </div>


      <el-dialog
        style="width: 35em;"
        v-model="dialogVisible" 
        :show-close="false" 
        :close-on-click-modal="false" 
        title="Create Component"
      >
        
        <ComponentData 
          v-if="dialogVisible" 
          :data="this.dialog_component"
          :use="this.dialog_component" 
          :dialog="true"
          :show_use="false"
          @close="closeModal" 
          @save="saveComponentData"
        />
      </el-dialog>
  
    </div>
</template>

<script>
  // import ComponentData from "@/components/calculator/ComponentData.vue"
  // import ComponentGroup from "@/components/calculator/ComponentGroup.vue"
  import LoadingC from "@/components/loadingC.vue"

  import { axios } from "@/common/api.service.js"
  import { useComponentsData } from "@/stores/ComponentsData"
  import { useNoAuthID } from "@/stores/NoAuthID"
  import { useState } from "@/stores/State"
  import { useOperations } from "@/stores/operations"
  import { ElMessage } from 'element-plus'


  import { defineAsyncComponent } from 'vue'

const ComponentData = defineAsyncComponent({
  // the loader function
  loader: () => import('@/components/calculator/ComponentData.vue'),

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

const ComponentGroup = defineAsyncComponent({
  loader: () => import('@/components/calculator/ComponentGroup.vue'),
  loadingComponent: LoadingC,
  delay: 0,
  timeout: 3000
})

export default {

  name: "ComponentsView", 
  components: {
    ComponentData,
    ComponentGroup,
  },
  setup(){
    const store = useComponentsData();
    const max_id = useNoAuthID();
    const state = useState();
    const operations = useOperations();
    return {
      store: store,
      state: state,
      max_id: max_id,
      operations: operations,
    }
  },
  data() {
    return {
      local_components: this.store.components,
      dialogVisible: false,
      new_component: [],
      dialog_component: [],
      dialog_component_index: 0,
      component_types: {
        "PC": [],
        "SE": [],
        "MO": [],
      },
      selected_components: {
        user: [],
        system: []
      },
      new_calculation: {
        name: "",
        emissions: this.store.mix[0].emissions,
      },

    }
  },
  watch: {
    // 'new_calculation.mix'(newValue, oldValue) {
    //   console.log("old")
    //   console.log(oldValue)
    //   console.log("new")
    //   console.log(newValue)
    //   // Utiliza una función de validación para asegurarte de que el valor sea numérico
    //   const numericValue = parseFloat(newValue);
    //   if (isNaN(numericValue)) {
    //     // Si el valor no es numérico, establece myNumber en null
    //     console.log("asignamos " + oldValue)
    //     this.new_calculation.mix = oldValue;
    //   } 
    // }
  },
  methods: {
    handleInput() {
      this.new_calculation.emissions = this.new_calculation.emissions.replace(/[^0-9]/g, "");

      // Si el valor no es numérico, no se actualizará myNumber y el campo seguirá siendo null
    },
    closeModal() {
      this.dialogVisible = false;
    },
    isAnyComponentSelected(){
      console.log("type")
      var types = ["system", "user"];
      for(var type_index in types){
        var type = types[type_index];
        for (const index in this.selected_components[type]){
          console.log(index)
          if(this.selected_components[type][index])
            return true;
        }
      }
      return false;
    },
    async CreateCalculation(){
      if (this.state.add_calc && this.new_calculation.name == "" ){
        ElMessage.error({
          duration: 8000,
          message: 'Escribe un nombre para el proyecto',
        })
        return
      }
      if (this.new_calculation.emissions == "" ){
        ElMessage.error({
          duration: 8000,
          message: 'Indica el ratio de emisiones',
        })
        return
      }
      if (!this.isAnyComponentSelected()){
        ElMessage.error({
          duration: 8000,
          message: 'Selecciona algún componente antes de continuar',
        })
        return
      }
      if (!this.state.add_use){
        await this.operations.saveCalculation(this.new_calculation);
        this.store.components_use = [];
      }
      this.createUses("system");
      this.createUses("user");
      this.$router.push('/');
      ElMessage.success({
          showClose: true,
          duration: 12000,
          message: 'Usos añadidos correctamente, ahora indica para cada uno el tiempo de uso o modifica las emisiones',
        })

    },
    createUses(type){
      for (const index in this.selected_components[type]){
        for (let uses = 0 ; uses < this.selected_components[type][index]; uses++) {
          const component = this.store.components[type][index];
          this.operations.newComponentUse(component, this.new_calculation.emissions);
       }
      }
    },
    toggleSelect(index,  value, system,){
      if(this.state.change_use){
        const component = system ? this.store.components.system[index] : this.store.components.user[index];
        this.updateComponentUse(component)
        this.$router.push('/') 
      }
      if(system)
        this.selected_components.system[index] = value;
      else
        this.selected_components.user[index] = value;
    },
    deleteComponent(index){
      this.operations.deleteComponent(index);
      this.selected_components.user.splice(index, 1)
    },
    addNewComponent(){
      this.dialogVisible = true;
      this.dialog_component = this.new_component;
    },
    duplicateComponent(index, system){  
      const component = system ? this.local_components.system[index] : this.local_components.user[index];
      this.dialog_component = JSON.parse(JSON.stringify(component));
      //borramos el elemento id para que cuando se cree uno nuevo al guardar
      delete this.dialog_component["id"];
      this.dialog_component.name = "New Copy"
      this.dialogVisible = true;
      
    },
    editComponent(index){
      this.dialog_component = this.local_components.user[index];
      this.dialogVisible = true;
      this.dialog_component_index = index;
    },
    validateComponent(c){
      if(c.name === "" || c.name == null || c.cfp_build_phase == null || 
        c.cfp_deviation_standard == null || c.middle_case == null || 
        c.worst_case == null || c.best_case == null || c.hosted_apps == null){
          return false;
      }
      return true;
    },
    saveComponentData(component){
      if(this.validateComponent(component)){
        this.dialogVisible = false;
        this.selected_components.user.push(0)
        this.operations.saveComponentData(component, this.dialog_component_index);
      }
      else {
        ElMessage.error({
          duration: 8000,
          message: 'Has introducido valores invalidos',
        })
      }
    },
    prepareNewComponent(){
      this.new_component = JSON.parse(JSON.stringify(this.local_components.system[0]));
      
      // borramos la id para indicar que tiene que crearse un componente nuevo
      delete this.new_component['id'];
      
      Object.keys(this.new_component).forEach((key) => {
        this.new_component[key] = null
      });
      this.new_component.cfp_build_phase = 0;
      this.new_component.cfp_deviation_standard = 0;
      
      this.new_component.middle_case = 0;
      this.new_component.best_case = 0;
      this.new_component.worst_case = 0;

      this.new_component.is_server = false;
      this.new_component.hosted_apps = 12;
      this.new_component.system_component = false;
    },
    prepareSelectedComponents(){ //revisar para no auth
      this.selected_components.system = new Array(this.store.components.system.length).fill(0);
      this.selected_components.user = new Array(this.store.components.user.length).fill(0);
    },
    prepareComponentTypes(){
      for (const index in this.store.components.system){
        const type = this.store.components.system[index].type;
        this.component_types[type].push(parseInt(index))
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
    updateTime(component){
        let old_component = this.getComponent(this.store.components_use[this.state.use_index].component, this.store.components_use[this.state.use_index].system_component)
        if(old_component.is_server == component.is_server)
          return  

        this.store.components_use[this.state.use_index].hours = 0;
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
  },
  created(){
    this.prepareNewComponent();
    this.prepareSelectedComponents();
    this.prepareComponentTypes();
  }
}
</script>

<style>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 240px;
  margin-bottom: 20px;
}



.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);;
  padding-left: 1px;
  padding-right: 1px;
  grid-auto-flow: dense;

}

.box-content {
  display: flex; 
  justify-content: space-between;
}

.el-card .el-card__body{
  padding: 0.4em;
  padding-left: 0.7em;
}

.button {
  padding: 8px !important;
}

.el-input-group__append{
  padding: 0 5px;
}

.name {
    padding-top: 0.5em;
    flex: 1;
    font-size: 0.9em;
  }

</style>