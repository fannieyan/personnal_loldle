<script lang="ts">
import { defineComponent, PropType } from "vue";

export default defineComponent({
  name: "InputWithSubmit",
  data() {
    return { championName: "" };
  },
  props: {
    onSubmit: {
      type: Function as PropType<(championName: string) => void>,
      required: true,
    },
  },
});
</script>

<template>
  <div>
    <input v-model="championName" />
    <button type="submit" v-on:click="onSubmit(championName)">Vérifier</button>
  </div>
</template>
