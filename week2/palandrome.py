def palindrome(text):
    text=text.lower()
    rev_text="".join(reversed(text))

    if text == rev_text:
        return True
    else:
        return False

print(palindrome("madam"))
print(palindrome("hello"))
print(palindrome(""))
