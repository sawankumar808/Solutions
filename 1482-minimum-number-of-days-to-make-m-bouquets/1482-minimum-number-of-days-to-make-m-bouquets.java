class Solution {
    static boolean isValid(int[] bloomDay, int m, int k, int mid){
        int count=0;
        int bouquet=0;
        for(int i=0;i<bloomDay.length;i++){
                if(bloomDay[i]<=mid){
                    count++;
                    if(count==k){
                        bouquet++;
                        count=0;
                    }
                }else{
                    count=0;
                }
        }return bouquet>=m;
        
    }
    public int minDays(int[] bloomDay, int m, int k) {
        if ((long) m * k > bloomDay.length) {
            return -1;
        }
       int s = Integer.MAX_VALUE;
       int e = Integer.MIN_VALUE;
       int ans=-1;

        for (int i=0;i<bloomDay.length;i++) {
            s = Math.min(s, bloomDay[i]);
            e = Math.max(e, bloomDay[i]);

        }while(s<=e){
            int mid=s+(e-s)/2;
            if(isValid(bloomDay,m,k,mid)){
                ans=mid;
                e=mid-1;
            }else{
                s=mid+1;
            }
        }return ans;
    }
}