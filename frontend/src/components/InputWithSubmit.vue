<script lang="ts">
import { searchChampions } from "@/services/Champion.services";
import { defineComponent, PropType } from "vue";
import { ChampionSubmitted } from "./ChampionGuessPage.vue";
import AutocompleteInput from "./UI/AutocompleteInput/AutocompleteInput.vue";

type Data = {
  input: string;
  debouncedInput: string;
  championSuggestions: string[];
  timer: number | undefined;
};

export default defineComponent({
  name: "InputWithSubmit",
  data(): Data {
    return {
      input: "",
      debouncedInput: "",
      championSuggestions: [],
      timer: undefined,
    };
  },
  props: {
    onSubmit: {
      type: Function as PropType<(championName: string) => Promise<void>>,
      required: true,
    },
    submittedChampions: { type: Object as PropType<ChampionSubmitted[]> },
    disabled: Boolean,
  },
  watch: {
    input: function (newValue: string) {
      this.debouncedInput = newValue;
      clearTimeout(this.timer);
      this.timer = setTimeout(async () => {
        try {
          this.championSuggestions = await searchChampions(newValue);
        } catch (error) {
          console.error(error);
        }
      }, 500);
    },
  },
  methods: {
    submitChampion: async function () {
      try {
        await this.onSubmit(this.input);
        this.input = "";
        this.championSuggestions = [];
      } catch (error) {
        alert(
          "Une erreur est survenue. Vérifiez l'orthographe du champion proposé ou votre connexion internet."
        );
      }
    },
    onChange: function (value: string) {
      this.input = value;
    },
  },
  components: { AutocompleteInput },
});
</script>

<template>
  <div id="input-with-submit-container">
    <AutocompleteInput
      :input="input"
      :suggestions="championSuggestions"
      :on-change="onChange"
    />
    <button type="submit" v-on:click="submitChampion()" :disabled="disabled">
      Vérifier
    </button>
  </div>
</template>

<style>
#input-with-submit-container {
  display: flex;
  justify-content: center;
  gap: 8px;
}
</style>
