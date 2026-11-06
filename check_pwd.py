"""
Must be between 8 and 20 characters (inclusive)
Must contain at least one lowercase letter (standard English alphabet)
Must contain at least one uppercase letter (standard English alphabet)
Must contain at least one digit
Must contain at least one symbol from: ~`!@#$%^&*()_+-=
(copy and paste to avoid missing characters) These are the only symbols that will meet this requirement.
Other symbols may be present, but they won't satisfy this requirement.
"""

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
        if not containsCapital or not containsLower or not containsDigit or not containsSymbol:
            return False
        return True

    else:
        return False