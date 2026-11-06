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
        for letter in pw:
            if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                containsCapital = True
        if not containsCapital:
            return False
        return True

    else:
        return False