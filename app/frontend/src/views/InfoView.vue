<template>
  <h1>CO2Cal</h1>a
  <font-awesome-icon icon="fa-solid fa-plus-square" />      
  <font-awesome-icon icon="fa-regular fa-folder-open" size="lg" /> 
  <font-awesome-icon icon="fa-solid fa-plus" size="lg" /> 
  <font-awesome-icon icon="fa-solid fa-microchip" />
  <font-awesome-icon icon="fa-regular fa-file-pdf" />
  <font-awesome-icon icon="fa-solid fa-bolt" />
  <font-awesome-icon icon="fa-solid fa-circle-info" />
  <font-awesome-icon icon="fa-regular fa-circle-question" size="lg"/>
  <font-awesome-icon icon="fa-solid fa-calculator" />


</template>

<script>
import { useComponentsData } from "@/stores/ComponentsData"


export default {
  name: "InfoView",
  setup(){
    const store = useComponentsData();
    return {
      store: store,
    }

  },
}
</script>