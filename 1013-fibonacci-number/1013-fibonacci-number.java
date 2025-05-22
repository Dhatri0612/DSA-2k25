class Solution {
    public int fib(int n) {
        if(n==0){
            return 0;
        }else if(n==1){
            return 1;
        }else{
            int first_number=0;
            int second_number=1;
            for(int i=1;i<=n;i++){
                int third_number= first_number+second_number;
                first_number=second_number;
                second_number=third_number;
            }
            return first_number;
        }
    }
}