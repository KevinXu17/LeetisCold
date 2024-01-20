## https://leetcode.com/problems/different-ways-to-add-parentheses/description/

"""
    Divide and Conquer  ++ memo or @cache to function
"""

def diffWaysToCompute(expression):
    ## TODO Memo
    dic_map = {}

    def helper(l, r):
        if (l, r) in dic_map:
            return dic_map[(l, r)]
        elif expression[l: r + 1].isdigit():
            dic_map[(l, r)] = [int(expression[l:r + 1])]
            return [int(expression[l: r + 1])]
        res = []
        for i in range(l, r + 1):
            if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
                ## TODO Divide
                ls = helper(l, i - 1)
                rs = helper(i + 1, r)
                ## TODO Conquer
                for ll in ls:
                    for rr in rs:
                        if expression[i] == '+':
                            res.append(ll + rr)
                        elif expression[i] == '*':
                            res.append(ll * rr)
                        else:
                            res.append(ll - rr)
        dic_map[(l, r)] = res
        return res

    return helper(0, len(expression) - 1)


res = diffWaysToCompute("2-1-1")
for i in res:
    print(i)