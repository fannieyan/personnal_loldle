import { ChampionCheck, Validity, Comparison } from "@/types/ChampionCheck";

export const championCheckFixture: ChampionCheck = {
  name: Validity.NOT_VALID,
  gender: Validity.VALID,
  position: Validity.PARTIALLY_VALID,
  species: Validity.VALID,
  resource: Validity.NOT_VALID,
  range: Validity.NOT_VALID,
  region: Validity.PARTIALLY_VALID,
  releaseDate: Comparison.MORE,
};

export const ChampionFixture = {
  name: "Riven",
  gender: "Female",
  position: ["Top"],
  species: ["Human"],
  resource: "Manaless",
  range: ["Melee"],
  region: ["Ionia", "Noxus"],
  releaseDate: 2011,
};
