class Solution {
    List<List<Integer>> result = new ArrayList<>();
    int[][] graph;
    public HashMap<Integer , int[]> mapper = new HashMap();
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        this.graph = graph;
        

        for(int i = 0; i<graph.length ; i++){
            mapper.put(i, graph[i]);
        }
        System.out.println(mapper);
        dfs(0,new ArrayList<>(List.of(0)));

        return result;
        
        
    }

    public void dfs(Integer node, ArrayList path){
        if (node == graph.length -1){
            result.add(new ArrayList(path));
            return;
        }

        for(int neigh: mapper.get(node)){
            path.add(neigh);
            dfs(neigh,path);
            path.remove(path.size()-1);
        }
    }
}