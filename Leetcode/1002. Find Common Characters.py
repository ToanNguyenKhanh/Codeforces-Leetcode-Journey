from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = [float('inf')] * 26
        for word in words:
            temp_freq = [0] * 26
            for char in word:
                temp_freq[ord(char) - ord('a')] += 1
            for i in range(26):
                freq[i] = min(freq[i], temp_freq[i])
        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * freq[i])
        return result


