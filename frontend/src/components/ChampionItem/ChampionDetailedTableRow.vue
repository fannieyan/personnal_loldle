<script lang="ts">
import { defineComponent, PropType } from "vue";
import PropertyTableData from "./PropertyTableData.vue";
import { Champion, ChampionCheck } from "@/types/ChampionCheck";

const properties: (keyof ChampionCheck)[] = [
  "name",
  "gender",
  "position",
  "species",
  "resource",
  "range",
  "region",
  "releaseDate",
];

export default defineComponent({
  name: "ChampionDetailedTableRow",
  data() {
    return { properties: Object.freeze(properties) };
  },
  props: {
    championCheck: {
      type: Object as PropType<{ champion: Champion; check: ChampionCheck }>,
      required: true,
    },
  },
  components: { PropertyTableData },
});
</script>

<template>
  <tr>
    <PropertyTableData
      v-for="property in properties"
      :key="property"
      :property="championCheck.champion[property]"
      :validity="championCheck.check[property]"
    />
  </tr>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
