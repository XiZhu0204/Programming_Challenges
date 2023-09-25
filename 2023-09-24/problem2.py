from typing import Dict

def is_anagram(s: str, t: str) -> bool:
    s_letter_counter = create_counter(s)
    t_letter_counter = create_counter(t)
    return s_letter_counter == t_letter_counter

def create_counter(s: str) -> Dict[str, int]:
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def main():
    test_1 = ["anagram", "nagaram"]
    test_2 = ["rat", "car"]
    test_3 = ["abcde", "abdce", "badec"]

    try: 
        assert is_anagram(test_1[0], test_1[1])
        assert is_anagram(test_1[1], test_1[0])
        assert not is_anagram(test_2[0], test_2[1])
        assert is_anagram(test_3[0], test_3[1])
        assert is_anagram(test_3[0], test_3[2])
        assert is_anagram(test_3[1], test_3[2])
    except AssertionError:
        print("Tests failed")
        return
    print("Tests success")

if __name__ == "__main__":
    main()
