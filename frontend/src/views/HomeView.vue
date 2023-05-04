<script lang="ts">
import { defineComponent } from "vue";
import { championCheckFixture } from "@/fixtures/ChampionCheck.fixture";
import { ChampionCheck } from "@/types/ChampionCheck";
import ChampionGuessPage from "@/components/ChampionGuessPage.vue";

type Data = {
  championsSubmitted: ChampionCheck[];
};

export default defineComponent({
  name: "HomeView",
  data(): Data {
    return {
      championsSubmitted: [championCheckFixture],
    };
  },
  components: {
    ChampionGuessPage,
  },
});
</script>

<template>
  <div class="home"><ChampionGuessPage /></div>
</template>
