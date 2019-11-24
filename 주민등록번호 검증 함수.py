def isleapyear(year):
    x = year
    if year >= 0:
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        else:
            return False

def aa(s):
    return s == ("01" or "03" or "07" or "08" or "10" or "12")
def kk(s):
    return s == ("04" or "06" or "09" or "11")
def ss(s):
    if (int(s[:2]) >= 20):
        y = int(s[:2]) + 1900
    else:
        y = int(s[:2]) + 2000
    return y

def front_ok(s):
    if(ss(s[:2]) == True and s[2:4] == "02"):
        if 1 <= int(s[4:6]) <= 29:
            return True
        else:
            return False
    elif int(s[2:4]) == 2:
        if 1 <= int(s[4:6]) <= 28:
            return True
        else:
            return False
    elif aa(s[2:4]) == True:
        if 1 <= int(s[4:6]) <= 31:
            return True
        else:
            return False
    else:
        if 1 <= int(s[4:6]) <= 30:
            return True
        else:
            return False
def back_ok(s):
    m = 11 - ((2 * int(s[0]) + 3 * int(s[1]) + 4 * int(s[2]) + 5 * int(s[3]) + 6 * int(s[4]) + 7 * int(
        s[5]) + 8 * int(s[7]) + 9 * int(s[8]) + 2 * int(s[9]) + 3 * int(s[10]) + 4 * int(s[11]) + 5 * int(
        s[12])) % 11)
    if int(s[13]) == m % 10 :
        return True
    else:
        return False

def isRRN(s):
    (front, mid, back) = s.partition("-")
    return front_ok(front) and mid == "-" and back_ok(s)

print(isRRN("001012-3187827"))
