12. Integer to Roman

https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
    #def int_to_roman(num):
        sym_dic = {
            'M': 1000, 
            'CM': 900, 'D': 500, 'CD': 400,'C': 100, 
            'XC': 90, 'L': 50, 'XL': 40,'X': 10, 
            'IX': 9, 'V': 5, 'IV': 4,'I': 1
            #for문 돌때 큰수부터 돌게 하려면 큰수부터
        }
        answer = ''
        
        for sym, val in sym_dic.items():
            while num >= val:
                answer += sym
                num -= val         
        return answer
    

