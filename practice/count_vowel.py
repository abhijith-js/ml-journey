def count_vowel(texts):
    vowels = "aeiouAEIOU"
    count = 0
    for char in texts:
        if char in vowels:
            count += 1
    return count

print(count_vowel("Education"))
print(count_vowel(""))
print(count_vowel("AEIOU"))
print(count_vowel("rhythm"))
