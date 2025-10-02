def isPalindrome(x):
    num = x 
    new_num = 0

    while num > 0:
        if new_num != 0:
            new_num *= 10
        new_num += num % 10
        num = num//10
        print(f"x: {x} - num: {num} - new_num {new_num}")
    
    if x == new_num:
        return True
    
    return False

print(isPalindrome(12321))
print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))