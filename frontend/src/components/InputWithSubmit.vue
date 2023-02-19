<script lang="ts">
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "InputWithSubmit",
  data() {
    return { championName: "" };
  },
  props: {
    onSubmit: { type: Function as PropType<() => void>, required: true },
  },
});
</script>

<template>
  <div>
    <input v-model="championName" />
    <button type="submit" v-on:click="onSubmit">Vérifier</button>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
