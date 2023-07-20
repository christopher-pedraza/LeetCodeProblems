def checkInclusion(self, s1: str, s2: str) -> bool:
    return s1 + s2

print(checkInclusion("ab", "eidbaooo")) # True
print(checkInclusion("ab", "eidboaoo")) # False