export const getAPIUrl = () => {
  const dev = new URLSearchParams(window.location.search).get("dev");
  if (dev && dev === "true") return "http://127.0.0.1:8000/game/api";
  else throw Error("Specify dev=true");
};
