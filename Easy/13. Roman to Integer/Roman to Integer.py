def romanToInt(s: str):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    s = list(s)
    for i in range(len(s)-1,-1,-1):
        current = roman[s[i]]
        if i < len(s)-1 and current< roman[s[i+1]]:
            result -= current
        else:
            result += current
    return result
print(romanToInt(s='MCMXCIV'))
