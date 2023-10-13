<template>
  <div
    v-for=" (use) in uses"
    :key="use.pk"
    style="
      margin-bottom: 50px;
      text-align: left;
      font-size: medium;
    "
  >
    <div v-if="use.component.is_server">
      <h1>{{ use.component.name }}</h1>

      <table class="component-table">
        <tbody>
          <tr>
            <td style="width: 80%">Descripción</td>
            <td colspan="2">Fabricación (kgCo2)</td>
            <td colspan="3">Casos de uso (W)<br /></td>
            <td>Tiempo de uso<br /></td>
            <td>Aplicaciones alojadas<br /></td>
            <td>Mix eléctrico<br /></td>
          </tr>
          <tr>
            <td rowspan="2">{{ use.component.description }}</td>
            <td class="sub-header">Emisiones</td>
            <td class="sub-header">Desviacón</td>
            <td class="sub-header">bueno</td>
            <td class="sub-header">medio</td>
            <td class="sub-header">malo</td>
            <td rowspan="2">{{ use.server_years }} años</td>
            <td rowspan="2">{{ use.component.hosted_apps }}</td>
            <td rowspan="2">{{ use.emissions }} gCO2/kWh</td>
          </tr>
          <tr>
            <td>{{ use.component.cfp_build_phase }}</td>
            <td>{{ use.component.cfp_deviation_standard }}</td>
            <td>{{ use.component.best_case }}</td>
            <td>{{ use.component.middle_case }}</td>
            <td>{{ use.component.worst_case }}<br /></td>
          </tr>
        </tbody>
      </table>
      <p style="text-align: justify">
        El coste de fabricación viene calculado por el coste de producción del
        servidor dividido por el número de aplicaciones que podría alojar sin que
        el rendimiento se viera excesivamente afectado.
      </p>

      <div class="equations-box">
        <EquationComponent :show_tex="latex" :formula="server_hours_exp" />
        <EquationComponent :show_tex="latex" :formula="build_cost_server_exp" />

        <EquationComponent
          :show_tex="latex"
          :formula="build_cost_server(use, 'middle')"
        />
      </div>

      <p style="text-align: justify">
        El coste de uso viene dado por dos partes según el consumo del servidor,
        teniendo en cuenta los gastos que equivalen que el servidor esté alojado
        en un CPD. El directo (50%) es el consumo eléctrico de la máquina (47%)
        más la red (3%), el coste indirecto (50%) es el que representa el
        sobreconsumo que tiene el servidor en el centro de datos (costes de
        refrigeración (37%), distribución de la energía (10%), iluminación (3%)
        y distribución de la energía (10%)).
        <br /><br />
        De esta forma primero calcularemos el coste directo del consumo de la
        aplicación en el servidor y lo multiplicaremos por dos para tener en
        cuenta el coste indirecto.
      </p>

      <div class="equations-box">
        <EquationComponent :show_tex="latex" :formula="consume_server_exp" />
        <EquationComponent
          :show_tex="latex"
          :formula="consume_server(use, 'middle')"
        />

        <EquationComponent
          :show_tex="latex"
          :formula="consume_network_server"
        />
        <EquationComponent
          :show_tex="latex"
          :formula="consume_network(use, 'middle')"
        />

        <EquationComponent :show_tex="latex" :formula="use_cost_server_exp" />
        <EquationComponent
          :show_tex="latex"
          :formula="use_cost_server(use, 'middle')"
        />
      </div>

      <div style="break-before: page">
        <p style="text-align: justify">
          Asumimos que el coste de destrucción es un 1% del coste de las fases
          de fabricación y uso.
        </p>

        <div class="equations-box">
          <EquationComponent :show_tex="latex" :formula="end_life_exp" />
          <EquationComponent
            :show_tex="latex"
            :formula="destruction_cost(use, 'middle')"
          />
        </div>

        <p style="text-align: justify">
          El coste total viene dado por la suma de las emisiones de las tres
          fases.
        </p>

        <div class="equations-box">
          <EquationComponent :show_tex="latex" :formula="total_cost_exp" />
          <EquationComponent
            :show_tex="latex"
            :formula="total_cost(use, 'middle')"
          />
        </div>

        <p style="text-align: justify">
          Estos son los calculos para el peor caso, en el que el consumo de
          electricidad y el coste de fabricación ha sido más elevado
        </p>

        <div class="equations-box">
          <EquationComponent
            :show_tex="latex"
            :formula="build_cost_server(use, 'worst')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="consume_server(use, 'worst')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="consume_network(use, 'worst')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="use_cost_server(use, 'worst')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="destruction_cost(use, 'worst')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="total_cost(use, 'worst')"
          />
        </div>

        <p style="text-align: justify">
          Estos son los cálculos para el mejor caso, en el que el consumo de
          electricidad y el coste de fabricación ha sido más bajo.
        </p>

        <div class="equations-box">
          <EquationComponent
            :show_tex="latex"
            :formula="build_cost_server(use, 'best')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="consume_server(use, 'best')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="consume_network(use, 'best')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="use_cost_server(use, 'best')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="destruction_cost(use, 'best')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="total_cost(use, 'best')"
          />
        </div>
      </div>
    </div>
    <div v-else>
      <h1>{{ use.component.name }}</h1>

      <table class="component-table">
        <tbody>
          <tr>
            <td style="width: 80%">Descripción</td>
            <td colspan="2">Fabricación (kgCO2)</td>
            <td colspan="3">Casos de uso (W)<br /></td>
            <td>Tiempo de uso<br /></td>
            <td>Mix eléctrico<br /></td>
          </tr>
          <tr>
            <td rowspan="2">{{ use.component.description }}</td>
            <td class="sub-header">Emisiones</td>
            <td class="sub-header">Desviacón</td>
            <td class="sub-header">bueno</td>
            <td class="sub-header">medio</td>
            <td class="sub-header">malo</td>
            <td rowspan="2">{{ use.server_years }} horas</td>
            <td rowspan="2">{{ use.emissions }} gCO2/kWh</td>
          </tr>
          <tr>
            <td>{{ use.component.cfp_build_phase }}</td>
            <td>{{ use.component.cfp_deviation_standard }}</td>
            <td>{{ use.component.best_case }}</td>
            <td>{{ use.component.middle_case }}</td>
            <td>{{ use.component.worst_case }}<br /></td>
          </tr>
        </tbody>
      </table>

      El coste de fabricación implicado al proyecto, viene dado por el coste de
      producción del componente multiplicado por el tiempo de uso dedicado al
      proyecto.

      <div class="equations-box">
        <EquationComponent :show_tex="latex" :formula="use_percentaje_exp" />
        <EquationComponent :show_tex="latex" :formula="build_cost_exp" />

        <EquationComponent :show_tex="latex" :formula="use_percentaje(use)" />
        <EquationComponent
          :show_tex="latex"
          :formula="build_cost(use, 'middle')"
        />
      </div>

      <p style="text-align: justify">
        Para medir el impacto que tiene el tiempo de uso se ha multiplicado el
        consumo eléctrico por el tiempo de uso dedicado al proyecto,
        convirtiéndolo posteriormente en kilos de CO2.
      </p>

      <div class="equations-box">
        <EquationComponent :show_tex="latex" :formula="use_cost_exp" />
        <EquationComponent
          :show_tex="latex"
          :formula="use_cost(use, 'middle')"
        />
      </div>

      <p style="text-align: justify">
        Asumimos que el coste de destrucción es un 1% del coste de las fases
        de fabricación y uso.
      </p>
      <div class="equations-box">
        <EquationComponent :show_tex="latex" :formula="end_life_exp" />
        <EquationComponent
          :show_tex="latex"
          :formula="destruction_cost(use, 'middle')"
        />
      </div>

      <p style="text-align: justify">
        El coste total viene dado por la suma de las emisiones de las tres
        fases.
      </p>

      <div class="equations-box">
        <EquationComponent :show_tex="latex" :formula="total_cost_exp" />
        <EquationComponent
          :show_tex="latex"
          :formula="total_cost(use, 'middle')"
        />
      </div>

      <div style="break-before: page">
        <p style="text-align: justify">
          Estos son los cálculos para el peor caso, en el que el consumo de
          electricidad y el coste de fabricación ha sido más elevado
        </p>

        <div class="equations-box">
          <EquationComponent
            :show_tex="latex"
            :formula="build_cost(use, 'worst')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="use_cost(use, 'worst')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="destruction_cost(use, 'worst')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="total_cost(use, 'worst')"
          />
        </div>

        <p style="text-align: justify">
          Estos son los cálculos para el mejor caso, en el que el consumo de
          electricidad y el coste de fabricación ha sido más bajo.
        </p>

        <div class="equations-box">
          <EquationComponent
            :show_tex="latex"
            :formula="build_cost(use, 'best')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="use_cost(use, 'best')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="destruction_cost(use, 'best')"
          />
          <EquationComponent
            :show_tex="latex"
            :formula="total_cost(use, 'best')"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import EquationComponent from "@/components/report/EquationComponent.vue"

