<template>
  <div id="result-element">  
  <div class="result-box">
    <h3>
      La estimación de emisiones de Co2 asociada proyecto en un caso medio es de: 
      <h1>
        {{ total_results.middle.total }} KgCo2
      </h1>
    </h3>
    Dependiendo de la intensidad del uso y de como se ha fabricado cada componente
    las emisiones pueden variar. En el mejor caso donde se ha emitido lo menos posible 
    y el uso de los componentes ha sido menos intensivo se estima una emisón de 
    {{ total_results.best.total }} KgCo2. En el peor de los casos se estima que las
    emisiones podrian llegar hasta {{ total_results.worst.total }} KgCo2. 
    
  </div>
  <br>
  <div class="result-box">
    <h3>
      El consumo electrico estimado es de: 
      <h1>
        {{ total_results.middle.use_cost }} kWh
      </h1>
    </h3>
    Dependiendo de la intensidad del uso el consumo puede variar. En el mejor caso donde 
    el uso de los componentes ha sido menos intensivo se estima un consumo de 
    {{ total_results.best.use_cost }} kWh. En el peor de los casos se estima que el
    consumo podria llegar hasta {{ total_results.worst.use_cost }} kWh. 
    
  </div>
  <div class="compare-box">
    <h3>
      {{ total_results.middle.total }} KgCo2 equivalen a:
    </h3>
    
    <ul>
      <li>{{  (total_results.middle.total / compare.beef).toFixed(0) }} hamburguesas de ternera</li>
      <li>{{  (total_results.middle.total / compare.beyond).toFixed(0) }}  hamburguesas de imitación vegetal</li>
      <br>
      <li>{{ (total_results.middle.total / compare.train_km).toFixed(1) }} viajes Barcelona-Madrid en AVE por pasajero</li>
      <li>{{  (total_results.middle.total / compare.plain_km).toFixed(1) }} viajes Barcelon-Madrid en avión por pasajero</li>
    </ul> 
    <p style="font-size: 0.4em;">
      <ul>
        <li>//https://css.umich.edu/publications/research-publications/beyond-meats-beyond-burger-life-cycle-assessment-detailed</li>
        <li>https://www.ecologistasenaccion.org/134774/la-aviacion-tiene-los-dias-contados/</li>
      </ul> 
    </p>
  </div>
  </div>
  <br><br>
  <el-backtop :right="100" :bottom="100" />
  <el-affix :offset="40" style="text-align: center;">
    <div class="panel">
      <el-button type="primary" @click="Convert_HTML_To_PDF">
        Descargar
        <font-awesome-icon style="margin-left: 0.5em;" icon="fa-regular fa-file-pdf" size="lg"/>
      </el-button>
      <el-switch
      v-model="switch_latex"
      class="mt-2"
      style="margin-left: 24px"
      inline-prompt
      />
    </div>
  </el-affix>
  <br><br>
  <div id="table-print">
  <table class="resume">
    <caption style="caption-side:bottom">
    Resumen de las emisiones (KgCo2) de las fases de vida de los componentes para el caso bueno, medio y optimo.
  </caption>
    <thead>
    <tr>
      <th  rowspan="3">Componente</th>
      <th  colspan="9">Fases</th>
      <th  colspan="3" rowspan="3">Total</th>
    </tr>
    <tr>
      <th  colspan="3">Fabricación</th>
      <th  colspan="3">Uso</th>
      <th  colspan="3">Destrucción<br></th>
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
      <td class="component">{{ use.component.name }} </td>

      <td>{{ use.best.build_cost }}<br></td>
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
      <td>{{ use.worst.total }}<br></td>
    </tr>
    
    <tr class="total">
      <td>Total (KgCo2)</td>
      <td>{{ total_results.best.build_cost }}<br></td>
      <td>{{ total_results.middle.build_cost }}</td>
      <td>{{ total_results.worst.build_cost }}</td>
      <td>{{ total_results.best.use_cost_co2 }}<br></td>
      <td>{{ total_results.middle.use_cost_co2 }}</td>
      <td>{{ total_results.worst.use_cost_co2 }}</td>
      <td>{{ total_results.best.destroy_cost }}</td>
      <td>{{ total_results.middle.destroy_cost }}</td>
      <td>{{ total_results.worst.destroy_cost }}</td>
      <td>{{ total_results.best.total }}<br></td>
      <td>{{ total_results.middle.total }}</td>
      <td>{{ total_results.worst.total }}<br></td>
    </tr>

  </tbody>
