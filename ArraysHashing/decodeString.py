class Codec:
    """
    Example
    endode(["Hello", "World"]) -> str s
    decode(s) -> ["Hello", "World"]
    s = "5#Hello5#World"
    """
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0

        while i < len(s):
            length = 0
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            string = s[i: i + length]
            res.append(string)
            i = i + length
        return res

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
