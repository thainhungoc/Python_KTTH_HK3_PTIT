def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]
def count_palindrome(str_input):
    words = str_input.split()
    count = 0
    for word in words:
        if is_palindrome(word):
            count += 1
    return count
def count_unique_palindromes(str_input):
    words = str_input.split()
    unique_palindromes = set()
    for word in words:
        if is_palindrome(word):
            unique_palindromes.add(word.lower())
    return len(unique_palindromes)
test_str2 = "computer science programming python java javascript"
test_str1 = "hello world apple banana orange grapes"

print(count_palindrome(test_str1))  
print(count_unique_palindromes(test_str1))  
print(count_palindrome(test_str2))  
print(count_unique_palindromes(test_str2))  