</table>
<table class="resume">
  <caption style="caption-side:bottom">
    Resumen del consumo electrico (kWh) durante el uso de los componentes para el caso bueno, medio y pesimo.
  </caption>
  <thead>
    <tr>
      <th  rowspan="2">Componente</th>
      <th  colspan="3">Consumo electrico fase uso</th>
    </tr>
    
    <tr>
      <th>mejor</th>
      <th>medio</th>
      <th>peor</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for=" (use) in uses" :key="use.pk">
      <td class="component">{{ use.component.name }} </td>


      <td>{{ use.best.use_cost }}</td>
      <td>{{ use.middle.use_cost }}</td>
      <td>{{ use.worst.use_cost }}</td>

    </tr>
    
    <tr class="total">
      <td>Total (kWh)</td>
      <td>{{ total_results.best.use_cost }}<br></td>
      <td>{{ total_results.middle.use_cost }}</td>
      <td>{{ total_results.worst.use_cost }}</td>
    </tr>

  </tbody>
</table>
<!-- <div class="tabla-contenedor">
  
  <table>
    <caption style="caption-side:bottom">
      Resumen de emisiones de KgCo2 de cada componente durante sus diferentes fases para el caso medio.
    </caption>
    <thead>
      <tr>
        <th rowspan="2">Componente</th>
        <th colspan="3">Fases</th>
        <th rowspan="2">Total</th>
      </tr>
      <tr>
        <th>Fabricación</th>
        <th>Uso</th>
        <th>Destrucción<br></th>
      </tr>
    </thead>
    <tbody>
      <tr v-for=" (use) in uses" :key="use.pk">
        <td class="component">{{ use.component.name }} </td>
        
        <td>{{ use.middle.build_cost }}</td>
  
        <td>{{ use.middle.use_cost_co2 }}</td>
        
        <td>{{ use.middle.destroy_cost }}</td>
        
        <td>{{ use.middle.total }}</td>
      </tr>
      
      <tr class="total">
        <td><b>Total (KgCo2)</b></td>
        <td>{{ total_results.middle.build_cost }}</td>
        <td>{{ total_results.middle.use_cost_co2 }}</td>
        <td>{{ total_results.middle.destroy_cost }}</td>
        <td>{{ total_results.middle.total }}</td>
      </tr>
  
    </tbody>
  </table>


</div>
<br><br>

<table>
  <caption style="caption-side:bottom">
    Resumen de emisiones (KgCo2) de cada componente durante sus diferentes fases, para el peor caso
    (▲) y el mejor caso (▼)
  </caption>
  <thead>
    <tr>
      <th  rowspan="3">Componente</th>
      <th  colspan="6">Fases</th>
      <th  colspan="2" rowspan="2">Total</th>
    </tr>
    <tr>
      <th  colspan="2">Fabricación</th>
      <th  colspan="2">Uso</th>
      <th  colspan="2">Destrucción<br></th>
    </tr>
    <tr>
      <th></th>
      <th>▲</th>
      <th>▼</th>
      <th>▲</th>
      <th>▼</th>
      <th>▲</th>
      <th>▼</th>
      <th>▲</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for=" (use) in uses" :key="use.pk">
      <td class="component">{{ use.component.name }} </td>

      <td>{{ use.best.build_cost }}<br></td>
      <td>{{ use.worst.build_cost }}</td>

      <td>{{ use.best.use_cost_co2 }}</td>
      <td>{{ use.worst.use_cost_co2 }}</td>

      <td>{{ use.best.destroy_cost }}</td>
      <td>{{ use.worst.destroy_cost }}</td>
      
      <td>{{ use.best.total }}</td>
      <td>{{ use.worst.total }}<br></td>
    </tr>
    
    <tr class="total">
      <td>Total (KgCo2)</td>
      <td>{{ total_results.best.build_cost }}<br></td>
      <td>{{ total_results.worst.build_cost }}</td>
      <td>{{ total_results.best.use_cost_co2 }}<br></td>
      <td>{{ total_results.worst.use_cost_co2 }}</td>
      <td>{{ total_results.best.destroy_cost }}</td>
      <td>{{ total_results.worst.destroy_cost }}</td>
      <td>{{ total_results.best.total }}<br></td>
      <td>{{ total_results.worst.total }}<br></td>
    </tr>
    
  </tbody>
