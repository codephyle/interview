# ENCODE AND DECODE STRINGS

# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded back to the original list of strings.

# So Machine 1 does:
#     string encoded_string = encode(strs);

# and Machine 2 does:
#     vector<string> strs2 = decode(encoded_string);
#     strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.
# You are not allowed to solve the problem using any serialize methods (such as eval).


# Example 1:
#     Input: dummy_input = ["Hello","World"]
#     Output: ["Hello","World"]

#     Explanation:
#         Machine 1:
#         Codec encoder = new Codec();
#         String msg = encoder.encode(strs);
#         Machine 1 ---msg---> Machine 2

# https://leetcode.com/problems/encode-and-decode-strings/

class Codec:

    def encode(self, strs):
        # return "π".join(strs)
        encoded = ['%d:' % len(s) + s for s in strs]
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        # return s.split("π")
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs

        