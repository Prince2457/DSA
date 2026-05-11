from collections import defaultdict
def group_anagram(strs):
    groups = defaultdict(list)
    for word in strs:
        sorted_words = ''.join(sorted(word))
        groups[sorted_words].append(word)
    return list(groups.values())    