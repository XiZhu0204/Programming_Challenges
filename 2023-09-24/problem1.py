from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    set_nums = set(nums)
    return len(set_nums) != len(nums)

def main():
    test_1 = [1, 2, 3, 1]
    test_2 = [1, 2, 3, 4]
    test_3 = [1]
    test_4 = [1, 1]
    test_5 = [1, 1, 2, 2, 3, 3, 3, 5, 6, 7]

    try: 
        assert contains_duplicate(test_1)
        assert not contains_duplicate(test_2)
        assert not contains_duplicate(test_3)
        assert contains_duplicate(test_4)
        assert contains_duplicate(test_5)
    except AssertionError:
        print("Tests failed")
        return
    print("Tests success")

if __name__ == "__main__":
    main()