<script lang="ts">
import {
  Champion,
  ChampionCheck,
  Comparison,
  Validity,
} from "@/types/ChampionCheck";
import { defineComponent } from "vue";
import InputWithSubmit from "./InputWithSubmit.vue";
import LoadingChampionComponent from "./LoadingChampionComponent.vue";
import LoaderIcon from "./UI/LoaderIcon.vue";
import ChampionsTable from "./ChampionsTable.vue";
import {
  checkChampion,
  getChampion,
  getRandomChampion,
} from "@/services/Champion.services";

export type ChampionSubmitted = { champion: Champion; check: ChampionCheck };
type Data = {
  championsSubmitted: ChampionSubmitted[];
  columnTitles: readonly string[];
  isLoading: boolean;
  isSubmitting: boolean;
  isGameWon: boolean;
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
      isSubmitting: false,
      isGameWon: false,
    };
  },
  methods: {
    _checkGameState: function ({ check }: ChampionSubmitted) {
      if (
        Object.values(check).some(
          (value) => !(value === Validity.VALID || value === Comparison.EQUAL)
        )
      )
        return;
      this.isGameWon = true;
    },
    submitChampion: async function (championName: string) {
      if (
        this.championsSubmitted.find(
          ({ champion }) =>
            champion.champion.toLowerCase() === championName.toLowerCase()
        )
      ) {
        alert("Vous avez déjà testé ce champion.");
        return;
      }
      this.isSubmitting = true;
      const result = await onSubmitChampion(championName);
      this.championsSubmitted.unshift(result);
      this._checkGameState(result);
      this.isSubmitting = false;
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
    ChampionsTable,
    InputWithSubmit,
    LoadingChampionComponent,
    LoaderIcon,
  },
});
</script>

<template>
  <h1>Devine le champion!</h1>
  <div v-if="isLoading">
    <LoadingChampionComponent />
  </div>
  <div v-if="!isLoading">
    <div class="loader-container"><LoaderIcon v-if="isSubmitting" /></div>
    <div>
      <InputWithSubmit
        :on-submit="submitChampion"
        :disabled="isSubmitting || isGameWon"
      />
    </div>
    <div v-if="championsSubmitted.length">
      <ChampionsTable :champions-submitted="championsSubmitted" />
    </div>
  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  margin-top: 32px;
}

.loader-container {
  width: 100%;

  height: 32px;
}
</style>
