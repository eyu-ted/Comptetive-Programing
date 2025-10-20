class Solution {
    public int lengthOfLongestSubstring(String s) {

        int left = 0;
        HashMap<Character, Integer> count = new HashMap<>();
        int maxx = 0;
        for(int r = 0; r<s.length(); r++){
            char c = s.charAt(r);
            count.put(c , count.getOrDefault(c,0)+1);

            while (count.get(c) >1 && r>left){
                char lc = s.charAt(left);
                count.put(lc, count.getOrDefault(lc, 0)- 1);
                left++;
            }
            maxx = Math.max(maxx,r-left+1);



        }
        return maxx;
        
    }
}