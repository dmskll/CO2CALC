<template>
    <h1>Lista de componentes</h1>
    <div style="text-align: left;">
      <h3>Componentes de pre-hechos</h3>
        <div v-for="(component, index) in local_components.system" :key="component.pk" style=" display: flex; align-items: center;justify-content: center;">
          <el-card class="box-card">
            <template #header>
              <div class="card-header">
                <span>{{ component.name }}</span>
                <el-dropdown>
                  <el-button class="button" text>
                   ⚙️
                  </el-button>
                  <template #dropdown>
                    <el-dropdown-menu>
                      <el-dropdown-item @click="editComponent" disabled>Editar</el-dropdown-item>
                      <el-dropdown-item @click="duplicateComponent(index, true)">Duplicar</el-dropdown-item>
                      <el-dropdown-item @click="deleteComponent" divided disabled>Eliminar</el-dropdown-item>
                    </el-dropdown-menu>
                  </template>
                </el-dropdown>
              </div>
            </template>
            <div class="text item">{{ component.description }}</div>
          </el-card>
          <br>     
        </div>
      <h3>Tus componentes</h3>
      <div v-for="(component, index) in local_components.user" :key="component.pk" style=" display: flex; align-items: center;justify-content: center;" >
        <el-card class="box-card">
          <template #header>
            <div class="card-header">
              <span>{{ component.name }}</span>
              <el-dropdown>
                <el-button class="button" text>
                  ⚙️
                </el-button>
                <template #dropdown>
                  <el-dropdown-menu>
                    <el-dropdown-item @click="editComponent(index)">Editar</el-dropdown-item>
                    <el-dropdown-item @click="duplicateComponent(index, false)">Duplicar</el-dropdown-item>
                    <el-dropdown-item @click="deleteComponent(index)" divided>Eliminar</el-dropdown-item>
                  </el-dropdown-menu>
                </template>
              </el-dropdown>
            </div>
          </template>
          <div class="text item">{{ component.description }}</div>
        </el-card>
        <br>     
      </div>
      <el-button text @click="addNewComponent">
        +
      </el-button>

      <el-dialog v-model="dialogVisible"  title="Create Component">
        <ComponentData 
          v-if="dialogVisible" 
          :data="this.dialog_component"
          :use="this.dialog_component" 
          :dialog="true"
          @close="this.dialogFormVisible = false;" 
          @save="saveComponentData"
        />
      </el-dialog>
  
    </div>
</template>

<script>
  import { axios } from "@/common/api.service.js"
  import ComponentData from "@/components/ComponentData.vue"
  import { useComponentsData } from "@/stores/ComponentsData"


export default {

  name: "ComponentsView",
  components: {
    ComponentData
  },
  setup(){
    const store = useComponentsData();
    return {
      store: store,
    }
  },
  data() {
    return {
      local_components: this.store.components,
      dialogVisible: false,
      new_component: [],
      dialog_component: [],
      dialog_component_index: 0,
    }
  },
  methods: {
    deleteComponent(index){
      console.log("delete!")
      const id = this.local_components.user[index].id
      this.local_components.user.splice(index, 1);
        
      if(!this.store.user_info.authenticated)
        return

      let endpoint = "/api/component/" + id +"/";
          axios.delete(endpoint)
            .then(response => {
              console.log(response);
            })
            .catch(error => {
              this.errorMessage = error.message;
              console.error("There was an error!", error);
            });
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
        
      // El cuerpo que se enviará en el POST
        const body = {
          "worse_case": component.worse_case,
          "best_case": component.best_case,
          "middle_case": component.middle_case,
          "cfp": 0,
          "cfp_build_phase": component.cfp,
          "cfp_deviation_standard": component.cfp_deviation_standard,
          "name": component.name,
          "description": component.description,
        };

        if (component.id){
          //si tiene id es un uso existente entonces hay que editarlo
          //encontramos el index en la array de usage y modificamos el elemento, 
          //si no se encuentra el index es -1
          
          //console.log("id")
          //const index = this.local_data.usage.findIndex((local_data) => local_data.id === data.id);
          const index = this.dialog_component_index;
          if(!this.store.user_info.authenticated){
            this.local_components.user[index] = component;
            return
          }

          let endpoint = "/api/component/" + component.id + "/"
          axios.put(endpoint, body)
          .then(response => {
            console.log(response.data);
            this.local_components.user[index] = component;
          })
          .catch(error => {
            this.errorMessage = error.message;
            console.error("There was an error!", error);
          });

          
        }
        else { //si no tiene indice significa que es un componente nuevo

          if(!this.store.user_info.authenticated){
            //le damos -1 como id para marcar que se ha creado pero que no se añade en la database
            component["id"] = "-1";
            this.local_components.user.push(component);
            console.log(this.local_components.usage)
            return
          }

          let endpoint = "/api/component/"
          console.log(body);
          axios.post(endpoint, body)
            .then(response => {
              console.log(response.data);
              this.local_components.user.push(response.data);
            })
            .catch(error => {
              this.errorMessage = error.message;
              console.error("There was an error!", error);
            });
        }
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
  },
  created(){
    this.prepareNewComponent()
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
  width: 480px;
  margin-bottom: 20px;
}
</style>