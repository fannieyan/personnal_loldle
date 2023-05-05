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
  champion: Validity;
  gender: Validity;
  lanes: Validity;
  species: Validity;
  resource: Validity;
  ranges: Validity;
  regions: Validity;
  release_date: Comparison;
}

export interface Champion {
  champion: string;
  gender: string;
  lanes: string[];
  species: string[];
  resource: string;
  ranges: string[];
  regions: string[];
  release_date: number;
}
