<template>
  <p>Report page!</p>
  <p>Hello {{ store.user_info.username }}</p>
  <!-- {{ katex.render("c = \\pm\\sqrt{a^2 + b^2}", element, {throwOnError: false}) }} -->
</template>

<script>
import { useComponentsData } from "@/stores/ComponentsData"
// import { katex } from 'katex';

export default {
name: "ReportView",
setup(){
  const store = useComponentsData();
  return {
    store: store,
  }

},
}
</script>
