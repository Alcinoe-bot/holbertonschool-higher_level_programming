#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    if (roman_string and isinstance(roman_string, str)):
        it = {'D': 500, 'C': 100, 'M': 1000, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        List = [it.get(i) for i in roman_string]
        for idx, char in enumerate(List):
            if (idx < len(List) - 1):
                if List[idx + 1] > char:
                    sum -= char
                else:
                    sum += char
            else:
                sum += char
    return(sum)
