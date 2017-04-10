def is_palindrome(n):
    l = str(n)
    a = l[::-1]
    if l == a:
        return True
output = filter(is_palindrome,range(1,10000))
print(list(output))
