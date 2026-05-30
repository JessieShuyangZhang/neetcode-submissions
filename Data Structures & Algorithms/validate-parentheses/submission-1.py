class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        lefts = ['(', '{','[']
        set_lefts = set(lefts)
        rights = [')','}',']']
        rtl = dict(zip(rights,lefts))
        for el in s: 
            if el in set_lefts:
                arr.append(el)
            else:
                if len(arr) == 0:
                    return False
                last = arr.pop()
                if last != rtl[el]:
                    return False

        return len(arr) == 0