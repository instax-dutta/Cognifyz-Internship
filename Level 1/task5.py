#task5 palindrome checker 
def palindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False

print(palindrome("abba"))
print(palindrome("abb"))
print(palindrome("ab"))
print(palindrome("a"))