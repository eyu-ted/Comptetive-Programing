class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer , Integer> Dict = new HashMap();

        for(int i =0 ; i< nums.length; i++){

            if (Dict.containsKey( (target - nums[i]))){
                return new int[] {Dict.get( (target - nums[i])), i };
            } 
            Dict.put(nums[i], i);
        }

        throw new IllegalArgumentException("No two sum solution");
    
    }
}