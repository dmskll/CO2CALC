<template>
    <el-row>
    <el-col :span="14" style="padding-right: 20px">
      <h3>Info</h3>
        <el-button  @click="editComponent()">Edit</el-button>
        <el-button  @click="removeComponent()">Remove</el-button> <br>
        <ComponentInfo :data="local_data" :dialog="false"/>

      <el-dialog v-model="dialogFormVisible"  title="Shipping address">
        <ComponentInfo v-if="dialogFormVisible" :data="local_data" :dialog="false" @close="closeDialog" @save="saveUsageData"/>
      </el-dialog>
    </el-col>
    <el-col :span="10" style="padding-left: 20px">
      <h3>Uso</h3>
      <div v-for=" (use, index) in local_data.usage" :key="use.pk" style="margin-bottom: 50px">
        <el-button  @click="editUsage(index)">Edit</el-button>
        <el-button  @click="removeUsage(index, use.id)">Remove</el-button> <br>
        <ComponentUsage :data="use" :dialog="false"/>
      </div>





   <el-button text @click="dialogFormVisible = true; usage_to_edit=new_usage;">
    +
  </el-button>

  <el-dialog v-model="dialogFormVisible"  title="Shipping address">
    <ComponentUsage v-if="dialogFormVisible" :data="usage_to_edit" :dialog="true" @close="closeDialog" @save="saveUsageData"/>
  </el-dialog>
    </el-col>
  </el-row>
</template>
  
<script setup>


</script>


<script>
import ComponentInfo from "@/components/ComponentInfo.vue"
import ComponentUsage from "@/components/ComponentUsage.vue"
import { axios } from "@/common/api.service.js"

  export default {
    name: "ComponentColapse",
    props: ["user", "data", "calculation_id"],
    data() {
      return {
        local_data: JSON.parse(JSON.stringify(this.data)),
        component_id: this.calculation_id,
        dialogFormVisible: false,
        usage_to_edit: {},
        dialog_usage_index: null,
        new_usage: {
          Description: null,
          calculation: 0,
          component: 0,
          hours: 0,
          id: null,
          use: 0,
        },
      }
    },
    components: {
      ComponentInfo,
      ComponentUsage
    },
    methods: {
      closeDialog() {
        this.dialogFormVisible = false;
      },
      saveUsageData(data) {
        this.dialogFormVisible = false;
        
        const component_usage = { 
          "hours": data.hours,
          "use": data.use,
          "Description": data.Description,
          "component": this.local_data.id
        };
        console.log(data)
        if (data.id){
          //si tiene id es un uso existente entonces hay que editarlo
          //encontramos el index en la array de usage y modificamos el elemento, 
          //si no se encuentra el index es -1
          
          //console.log("id")
          //const index = this.local_data.usage.findIndex((local_data) => local_data.id === data.id);
          const index = this.dialog_usage_index;
          if (index !== -1){
            if(!this.user.authenticated){
              //le damos -1 como id para marcar que se ha creado pero que no se añade en la database
              component_usage["id"] = "-1";
              this.local_data.usage[index] = component_usage;
              return
            }

            let endpoint = "/api/usage/" + data.id
            axios.put(endpoint, component_usage)
            .then(response => {
              console.log(response.data);
              this.local_data.usage[index] = data;
            })
            .catch(error => {
              this.errorMessage = error.message;
              console.error("There was an error!", error);
            });
          }
          
        }
        else { //si no tiene indice significa que es un uso nuevo

          //CREAR UN IF NOT AUTHENTITICATED
          // let new_usage = {
          //   "Description": data.Description,
          //   "calculation":data.calculation,
          //   "component": this.local_data.id,
          //   "hours": data.hours,
          //   "id":"-1",
          //   "use": data.use,
          // }
          // this.local_data.usage.push(new_usage);
          console.log("no id")
          if(!this.user.authenticated){
            //le damos -1 como id para marcar que se ha creado pero que no se añade en la database
            component_usage["id"] = "-1";
            this.local_data.usage.push(component_usage);
            console.log(this.local_data.usage)
            return
          }

          let endpoint = "/api/calculation/"+ this.calculation_id +"/usage/"
          axios.post(endpoint, component_usage)
            .then(response => {
              console.log(response.data);
              this.local_data.usage.push(response.data);
            })
            .catch(error => {
              this.errorMessage = error.message;
              console.error("There was an error!", error);
            });
        }
      },
      removeUsage(index, id) {

        console.log(index);
        this.local_data.usage.splice(index, 1);
        if(!this.user.authenticated)
          return

          let endpoint = "/api/usage/" + id;
          axios.delete(endpoint,)
            .then(response => {
              console.log(response);
            })
            .catch(error => {
              this.errorMessage = error.message;
              console.error("There was an error!", error);
            });

      },
      editUsage(index) {
        this.dialog_usage_index = index;
        this.usage_to_edit = this.local_data.usage[index];
        this.dialogFormVisible = true;
      }

    }
  }
</script>


<style>
  .slider-demo-block {
    display: flex;
    flex-direction: column; /* Cambiar la dirección del flujo a vertical */
    align-items: flex-start; /* Alinear el contenido a la izquierda */
  }
  .slider-demo-block .el-slider {
    margin-top: 12px; /* Añadir un margen superior para separar del texto */
  }
  .slider-demo-block .demonstration {
    font-size: 14px;
    color: var(--el-text-color-secondary);
    line-height: 44px;
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-bottom: 0;
  }
  .slider-demo-block .demonstration + .el-slider {
    flex: 0 0 100%; /* Establecer el ancho del slider al 100% */
  }

  
</style>


  