class Solution {
    public int[] sortedSquares(int[] nums) {
        int l=0;
        int r=nums.length-1;
        int[] result=new int[nums.length];
        int k=nums.length-1;
        while(l<=r){
           int leftSq=nums[l]*nums[l];
           int rightSq=nums[r]*nums[r];
            if(leftSq>rightSq){
                result[k]=leftSq;
                k--;
                l++;
            }else{
                result[k]=rightSq;
                k--;
                r--;
            }
        }
        return result;
    }
}