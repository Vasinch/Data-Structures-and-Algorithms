def longest_common_substring(s1, s2):
    dp, mxl, endi = {}, 0, 0

    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                dp[i, j] = dp.get((i-1, j-1), 0) + 1
                if dp[i, j] > mxl:
                    mxl, endi = dp[i, j], j
    if mxl == 0:
        print("No common substring.")
    else:
        ans = s2[endi - mxl + 1:endi + 1]
        print(ans, mxl if mxl else "", sep="\n")

longest_common_substring(input(), input())
