'''
给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石
的类型，你想知道你拥有的石头中有多少是宝石。J 中的字母不重复，J 和 S中的所有字符都是字母。
字母区分大小写，因此"a"和"A"是不同类型的石头。
示例 1:
输入: J = "aA", S = "aAAbbbb"
输出: 3

示例 2:
输入: J = "z", S = "ZZ"
输出: 0
'''

class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        t=0
        for i in range(0,len(J)):
            for j in range(0,len(S)):

                if J[i]==S[j]:
                    t+=1
        return t
s = Solution()
J ='aA'
S = 'aAAbbbb'
print(s.numJewelsInStones(J,S))
