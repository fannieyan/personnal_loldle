<script lang="ts">
import { Champion, ChampionCheck } from "@/types/ChampionCheck";
import { defineComponent } from "vue";
import InputWithSubmit from "./InputWithSubmit.vue";
import ChampionDetailedTableRow from "./ChampionItem/ChampionDetailedTableRow.vue";
import { checkChampion, getChampion } from "@/services/Champion.services";

type ChampionSubmitted = { champion: Champion; check: ChampionCheck };
type Data = {
  championsSubmitted: ChampionSubmitted[];
  columnTitles: readonly string[];
};

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

const onSubmitChampion = async (championSubmitted: ChampionSubmitted[]) => {
  const [champion, check] = await Promise.all([getChampion(), checkChampion()]);
  championSubmitted.push({ champion, check });
};

export default defineComponent({
  name: "ChampionGuessPage",
  data(): Data {
    return {
      columnTitles: Object.freeze(columnTitles),
      championsSubmitted: [] as ChampionSubmitted[],
    };
  },
  methods: {
    submitChampion: function () {
      return onSubmitChampion(this.championsSubmitted);
    },
  },
  components: { ChampionDetailedTableRow, InputWithSubmit },
});
</script>

<template>
  <h1>Devine le champion!</h1>
  <div>
    <InputWithSubmit :on-submit="submitChampion" />
  </div>
  <div>
    <table v-if="championsSubmitted.length">
      <thead>
        <td v-for="columnTitle in columnTitles" :key="columnTitle">
          <div>{{ columnTitle }}</div>
        </td>
      </thead>
      <tbody>
        <ChampionDetailedTableRow
          v-for="championSubmitted in championsSubmitted"
          :key="championSubmitted.champion.name"
          :champion-check="championSubmitted"
        />
      </tbody>
    </table>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
table {
  margin: auto;
}
thead > td > div {
  border-bottom: 3px solid white;
  width: 80%;
  height: 100%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 0px;
  margin-bottom: 0px;
}
td {
  height: 32px;
}
tbody::before {
  content: "";
  display: block;
  height: 8px;
}
div {
  margin-top: 32px;
}
</style>
