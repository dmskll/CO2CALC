<template>
  <p>Report page!</p>
  <p>Hello {{ store.user_info.username }}</p>
  FABRICACION
  <div v-katex="use_percentaje_exp"></div>
  <br>
  <div v-katex="build_cost_exp"></div>
  <br>
  USO
  <div v-katex="use_cost_exp"></div>
  FIN DE CICLO DE VIDA
  <div v-katex="end_life_exp"></div>
  <div v-katex="test()"></div>

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
    calculat2e(){
      console.log("hola")
      for (const i in this.uses){
        this.uses[i]["use_percent"] = (this.uses[i].hours / this.useful_hours.number) * 100;
        this.uses[i]["build_cost"] = 2;
      }
    },
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

        this.uses[i] = use;
      }
    },
    test() {
      console.log("test")
      console.log(this.uses)
      return "\\textbf{Coste destrucción}= (\\text{"+ this.uses[0]["build_cost"] +"} +  \\text{"+ this.uses[0]["use_cost"] +"})\\cdot 0.01"
    }
  },
  created(){
    console.log('creado!!!!');
    this.uses = JSON.parse(JSON.stringify(this.store.components_use))
    this.calculate();
  }
}
</script>
