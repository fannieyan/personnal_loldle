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
    disabled: Boolean,
  },
  methods: {
    submitChampion: function () {
      this.onSubmit(this.championName);
      this.championName = "";
    },
  },
});
</script>

<template>
  <div>
    <input v-model="championName" :disabled="disabled" />
    <button type="submit" v-on:click="submitChampion()" :disabled="disabled">
      Vérifier
    </button>
  </div>
</template>

<style scoped>
div {
  display: flex;
  justify-content: center;
  gap: 8px;
}
</style>
