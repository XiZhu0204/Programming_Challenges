from typing import List

def two_sum(nums: List[int], target:int) -> List[int]:
    seen_vals = {}
    for i, num in enumerate(nums):
        needed_num = target - num
        if needed_num in seen_vals:
            return [i, seen_vals[needed_num]]
        seen_vals[num] = i

def main():
    test_1 = ([2, 7, 11, 15], 9)
    test_2 = ([3, 2, 4], 6)
    test_3 = ([3, 3], 6)
    test_4 = ([3, 5, 7, 9, 1, 2, 4], 16)
    test_5 = ([1, 2, 3, 5, 1, 6, 8], 14)

    try:
        assert set(two_sum(test_1[0], test_1[1])) == set([0, 1])
        assert set(two_sum(test_2[0], test_2[1])) == set([1, 2])
        assert set(two_sum(test_3[0], test_3[1])) == set([0, 1])
        assert set(two_sum(test_4[0], test_4[1])) == set([2, 3])
        assert set(two_sum(test_5[0], test_5[1])) == set([5, 6])
    except AssertionError:
        print("Tests failed")
        return
    print("Tests success")

if __name__ == "__main__":
    main()