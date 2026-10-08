# total = 0
# a = 200
# def count(total):
#     total += 1  
#     return total

# print(count(count(count(0))))

# def local():
#     x = "local"
#     def nonloc():
#         x = "Non local"
#         return x
#     return nonloc()
# print(local())


def local():
    x = "local"
    def nonloc():
        nonloc()
        print(x)

local()
