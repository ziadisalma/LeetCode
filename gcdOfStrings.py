class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        // Check if the concatenation of the strings is the same
        if str1+str2 != str2+str1:
            return ""
        // if it's the same, find the largest common divisor of the lengths of the strings 
        gcd_length= math.gcd(len(str1), len(str2))
        // return the first string in str1 with length of gcd
        return str1[:gcd_length]
        
