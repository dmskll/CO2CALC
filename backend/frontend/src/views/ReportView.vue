<template>
  <p>Report page!</p>
  <button @click="savePDF">Export to PDF</button>
  <button @click="savePDF">Export to PDF</button>
  <button @click="savePDF">Export to PDF</button>

  <div id="element-to-print">
  <img src="https://d27jswm5an3efw.cloudfront.net/app/uploads/2019/07/insert-image-html-3.jpg" style="width: 30%;">

  <table>
  <thead>
    <tr>
      <th  rowspan="3">componete</th>
      <th  colspan="9">fases</th>
      <th  colspan="3" rowspan="2">total</th>
    </tr>
    <tr>
      <th  colspan="3">fabricación</th>
      <th  colspan="3">uso</th>
      <th  colspan="3">destrucción<br></th>
    </tr>
    <tr>
      <th>▼</th>
      <th>▬</th>
      <th>▲</th>
      <th>▼</th>
      <th>▬</th>
      <th>▲</th>
      <th>▼</th>
      <th>▬</th>
      <th>▲</th>
      <th>▼</th>
      <th>▬</th>
      <th>▲</th>
    </tr>
  </thead>
  <tbody>
    <!-- <div v-for=" (use) in uses" :key="use.pk">
      <tr>
        <td>{{ use.component.name }} </td>

        <td>{{ use.build_cost_bc }}<br></td>
        <td>{{ use.build_cost }}</td>
        <td>{{ use.build_cost_wc }}</td>
        
        <td>{{ use.use_cost_co2_bc }}</td>
        <td>{{ use.use_cost_co2 }}</td>
        <td>{{ use.use_cost_co2_wc }}</td>
        
        <td>{{ use.total_bc }}</td>
        <td>{{ use.total }}</td>
        <td>{{ use.total_wc }}<br></td>
      </tr>
    </div> -->
    <tr v-for=" (use) in uses" :key="use.pk">
      <td>{{ use.component.name }} </td>

      <td>{{ use.build_cost_bc }}<br></td>
      <td>{{ use.build_cost }}</td>
      <td>{{ use.build_cost_wc }}</td>

      <td>{{ use.use_cost_co2_bc }}</td>
      <td>{{ use.use_cost_co2 }}</td>
      <td>{{ use.use_cost_co2_wc }}</td>

      <td>{{ use.destroy_cost_wc }}</td>
      <td>{{ use.destroy_cost }}</td>
      <td>{{ use.destroy_cost_wc }}</td>

      <td>{{ use.total_bc }}</td>
      <td>{{ use.total }}</td>
      <td>{{ use.total_wc }}<br></td>
    </tr>
    
    <tr>
      <td>total</td>
      <td><br></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td><br></td>
    </tr>

  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th  rowspan="2">componete</th>
      <th  colspan="3">fases</th>
      <th  rowspan="2">total</th>
    </tr>
    <tr>
      <th>fabricación</th>
      <th>uso</th>
      <th>destrucción<br></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>componete1</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <td>componete2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>6</td>
    </tr>

  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th  rowspan="3">componete</th>
      <th  colspan="6">fases</th>
      <th  colspan="2" rowspan="2">total</th>
    </tr>
    <tr>
      <th  colspan="2">fabricación</th>
      <th  colspan="2">uso</th>
      <th  colspan="2">destrucción<br></th>
    </tr>
    <tr>
      <th>bueno</th>
      <th>malo</th>
      <th>bueno</th>
      <th>malo</th>
      <th>bueno</th>
      <th>malo</th>
      <th>bueno</th>
      <th>malo</th>
    </tr>
  </thead>
  <tbody>
    <tr>

      <td>componete1</td>
      <td>1<br></td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>9<br></td>
    </tr>
    <tr>
      <td>componete2</td>
      <td>1<br></td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>9<br></td>
    </tr>

  </tbody>
</table>
  
  <p>Hello {{ store.user_info.username }}</p>
  <div class="html2pdf__page-break"></div>

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
    <div v-katex="use_cost(use, 'middle')"></div>
    <div v-katex="use_cost(use, 'worst')"></div>
    <div v-katex="use_cost(use, 'best')"></div>

    <h3>FIN DE CICLO DE VIDA</h3>
    <div v-katex="end_life_exp"></div>
    <div v-katex="destruction_cost(use, 'middle')"></div>
    <div v-katex="destruction_cost(use, 'worst')"></div>
    <div v-katex="destruction_cost(use, 'best')"></div>
    <div class="html2pdf__page-break"></div>
  </div>
  </div>

</template>

