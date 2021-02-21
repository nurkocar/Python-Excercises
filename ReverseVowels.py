    def reverseVowels(self, s: str) -> str:
        v = ['a', 'e', 'i', 'o', 'u']
        
        s_vowels = [i for i in s if i.lower() in v]
        
        s = list(s)
        
        for i in range(len(s)):
            if s[i].lower() in v:
                s[i] = s_vowels.pop()
        return ''.join(s)
            