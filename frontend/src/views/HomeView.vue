<script lang="ts">
import { defineComponent } from "vue";
import ChampionGuessPage from "@/components/ChampionGuessPage.vue";

export default defineComponent({
  name: "HomeView",
  components: {
    ChampionGuessPage,
  },
});
</script>

<template>
  <div class="home"><ChampionGuessPage /></div>
</template>
