def check_pwd(pw: str) -> bool:
    if 8 <= len(pw) <= 20:
        containsCapital = False
        containsLower = False
        containsDigit = False
        containsSymbol = False
        for char in pw:
            if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                containsCapital = True
            if char in "abcdefghijklmnopqrstuvwxyz":
                containsLower = True
            if char in "0123456789":
                containsDigit = True
            if char in "~`!@#$%^&*()_+-=":
                containsSymbol = True
        return containsCapital and containsLower and containsDigit and containsSymbol
    else:
        return False