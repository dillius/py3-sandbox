from typing import List


class Array:
    def addBinary1(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []

        for i in range(n - 1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2 == 1:
                answer.append("1")
            else:
                answer.append("0")

            carry //= 2

        if carry == 1:
            answer.append("1")
        answer.reverse()

        return "".join(answer)

    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y > 0:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n):
            idx = n - 1 - i

            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits

        return [1] + digits

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        read = 0

        while write < len(nums):
            if read < len(nums):
                if nums[read] != 0:
                    nums[write] = nums[read]
                    write += 1
                read += 1
            else:
                nums[write] = 0
                write += 1

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        front = 0
        end = len(nums) - 1

        total = nums[front] + nums[end]
        while total != target:
            if total < target:
                front += 1
            elif total > target:
                end -= 1
            total = nums[front] + nums[end]

        return [front, end]

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in checked:
                return [i, checked[comp]]
            checked[nums[i]] = i

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, val in enumerate(nums):
            comp = target - val
            if comp in checked:
                return [i, checked[comp]]
            checked[val] = i


def main():
    print(Array().addBinary("1110", "101101"))
    print(Array().plusOne([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    zeroes_test = [0, 1, 0, 3, 12]
    Array().moveZeroes(zeroes_test)
    print(zeroes_test)
    print(Array().twoSum([2, 7, 11, 15], 9))
    print(Array().twoSum([-1, -2, -3, -4, -5], -8))
    print(Array().twoSum([-3, 4, 3, 90], 0))


if __name__ == "__main__":
    main()
