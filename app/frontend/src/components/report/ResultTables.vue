<template>
  <table class="resume">
    <caption style="caption-side: bottom">
      Resumen de las emisiones (KgCO2) de las fases de vida de los componentes
      para el caso bueno, medio y óptimo.
    </caption>
    <thead>
      <tr>
        <th rowspan="3">Componente</th>
        <th colspan="9">Fases</th>
        <th colspan="3" rowspan="3">Total</th>
      </tr>
      <tr>
        <th colspan="3">Fabricación</th>
        <th colspan="3">Uso</th>
        <th colspan="3">Destrucción<br /></th>
      </tr>
      <tr class="case">
        <th>mejor</th>
        <th>medio</th>
        <th>peor</th>

        <th>mejor</th>
        <th>medio</th>
        <th>peor</th>

        <th>mejor</th>
        <th>medio</th>
        <th>peor</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for=" (use) in uses" :key="use.pk" class="color-row">
        <td class="component">{{ use.component.name }}</td>

        <td>{{ use.best.build_cost }}<br /></td>
        <td>{{ use.middle.build_cost }}</td>
        <td>{{ use.worst.build_cost }}</td>

        <td>{{ use.best.use_cost_co2 }}</td>
        <td>{{ use.middle.use_cost_co2 }}</td>
        <td>{{ use.worst.use_cost_co2 }}</td>

        <td>{{ use.best.destroy_cost }}</td>
        <td>{{ use.middle.destroy_cost }}</td>
        <td>{{ use.worst.destroy_cost }}</td>

        <td>{{ use.best.total }}</td>
        <td>{{ use.middle.total }}</td>
        <td>{{ use.worst.total }}<br /></td>
      </tr>

      <tr class="total">
        <td>Total (KgCO2)</td>
        <td>{{ results.best.build_cost }}<br /></td>
        <td>{{ results.middle.build_cost }}</td>
        <td>{{ results.worst.build_cost }}</td>
        <td>{{ results.best.use_cost_co2 }}<br /></td>
        <td>{{ results.middle.use_cost_co2 }}</td>
        <td>{{ results.worst.use_cost_co2 }}</td>
        <td>{{ results.best.destroy_cost }}</td>
        <td>{{ results.middle.destroy_cost }}</td>
        <td>{{ results.worst.destroy_cost }}</td>
        <td>{{ results.best.total }}<br /></td>
        <td>{{ results.middle.total }}</td>
        <td>{{ results.worst.total }}<br /></td>
      </tr>
    </tbody>
  </table>

  <table class="resume">
    <caption style="caption-side: bottom">
      Resumen del consumo eléctrico (kWh) durante el uso de los componentes para
      el caso bueno, medio y pésimo.
    </caption>
    <thead>
      <tr>
        <th rowspan="2">Componente</th>
        <th colspan="3">Consumo eléctrico fase uso</th>
      </tr>

      <tr>
        <th>mejor</th>
        <th>medio</th>
        <th>peor</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for=" (use) in uses" :key="use.pk">
        <td class="component">{{ use.component.name }}</td>
        <td>{{ use.best.use_cost }}</td>
        <td>{{ use.middle.use_cost }}</td>
        <td>{{ use.worst.use_cost }}</td>
      </tr>

      <tr class="total">
        <td>Total (kWh)</td>
        <td>{{ results.best.use_cost }}<br /></td>
        <td>{{ results.middle.use_cost }}</td>
        <td>{{ results.worst.use_cost }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>

export default {
  name: "ResultTables",
  props: ["results", "uses"],
}
</script>

<style></style>
