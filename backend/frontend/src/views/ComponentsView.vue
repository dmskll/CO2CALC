<template>
    <div v-if="state.add_use">
      <el-form
        :model="new_calculation"
        style="max-width: 300px"
        label-position="top"
        :inline="true"
      >

        <el-form-item label="Nombre del projecto">
              <el-input v-model="this.new_calculation.name"  />
        </el-form-item>

        <el-form-item label="Emisiones">
              <el-input style="width: 80%;" v-model="this.new_calculation.emissions"  maxlength="3" @input="handleInput">
                <template #prepend>
                  <el-dropdown>
                  <el-button style="width: 3.7em;">
                    <font-awesome-icon icon="fa-regular fa-folder-open" size="lg" /> 
                  </el-button>
                  <template #dropdown>
                    <el-dropdown-menu >
                      <div v-for="(mix, index) in store.mix" :key="mix.pk" >

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
        <el-button text @click="CreateCalculation()">
          Save
        </el-button>
      </el-form>

      

    </div>
    <h1>Lista de componentes</h1>
    <div style="text-align: left;">
      
      <h3>Componentes de pre-hechos</h3>
      <ComponentGroup
        :data2="this.store.components.system"
        :system="true"
        :selected="selected_components.system"
        type="system"
        @duplicate="duplicateComponent"
        @toggleSelect="toggleSelect"
      />

      <h3>tus compas de pre-hechos</h3>


      <ComponentGroup
        :data2="this.store.components.user"
        :system="false"
        :selected="selected_components.user"
        type="user"
        @duplicate="duplnumbericateComponent"
        @edit="editComponent"
        @delete="deleteComponent"
        @toggleSelect="toggleSelect"
      />

      <el-button text @click="addNewComponent">
        +
      </el-button>

      <el-dialog v-model="dialogVisible"  title="Create Component">
        <ComponentData 
          v-if="dialogVisible" 
          :data="this.dialog_component"
          :use="this.dialog_component" 
          :dialog="true"
          :show_use="false"
          @close="this.dialogFormVisible = false;" 
          @save="saveComponentData"
        />
      </el-dialog>
  
    </div>
</template>

<script>
  import ComponentData from "@/components/ComponentData.vue"
  import ComponentGroup from "@/components/ComponentGroup.vue"

  import { useComponentsData } from "@/stores/ComponentsData"
  import { useNoAuthID } from "@/stores/NoAuthID"
  import { useState } from "@/stores/State"
  import { useOperations } from "@/stores/operations"



export default {

  name: "ComponentsView", 
  components: {
    ComponentData,
    ComponentGroup
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
      selected_components: {
        user: [],
        system: []
      },
      new_calculation: {
        name: "",
        emissions: "",
      }
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
    handleInput(value) {
      this.new_calculation.emissions = this.new_calculation.emissions.replace(/[^0-9]/g, "");

      // Si el valor no es numérico, no se actualizará myNumber y el campo seguirá siendo null
    },
    async CreateCalculation(){
      await this.operations.saveCalculation(this.new_calculation);
      this.store.components_use = [];
      this.createUses("system");
      this.createUses("user");
      this.$router.push('/') 

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
      console.log("a")
      if(system)
        this.selected_components.system[index] = value;
      else
        this.selected_components.user[index] = value;
    },
    deleteComponent(index){
      this.operations.deleteComponent(index);
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
    saveComponentData(component){
      this.dialogVisible = false;
      this.operations.saveComponentData(component, this.dialog_component_index);  
    },
    prepareNewComponent(){
      this.new_component = JSON.parse(JSON.stringify(this.local_components.system[0]));
      
      // borramos la id para indicar que tiene que crearse un componente nuevo
      delete this.new_component['id'];
      
      Object.keys(this.new_component).forEach((key) => {
        this.new_component[key] = null
      });
      this.new_component["system_component"] = false;
    },
    prepareSelectedComponents(){ //revisar para no auth
      this.selected_components.system = new Array(this.store.components.system.length).fill(0);
      this.selected_components.user = new Array(this.store.components.user.length).fill(0);
    },
  },
  created(){
    this.prepareNewComponent();
    this.prepareSelectedComponents();
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