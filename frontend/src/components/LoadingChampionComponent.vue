<script lang="ts">
import { defineComponent } from "vue";
import LoaderIcon from "@/components/UI/LoaderIcon.vue";

export default defineComponent({
  name: "LoadingChampionComponent",
  components: { LoaderIcon },
});
</script>

<template>
  <div><h3>Un champion un appelé à la barre...</h3></div>
  <LoaderIcon />
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 32px;
}
</style>
