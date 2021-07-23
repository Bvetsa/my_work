list = [ 7, 10, 13]


def get_lcm(list):
    local_lcm = 1
    while True:
        temp = 0
        for n in list:
            temp = temp + (local_lcm % n)
        if temp == 0:
            return local_lcm  
        local_lcm = local_lcm + 1


    return local_lcm


print(get_lcm(list))