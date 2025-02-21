def solution(cap, n, deliveries, pickups):


    def func(lis):
        p = n - 1
        remain = cap
        point_list = []
        while p >= 0:

            if lis[p] > 0:
                if remain == cap:
                    point_list.append(p)

                if lis[p] >= remain:

                    lis[p] -= remain

                    remain = cap

                else:

                    tmp = lis[p]
                    lis[p] = 0
                    remain -= tmp

                    p -= 1
            else:
                p -= 1

        return point_list

    result = 0
    delivery_point = func(deliveries)
    pickup_point = func(pickups)

    for i in range(max(len(delivery_point), len(pickup_point))):
        if i < len(delivery_point) and i < len(pickup_point):
            result += (max(delivery_point[i], pickup_point[i]) + 1) * 2
        elif i < len(delivery_point):
            result += (delivery_point[i] + 1) * 2

        elif i < len(pickup_point):

            result += (pickup_point[i] + 1) * 2






    return result
