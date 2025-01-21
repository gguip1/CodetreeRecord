Y, M, D = map(int, input().split())

# Write your code here!

def is_leaf_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_season(month):
    if month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Fall'
    else:
        return 'Winter'

def is_day(year, month, day):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day <= 31:
            return True
    elif month in [4, 6, 9, 11]:
        if day <= 30:
            return True
    else:
        if is_leaf_year(year):
            if day <= 29:
                return True
        else:
            if day <= 28:
                return True
    return False

if is_day(Y, M, D):
    print(is_season(M))
else:
    print(-1)