</table> -->


<!-- </div>
<div > -->
</div>

<div id="equation-print" >
<div v-for=" (use) in uses" :key="use.pk" style="margin-bottom: 50px; text-align: left; font-size: medium; break-before: page;">
  <div v-if="use.component.is_server"> 
      <h1>{{ use.component.name }} (Server)</h1>
      
      
      
<table class="component-table">
  <tbody>
    <tr>
      <td style="width: 80%;">Descripción</td>
      <td colspan="2">Fabricación (kgCo2)</td>
      <td colspan="3">Casos de uso (W)<br></td>
      <td>Tiempo de uso<br></td>
      <td>Aplicaciones alojadas<br></td>
      <td>mix eléctrico<br></td>
      
    </tr>
    <tr>
      <td rowspan="2">{{ use.component.description }}</td>
      <td class="sub-header">emisiones</td>
      <td class="sub-header">Desviacón</td>
      <td class="sub-header">bueno</td>
      <td class="sub-header">medio</td>
      <td class="sub-header">malo</td>
      <td rowspan="2">{{ use.server_years }} años</td>
      <td rowspan="2">{{ use.component.hosted_apps }}</td>
      <td rowspan="2">{{ use.emissions }} gCO2/kWh</td>
    </tr>
    <tr>
      <td >{{ use.component.cfp_build_phase }}</td>
      <td >{{ use.component.cfp_deviation_standard }}</td>
      <td>{{ use.component.best_case }}</td>
      <td>{{ use.component.middle_case }}</td>
      <td>{{ use.component.worst_case }}<br></td>
    </tr>
  </tbody>
