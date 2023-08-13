<template>
    <p>Info page!</p>
    <p>Hello {{ store.user_info.username }}</p>
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