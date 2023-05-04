export enum Validity {
  VALID = "isValid",
  NOT_VALID = "isNotValid",
  PARTIALLY_VALID = "isPartiallyValid",
}

export enum Comparison {
  MORE = "more",
  LESS = "less",
  EQUAL = "equal",
}

// TODO: Should probably define one type check per attribute, with enum for each.

export interface ChampionCheck {
  name: Validity;
  gender: Validity;
  position: Validity;
  species: Validity;
  resource: Validity;
  range: Validity;
  region: Validity;
  releaseDate: Comparison;
}

export interface Champion {
  name: string;
  gender: string;
  position: string[];
  species: string[];
  resource: string;
  range: string[];
  region: string[];
  releaseDate: number;
}
