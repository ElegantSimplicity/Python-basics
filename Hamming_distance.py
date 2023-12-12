""" Program 101
Hamming distance is the number of characters that differ between two strings.
Bài này liên quan đến cosin similarity (đồng dạng cosine)
Hai khái niệm đều rất thú vị
"""

def hamming_distance(str1, str2):
    # Check if the strings have the same length
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length.")

    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1 
    return distance

print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strungg"))