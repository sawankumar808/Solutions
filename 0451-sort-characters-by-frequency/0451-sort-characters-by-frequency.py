class Solution:
    def frequencySort(self, s: str) -> str:
        n=len(s)
        max=0
        ans=[]
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        sort=sorted(freq,key=freq.get, reverse=True)

        for ch in sort:
            ans.append(ch*freq[ch])
        return "".join(ans)
    