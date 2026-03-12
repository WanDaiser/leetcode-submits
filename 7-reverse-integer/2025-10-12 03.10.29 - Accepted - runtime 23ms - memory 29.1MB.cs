public class Solution
{
    public int Reverse(int x)
    {
        long MIN_INT = -2147483648L; 
        long MAX_INT = 2147483647L; 

        long num = x; 
        long reversedNum = 0;

        int sign = num < 0 ? -1 : 1;
        num = Math.Abs(num);

        while (num != 0)
        {
            long pop = num % 10;
            reversedNum = reversedNum * 10 + pop;
            num /= 10;
        }

        reversedNum *= sign;

        if (reversedNum < MIN_INT || reversedNum > MAX_INT)
            return 0;

        return (int)reversedNum;
    }
}
