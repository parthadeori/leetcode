def lengthOfLongestSubstring(s: str) -> int:
    start = 0
    max_length = 0
    seen = {}

    for end in range(len(s)):
        char = s[end]

        # If we have seen the character and it's inside the current window
        if char in seen and seen[char] >= start:
            start = seen[char] + 1  # Move the start to right of the duplicate

        seen[char] = end  # Update or insert the character’s latest index
        max_length = max(max_length, end - start + 1)

    return max_length


# Example usage
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3
