class Solution {
  List<int> twoSum(List<int> nums, int target){
    for (var i = 0; i < nums.length; i += 1) {
      for (var j = i + 1; j < nums.length; j += 1) {
        if (nums[i] + nums[j] == target) {
          return [i, j];
        }
      }
    }
    return []; 
  }
}