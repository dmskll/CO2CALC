<template>
  <div id="result-element">
    <ResultBoxes :results="results" />
  </div>

  <el-backtop :right="100" :bottom="100" />

  <el-affix
    :offset="40"
    style="text-align: center; margin-bottom: 4em; margin-top: 4em"
  >
    <div class="panel">
      <el-button type="primary" @click="exportToPDF">
        Descargar
        <font-awesome-icon
          style="margin-left: 0.5em"
          icon="fa-regular fa-file-pdf"
          size="lg"
        />
      </el-button>
      <el-switch
        v-model="switch_latex"
        style="margin-left: 24px"
      />
    </div>
  </el-affix>

  <div id="table-print">
    <ResultTables :results="results" :uses="uses"/>
  </div>

  <div id="equation-print">
    <ResultDetails :latex="switch_latex" :uses="uses" />
  </div>
</template>

<script>
import { useComponentsData } from "@/stores/ComponentsData"
// import { PDFDocument } from 'pdf-lib';
// import jsPDF from 'jspdf'
import { font1 } from "@/MathJax/font-math_main"
import { font2 } from "@/MathJax/font-nimbussans"

import LoadingC from "@/components/loadingC.vue"
import { defineAsyncComponent } from 'vue'

import ResultBoxes from "@/components/report/ResultBoxes.vue"

const ResultTables = defineAsyncComponent({
  loader: () => import("@/components/report/ResultTables.vue"),
  loadingComponent: LoadingC,
  delay: 0,
  timeout: 3000
})

const ResultDetails = defineAsyncComponent({
  loader: () => import("@/components/report/ResultDetails.vue"),
  loadingComponent: LoadingC,
  delay: 0,
  timeout: 3000
})