<script>
import { useComponentsData } from "@/stores/ComponentsData"
import html2pdf from "html2pdf.js";

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
      kgCO2_Wh: 259/1000000,
      useful_hours: {
                      string: "8*5*48*6",
                      number: 8*5*48*6,
                    },
    }
  },
  methods: {
    savePDF() {
      console.log("que está pasando")
      var opt = {
        margin:       1,
        filename:     'myfile.pdf',
        image:        { type: 'html', quality: 0.98 },
        html2canvas:  { scale: 1, useCORS: true  },
        jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
      };
      var element = document.getElementById('element-to-print');
      console.log(element)
      html2pdf().set(opt).from(element).save();
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
        var use_percent = parseFloat(((use.hours / this.useful_hours.number)).toFixed(2));
        use["use_percent"] = parseFloat(use_percent)

        use["build_cost"] = component.cfp_build_phase * use["use_percent"];
        use["use_cost"] = component.middle_case * use.hours;
        use["use_cost_co2"] = parseFloat((use["use_cost"] * this.kgCO2_Wh).toFixed(2));

        var destroy_cost = (use["use_cost_co2"] + use["build_cost"]) * 0.01;
        use["destroy_cost"] = parseFloat(destroy_cost.toFixed(2));
        use["total"] = parseFloat((use["destroy_cost"] + use["use_cost_co2"] + use["build_cost"]).toFixed(2));

        console.log("(" + component.cfp_build_phase + " + " + component.cfp_deviation_standard + ") * " + use["use_percent"])
        use["build_cost_wc"] = (parseFloat(component.cfp_build_phase) + parseFloat(component.cfp_deviation_standard))* use["use_percent"];
        console.log( use["build_cost_wc"])
        use["use_cost_wc"] = component.worse_case * use.hours;
        use["use_cost_co2_wc"] = parseFloat((use["use_cost_wc"] * this.kgCO2_Wh).toFixed(2));

        var destroy_cost_wc = (use["use_cost_co2_wc"] + use["build_cost_wc"]) * 0.01;
        use["destroy_cost_wc"] = parseFloat(destroy_cost_wc.toFixed(2));
        use["total_wc"] =  parseFloat((use["destroy_cost_wc"] + use["use_cost_co2_wc"] + use["build_cost_wc"]).toFixed(2));

        console.log(component.cfp_deviation_standard)
        use["build_cost_bc"] = (component.cfp_build_phase - component.cfp_deviation_standard)* use["use_percent"];
        use["use_cost_bc"] = component.best_case * use.hours;
        use["use_cost_co2_bc"] = parseFloat((use["use_cost_bc"] * this.kgCO2_Wh).toFixed(2));


        var destroy_cost_bc = (use["use_cost_co2_bc"] + use["build_cost_bc"]) * 0.01;
        use["destroy_cost_bc"] = parseFloat(destroy_cost_bc.toFixed(2));
        use["total_bc"] = use["destroy_cost_bc"] + use["use_cost_co2_bc"] + use["build_cost_bc"];        

        use["component"] = component;
        this.uses[i] = use;
      }
    },
    use_percentaje(use) {
      return "\\textbf{Porcentaje de uso} = \\frac{\\text{" + use.hours +"(h)}}{\\text{" + this.useful_hours.string +"(h)}}\\cdot 100 = "+ use.use_percent;
    },
    use_cost(use, case_type) {
      var consume = "";
      var hours = "";
      var use_cost = "";
      var name = ""
      var use_cost_co2 = "";
      switch (case_type) {
        case 'middle':
          name = " (caso medio)"
          consume = use.component.middle_case;
          hours = use.hours;
          use_cost = use.use_cost;
          use_cost_co2 = use.use_cost_co2;
          break;
        case 'worst':
          name = " (peor caso)"
          consume = use.component.worse_case;
          hours = use.hours;
          use_cost = use.use_cost_wc;
          use_cost_co2 = use.use_cost_co2_wc;
          break;
        case 'best':
          name = " (mejor caso)"
          consume = use.component.best_case;
          hours = use.hours;
          use_cost = use.use_cost_bc;
          use_cost_co2 = use.use_cost_co2_bc;
          break;
      }
      return "\\textbf{Coste de uso "+ name +"}= \\text{"+ consume +"W} \\cdot  \\text{" + hours +"h} = "+ use_cost + "Wh --> " + use_cost_co2 + "KgCo2";
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
          cfp_build_phase = parseFloat(use.component.cfp_build_phase) + parseFloat(use.component.cfp_deviation_standard);
          build_cost = use.build_cost_wc;
          break;
        case 'best':
          name = " (mejor caso)"
          cfp_build_phase = use.component.cfp_build_phase - use.component.cfp_deviation_standard;
          build_cost = use.build_cost_bc;
          break;
      }
      return "\\textbf{Coste fabricacion en el proyecto "+ name +"}=\\text{"+ cfp_build_phase +"KgCo2}\\cdot \\text{"+ use_percent +"} = "+ build_cost + "KgCo2";
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
          use_cost = use.use_cost_co2;
          destroy_cost = use.destroy_cost;
          break;
        case 'worst':
          name = " (peor caso)"
          build_cost = use.build_cost_wc;
          use_cost = use.use_cost_co2_wc;
          destroy_cost = use.destroy_cost_wc;
          break;
        case 'best':
          name = " (mejor caso)"
          build_cost = use.build_cost_bc;
          use_cost = use.use_cost_co2_bc;
          destroy_cost = use.destroy_cost_bc;
          break;
      }
      return "\\textbf{Coste destrucción" + name + "}= (\\text{" + build_cost + "KgCo2} +  \\text{"+ use_cost +"KgCo2})\\cdot 0.01 = " + destroy_cost + "KgCo2";
    }
  },
  created(){
    console.log('creado!!!!');
    this.uses = JSON.parse(JSON.stringify(this.store.components_use))
    this.calculate();
  }
}
</script>

<style>
table {
  font-family: arial, sans-serif;
  font-size:80%;
  border-collapse: collapse;
  width: 20%;
  
}

th {
  border: 1px solid #dddddd;
  text-align: center;
  padding: 1px;
}

td {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

/* tr:nth-child(even) {
  background-color: #dddddd;
} */


</style>
