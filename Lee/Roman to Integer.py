13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/description/
class Solution:
    def romanToInt(self, s: str) -> int:
        sym_dic = {
            'M': 1000, 'D': 500, 'C': 100,
            'L': 50, 'X': 10, 'V': 5, 'I': 1
        }
        prev_val = 0
        answer = 0
        print("ss",s) #IV
        for i in s:
            val = sym_dic[i] #안에서 정의해야함 문자 하나씩
            if val > prev_val:
                answer += val - prev_val*2 #현재값이이전값보다 크면 이전값을 두번 뺌
                #IV 이면 V를 처리할때  
                # 1(answer) + 5(val) -1(prev_val) -1(prev_val) 해야 4가 나옴 
            else:
                answer += val
            prev_val = val # 이전 숫자 재설정
        return answer




