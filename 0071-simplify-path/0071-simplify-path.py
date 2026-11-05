class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        parts = path.split('/')  # 'splits' ki jagah 'split'
        
        for ch in parts:
            if not ch or ch == '.':
                continue
            elif ch == '..':
                if st:  # Agar stack khali nahi hai, tabhi pop karo
                    st.pop()
            else:
                st.append(ch)
                
        # Saare directories ko '/' se jod kar return kar do
        return '/' + '/'.join(st)