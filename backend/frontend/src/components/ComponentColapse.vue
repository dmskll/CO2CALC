<template>
    <el-row>
    <el-col :span="14" style="padding-right: 20px">
      <h3>Info</h3>
        <el-input
          v-model="local_data.description"
          type="textarea"
          autosize
          placeholder="Please input"
        />
        <div  style="text-align: left; margin-top:30px;">
          <b>Fase de fabricación</b>
        </div>
        <br>

      
        <ComponentInfo :data="local_data" />



    </el-col>
    <el-col :span="10" style="padding-left: 20px">
      <h3>Uso</h3>
      <div v-for="use in local_data.usage" :key="use.pk" style="margin-bottom: 50px">
        <ComponentUsage :data="use" :dialog="false" />
      </div>





   <el-button text @click="dialogFormVisible = true">
    +
  </el-button>

  <el-dialog v-model="dialogFormVisible" title="Shipping address">

    <ComponentUsage :data="add_usage" :dialog="true" @close="closeDialog" @save="saveUsageData"/>

  </el-dialog>
    </el-col>
  </el-row>
</template>
  
<script setup>


</script>


<script>
import ComponentInfo from "@/components/ComponentInfo.vue"
import ComponentUsage from "@/components/ComponentUsage.vue"

  export default {
    name: "ComponentColapse",
    props: ["data"],
    data() {
      return {
        local_data: JSON.parse(JSON.stringify(this.data)),
        dialogFormVisible: false,
        add_usage: {
          Description: "Uso nuevo",
          calculation: 0,
          component: 0,
          hours: 0,
          id: -1,
          use: 0,
        },
      }
    },
    components: {
      ComponentInfo,
      ComponentUsage
    },
    methods: {
      async addUse() {
        let new_usage = {
          "Description":"Uso nuevo",
          "calculation":"0",
          "component": this.local_data.id,
          "hours":"0",
          "id":"-1",
          "use":"0",
        }
        this.local_data.usage.push(new_usage);
      },
      closeDialog() {
        this.dialogFormVisible = false;
      },
      saveUsageData(data) {
        this.dialogFormVisible = false;
        console.log(data);
        let new_usage = {
          "Description": data.Description,
          "calculation":data.calculation,
          "component": this.local_data.id,
          "hours": data.hours,
          "id":"-1",
          "use": data.use,
        }
        this.local_data.usage.push(new_usage);
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


  