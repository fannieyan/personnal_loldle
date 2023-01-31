import {
  championCheckFixture,
  ChampionFixture,
} from "@/fixtures/ChampionCheck.fixture";
import { Champion, ChampionCheck } from "@/types/ChampionCheck";

export const getChampion = async (): Promise<Champion> => {
  return Promise.resolve(ChampionFixture);
};

export const checkChampion = async (): Promise<ChampionCheck> => {
  return Promise.resolve(championCheckFixture);
};
