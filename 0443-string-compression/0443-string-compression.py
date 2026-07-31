class Solution:
    def compress(self, chars: List[str]) -> int:
        write=0
        count=1
        for i in range(1,len(chars)+1):
            if i==len(chars) or chars[i]!=chars[i-1]:
                chars[write]=chars[i-1]
                write+=1
                if count>1:
                    for digit in str(count):
                        chars[write]=digit
                        write+=1
                count = 1
            else:
                # Same character mil raha hai, count badhao
                count += 1
        return write

        