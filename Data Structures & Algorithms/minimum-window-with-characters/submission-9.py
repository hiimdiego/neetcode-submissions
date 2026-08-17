class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, window = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        have, need = 0, len(count_t)
        output, output_len = [-1, -1], float("infinity")
        l = 0
        for r, c in enumerate(s):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                if (r - l + 1) < output_len:
                    output = [l, r]
                    output_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = output
        return s[l : r + 1] if output_len != float("infinity") else ""