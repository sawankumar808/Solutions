class Solution:
    def decodeString(self, s: str) -> str:
        countst = []
        stringst = []
        number = 0
        curr = ""
        
        for ch in s:
            if ch.isdigit():  # Issue 1 fixed: argument hata diya
                number = number * 10 + int(ch)  # Issue 2 fixed: int(ch) use kiya
            elif ch == '[':
                countst.append(number)
                stringst.append(curr)
                number = 0
                curr = ""
            elif ch == ']':
                repeatcount = countst.pop()
                prev = stringst.pop()  # Issue 3 fixed: pop() kiya taaki stack se bahar aaye
                
                # Issue 4 fixed: append ki jagah string multiplication aur addition use kiya
                curr = prev + (curr * repeatcount)
            else:
                curr += ch  # Issue 5 fixed: curr.append ki jagah += ch kiya
                
        return curr