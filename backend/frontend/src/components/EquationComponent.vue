<template>
  <div v-if="show_tex">
    <p> {{ formula }} </p>
  </div>
  <div v-else>
    <VueMathjax class="equations" :formula="mathDisplay(formula)" />
  </div>
</template>
  



<script>
  import VueMathjax from 'vue-mathjax-next';
  export default {
    name: "EquationComponent",
    components:{
      VueMathjax,
    },
    props: ["show_tex","formula"],
    methods:{
      mathDisplay(s){
        return "$"+s+"$"
      },
    }
  }
</script>


<style>
.equations{
  font-size: 0.75em;
}
p {
  margin-bottom: 1em;
  text-align: justify;
}
</style>


  