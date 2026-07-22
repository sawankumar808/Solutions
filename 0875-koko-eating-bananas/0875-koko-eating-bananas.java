class Solution {
    static boolean isValid(int[] piles, int h,int mid){
        long totalh=0;
        long ans=0;
        for(int i=0;i<piles.length;i++){
            ans=(piles[i]+mid-1)/mid;
                totalh+=ans;
            }
            if(totalh<=h){
                return true;
            }else{
                return false;
        }

    }
    public int minEatingSpeed(int[] piles, int h) {
        int n=piles.length;
        int s=1;
        int max=0;
        int ans=0;
        for(int i=0;i<n;i++){
            if(piles[i]>max){
                max=piles[i];
            }
        }
            int e=max;
            while(s<=e){
                int mid=s+(e-s)/2;
                if(isValid(piles, h, mid)){
                    ans=mid;
                    e=mid-1;
                }else{
                    s=mid+1;

                }
            
        }return ans;
    }
}