export default {
  name: "ReportView",
  setup(){
    const store = useComponentsData();
    return {
      store: store,
    }
  },
  components:{
    ResultBoxes, ResultTables, ResultDetails
  },
  data(){
    return{

      switch_latex: false,
      uses: [],
      results: {},
      kgCO2_Wh: 259/1000000,
      kgCO2_KWh: 259/1000,
      server_hours: {
        string: "24*365*6",
        number: 24*365*6
      },
      useful_hours: {
        string: "8*5*48*6",
        number: 8*5*48*6,
      },
      font1: font1,
      font2: font2,
    }
  },
  methods: {

    
    
    exportToPDF() {
      import("jspdf").then(({ jsPDF }) => {
        import("pdf-lib").then(({ PDFDocument }) => {
          this.Convert_HTML_To_PDF(jsPDF, PDFDocument)
        }).catch(error => console.log(error));
      }).catch(error => console.log(error));
    },

    async Convert_HTML_To_PDF(jsPDF, PDFDocument) {


      
      var results = new jsPDF();
      var table = new jsPDF();
      var equations = new jsPDF();

      // Source HTMLElement or a string containing HTML.
      var resultsHTML = document.getElementById("result-element");
      var tableHTML = document.getElementById("table-print");
      var equationHTML = document.getElementById("equation-print");

      this.addFonts(results);
      this.addFonts(table);
      this.addFonts(equations);

      results = this.htmlToPDF(results, resultsHTML);
      table = this.htmlToPDF(table, tableHTML);
      equations = this.htmlToPDF(equations, equationHTML);

      this.merge([results, table, equations], PDFDocument)
    },
    htmlToPDF(doc, html){
      return doc.html(html, {
                callback:  function(doc) {
                    // Save the PDF
                    // doc.save();
                    return doc

                },
                margin: [10, 10, 10, 10],
                autoPaging: 'text',
                x: 0,
                y: 0,
                width: 190, //target width in the PDF document
                windowWidth: 675 //window w idth in CSS pixels
            });
    },
    async merge(docs, PDFDocument){
      const pdfDoc =  await PDFDocument.create();
      for (const index in docs){
        var doc_array = await docs[index].output("arraybuffer")
        const firstDoc =  await PDFDocument.load(doc_array); //arrayB from the last step of jspdf above.
        const pages =  await  pdfDoc.copyPages(firstDoc, firstDoc.getPageIndices());
        pages.forEach((page) => pdfDoc.addPage(page));
      }

      const pdfBytes =  await pdfDoc.save("file.pdf");
      let file = new Blob([pdfBytes], { type: 'application/pdf' });
      var fileURL = URL.createObjectURL(file);
      window.open(fileURL);
    },
    addFonts(doc){
      doc.addFileToVFS('mathjax_mainregular-normal.ttf', this.font1);
      doc.addFileToVFS('nimbus.otf', this.font2);

      doc.addFont('mathjax_mainregular-normal.ttf', 'MathJax_Main-Regular', 'normal');
      doc.addFont('mathjax_mainregular-normal.ttf', 'MathJax_Main', 'normal');
      doc.addFont('mathjax_mainregular-normal.ttf', 'MathJax_Math-Italic', 'normal');
      doc.addFont('mathjax_mainregular-normal.ttf', 'MathJax_Main-Bold', 'bold');
      doc.addFont('mathjax_mainregular-normal.ttf', 'MathJax_Size1-Regular', 'normal');


      // doc.addFont('mathjax_mainregular-normal.ttf', 'KaTeX_Main-Bold', 'normal');
      // doc.addFont('mathjax_mainregular-normal.ttf', 'KaTeX_Main-Regular', 'normal');
      // doc.addFont('nimbus.otf', 'Liberation Serif Bold', 'bold');
      // doc.addFont('nimbus.otf', 'Liberation Serif', 'normal');

      doc.setFont("MathJax_Main-Regular");
      doc.setFont("MathJax_Main");
      doc.setFont("MathJax_Math-Italic");
      doc.setFont("MathJax_Main-Bold");
      doc.setFont("MathJax_Size1-Regular");
    },

    getComponent(id, system){
      let component = null
      if (!this.store.user_info.authenticated){
        let type = system ?  "system" : "user"
        component = this.store.components[type].filter((item) => item.id === id);
        return component[0];
      }

      component = this.store.components.system.filter((item) => item.id === id);
      if(component.length == 0)
        component = this.store.components.user.filter((item) => item.id === id)
      return component[0];
    },
    calculate(){
      //this.uses["total"] = {};
      const results = {
        "build_cost": 0,
        "use_cost": 0,
        "use_cost_co2": 0,
        "destroy_cost": 0,
        "total": 0,
      }
      this.results = {
        "middle": JSON.parse(JSON.stringify(results)),
        "worst": JSON.parse(JSON.stringify(results)),
        "best": JSON.parse(JSON.stringify(results)),
      }
      var cases = {
        "middle": {},
        "worst": {},
        "best": {},
      }
      for (const i in this.uses){
        var use = this.uses[i];
        const component = this.getComponent(use.component, use.system_component);
        for (const key in cases){
          use[key] = {};
          if (component.is_server)
            this.serverCalculations(use[key], component, key, use.server_years, use.emissions);
          else
            this.normalCalculations(use[key], component, key, use.hours, use.emissions);
        }

        use["component"] = component;
        this.sum_results(use);
        this.uses[i] = use;

      }
    },
    round(x){
      return parseFloat((x).toFixed(2))
    },
    powerByCase(key, component){
      switch(key){
        case 'middle':
          return component.middle_case;
        case 'worst':
          return component.worst_case;
        case 'best':
          return component.best_case
      }
    },
    deviationByCase(key){
      switch(key){
        case 'middle':
          return 0;
        case 'worst':
          return 1;
        case 'best':
          return -1;
      }
    },
    serverCalculations(use, component, key, years, emissions){

      const power = this.powerByCase(key, component);
      const deviation = component.cfp_deviation_standard * this.deviationByCase(key)

      use["build_cost"] = this.round(((component.cfp_build_phase + deviation)/ component.hosted_apps) * (years / 6));
       //multiplicamos los años por als horas teniendo en cuenta los años bisiestos
      use["server_cost"] = this.round(((power/1000) * years * 8766) / component.hosted_apps);
      use["network_cost"] = this.round((use["server_cost"] / 47) * 3);
      use["direct_cost"] = use["server_cost"] + use["network_cost"];
      use["use_cost"] = this.round(use["direct_cost"] * 2);
      use["use_cost_co2"] = this.round(use["use_cost"] * emissions/1000);

      var destroy_cost = (use["use_cost_co2"] + use["build_cost"]) * 0.01;
      use["destroy_cost"] = this.round(destroy_cost);
      use["total"] = this.round(use["destroy_cost"] + use["use_cost_co2"] + use["build_cost"]);

    },
    normalCalculations(use, component, key, hours, emissions){

      const power = this.powerByCase(key, component);
      const deviation = component.cfp_deviation_standard * this.deviationByCase(key)

      use["use_percent"] = this.round((hours / this.useful_hours.number)*100);

      use["build_cost"] = this.round((component.cfp_build_phase + deviation) * use["use_percent"]/100);
      use["use_cost"] = this.round((power * hours)/1000);
      use["use_cost_co2"] = this.round(use["use_cost"] * emissions/1000);

      var destroy_cost = (use["use_cost_co2"] + use["build_cost"]) * 0.01;
      use["destroy_cost"] = this.round(destroy_cost);
      use["total"] = this.round(use["destroy_cost"] + use["use_cost_co2"] + use["build_cost"]);

    },
    sum_results(use){
      for (var i in this.results){
        if (Object.prototype.hasOwnProperty.call(this.results, i)) {
          for (var j in this.results[i]){
            this.results[i][j] += use[i][j];
            this.results[i][j] = this.round(this.results[i][j])
          }
        }
      }
    },
    mathDisplay(s){
      return "$$"+s+"$$"
    },

  },
  created(){
    console.log('creado!!!!');
    this.uses = JSON.parse(JSON.stringify(this.store.components_use))
    console.log(this.store.components_use);
    this.calculate();
  },
  mounted() {

  }
}
</script>

