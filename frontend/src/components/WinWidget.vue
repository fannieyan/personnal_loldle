<script lang="ts">
import { defineComponent, PropType } from "vue";
import { ChampionSubmitted } from "./ChampionGuessPage.vue";
import ChampionDetailedTableRow from "./ChampionItem/ChampionDetailedTableRow.vue";

const columnTitles = [
  "Nom",
  "Genre",
  "Lane",
  "Espèce",
  "Ressource",
  "Range",
  "Région",
  "Sortie",
];

type Data = {
  columnTitles: string[];
};

export default defineComponent({
  name: "WinWidget",
  data(): Data {
    return { columnTitles };
  },
  props: {
    answer: { type: String, required: true },
    numberOfTries: { type: Number, required: true },
    onPlayAgain: {
      type: Function as PropType<() => void>,
      required: true,
    },
  },
});
</script>

<template>
  <div id="widget-container">
    <div id="border-container">
      <div id="text-content">
        <img src="/teemo-thumbs-up.png" alt="Teemo thumbs up emote" />
        <div id="congratulation-container">
          <h3>Bravo !</h3>
          <p>
            Vous avez trouvé <em>{{ answer }}</em> en
            <em>{{ numberOfTries?.toString() }}</em> tentative{{
              numberOfTries > 1 ? "" : "s"
            }}.
          </p>
        </div>
      </div>
      <button type="button" v-on:click="onPlayAgain">Rejouer</button>
    </div>
  </div>
</template>

<style scoped>
h3 {
  margin-top: 0px;
  text-align: left;
}
em {
  font-weight: bold;
  font-style: normal;
  color: #c28f2c;
}
#widget-container {
  display: flex;
  justify-content: center;
}
#border-container {
  border-color: "white";
  border-width: 1px;
  border-style: solid;
  padding: 32px;
  width: 40%;
}
#text-content {
  display: flex;
  justify-content: center;
  align-items: center;
}
#congratulation-container {
  margin-left: 32px;
  text-align: left;
}
img {
  width: 100px;
  height: 100px;
}
</style>
