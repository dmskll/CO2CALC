<template>
  <el-input
    :disabled="!dialog"
    v-model="local_data.Description"
    type="textarea"
    autosize
    placeholder="Please input"
  />
  <el-form-item label="Horas usadas">
    <el-input-number :disabled="!dialog" v-model="local_data.hours" :precision="2" :step="0.1" :max="1000" :controls="false" />
  </el-form-item>
  <div class="slider-demo-block">
    <span class="demonstration">Porcentaje de uso</span>
    <el-slider :disabled="!dialog" v-model="local_data.use" :step="10" show-stops />
  </div>          
    <div  class="dialog-footer" v-if="dialog" style="text-align: right;">
    <el-button @click="$emit('close')" plain>Cancelar</el-button>
    <el-button color="#7cd4ac" @click="$emit('save', local_data)" plain>
      Guardar
    </el-button>
  </div>
</template>
  


<script>
  export default {
    name: "ComponentUsage",
    props: ["data", "dialog"],
    watch: {
      data() {
        this.local_data = JSON.parse(JSON.stringify(this.data))
      },
    },
    emits: ["save", "close"],
    // setup(props, ctx) {
    //    ctx.emit()
    // },
    data() {
      return {
        local_data: JSON.parse(JSON.stringify(this.data))
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

.dialog-footer button:first-child {
  margin-right: 10px;
}

::v-deep .el-form-item.is-disabled,
::v-deep .el-slider.is-disabled {
  cursor: not-allowed !important;

}
</style>


  