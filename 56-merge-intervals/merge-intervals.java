class Solution {
    public int[][] merge(int[][] intervals) {

        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0],b[0]));

        ArrayList<int[]> result = new ArrayList<>();
        result.add(intervals[0]);

        for (int i = 1 ; i<intervals.length; i++){
            int start = intervals[i][0];
            int end = intervals[i][1];
            int[] last = result.get(result.size() - 1);

            if (last[1] >= start){
                last[1] = Math.max(last[1],end);
            }else{
                result.add(intervals[i]);
            }
        }

        return result.toArray(new int[result.size()][]);
        
    }
}