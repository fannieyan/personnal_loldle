<script lang="ts">
import { Comparison, Validity } from "@/types/ChampionCheck";
import { defineComponent, PropType } from "vue";

const getClassName = (validity: Validity | Comparison) => {
  if (validity === Validity.VALID || validity === Comparison.EQUAL)
    return "isValid";
  if (validity === Validity.PARTIALLY_VALID) return "isPartiallyValid";
  return "isNotValid";
};

const getPropertyName = (property: string | number | unknown[]) => {
  if (typeof property === "number") return property.toString();
  if (typeof property === "string") return property;
  if (Array.isArray(property)) return property.join(", ");
};

export default defineComponent({
  name: "PropertyTableData",
  props: {
    property: { type: [String, Array, Number], required: true },
    validity: {
      type: String as PropType<Validity | Comparison>,
      required: true,
    },
  },
  computed: {
    className: function () {
      return getClassName(this.validity);
    },
    propertyName: function () {
      return getPropertyName(this.property);
    },
  },
});
</script>

<template>
  <td :class="[className, 'championData']">
    <p>{{ propertyName }}</p>
  </td>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.championData {
  color: #f1f1f1;
  width: 100px;
  max-width: 100px;
  white-space: break-spaces;
  height: 100px;
  padding: 4px;
}
.isValid {
  background-color: #069c56;
}
.isNotValid {
  background-color: #d3212c;
}
.isPartiallyValid {
  background-color: #ff980e;
}
</style>