</table>
<p style="text-align: justify;">
        El coste de fabricación viene calculado por el coste de producción del server dividido por 
        el numero de aplicaciones que podria alojar sin que el rendimiento se viera excesivamente afectado.
      </p>
      
      <div class="equations-box">
        <EquationComponent :show_tex="switch_latex" :formula="server_hours_exp" />
        <EquationComponent :show_tex="switch_latex" :formula="build_cost_server_exp" />

        <EquationComponent :show_tex="switch_latex" :formula="build_cost_server(use, 'middle')" />
      </div>

      <p style="text-align: justify;">
        El coste de uso viene dado por dos partes según el consumo del servidor, teniendo en cuenta 
        los gastos que equivalen que el servidor esté alojado en un CPD.
        El directo (50%) es el consumo electrico de la maquina (47%) más la red (3%), el coste indirecto (50%) es el que representa el 
        sobreconsumo que tiene el servidor en el centro de datos (costes de refrigeración (37%), distribución 
        de la energia (10%), iluminación (3%) y distribución de la energia (10%)). 
        <br><br>
        De esta forma primero calcularemos el coste directo del consumo de la aplicación en el servidor y 
        lo multiplicaremos por dos para tener en cuenta el coste indirecto.
      </p>

      <div class="equations-box">
        <EquationComponent :show_tex="switch_latex" :formula="consume_server_exp" />
        <EquationComponent :show_tex="switch_latex" :formula="consume_server(use, 'middle')" />

        <EquationComponent :show_tex="switch_latex" :formula="consume_network_server" />
        <EquationComponent :show_tex="switch_latex" :formula="consume_network(use, 'middle')" />

        <EquationComponent :show_tex="switch_latex" :formula="use_cost_server_exp" />
        <EquationComponent :show_tex="switch_latex" :formula="use_cost_server(use, 'middle')" />

      </div>
      
      <div style="break-before: page;">
        
      <p style="text-align: justify;">
        Asumimos que el coste de destrucción es un 1% del coste de las fases de fabricación y uso.					
      </p>

      <div class="equations-box">
        <EquationComponent :show_tex="switch_latex" :formula="end_life_exp" />
        <EquationComponent :show_tex="switch_latex" :formula="destruction_cost(use, 'middle')" />
      </div>
      
      <p style="text-align: justify;">
        El coste total viene dado por la suma de las emisiones de las tres fases.					
      </p>

      <div class="equations-box">
        <EquationComponent :show_tex="switch_latex" :formula="total_cost_exp" />
        <EquationComponent :show_tex="switch_latex" :formula="total_cost(use, 'middle')" />
      </div>


      <p style="text-align: justify;">
        Estos son los calculos para el peor caso, en el que el consumo de electricidad
        y el coste de fabricación ha sido más elevado					
        </p>
        
        <div class="equations-box">
          <EquationComponent :show_tex="switch_latex" :formula="build_cost_server(use, 'worst')" />
          <EquationComponent :show_tex="switch_latex" :formula="consume_server(use, 'worst')" />
          <EquationComponent :show_tex="switch_latex" :formula="consume_network(use, 'worst')" />
          <EquationComponent :show_tex="switch_latex" :formula="use_cost_server(use, 'worst')" />
          <EquationComponent :show_tex="switch_latex" :formula="destruction_cost(use, 'worst')" />
          <EquationComponent :show_tex="switch_latex" :formula="total_cost(use, 'worst')" />
        </div>
        
        
        <p style="text-align: justify;">
        Estos son los calculos para el mejor caso, en el que el consumo de electricidad
        y el coste de fabricación ha más bajo.  					
      </p>

      <div class="equations-box">
        <EquationComponent :show_tex="switch_latex" :formula="build_cost_server(use, 'best')" />
        <EquationComponent :show_tex="switch_latex" :formula="consume_server(use, 'best')" />
        <EquationComponent :show_tex="switch_latex" :formula="consume_network(use, 'best')" />
        <EquationComponent :show_tex="switch_latex" :formula="use_cost_server(use, 'best')" />
        <EquationComponent :show_tex="switch_latex" :formula="destruction_cost(use, 'best')" />
        <EquationComponent :show_tex="switch_latex" :formula="total_cost(use, 'best')" />
      </div>
    </div>
      
  </div>
    <div v-else>
      <h1>{{ use.component.name }}</h1>

      <table class="component-table">
  <tbody>
    <tr>
      <td style="width: 80%;">Descripción</td>
      <td colspan="2">Fabricación (kgCo2)</td>
      <td colspan="3">Casos de uso (W)<br></td>
      <td>Tiempo de uso<br></td>
      <td>mix eléctrico<br></td>
      
    </tr>
    <tr>
      <td rowspan="2">{{ use.component.description }}</td>
      <td class="sub-header">emisiones</td>
      <td class="sub-header">Desviacón</td>
      <td class="sub-header">bueno</td>
      <td class="sub-header">medio</td>
      <td class="sub-header">malo</td>
      <td rowspan="2">{{ use.server_years }} horas</td>
      <td rowspan="2">{{ use.emissions }} gCO2/kWh</td>
    </tr>
    <tr>
      <td >{{ use.component.cfp_build_phase }}</td>
      <td >{{ use.component.cfp_deviation_standard }}</td>
      <td>{{ use.component.best_case }}</td>
      <td>{{ use.component.middle_case }}</td>
      <td>{{ use.component.worst_case }}<br></td>
    </tr>
  </tbody>
