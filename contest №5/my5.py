def polynomial_hash(s):
    return sum(s)#hash_value


def find_longest_anagram_subsequence(arr1, arr2):
    # Создаем словарь для хранения хешей и позиций подотрезков второй последовательности
    hashes = {}
    for i in range(len(arr2)):
        for j in range(i + 1, len(arr2) + 1):
            hash_value = polynomial_hash(arr2[i:j])
            if hash_value not in hashes:
                hashes[hash_value] = []
            hashes[hash_value].append(i)

    # Ищем самый длинный анаграммный подотрезок
    max_len = 0
    #max_subsequence = []
    for i in range(len(arr1)):
        for j in range(i + 1, len(arr1) + 1):
            hash_value = polynomial_hash(arr1[i:j])
            if hash_value in hashes:
                positions = hashes[hash_value]
                for pos in positions:
                    subseq_len = j - i
                    if subseq_len > max_len and arr2[pos:pos + subseq_len] == arr1[i:j]:
                        max_len = subseq_len
                        #max_subsequence = arr1[i:j]

    return max_len

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

print(find_longest_anagram_subsequence(a, b))