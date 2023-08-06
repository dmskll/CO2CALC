<template>
 <el-form
    label-position="left"
    label-width="200px"
    :model="local_data"
    style="max-width: 300px; text-align: left;"
    :disabled="!dialog"
  >
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
  <el-form-item label="CFP Fabricación">
        <el-input-number v-model="local_data.cfp" :precision="2" :step="0.1" :max="10" :controls="false" />
  </el-form-item>
  <el-form-item label="Desviación estandard">
          <el-input-number v-model="local_data.cfp_deviation_standard" :precision="2" :step="0.1" :max="10" :controls="false" />
  </el-form-item>
  <div  style="text-align: left; margin-top:30px;">
    <b>Fase de uso</b> <br><br>
    <u>Consumo en reposo (W)</u>
  </div>

          <el-form-item label="Consumo medio">
                <el-input-number v-model="local_data.idle_power" :precision="2" :step="0.1" :max="10" :controls="false" />
          </el-form-item>

          <el-form-item label="Consumo pesimo">
                  <el-input-number v-model="local_data.bad_case_idle_power" :precision="2" :step="0.1" :max="10" :controls="false" />
          </el-form-item>

          <el-form-item label="Consumo optimo">
                  <el-input-number v-model="local_data.good_case_idle_power" :precision="2" :step="0.1" :max="10" :controls="false" />
          </el-form-item>
          <u >Consumo en maximo (W)</u>
          <el-form-item label="Consumo medio">
                <el-input-number v-model="local_data.max_power" :precision="2" :step="0.1" :max="10" :controls="false" />
          </el-form-item>

          <el-form-item label="Consumo pesimo">
                  <el-input-number v-model="local_data.bad_case_max_power" :precision="2" :step="0.1" :max="10" :controls="false" />
          </el-form-item>

          <el-form-item label="Consumo optimo">
                  <el-input-number v-model="local_data.good_case_max_power" :precision="2" :step="0.1" :max="10" :controls="false" />
          </el-form-item>
</el-form>
</template>
  
<script setup>
//import { ref } from 'vue';



</script>


<script>
  export default {
    name: "ComponentInfo",
    props: ["data", "dialog"],
    data() {
      return {
        local_data: JSON.parse(JSON.stringify(this.data))
      }
    },
    methods: {

    }
  }
</script>


<style>

</style>


  