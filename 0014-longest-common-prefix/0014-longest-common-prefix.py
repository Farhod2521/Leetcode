class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Eng qisqa stringni topamiz
        shortest = min(strs, key=len)

        # Eng qisqa stringning har bir harfini qolgan stringlar bilan taqqoslaymiz
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]

        return shortest