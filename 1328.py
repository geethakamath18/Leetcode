#LeetCode problem 1328: Break a Palindrome
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(0, len(palindrome)//2):
            if(palindrome[i]!='a'):
                return(palindrome[:i]+'a'+palindrome[i+1:])
        return (palindrome[:len(palindrome)-1]+'b') if palindrome[:-1] else ''

                