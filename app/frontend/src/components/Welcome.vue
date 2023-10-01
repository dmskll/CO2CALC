<template>
  <h1 style="margin: 0;">CO2Calc</h1>
  <h3 style="margin: 0;">Calcula las emisiones de tu proyecto</h3>

  <p style="text-align: justify;">
    Con esta herramienta podrás estimar las emisiones asociadas a tu proyecto,
    según los componentes usados y el consumo electrico.
  </p>

  <el-alert type="info" :closable="false" style="margin-bottom: 1.3em;">
    <p style="font-size: 1.15em; text-align: justify;">
      Si eres un estudiante de la UPC y te gustaria guardar tus calculos, inicia sesión 
      con tus credenciales de la universidad antes de empezar.
    </p>
  </el-alert>

  <el-button @click="$emit('start')" class="button">
    Empezemos!  
  </el-button>
</template>
  



<script>


  export default {
    name: "WelcomePage",
    emits: ['start']
  }
</script>

<style>
.flex-grow {
flex-grow: 1;
}
.flex-shrink {
flex-shrink: 1;
}
</style>
  