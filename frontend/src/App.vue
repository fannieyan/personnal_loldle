<template>
  <router-view />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
body {
  background-color: #111111;
  color: #f9f9f9;
  height: "100%";
}

button {
  background-color: #0bc6e3;
  color: #111111;
  padding: 8px 16px;
  font-weight: bold;
  border: none;
  transition-duration: 0.2s;
  font-size: 18px;
}

button:hover {
  background-color: #13d8f6;
}

input {
  padding: 8px 8px;
  border-radius: 4px;
  border: none;
}
</style>
