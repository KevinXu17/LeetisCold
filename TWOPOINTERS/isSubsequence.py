# https://leetcode.com/problems/is-subsequence/description/

# class Solution {
# public:
#     bool isSubsequence(string s, string t) {
#         if (s.length() > t.length()) return false;
#         int idx = 0;
#         for (auto tt : t) {
#             if (tt == s[idx]) {
#                 idx++;
#             }
#         }
#         return idx == s.length();
#     }
# };