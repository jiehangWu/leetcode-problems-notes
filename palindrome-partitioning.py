# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
# Example "aab"
# Output: [["aa", b]. ["a", "a", "b"]]

def partition(s):
    res = []
    dfs(s, [], 0, res)
    return res

def dfs(s, path, pos, res):
    if pos >= len(s):
        res += [path]
        return
    for i in range(pos, len(s)):
        substring = s[pos:i+1]
        if substring == substring[::-1]:
            dfs(s, path+[substring], i+1, res)
    return

print(partition("aab"))