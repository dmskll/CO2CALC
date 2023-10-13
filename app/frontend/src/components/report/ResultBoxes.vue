<template>
  <div class="result-box">
    <h3>
      La estimación de emisiones de CO2 asociada al proyecto es de:
      <h1>
        {{ results.middle.total }} KgCo2
      </h1>
    </h3>
    Dependiendo de la intensidad del uso y de como se ha fabricado cada componente, 
    las emisiones pueden variar. En el mejor caso, donde se ha emitido lo menos 
    posible y el uso de los componentes ha sido menos intensivo, se estima una 
    emisión de {{ results.best.total }} KgCo2. En el peor de los casos se estima que las emisiones 
    podrían llegar hasta {{ results.worst.total }} KgCo2.
  </div>
  <br>
  <div class="result-box">
    <h3>
      El consumo eléctrico estimado es de:
      <h1>
        {{ results.middle.use_cost }} kWh
      </h1>
    </h3>
    Dependiendo de la intensidad del uso, el consumo puede variar. En el mejor caso, donde
    el uso de los componentes ha sido menos intensivo, se estima un consumo de
    {{ results.best.use_cost }} kWh. En el peor de los casos se estima que el
    consumo podría llegar hasta {{ results.worst.use_cost }} kWh.
  </div>
  <div class="compare-box">
    <h3>
      {{ results.middle.total }} KgCO2 equivalen a:
    </h3>
    
    <ul>
      <li>{{  (results.middle.total / compare.beef).toFixed(0) }} hamburguesas de ternera</li>
      <li>{{  (results.middle.total / compare.beyond).toFixed(0) }}  hamburguesas de imitación vegetal</li>
      <br>
      <li>{{ (results.middle.total / compare.train_km).toFixed(1) }} viajes Barcelona-Madrid en AVE por pasajero</li>
      <li>{{  (results.middle.total / compare.plain_km).toFixed(1) }} viajes Barcelona-Madrid en avión por pasajero</li>
    </ul> 
    <p style="font-size: 0.4em;">
      <ul>
        <li>//https://css.umich.edu/publications/research-publications/beyond-meats-beyond-burger-life-cycle-assessment-detailed</li>
        <li>https://www.ecologistasenaccion.org/134774/la-aviacion-tiene-los-dias-contados/</li>
      </ul> 
    </p>
  </div>
</template>
  



<script>

  export default {
    name: "ResultBoxes",
    props: ["results"],

    data(){
      return{
        compare: { //kgCo2
          beef: 3.7, //https://css.umich.edu/publications/research-publications/beyond-meats-beyond-burger-life-cycle-assessment-detailed
          beyond: 0.4,
          car_km: 70.3, //104 gco2
          bus_km: 0.068, //68 gco2
          train_km: 14.4, //14 gco2
          plain_km: 114, //285 gco2 //https://www.ecologistasenaccion.org/134774/la-aviacion-tiene-los-dias-contados/
        }
      }
    },

  }
</script>

<style>

</style>
  