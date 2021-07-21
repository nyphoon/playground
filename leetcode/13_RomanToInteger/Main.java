import java.io.*;
import java.util.*;  //HashMap

class Solution {
    public int practice(String s) {
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        Character c;
        Integer ans = 0;
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            ans += map.get(c);
        }
        return ans;
    }

    public int convert(ArrayList<Integer> nums) {
        // System.out.println(nums);
        var sz = nums.size();
        if(sz == 0){
            return 0;
        }
        int num = nums.get(0);
        for(int i=1; i<sz; i++){
            num-= nums.get(i);
        }
        return num;
    }

    public int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        Character c;
        Integer ans = 0, num = 0;
        ArrayList<Integer> nums = new ArrayList<Integer>();
        for (int i = s.length()-1; i>=0 ; i--) {
            c = s.charAt(i);
            // System.out.println(c);
            num = map.get(c);
            Integer sz = nums.size();
            if(sz>0 && num >= nums.get(sz-1)){
                ans += this.convert(nums);
                nums = new ArrayList<Integer>();
                nums.add(num);
            }else{
                nums.add(num);
            }
        }
        if(nums.size()>0){
            ans += this.convert(nums);
        }
        return ans;
    }
}

// Runtime: 6 ms, faster than 33.20% of Java online submissions for Roman to Integer.
// Memory Usage: 39.5 MB, less than 36.33% of Java online submissions for Roman to Integer.
public class Main { 
    public static void main(String args[]) { 
        var s = new Solution();
        System.out.println( s.romanToInt("III") );
        System.out.println( s.romanToInt("IV") );
        System.out.println( s.romanToInt("IX") );
        System.out.println( s.romanToInt("LVIII") );
        System.out.println( s.romanToInt("MCMXCIV") );
    } 
}