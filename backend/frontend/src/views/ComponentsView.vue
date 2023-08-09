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
                      <el-dropdown-item @click="duplicateComponent(index)">Duplicar</el-dropdown-item>
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
                    <el-dropdown-item @click="duplicateComponent(index)">Duplicar</el-dropdown-item>
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
      <el-button text @click="dialogVisible = true;">
        +
      </el-button>

      <el-dialog v-model="dialogVisible"  title="Create Component">
        <ComponentInfo 
          v-if="dialogVisible" 
          :data="this.dialog_component" 
          :dialog="true"
          @close="this.dialogFormVisible = false;" 
          @save="saveComponentData"
        />
      </el-dialog>
  
    </div>
</template>

<script>
  import { axios } from "@/common/api.service.js"
  import ComponentInfo from "@/components/ComponentInfo.vue"
export default {

  name: "ComponentsView",
  props: ["user", "components", "calculation_data", "calculations_data"],
  emits: ["updateComponents"],
  components: {
    ComponentInfo
  },
  data() {
    return {
      local_components: JSON.parse(JSON.stringify(this.components)),
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
      this.$emit("updateComponents", this.local_components.user);
        
      if(!this.user.authenticated)
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
    duplicateComponent(index){
      console.log("duplicate!");
      this.dialog_component = JSON.parse(JSON.stringify(this.local_components.user[index]));
       //borramos el elemento id para que cuando se cree uno nuevo al guardar
      delete this.dialog_component["id"];
      this.dialog_component.name = this.dialog_component.name + " (copy)" 
      this.dialogVisible = true;
      
    },
    editComponent(index){
      this.dialog_component = this.local_components.user[index];
      this.dialogVisible = true;
      this.dialog_component_index = index;
    },
    saveComponentData(component){
      this.dialogVisible = false;
        
        const body = {
          "name": component.name,
          "description": component.description,
          "idle_power": component.idle_power,
          "bad_case_idle_power": component.bad_case_idle_power,
          "good_case_idle_power": component.good_case_idle_power,
          "max_power": component.max_power,
          "bad_case_max_power": component.bad_case_max_power,
          "good_case_max_power": component.good_case_max_power,
          "cfp": component.cfp,
          "cfp_use_phase": "0",
          "cfp_deviation_standard": component.cfp_deviation_standard
        };
        if (component.id){
          //si tiene id es un uso existente entonces hay que editarlo
          //encontramos el index en la array de usage y modificamos el elemento, 
          //si no se encuentra el index es -1
          
          //console.log("id")
          //const index = this.local_data.usage.findIndex((local_data) => local_data.id === data.id);
          const index = this.dialog_component_index;
          if(!this.user.authenticated){
            this.local_components.user[index] = component;
            this.$emit("updateComponents", this.local_components.user);
            return
          }

          let endpoint = "/api/component/" + component.id + "/"
          axios.put(endpoint, body)
          .then(response => {
            console.log(response.data);
            this.local_components.user[index] = component;
            this.$emit("updateComponents", this.local_components.user);
          })
          .catch(error => {
            this.errorMessage = error.message;
            console.error("There was an error!", error);
          });

          
        }
        else { //si no tiene indice significa que es un componente nuevo

          console.log("no id")
          if(!this.user.authenticated){
            //le damos -1 como id para marcar que se ha creado pero que no se añade en la database
            component["id"] = "-1";
            this.local_components.user.push(component);
            this.$emit("updateComponents", this.local_components.user);
            console.log(this.local_components.usage)
            return
          }

          let endpoint = "/api/component/"
          console.log(body);
          axios.post(endpoint, body)
            .then(response => {
              console.log(response.data);
              this.local_components.user.push(response.data);
              this.$emit("updateComponents", this.local_components.user);
            })
            .catch(error => {
              this.errorMessage = error.message;
              console.error("There was an error!", error);
            });
        }
    }
  },
  oncreate(){
    this.new_component = this.local_components.system[0],
    Object.keys(this.new_component).forEach((key) => {
      this.new_component[key] = null
    });
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