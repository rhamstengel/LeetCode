class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));

        dp[0][0] = true;

        for (int j = 2; j <= n; j += 2) {
            if (p[j - 1] == '*' && dp[0][j - 2]) {
                dp[0][j] = true;
            }
        }

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (p[j - 1] == '*') {
                    // Two possibilities:
                    // 1. '*' stands for zero of the previous character
                    // 2. '*' stands for one or more of the previous character
                    dp[i][j] = dp[i][j - 2] || 
                               ((p[j - 2] == '.' || p[j - 2] == s[i - 1]) && dp[i - 1][j]);
                } else {
                    if (p[j - 1] == '.' || p[j - 1] == s[i - 1]) {
                        dp[i][j] = dp[i - 1][j - 1];
                    }
                }
            }
        }

        return dp[m][n];
    }
};