export default {
  name: "ResultDetails",
  props: ["uses", "latex"],
  components: {
    EquationComponent,
  },
  data(){
  return{
    formula: '$$x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}.$$',
    use_percentaje_exp: "\\textbf{Porcentaje de uso} = \\frac{\\text{horas de desarrollo}}{\\text{horas útiles}}\\cdot 100",
    build_cost_exp: "\\textbf{Coste fabricación en el proyecto}=\\text{coste fabricación}\\cdot \\text{porcentaje de uso}",
    use_cost_exp: "\\textbf{Coste de uso}= \\text{consumo} \\cdot  \\text{horas de uso}",
    server_hours_exp: "\\textbf{Total de horas} = 24 \\cdot 365 \\cdot 6 = \\text{52560 horas}",
    build_cost_server_exp: "\\textbf{Coste de fabricación} = \\frac{\\text{emisiones de CO2}}{\\text{aplicaicones alojadas}}\\cdot \\frac{\\text{Años de uso}}{\\text{Años utiles}}",
    consume_server_exp: "\\textbf{Consumo servidor} = \\frac{\\text{consumo} \\cdot \\text{total de horas}}{\\text{aplicaicones alojadas}}",
    consume_network_server: "\\textbf{Consumo red} = \\frac{\\text{Consumo servidor}}{47} \\cdot 3",
    use_cost_server_exp: "\\textbf{Coste de uso} = (\\text{Consumo servidor} + \\text{Consumo red}) \\cdot 2",
    end_life_exp: "\\textbf{Coste destrucción}= (\\text{Coste fabricación en el proyecto} +  \\text{Coste de uso})\\cdot 0.01",
    total_cost_exp: "\\textbf{Coste total} = \\text{Coste de fabricación} + \\text{Coste de uso} + \\text{Coste de destrucción}",
    server_hours: {
      string: "24*365*6",
      number: 24*365*6
    },
    useful_hours: {
      string: "8*5*48*6",
      number: 8*5*48*6,
    },
  }
},
  methods: {
    use_percentaje(use) {
    var equation = "\\textbf{Porcentaje de uso} = \\frac{\\text{" + use.hours +"(h)}}{\\text{" + this.useful_hours.string +"(h)}}\\cdot 100 = "+ use.middle.use_percent;
    return equation
  },
  use_cost(use, case_type) {
    var name = ""
    var consume = use.component[case_type + "_case"];
    var hours = use.hours;
    var use_cost = use[case_type].use_cost;
    var use_cost_co2 = use[case_type].use_cost_co2;

    switch (case_type) {
      case 'middle':
        name = " (caso medio)"
        break;
      case 'worst':
        name = " (peor caso)"
        break;
      case 'best':
        name = " (mejor caso)"
        break;
    }
    var equation =  "\\textbf{Coste de uso "+ name +"}= \\text{"+ consume +"W} \\cdot  \\text{" + hours +"h} = "+ use_cost + "KWh \\Rightarrow " + use_cost_co2 + "KgCo2";
    return equation
  },
  build_cost(use, case_type) {
    var name = ""
    var use_percent = use.middle.use_percent;
    var build_cost = use[case_type].build_cost;
    var cfp_build_phase = null;

    switch (case_type) {
      case 'middle':
        name = " (caso medio)"
        cfp_build_phase = use.component.cfp_build_phase;
        break;
      case 'worst':
        cfp_build_phase = parseFloat(use.component.cfp_build_phase) + parseFloat(use.component.cfp_deviation_standard);
        name = " (peor caso)"
        break;
      case 'best':
        cfp_build_phase = use.component.cfp_build_phase - use.component.cfp_deviation_standard;
        name = " (mejor caso)"
        break;
    }
    var equation = "\\textbf{Coste fabricación en el proyecto "+ name +"}=\\text{"+ cfp_build_phase +"KgCo2}\\cdot \\text{"+ use_percent +"} = "+ build_cost + "KgCo2";
    return equation;
  },
  build_cost_server(use, case_type) {
    var name = ""
    var build_cost = use[case_type].build_cost;
    var cfp_build_phase = use.component.cfp_build_phase;
    var app = use.component.hosted_apps;
    var years = use.server_years;

    switch (case_type) {
      case 'middle':
        name = " (caso medio)"
        break;
      case 'worst':
        name = " (peor caso)"
        break;
      case 'best':
        name = " (mejor caso)"
        break;
    }
    var equation =  "\\textbf{Coste fabricación en el proyecto "+ name +"}=\\frac{\\text{"+cfp_build_phase+"KgCo2}}{"+app+"}\\cdot \\frac{\\text{6 años}}{\\text{"+years+" años}} = " +build_cost+"KgCo2";
    return equation;
  },
  destruction_cost(use, case_type) {
    var build_cost = "";
    var use_cost = "";
    var destroy_cost = "";
    var name = ""
    build_cost = use[case_type].build_cost;
    use_cost = use[case_type].use_cost_co2;
    destroy_cost = use[case_type].destroy_cost;
    switch (case_type) {
      case 'middle':
        name = " (caso medio)"
        break;
      case 'worst':
        name = " (peor caso)"
        break;
      case 'best':
        name = " (mejor caso)"
        break;
    }
    var equation = "\\textbf{Coste destrucción" + name + "}= (\\text{" + build_cost + "KgCo2} +  \\text{"+ use_cost +"KgCo2})\\cdot 0.01 = " + destroy_cost + "KgCo2";
    return equation;
  },
  consume_server(use, case_type) {
    var name = ""
    var consume = use.component.middle_case;
    var app = 12;
    var hours = this.server_hours.number;
    var server_cost = use[case_type].server_cost;
    switch (case_type) {
      case 'middle':
        name = " (caso medio)"
        break;
      case 'worst':
        name = " (peor caso)"
        break;
      case 'best':
        name = " (mejor caso)"
        break;
    }
    var equation = "\\textbf{Consumo servidor"+ name +"} = \\frac{\\text{"+consume+"W} \\cdot \\text{"+hours+"h}}{\\text{"+app+"}} = "+server_cost+"KWh/app";
    return equation;
  },
  consume_network(use, case_type) {
    var name = ""
    var server_cost = use[case_type].server_cost;
    var network_cost = use[case_type].network_cost;
    switch (case_type) {
      case 'middle':
        name = " (caso medio)"
        break;
      case 'worst':
        name = " (peor caso)"
        break;
      case 'best':
        name = " (mejor caso)"
        break;
    }
    var equation = "\\textbf{Consumo red "+name+"} = \\frac{\\text{"+server_cost+"KWh/app}}{47} \\cdot 3 = "+network_cost+"KWh/app";
    return equation;
  },
  use_cost_server(use, case_type) {
    var name = ""
    var server_cost = use[case_type].server_cost;
    var network_cost = use[case_type].network_cost;
    var use_cost = use[case_type].use_cost;
    var use_cost_co2 = use[case_type].use_cost_co2;
    switch (case_type) {
      case 'middle':
        name = " (caso medio)"
        break;
      case 'worst':
        name = " (peor caso)"
        break;
      case 'best':
        name = " (mejor caso)"
        break;
    }
    var equation = "\\textbf{Coste de uso"+name+"} = (\\text{"+server_cost+"KWh/app + "+network_cost+"KWh/app}) \\cdot 2 ="+use_cost+"KWh/app \\Rightarrow"+use_cost_co2+"KgCo2/app" ;
    return equation;
  },
  total_cost(use, case_type){
    var name = ""
    var build = use[case_type].build_cost;
    var use_cost = use[case_type].use_cost;
    var endlife = use[case_type].destroy_cost;
    var total = use[case_type].total;
    switch (case_type) {
      case 'middle':
        name = " (caso medio)"
        break;
      case 'worst':
        name = " (peor caso)"
        break;
      case 'best':
        name = " (mejor caso)"
        break;
    }
    var equation = "\\textbf{Coste total"+name+"} = \\text{"+build+"} + \\text{"+use_cost+"} + \\text{"+endlife+"} = "+total+"KgCo2"
    return equation;
  }
  }

}
</script>

<style></style>
