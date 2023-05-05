<script lang="ts">
import { Champion, ChampionCheck } from "@/types/ChampionCheck";
import { defineComponent } from "vue";
import InputWithSubmit from "./InputWithSubmit.vue";
import ChampionDetailedTableRow from "./ChampionItem/ChampionDetailedTableRow.vue";
import LoadingChampionComponent from "./LoadingChampionComponent.vue";
import {
  checkChampion,
  getChampion,
  getRandomChampion,
} from "@/services/Champion.services";

type ChampionSubmitted = { champion: Champion; check: ChampionCheck };
type Data = {
  championsSubmitted: ChampionSubmitted[];
  columnTitles: readonly string[];
  isLoading: boolean;
};

const localStorageChampionKey = "guessChampion";

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

const onSubmitChampion = async (championName: string) => {
  const referenceChampion = window.localStorage.getItem(
    localStorageChampionKey
  );
  if (!referenceChampion) throw new Error("No reference champion!");
  const [champion, check] = await Promise.all([
    getChampion(championName),
    checkChampion(referenceChampion, championName),
  ]);
  return { champion, check };
};

export default defineComponent({
  name: "ChampionGuessPage",
  data(): Data {
    return {
      columnTitles: Object.freeze(columnTitles),
      championsSubmitted: [] as ChampionSubmitted[],
      isLoading: true,
    };
  },
  methods: {
    submitChampion: async function (championName: string) {
      const result = await onSubmitChampion(championName);
      this.championsSubmitted.unshift(result);
    },
  },

  async mounted() {
    this.isLoading = true;
    const championToGuess = window.localStorage.getItem(
      localStorageChampionKey
    );
    if (!championToGuess) {
      const newChampion = await getRandomChampion();
      window.localStorage.setItem(localStorageChampionKey, newChampion);
    }
    this.isLoading = false;
  },
  components: {
    ChampionDetailedTableRow,
    InputWithSubmit,
    LoadingChampionComponent,
  },
});
</script>

<template>
  <h1>Devine le champion!</h1>
  <div v-if="isLoading">
    <LoadingChampionComponent />
  </div>
  <div v-if="!isLoading">
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
            :key="championSubmitted.champion.champion"
            :champion-check="championSubmitted"
          />
        </tbody>
      </table>
    </div>
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
