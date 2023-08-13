
<template>
  <main>
    <el-dropdown>
    <span class="el-dropdown-link">
      Seleccionar Calculos
    </span>
    <template #dropdown>
      <el-dropdown-menu >
        <div v-for="calculation in this.store.calculations" :key="calculation.pk" >
          <el-dropdown-item @click="changeCalculation(calculation.id)"> {{ calculation.name }}</el-dropdown-item>
        </div>
      </el-dropdown-menu>
    </template>
  </el-dropdown>



    <h1>Calculadora: {{ this.store.calculations.name }}</h1>
    <div v-for="(used_component, index) in this.store.components_use" :key="used_component.pk">
      <div class="hw-collapse">
        <el-card>


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
              <br>




              <ComponentData
                :dialog="false"
                :data="getComponent(used_component.component)"
                :use="used_component"
                @saveUse="updateData"
              />



        </el-card>
      </div> 
    </div>
    <el-button text @click="dialogComponentVisible = true; usage_to_edit=new_usage;">
      +
    </el-button>

    <el-dialog v-model="dialogComponentVisible"  title="Add component" width="40%">
      <el-scrollbar height="400px" style="width: auto;">
        <div v-for="(component, index) in this.store.components.system" :key="component.pk">
          <el-card @click="addComponent(component.system_component, index)" class="box-card" el-card shadow="hover">
            <div class="text item"><b>{{ component.name }}</b></div>
            <div class="text item">{{ component.description }}</div>
          </el-card>
        </div>
        <div v-for="(component, index) in this.store.components.user" :key="component.pk" style="width: auto;">
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

//import ComponentColapse from "@/components/ComponentColapse.vue"
import ComponentData from "@/components/ComponentData.vue"
import { useComponentsData } from "@/stores/ComponentsData"
import { axios } from "@/common/api.service.js"

export default {
  name: "HomeView",
  setup(){
    const store = useComponentsData();
    return {
      store: store,
    }

  },
  data() {
    return {
      dialogComponentVisible: false,
    }
  },
  props: ["user", "calculation_data", "calculations_data", "components", "current_calculation" ],
  emits: ["updateCalculation", "changeCalculation", "removeUsedComponent"],
  components: {
    ComponentData
  },
  methods: {
    updateData(data){
      console.log("pierde contexto")
      console.log(data)
      const body = {
        "component": data.component,
        "hours": data.hours,
      }
      const index = this.store.components_use.findIndex((use) => use.id === data.id);
      this.store.components_use[index] = data;
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
    getComponent(id){
      let component = this.store.components.system.filter((item) => item.id === id);
      
      if(typeof component[0] === 'undefined'){
        component = this.store.components.user.filter((item) => item.id === id)
        console.log("dentro")
      }
      console.log(component[0])
      return component[0];
    },
    getComponentName(id){
      let component = this.store.components.system.filter((item) => item.id === id);
      
      if(typeof component === 'undefined')
        component = this.store.components.user.filter((item) => item.id === id)

      return component[0].name;
    },


    
    addComponent(system, index){
      console.log("añadido!" + index);
      const component = system ? this.store.components.system[index] : this.store.components.user[index];

      const body = {
        "component": component.id,
        "hours": 0,
      }
      let endpoint = "/api/calculation/"+ this.store.current_calculation +"/usage/"
      axios.post(endpoint, body)
      .then(response => {
        console.log(response.data);
        this.store.components_use.push(response.data);
      })
      .catch(error => {
        this.errorMessage = error.message;
        console.error("There was an error!", error);
      });

      this.dialogComponentVisible = false;
    },
    changeCalculation(id){
      this.$emit('changeCalculation', id)
    },
    removeUsedComponent(index){
      let endpoint = "/api/usage/" + this.store.components_use[index].id;
        axios.delete(endpoint)
          .then(response => {
            console.log(response);
          })
          .catch(error => {
            this.errorMessage = error.message;
            console.error("There was an error!", error);
          });
      this.store.components_use.splice(index, 1)
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
  margin-bottom: 2px;
}



.example-showcase .el-dropdown-link {
  cursor: pointer;
  color: var(--el-color-primary);
  display: flex;
  align-items: center;
}


</style>