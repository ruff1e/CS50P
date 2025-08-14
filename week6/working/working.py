import sys
import re


def main():
    print(convert(input("Hours: ")))






def convert(s):

    pattern = (
        r'^(?P<h1>\d{1,2})'
        r'(?:\:(?P<m1>[0-5]\d))?'
        r' (?P<ap1>AM|PM)'
        r' to '
        r'(?P<h2>\d{1,2})'
        r'(?:\:(?P<m2>[0-5]\d))?'
        r' (?P<ap2>AM|PM)$'
    )
    match = re.match(pattern, s)

    if not match:
        raise ValueError
    

    h1 = int(match.group("h1"))
    m1 = int(match.group("m1") or 0)
    ap1 = match.group("ap1")
    h2 = int(match.group("h2"))
    m2 = int(match.group("m2") or 0)
    ap2 = match.group("ap2")

    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError("Hour out of range")

    def to24(h, m, ap):
        if ap == "AM":
            h24 = 0 if h == 12 else h
        else:
            h24 = h if h == 12 else h + 12
        return f"{h24:02d}:{m:02d}"

    start = to24(h1, m1, ap1)
    end   = to24(h2, m2, ap2)

    return f"{start} to {end}"
     
 


if __name__ == "__main__":
    main()
