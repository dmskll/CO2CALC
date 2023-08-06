<template>
    <p>Components page!</p>
    <p>Hello {{ user.username }}</p>
</template>

<script>
export default {
  name: "ComponentsView",
  props: ["user"],
}
</script>