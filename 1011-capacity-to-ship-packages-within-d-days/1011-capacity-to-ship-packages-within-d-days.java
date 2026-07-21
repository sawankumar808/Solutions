class Solution {
    static boolean iscorrect(int weigths[], int days, int mid){
        int day=1;
        int dayslength=0;
        for(int i=0;i<weigths.length;i++){

            if(dayslength+weigths[i]<=mid){
                dayslength+=weigths[i];
            }else{
                day++;
                dayslength=weigths[i];
                if(day>days || weigths[i]>mid){
                    return false;
                }


            }
        }return true;
    }
    public int shipWithinDays(int[] weights, int days) {
        int sum=0;
        int n=weights.length;
        for(int i=0;i<n;i++){
            sum+=weights[i];
        }
        int s=0;
        int e=sum;
        int ans=0;
        while(s<=e){
            int mid=s+(e-s)/2;
            if(iscorrect(weights, days, mid)){
                ans=mid;
                e=mid-1;

            }else{
                s=mid+1;

            }
        }return ans;
        
    }
}