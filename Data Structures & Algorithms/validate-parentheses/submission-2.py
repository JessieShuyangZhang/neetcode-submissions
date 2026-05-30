class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        rtl = { ")" : "(", "]" : "[", "}" : "{" }
        for el in s: 
            if el in rtl:
                if len(arr) == 0 or arr.pop() != rtl[el]:
                    return False                
            else:
                arr.append(el)

        return len(arr) == 0