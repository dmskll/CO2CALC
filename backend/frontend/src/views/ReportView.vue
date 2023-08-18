<template>
  <p>Report page!</p>
  <p>Hello {{ store.user_info.username }}</p>
  <div v-for=" (use) in uses" :key="use.pk" style="margin-bottom: 50px">
    <h1>{{ use.component.name }}</h1>
    <h3>FABRICACION</h3>
    <div v-katex="use_percentaje_exp"></div>
    <div v-katex="build_cost_exp"></div>

    <div v-katex="use_percentaje(use)"></div>

    <div v-katex="build_cost(use, 'middle')"></div>
    <div v-katex="build_cost(use, 'worst')"></div>
    <div v-katex="build_cost(use, 'best')"></div>

    <h3>USO</h3>
    <div v-katex="use_cost_exp"></div>

    <h3>FIN DE CICLO DE VIDA</h3>
    <div v-katex="end_life_exp"></div>
    <div v-katex="destruction_cost(use, 'middle')"></div>
    <div v-katex="destruction_cost(use, 'worst')"></div>
    <div v-katex="destruction_cost(use, 'best')"></div>
  </div>


</template>

<script>
import { useComponentsData } from "@/stores/ComponentsData"

export default {
  name: "ReportView",
  setup(){
    const store = useComponentsData();
    return {
      store: store,
    }
  },
  data(){
    return{
      use_percentaje_exp: "\\textbf{Porcentaje de uso} = \\frac{\\text{horas de desarrollo}}{\\text{horas útiles}}\\cdot 100",
      build_cost_exp: "\\textbf{Coste fabricacion en el proyecto}=\\text{coste fabricación}\\cdot \\text{porcentaje de uso}",
      use_cost_exp: "\\textbf{Coste de uso}= \\text{consumo} \\cdot  \\text{horas de uso}",
      end_life_exp: "\\textbf{Coste destrucción}= (\\text{Coste fabricacion en el proyecto} +  \\text{Coste de uso})\\cdot 0.01",

      uses: [],
      useful_hours: {
                      string: "8*5*48*6",
                      number: 8*5*48*6,
                    },
    }
  },
  methods: {
    getComponent(id){
      let component = this.store.components.system.filter((item) => item.id === id);
      
      if(typeof component[0] === 'undefined'){
        component = this.store.components.user.filter((item) => item.id === id)
      }
      return component[0];
    },
    calculate(){
      for (const i in this.uses){
        var use = this.uses[i];
        console.log(i)
        const component = this.getComponent(use.component)
        var use_percent = ((use.hours / this.useful_hours.number) * 100).toFixed(2);
        use["use_percent"] = parseFloat(use_percent)

        use["build_cost"] = component.cfp_build_phase * use["use_percent"];
        use["use_cost"] = component.middle_case * use.hours;
        var destroy_cost = (use["use_cost"] + use["build_cost"]) * 0.01;
        use["destroy_cost"] = parseFloat(destroy_cost.toFixed(2));
        use["total"] = use["destroy_cost"] + use["use_cost"] + use["build_cost"];

        console.log("(" + component.cfp_build_phase + " + " + component.cfp_deviation_standard + ") * " + use["use_percent"])
        use["build_cost_wc"] = (component.cfp_build_phase - (component.cfp_deviation_standard * -1))* use["use_percent"];
        console.log( use["build_cost_wc"])
        use["use_cost_wc"] = component.worse_case * use.hours;
        var destroy_cost_wc = (use["use_cost_wc"] + use["build_cost_wc"]) * 0.01;
        use["destroy_cost_wc"] = parseFloat(destroy_cost_wc.toFixed(2));
        use["total_wc"] = use["destroy_cost_wc"] + use["use_cost_wc"] + use["build_cost_wc"];

        console.log(component.cfp_deviation_standard)
        use["build_cost_bc"] = (component.cfp_build_phase - component.cfp_deviation_standard)* use["use_percent"];
        use["use_cost_bc"] = component.best_case * use.hours;
        var destroy_cost_bc = (use["use_cost_bc"] + use["build_cost_bc"]) * 0.01;
        use["destroy_cost_bc"] = parseFloat(destroy_cost_bc.toFixed(2));
        use["total_bc"] = use["destroy_cost_bc"] + use["use_cost_bc"] + use["build_cost_bc"];        

        use["component"] = component;
        this.uses[i] = use;
      }
    },
    use_percentaje(use) {
      return "\\textbf{Porcentaje de uso} = \\frac{\\text{" + use.hours +"}}{\\text{" + this.useful_hours.string +"}}\\cdot 100 = "+ use.use_percent;
    },
    build_cost(use, case_type) {
      var cfp_build_phase = "";
      var use_percent = "";
      var build_cost = "";
      var name = ""


      use_percent = use.use_percent;
      switch (case_type) {
        case 'middle':
          name = " (caso medio)"
          cfp_build_phase = use.component.cfp_build_phase;
          build_cost = use.build_cost;
          break;
        case 'worst':
          name = " (peor caso)"
          cfp_build_phase = use.component.cfp_build_phase + use.component.cfp_deviation_standard;
          build_cost = use.build_cost_wc;
          break;
        case 'best':
          name = " (mejor caso)"
          cfp_build_phase = use.component.cfp_build_phase - use.component.cfp_deviation_standard;
          build_cost = use.build_cost_bc;
          break;
      }
      return "\\textbf{Coste fabricacion en el proyecto "+ name +"}=\\text{"+ cfp_build_phase +"}\\cdot \\text{"+ use_percent +"} = "+ build_cost;
    },
    destruction_cost(use, case_type) {
      var build_cost = "";
      var use_cost = "";
      var destroy_cost = "";
      var name = ""
      switch (case_type) {
        case 'middle':
          name = " (caso medio)"
          build_cost = use.build_cost;
          use_cost = use.use_cost;
          destroy_cost = use.destroy_cost;
          break;
        case 'worst':
          name = " (peor caso)"
          build_cost = use.build_cost_wc;
          use_cost = use.use_cost_wc;
          destroy_cost = use.destroy_cost_wc;
          break;
        case 'best':
          name = " (mejor caso)"
          build_cost = use.build_cost_bc;
          use_cost = use.use_cost_bc;
          destroy_cost = use.destroy_cost_bc;
          break;
      }
      return "\\textbf{Coste destrucción" + name + "}= (\\text{" + build_cost + "} +  \\text{"+ use_cost +"})\\cdot 0.01 = " + destroy_cost;
    }
  },
  created(){
    console.log('creado!!!!');
    this.uses = JSON.parse(JSON.stringify(this.store.components_use))
    this.calculate();
  }
}
</script>
