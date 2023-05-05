validity = {
    "VALID": "isValid",
    "NOT_VALID": "isNotValid",
    "PARTIALLY_VALID": "isPartiallyValid",
}

comparison = {
    "MORE": "more",
    "LESS": "less",
    "EQUAL": "equal",
}


def check_list(ref, to_check):
    ref_set = set(ref)
    to_check_set = set(to_check)
    if ref_set == to_check_set:
        return validity["VALID"]
    if len(ref_set.intersection(to_check_set)) != 0:
        return validity["PARTIALLY_VALID"]
    return validity["NOT_VALID"]


def compare_number(ref, to_check):
    if ref == to_check:
        return comparison["EQUAL"]
    if ref < to_check:
        return comparison["LESS"]
    return comparison["MORE"]


def check_string(ref, to_check):
    return validity["VALID"] if ref == to_check else validity["NOT_VALID"]


def check_properties(ref, to_check):
    check_result = dict()
    for property in ref:
        result = ""
        if isinstance(ref[property], list):
            result = check_list(
                ref[property], to_check[property])
        elif isinstance(ref[property], int):
            result = compare_number(ref[property], to_check[property])
        else:
            result = check_string(ref[property], to_check[property])
        check_result[property] = result
    return check_result


def get_champion_names(champions):
    result = []
    for champion in champions:
        result.append(champion.champion)
    return result
