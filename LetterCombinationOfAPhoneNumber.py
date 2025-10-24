class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def rec_add(i, cur):
            if i == len(digits):
                res.append("".join(cur))
                return
            for ch in phone[digits[i]]:
                cur.append(ch)
                rec_add(i + 1, cur)
                cur.pop()
        
        rec_add(0, [])
        return res