</table>
      
      El coste de fabricación implicado al proyecto, viene dado por el coste de producción del componente
      multiplicado por el tiempo de uso dedicado al proyecto.
      
      <div class="equations-box">
        <EquationComponent :show_tex="switch_latex" :formula="use_percentaje_exp"/>
        <EquationComponent :show_tex="switch_latex" :formula="build_cost_exp"/>

        <EquationComponent :show_tex="switch_latex" :formula="use_percentaje(use)"/>
        <EquationComponent :show_tex="switch_latex" :formula="build_cost(use, 'middle')"/>
      </div>

      <p style="text-align: justify;">	
        Para medir el impacto que tiene el tiempo de uso se ha multiplicado el consumo electrico
        por el tiempo de uso dedicado al proyecto, conviertiendolo posteriormente en kilos de CO2.
      </p>
      
      <div class="equations-box">
        <EquationComponent :show_tex="switch_latex" :formula="use_cost_exp"/>
        <EquationComponent :show_tex="switch_latex" :formula="use_cost(use, 'middle')"/>
      </div>
      
      <p style="text-align: justify;">	
        Para el coste de destrucción se ha tenido obtenido el porcentaje equivalente a partir 
        del datasheet del fabricante.
      </p>
      <div class="equations-box">
        <EquationComponent :show_tex="switch_latex" :formula="end_life_exp"/>
        <EquationComponent :show_tex="switch_latex" :formula="destruction_cost(use, 'middle')"/>
      </div>

      <p style="text-align: justify;">
        El coste total viene dado por la suma de las emisiones de las tres fases.					
      </p>

      <div class="equations-box">
        <EquationComponent :show_tex="switch_latex" :formula="total_cost_exp"/>
        <EquationComponent :show_tex="switch_latex" :formula="total_cost(use, 'middle')"/>
      </div>
      
      <div style="break-before: page;">

        <p style="text-align: justify;">
          Estos son los calculos para el peor caso, en el que el consumo de electricidad
          y el coste de fabricación ha sido más elevado					
        </p>

        <div class="equations-box">
          <EquationComponent :show_tex="switch_latex" :formula="build_cost(use, 'worst')"/>
          <EquationComponent :show_tex="switch_latex" :formula="use_cost(use, 'worst')"/>
          <EquationComponent :show_tex="switch_latex" :formula="destruction_cost(use, 'worst')"/>
          <EquationComponent :show_tex="switch_latex" :formula="total_cost(use, 'worst')"/>
        </div>

        <p style="text-align: justify;">
          Estos son los calculos para el mejor caso, en el que el consumo de electricidad
          y el coste de fabricación ha más bajo.  					
        </p>

        <div class="equations-box">
          <EquationComponent :show_tex="switch_latex" :formula="build_cost(use, 'best')"/>
          <EquationComponent :show_tex="switch_latex" :formula="use_cost(use, 'best')"/>
          <EquationComponent :show_tex="switch_latex" :formula="destruction_cost(use, 'best')"/>
          <EquationComponent :show_tex="switch_latex" :formula="total_cost(use, 'best')"/>
        </div>
    </div>



  </div>
  </div>
  </div>


</template>
<!-- <script src="https://html2canvas.hertzen.com/dist/html2canvas.js"></script> -->
<script>
import { useComponentsData } from "@/stores/ComponentsData"
import { PDFDocument } from 'pdf-lib';
// import html2pdf from "html2pdf.js";
import jsPDF from 'jspdf'
import { font1 } from "@/MathJax/font-math_main"
import { font2 } from "@/MathJax/font-nimbussans"
import EquationComponent from "@/components/EquationComponent.vue"

// import MathJax from 'mathjax';
// const mathjaxConfig = {
//   options: {
//     renderActions: {
//       addMenu: [0, '', '']
//     },
//   },
// };

// Inicializa MathJax
// MathJax.config(mathjaxConfig).init();

