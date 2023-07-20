
<template>
  <main>
    <button v-on:click="getComponents">load components</button>
    <p>Home page!</p>
  </main>
</template>

<script>

import { axios } from "@/common/api.service.js"

export default {
  name: "HomeView",
  data() {
    return {
      components: [] 
    }
  },
  methods: {
    async getComponents() {
      let endpoint = "/api/component/5/";
      try {
        const response = await axios.get(endpoint);
        this.components = response.data;
        console.log(this.components);
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    }
  }
}
</script>
