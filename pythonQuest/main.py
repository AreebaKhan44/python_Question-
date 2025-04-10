# from collections import Counter

# def reverse_string(s):
#     print(s[::-1])

# def is_palindrome(s):
#     print(s == s[::-1])

# def remove_duplicates(s):
#     print("".join(dict.fromkeys(s)))

# def first_non_repeating_character(s):
#     counts = Counter(s)
#     for char in s:
#         if counts[char] == 1:
#             print(char)
#             return
#     print(None)

# def count_character_occurrences(s):
#     print(Counter(s))

# def reverse_words(sentence):
#     print(" ".join(sentence.split()[::-1]))

# def are_anagrams(s1, s2):
#     print(Counter(s1) == Counter(s2))

# def longest_unique_substring(s):
#     seen, start, max_length, max_substr = {}, 0, 0, ""
#     for i, char in enumerate(s):
#         if char in seen and seen[char] >= start:
#             start = seen[char] + 1
#         seen[char] = i
#         if i - start + 1 > max_length:
#             max_length = i - start + 1
#             max_substr = s[start:i+1]
#     print(max_substr)

# def atoi(s):
#     try:
#         print(int(s))
#     except ValueError:
#         print(None)

# def run_length_encoding(s):
#     encoded, i = "", 0
#     while i < len(s):
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             i += 1
#             count += 1
#         encoded += s[i] + str(count)
#         i += 1
#     print(encoded)

# def most_frequent_character(s):
#     print(max(Counter(s), key=Counter(s).get))

# def find_all_substrings(s):
#     print([s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)])

# def is_rotation(s1, s2):
#     print(len(s1) == len(s2) and s2 in (s1 + s1))

# def remove_whitespaces(s):
#     print(s.replace(" ", ""))

# def is_valid_shuffle(s1, s2, s3):
#     print(Counter(s1 + s2) == Counter(s3))

# def to_title_case(s):
#     print(s.title())

# def longest_common_prefix(strs):
#     if not strs: 
#         print("")
#         return
#     prefix = strs[0]
#     for s in strs[1:]:
#         while not s.startswith(prefix):
#             prefix = prefix[:-1]
#             if not prefix: 
#                 print("")
#                 return
#     print(prefix)

# def string_to_char_array(s):
#     print(list(s))

# def url_encode_spaces(s):
#     print(s.replace(" ", "%20"))

# def sentence_to_acronym(sentence):
#     print("".join(word[0].upper() for word in sentence.split()))

# def contains_only_digits(s):
#     print(s.isdigit())

# def word_count(s):
#     print(len(s.split()))

# def remove_character(s, char):
#     print(s.replace(char, ""))

# def shortest_word(s):
#     words = s.split()
#     print(min(words, key=len) if words else "")

# def longest_palindromic_substring(s):
#     if not s:
#         print("")
#         return
#     start, max_length = 0, 0
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             if s[i:j+1] == s[i:j+1][::-1] and j - i + 1 > max_length:
#                 start, max_length = i, j - i + 1
#     print(s[start:start+max_length])










from collections import Counter

def reverse_string(s):
    print("Reversed String:", s[::-1])

def is_palindrome(s):
    print("Is Palindrome:", s == s[::-1])

def remove_duplicates(s):
    print("Remove Duplicates:", "".join(dict.fromkeys(s)))

def first_non_repeating_character(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            print("First Non-Repeating Character:", char)
            return
    print("First Non-Repeating Character: None")

def count_character_occurrences(s):
    print("Count Character Occurrences:", Counter(s))

def reverse_words(sentence):
    print("Reverse Words:", " ".join(sentence.split()[::-1]))

def are_anagrams(s1, s2):
    print("Are Anagrams:", Counter(s1) == Counter(s2))

def longest_unique_substring(s):
    seen, start, max_length, max_substr = {}, 0, 0, ""
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        if i - start + 1 > max_length:
            max_length = i - start + 1
            max_substr = s[start:i+1]
    print("Longest Unique Substring:", max_substr)

def atoi(s):
    try:
        print("String to Integer:", int(s))
    except ValueError:
        print("String to Integer: None")

def run_length_encoding(s):
    encoded, i = "", 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        encoded += s[i] + str(count)
        i += 1
    print("Run Length Encoding:", encoded)

def most_frequent_character(s):
    print("Most Frequent Character:", max(Counter(s), key=Counter(s).get))

def find_all_substrings(s):
    print("Find All Substrings:", [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)])

def is_rotation(s1, s2):
    print("Is Rotation:", len(s1) == len(s2) and s2 in (s1 + s1))

def remove_whitespaces(s):
    print("Remove Whitespaces:", s.replace(" ", ""))

def is_valid_shuffle(s1, s2, s3):
    print("Is Valid Shuffle:", Counter(s1 + s2) == Counter(s3))

def to_title_case(s):
    print("Title Case:", s.title())

def longest_common_prefix(strs):
    if not strs:
        print("Longest Common Prefix:", "")
        return
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                print("Longest Common Prefix:", "")
                return
    print("Longest Common Prefix:", prefix)

def string_to_char_array(s):
    print("String to Character Array:", list(s))

def url_encode_spaces(s):
    print("URL Encoding:", s.replace(" ", "%20"))

def sentence_to_acronym(sentence):
    print("Acronym:", "".join(word[0].upper() for word in sentence.split()))

def contains_only_digits(s):
    print("Contains Only Digits:", s.isdigit())

def word_count(s):
    print("Word Count:", len(s.split()))

def remove_character(s, char):
    print("Remove Character:", s.replace(char, ""))

def shortest_word(s):
    words = s.split()
    print("Shortest Word:", min(words, key=len) if words else "")

def longest_palindromic_substring(s):
    if not s:
        print("Longest Palindromic Substring:", "")
        return
    start, max_length = 0, 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1] and j - i + 1 > max_length:
                start, max_length = i, j - i + 1
    print("Longest Palindromic Substring:", s[start:start+max_length])

if __name__ == "__main__":
    reverse_string("hello")
    is_palindrome("racecar")
    remove_duplicates("aabbcc")
    first_non_repeating_character("aabbcdde")
    count_character_occurrences("aabbcc")
    reverse_words("hello world")
    are_anagrams("listen", "silent")
    longest_unique_substring("abcabcbb")
    atoi("12345")
    run_length_encoding("aaabbcddd")
    most_frequent_character("aabbccddeee")
    find_all_substrings("abc")
    is_rotation("abcd", "dabc")
    remove_whitespaces("hello world")
    is_valid_shuffle("abc", "def", "dabecf")
    to_title_case("hello world")
    longest_common_prefix(["flower", "flow", "flight"])
    string_to_char_array("hello")
    url_encode_spaces("hello world")
    sentence_to_acronym("hello world")
    contains_only_digits("123456")
    word_count("hello world how are you")
    remove_character("hello", "l")
    shortest_word("I am learning Python")
    longest_palindromic_substring("babad")

