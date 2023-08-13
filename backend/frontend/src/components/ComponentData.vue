<template>

  <div style="display: flex;  justify-content: center;">
    <div style="flex: 1; text-align: left;">
      {{ local_data.name }}
      <el-form
        :model="local_data"
        style="max-width: 300px"
        :disabled="!dialog"
      >
    <el-input
      v-model="local_data.description"
      type="textarea"
      autosize
      placeholder="Please input"
      style="margin-top: 10px;"
    />
    </el-form>
    </div>
    <div style="flex: 1">
      <el-form-item label="horas usadas">
            <el-input-number v-model="local_use.hours" @focusin="old_hours=local_use.hours" @focusout="saveUse" :precision="2" :step="0.1" :max="1000" :controls="false" />
      </el-form-item>
    </div>
  </div>



<el-collapse v-model="activeNames" @change="handleChange">
  <el-collapse-item title="mas información" name="1">
  <el-row :gutter="20">
    <el-col :span="12">
      <div  style="text-align: center; margin-top:30px;">
        <b>Fase de fabricación</b>
      </div>
      <br>
      <el-form
        label-width="150px"
        :model="local_data"
        style="max-width: 300px; text-align: left;"
        :disabled="!dialog"
      >
      <el-form-item label="CFP Fabricación">
            <el-input-number v-model="local_data.cfp" :precision="2" :step="0.1" :max="1000" :controls="false" />
      </el-form-item>
      <el-form-item label="Desviación estandard">
              <el-input-number v-model="local_data.cfp_deviation_standard" :precision="2" :step="0.1" :max="1000" :controls="false" />
      </el-form-item>
    </el-form>
    </el-col>
    <el-col :span="12">
      <el-form
        label-width="150px"
        :model="local_data"
        
        :disabled="!dialog"
      >
      <div  style="text-align: center; margin-top:30px;">
        <b>Fase de uso</b> <br><br>
      </div>
    
      <el-form-item label="Caso medio">
            <el-input-number v-model="local_data.middle_case" :precision="2" :step="0.1" :max="1000" :controls="false" />
      </el-form-item>
    
      <el-form-item label="Caso pesimo">
              <el-input-number v-model="local_data.worse_case" :precision="2" :step="0.1" :max="1000" :controls="false" />
      </el-form-item>
    
      <el-form-item label="Caso optimo">
              <el-input-number v-model="local_data.best_case" :precision="2" :step="0.1" :max="1000" :controls="false" />
      </el-form-item>
    </el-form>
    </el-col>
  </el-row>
</el-collapse-item>
    </el-collapse>

  <span class="dialog-footer" v-if="dialog">
    <el-button @click="$emit('close')">Cancel</el-button>
    <el-button type="primary" @click="$emit('save', local_data)">
      Confirm
    </el-button>
  </span>
</template>
  



<script>
  export default {
    name: "ComponentData",
    props: ["data", "dialog", "use"],
    emits: ["saveUse", "save", "close"],
    data() {
      return {
        local_data: JSON.parse(JSON.stringify(this.data)),
        local_use: JSON.parse(JSON.stringify(this.use)),
        old_hours: 0
      }
    },
    methods: {
      saveUse(){
        // si se ha modificado el campo lo enviamos
        if(this.old_hours != this.local_use.hours)
          this.$emit('saveUse', this.local_use)
      }
    }
  }
</script>


<style>
.code-container{
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
}
.code-block{
  flex: 1;
  width: 50%;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
}
</style>


  