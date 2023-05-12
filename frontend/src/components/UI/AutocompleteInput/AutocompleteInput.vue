<script lang="ts">
import { defineComponent, PropType, ref } from "vue";

export default defineComponent({
  name: "AutocompleteInput",
  data() {
    return { open: false };
  },
  setup() {
    const autocompleteInput = ref<HTMLInputElement | null>(null);
    return { autocompleteInput };
  },
  props: {
    input: String,
    suggestions: { type: Object as PropType<Array<string>>, required: true },
    onChange: {
      type: Function as PropType<(value: string) => void>,
    },
  },
  methods: {
    focusInput: function () {
      this.autocompleteInput && this.autocompleteInput.focus();
    },
    onClickItem: function (suggestion: string) {
      console.log("click", suggestion);
      this.onChange && this.onChange(suggestion);
      this.focusInput();
    },
    onFocus: function () {
      this.open = true;
    },
    onBlur: function () {
      this.open = false;
    },
    onInput: function () {
      this.onChange &&
        this.autocompleteInput &&
        this.onChange(this.autocompleteInput.value);
    },
  },
});
</script>

<template>
  <div id="autocomplete-container">
    <input
      ref="autocompleteInput"
      type="text"
      id="search-input"
      placeholder="Nom d'un champion..."
      :value="input"
      @focus="onFocus"
      @blur="onBlur"
      @input="onInput"
    />
    <ul id="suggestion-list" v-if="open && suggestions.length">
      <li
        v-for="suggestion in suggestions"
        v-bind:key="suggestion"
        @mousedown="onClickItem(suggestion)"
      >
        {{ suggestion }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
#search-input {
  position: relative;
  font-size: 18px;
}

#autocomplete-container {
  position: relative;
}
#suggestion-list {
  position: absolute;
  top: 100%;
  left: 0px;
  width: 100%;
  max-height: 400px;
  overflow: auto;
  z-index: 4;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}
li {
  padding: 12px 16px;
  font-size: 18px;
  text-align: left;
  border-bottom: solid 1px white;
  background-color: #222222;
}

li:hover {
  background-color: #0bc6e3;
  color: #111;
}
</style>
