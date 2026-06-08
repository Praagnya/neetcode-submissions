class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs: 
            encoded_str += str(len(i)) + "#" + i
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s): 
            delim = s.find("#", i)
            length = int(s[i:delim])
            str_ = s[delim+1:delim+1+length]
            decoded_str.append(str_)
            i = delim + 1 + length 
        return decoded_str 
