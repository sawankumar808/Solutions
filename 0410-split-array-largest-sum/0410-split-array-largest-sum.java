class Solution {


    static boolean isValid(int nums[], int k ,int mid){
        int paintercount=1;
        int painterlength=0;
        for(int i=0;i<nums.length; i++){
            if(painterlength+ nums[i]<=mid){
                painterlength+=nums[i];



            }else{
                paintercount++;
                painterlength=0;
                if(paintercount>k || nums[i]>mid ){
                    return false;

                }
                else if(nums[i]>mid){
                    return false;

                }else{

                    painterlength+=nums[i];
            }
            

        }

    }return true;
}
    public int splitArray(int[] nums, int k) {
        int n=nums.length;
        int sum=0;
        int ans=-1;
        int s=0;
        
        for(int i=0;i<n;i++){
        
            sum+=nums[i];
        }
        
        int e=sum;
        while(s<=e){
            int mid=s+(e-s)/2;
            if(isValid(nums,k,mid)){
                ans=mid;
                e=mid-1;
            }else{
                s=mid+1;
            
            }
        }return ans;
    }
}