<style>
table {
  font-family: arial, sans-serif;
  font-size: 80%;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 3em;
}

.panel {
  width: auto;
  margin-left: 10em;
  margin-right: 10em;
  height: 2em;
  padding: 15px;
  background-color: #bff1da;
  border-radius: 15px;
}
.component-table {
  font-family: arial, sans-serif;
  font-size: 80%;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
}

.component-table tr:first-child {
  background-color: #bff1daae !important;
}

.component-table .sub-header {
  background-color: #bff1da4d !important;
}

.component {
  font-size: 80%;
}

table .case {
  font-size: 80%;
}

th {
  border: 1px solid #dddddd;
  text-align: center;
  padding: 1px;
}

.color-row:nth-child(even) {
  background-color: rgb(120, 120, 120, 0.3);
}
/* Define los estilos para las columnas impares */
.resume td:first-child {
  background-color: rgba(253, 253, 253, 0.9) !important;
}

/* Define los estilos para las columnas impares */
.resume td:nth-child(3n-1) {
  background-color: rgba(238, 255, 241, 0.8);
}

/* Cambia el color de las columnas en el medio a amarillo */
.resume td:nth-child(3n) {
  background-color: rgba(255, 247, 239, 0.837);
}

/* Define los estilos para las columnas pares */
.resume td:nth-child(3n + 1) {
  background-color: rgba(255, 239, 239, 0.796);
}

td {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
.total {
  border: 2px solid #343333;
  text-align: left;
  padding: 8px;
}

/* tr:nth-child(even) {
  background-color: #dddddd;
} */

.result-box {
  font-family: arial, sans-serif;
  border-radius: 15px;

  background-color: #7cd4ac;
  padding: 20px;
  padding-top: 5px;
  text-align: left;
  color: rgb(9, 9, 9);
}

.compare-box {
  font-family: arial, sans-serif;
  border-radius: 15px;
  border: solid 4px;
  border-color: #7cd4ac;
  margin-top: 20px;
  padding: 20px;
  padding-top: 5px;
  text-align: left;
  color: rgb(9, 9, 9);
}

.result-box h1 {
  color: rgb(255, 255, 255);
}

.result-box span {
  /* font-size: 1.2em;
  color: rgb(255, 255, 255); */
}

.equations-box {
  text-align: left !important;
  border-radius: 10px;
  border: 1px solid #000;
  padding: 0.4em;
  padding-left: 1.2em;
  line-height: 1.6em;
}

.tabla-contenedor {
  display: flex;
  justify-content: space-between;
  padding-left: 0.5em;
  padding-right: 0.5em;
}
.result-box h1 {
  text-align: center;
}
</style>
