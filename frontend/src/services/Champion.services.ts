import { Champion, ChampionCheck } from "@/types/ChampionCheck";
import { getAPIUrl } from "./api";

export const getChampion = async (championName: string): Promise<Champion> => {
  return fetch(`${getAPIUrl()}/champion/${championName}`).then((response) =>
    response.json()
  );
};

export const checkChampion = async (
  reference: string,
  championName: string
): Promise<ChampionCheck> => {
  return fetch(
    `${getAPIUrl()}/champion/check?` +
      new URLSearchParams({ ref: reference, champion: championName })
  ).then((response) => response.json());
};

export const getRandomChampion = async (): Promise<string> => {
  const response = await fetch(`${getAPIUrl()}/champion/random`);
  return response.text();
};
