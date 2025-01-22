A = input()

# Write your code here!

def is_palindrome(string):
    
    reverse_string = ""

    for i in range(len(string) - 1, -1, -1):
        reverse_string += string[i]
    
    if string == reverse_string:
        return True
    
    return False

if is_palindrome(A):
    print("Yes")
else:
    print("No")
