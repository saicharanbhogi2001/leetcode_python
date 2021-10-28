class Solution {
public:
    int mySqrt(int x) {
        if(x==0)
        {
            return 0;
        }
        long long int l=1,h=x/2;
        long long int result=1;
        while (l<=h)
        {
            long long int mid=(l+h)>>1;
            if (mid*mid==x)
            {
                return mid;
            }
            else if (mid*mid>x)
            {
                h=mid-1;
                
            }
            else
            {
                l=mid+1;
                result=mid;
            }
            
        }
        return result;    
        
        
    }
};