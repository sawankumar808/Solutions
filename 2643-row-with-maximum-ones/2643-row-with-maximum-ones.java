class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        int trow=mat.length;
        int tcol=mat[0].length;
        int maxrow=0;
        int maxone=0;
        for(int i=0;i<trow; i++){
            int count=0;
            for(int j=0;j<tcol; j++){
                if(mat[i][j]==1){
                count++;
                }
            }if(count>maxone){
                maxone=count;
                maxrow=i;
            }
            

        }
        
        return new int[]{maxrow, maxone};
        
    }
}