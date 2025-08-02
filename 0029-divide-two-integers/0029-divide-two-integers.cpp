class Solution {
public:
    int divide(int dividend, int divisor) {
        // Handle overflow case
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }
        
        // Determine the sign of result
        bool negative = (dividend < 0) ^ (divisor < 0);
        
        // Work with positive values to avoid overflow issues
        long long dvd = abs((long long)dividend);
        long long dvs = abs((long long)divisor);
        
        long long result = 0;
        
        // Use bit shifting to find quotient efficiently
        while (dvd >= dvs) {
            long long temp = dvs;
            long long multiple = 1;
            
            // Find the largest multiple of divisor that fits
            while ((temp << 1) <= dvd) {
                temp <<= 1;
                multiple <<= 1;
            }
            
            dvd -= temp;
            result += multiple;
        }
        
        // Apply sign and handle potential overflow
        if (negative) {
            result = -result;
        }
        
        // Ensure result is within 32-bit signed integer range
        return (int)max((long long)INT_MIN, min(result, (long long)INT_MAX));
    }
};