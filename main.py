"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x<=1:
        return x
    else:
        return foo(x-1)+foo(x-2)

# print(foo(15))

def longest_run(mylist, key):
    keep = []
    run = 0
    for i in mylist:
        if i == key:
            # print('found')
            run += 1
        else: 
            if run != 0:
                keep.append(run)
            run = 0
            # print(keep)
    keep.append(run)
    return max(keep)
        
    #     if len(keep) > 1:
    #         if i == keep[0]:
    #             pass
    #         else:
    #             keep = []
    # return len(keep)

# print(longest_run([2,12,12,8,12,12,12,0,12,1], 12))
# print(longest_run([2,12,12,8,12,12,0,12,1,1,1,1,1], 1))

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    


def longest_run_recursive(mylist, key):
    # flag = False
    # longest = 0
    # if len(mylist) == 1:
    #     if mylist[0] == key:
    #         flag = True
    #         longest += 1
    #         print(mylist)
    #         return
    #     else:
    #         return
    
    # final = Result(left_size=longest_run_recursive(mylist[:len(mylist)//2],key),
    #               right_size=longest_run_recursive(mylist[len(mylist)//2:],key),
    #               longest_size = longest,
    #               is_entire_range = flag)
    # return final.longest_size
    if len(mylist) == 0:
        return Result(0, 0, 0, False)

    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    left = longest_run_recursive(mylist[:len(mylist) // 2], key)
    right = longest_run_recursive(mylist[len(mylist) // 2:], key)

    left_size = left.left_size
    right_size = right.right_size

    if mylist[len(mylist) // 2 - 1] == key:
        left_size += right.left_size

    if mylist[len(mylist) // 2] == key:
        right_size += left.right_size

    longest_size = max(left.longest_size, right.longest_size)

    if mylist[len(mylist) // 2 - 1] == key and mylist[len(mylist) // 2] == key:
        longest_size = max(longest_size, left.right_size + right.left_size)

    is_entire_range = (left.is_entire_range and right.is_entire_range)

    return Result(left_size, right_size, longest_size, is_entire_range)


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([2,12,12,8,12,12,0,12,1,1,1,1,1], 1) == 5
    assert longest_run([2,12,12,8,12,12,0,12,1,1,1,1,1], 8) == 1
    assert longest_run([2,12,12,8,12,12,0,12,1,1,1,1,1], 134) == 0

print('!!!TEST!!!! ' + str(longest_run_recursive([2,12,12,8,12,12,0,12,1,1,1,1,1], 8)))
print(longest_run_recursive([1],1))
print(longest_run_recursive([1,1,1,1,1,1,1],1))
print(longest_run_recursive([1,2,3,4,5,6,7],8))
print(longest_run_recursive([1,2,2,3,4,4,5,5,2,2,2,2,2,3],2))
# test_longest_run()