class Solution {
    
    final static int[] val = {1000,900,500,400,100,90,50,40,10,9,5,4,1};
    final static String[] sym = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
    
    public String intToRoman(int num) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; num > 0; i++) {
            while (num >= val[i]) {
                sb.append(sym[i]);
                num -= val[i];
            }
        }
        return sb.toString();
    }
}