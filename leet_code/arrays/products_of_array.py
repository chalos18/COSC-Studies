
def productExceptSelf(nums: list[int]) -> list[int]:
    i, prev = 0, 1
    res = []
    while i < len(nums):
        product = 1
        for key, value in enumerate(nums):
            if key != i:
                product = prev * value
                prev = product
        res.append(product)
        prev, product = 1, 1
        i+=1
    return res

nums = [1,2,4,6]
# nums=[1,0]

print(productExceptSelf(nums))