export default {
  name: "ReportView",
  setup(){
    const store = useComponentsData();
    return {
      store: store,
    }
  },
  components:{
    EquationComponent,
  },
  data(){
    return{
      formula: '$$x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}.$$',
      use_percentaje_exp: "\\textbf{Porcentaje de uso} = \\frac{\\text{horas de desarrollo}}{\\text{horas útiles}}\\cdot 100",
      build_cost_exp: "\\textbf{Coste fabricacion en el proyecto}=\\text{coste fabricación}\\cdot \\text{porcentaje de uso}",
      use_cost_exp: "\\textbf{Coste de uso}= \\text{consumo} \\cdot  \\text{horas de uso}",
      server_hours_exp: "\\textbf{Total de horas} = 24 \\cdot 365 \\cdot 6 = \\text{52560 horas}",
      build_cost_server_exp: "\\textbf{Coste de fabricacion} = \\frac{\\text{emisiones de CO2}}{\\text{aplicaicones alojadas}}",
      consume_server_exp: "\\textbf{Consumo servidor} = \\frac{\\text{consumo} \\cdot \\text{total de horas}}{\\text{aplicaicones alojadas}}",
      consume_network_server: "\\textbf{Consumo red} = \\frac{\\text{Consumo servidor}}{47} \\cdot 3",
      use_cost_server_exp: "\\textbf{Coste de uso} = (\\text{Consumo servidor} + \\text{Consumo red}) \\cdot 2",
      end_life_exp: "\\textbf{Coste destrucción}= (\\text{Coste fabricacion en el proyecto} +  \\text{Coste de uso})\\cdot 0.01",
      total_cost_exp: "\\textbf{Coste total} = \\text{Coste de fabricacion} + \\text{Coste de uso} + \\text{Coste de destruccion}",

      switch_latex: false,
      uses: [],
      total_results: {},
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
  methods: {
    createPDF () {
      let pdfName = 'test'; 
      var doc = new jsPDF();
      doc.text("Hello World", 10, 10);
      doc.save(pdfName + '.pdf');
    },
    // async  mergePdfs(pdfsToMerges) {
    //   const mergedPdf = await PDFDocument.create();
    //   const actions = pdfsToMerges.map(async pdfBuffer => {
    //     const pdf = await PDFDocument.load(pdfBuffer);
    //     const copiedPages = await mergedPdf.copyPages(pdf, pdf.getPageIndices());
    //     copiedPages.forEach((page) => {
    //       // console.log('page', page.getWidth(), page.getHeight());
    //       // page.setWidth(210);
    //       mergedPdf.addPage(page);
    //     });
    //   });
    //   await Promise.all(actions);
    //   const mergedPdfFile = await mergedPdf.save();
    //   return mergedPdfFile;
    // },
    async Convert_HTML_To_PDF() {

      var results = new jsPDF();
      var table = new jsPDF();
      var equations = new jsPDF();


      // Source HTMLElement or a string containing HTML.
      var resultsHTML = document.getElementById("result-element");
      var tableHTML = document.getElementById("table-print");
      var equationHTML = document.getElementById("equation-print");

      // Utiliza querySelectorAll para seleccionar todos los elementos div con la clase "miClase"
      
      // resultsHTML = resultsHTML.cloneNode(true);
      
      // var panel_div = resultsHTML.querySelector(".panel");

      // // Itera a través de los elementos seleccionados y elimina cada uno
      // if (panel_div) {
      //   panel_div.remove();
      // }
     
      this.addFonts(results);
      this.addFonts(table);
      this.addFonts(equations);

      results = this.htmlToPDF(results, resultsHTML);
      table = this.htmlToPDF(table, tableHTML);
      equations = this.htmlToPDF(equations, equationHTML);

      this.merge([results, table, equations])
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
    async merge(docs){
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
    savePDF() {
      // var opt = {
      //   margin:       1,
      //   filename:     'myfile.pdf',
      //   image:        { type: 'html', quality: 0.98 },
      //   html2canvas:  { scale: 2, useCORS: true, width: 793 ,dpi: 300},
      //   jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
      // };
      // var opt = {
      //   margin:       0.6,
      //   filename:     'myfile.pdf',
      //   image:        { type: 'html', quality: 0.98 },
      //   html2canvas:  { scale: 2, useCORS: true},
      //   jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
      // };
      // var element = document.getElementById('element-to-print');
      // console.log(element)
      // html2pdf().set(opt).from(element).save();
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
      this.total_results = {
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
            this.serverCalculations(use[key], component, key);
          else
            this.normalCalculations(use[key], component, key, use.hours);
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
    serverCalculations(use, component, key){
      
      const power = this.powerByCase(key, component);

      use["build_cost"] = this.round(component.cfp_build_phase / 12);
      use["server_cost"] = this.round(((power/1000) * this.server_hours.number) / component.hosted_apps);
      use["network_cost"] = this.round((use["server_cost"] / 47) * 3);
      use["direct_cost"] = use["server_cost"] + use["network_cost"];
      use["use_cost"] = this.round(use["direct_cost"] * 2);
      use["use_cost_co2"] = this.round(use["use_cost"] * this.kgCO2_KWh);

      var destroy_cost = (use["use_cost_co2"] + use["build_cost"]) * 0.01;
      use["destroy_cost"] = this.round(destroy_cost);
      use["total"] = this.round(use["destroy_cost"] + use["use_cost_co2"] + use["build_cost"]);

    },
    normalCalculations(use, component, key, hours){

      const power = this.powerByCase(key, component);
      const deviation = component.cfp_deviation_standard * this.deviationByCase(key) 

      use["use_percent"] = this.round((hours / this.useful_hours.number)*100);

      use["build_cost"] = this.round((component.cfp_build_phase + deviation) * use["use_percent"]/100);
      use["use_cost"] = this.round((power * hours)/1000);
      use["use_cost_co2"] = this.round(use["use_cost"] * this.kgCO2_KWh);

      var destroy_cost = (use["use_cost_co2"] + use["build_cost"]) * 0.01;
      use["destroy_cost"] = this.round(destroy_cost);
      use["total"] = this.round(use["destroy_cost"] + use["use_cost_co2"] + use["build_cost"]);

    },
    normalCalculations2(use, component){
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
      use["use_cost_wc"] = component.worst_case * use.hours;
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

    },
    sum_results(use){
      for (var i in this.total_results){
        if (Object.prototype.hasOwnProperty.call(this.total_results, i)) {
          for (var j in this.total_results[i]){
            this.total_results[i][j] += use[i][j];
            this.total_results[i][j] = this.round(this.total_results[i][j])
          }
        } 
      }
    },
    mathDisplay(s){
      return "$$"+s+"$$"
    },
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
      var equation = "\\textbf{Coste fabricacion en el proyecto "+ name +"}=\\text{"+ cfp_build_phase +"KgCo2}\\cdot \\text{"+ use_percent +"} = "+ build_cost + "KgCo2";
      return equation;
    },
    build_cost_server(use, case_type) {
      var name = ""
      var build_cost = use[case_type].build_cost;
      var cfp_build_phase = use.component.cfp_build_phase;
      var app = use.component.hosted_apps;

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
      var equation =  "\\textbf{Coste fabricacion en el proyecto "+ name +"}=\\frac{\\text{"+cfp_build_phase+"KgCo2}}{"+app+"} = " +build_cost+"KgCo2";
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
  },
  created(){
    console.log('creado!!!!');
    this.uses = JSON.parse(JSON.stringify(this.store.components_use))
    console.log(this.store.components_use);
    this.calculate();
  },
  mounted() {
    // Espera a que MathJax se cargue y procese
    // MathJax.startup.promise.then(() => {
    //   // Renderiza la ecuación LaTeX
    //   MathJax.typesetPromise([document.getElementById('mathjax-equation')]);
    // });
  }
}
</script>

<style>
table {
  font-family: arial, sans-serif;
  font-size:80%;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 3em;
  
}

.panel{
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
  font-size:80%;
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
}

.component-table tr:first-child {
 background-color: #bff1daae !important
}

.component-table .sub-header {
 background-color: #bff1da4d !important
}

.component {
  font-size:80%;
}

table .case{
  font-size: 80%;
}

th {
  border: 1px solid #dddddd;
  text-align: center;
  padding: 1px;
}

.color-row:nth-child(even){

background-color: rgb(120, 120, 120, 0.3);


}
/* Define los estilos para las columnas impares */
.resume td:first-child {
 background-color: rgba(253, 253, 253, 0.9) !important
}

/* Define los estilos para las columnas impares */
.resume td:nth-child(3n-1) {
 background-color: rgba(238, 255, 241, 0.8)
}

/* Cambia el color de las columnas en el medio a amarillo */
.resume td:nth-child(3n){
background-color: rgba(255, 247, 239, 0.837)

}

/* Define los estilos para las columnas pares */
.resume td:nth-child(3n+1) {
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

.result-box{
  font-family: arial, sans-serif;
  border-radius: 15px;

  background-color: #7CD4AC;
  padding: 20px;
  padding-top: 5px;
  text-align: left;
  color: rgb(9, 9, 9);
}

.compare-box{
  font-family: arial, sans-serif;
  border-radius: 15px;
  border: solid 4px;
  border-color: #7CD4AC;
  margin-top: 20px;
  padding: 20px;
  padding-top: 5px;
  text-align: left;
  color: rgb(9, 9, 9);
}

.result-box h1{
  color: rgb(255, 255, 255);
}

.result-box span{
  /* font-size: 1.2em;
  color: rgb(255, 255, 255); */
}


.equations-box{
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
