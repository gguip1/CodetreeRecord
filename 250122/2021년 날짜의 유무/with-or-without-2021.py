M, D = map(int, input().split())

# Write your code here!

def is_month(month):
    if month <= 12:
        return True
    else:
        return False

def odd_month(month, day):
    if day <= 31 and is_month(month):
        return True
    else:
        return False

def even_month(month, day):
    if month == 2:
        if day <= 28 and is_month(month):
            return True
        else:
            False
    else:
        if day <= 30 and is_month(month):
            return True
        else:
            return False

if M % 2 == 0:
    if even_month(M, D):
        print("Yes")
    else:
        print("No")
else:
    if odd_month(M, D):
        print("Yes")
    else:
        print("No")
