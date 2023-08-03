<template>
    <p>Info page!</p>
    <p>Hello {{ user.username }}</p>
</template>

<script>
export default {
  name: "InfoView",
  props: ["user"],
}
</script>