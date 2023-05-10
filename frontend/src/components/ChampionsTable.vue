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
  columnTitles: readonly string[];
};

export default defineComponent({
  name: "ChampionsTable",
  data(): Data {
    return { columnTitles: Object.freeze(columnTitles) };
  },
  props: {
    championsSubmitted: {
      type: Object as PropType<ChampionSubmitted[]>,
      required: true,
    },
  },
  components: { ChampionDetailedTableRow },
});
</script>

<template>
  <table>
    <thead>
      <td v-for="columnTitle in columnTitles" :key="columnTitle">
        <div>{{ columnTitle }}</div>
      </td>
    </thead>
    <tbody>
      <ChampionDetailedTableRow
        v-for="championSubmitted in championsSubmitted"
        :key="championSubmitted.champion.champion"
        :champion-check="championSubmitted"
      />
    </tbody>
  </table>
</template>

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
</style>
