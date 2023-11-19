def solution(chicken):
    coupon = chicken
    total = 0

    while coupon >= 10:
        eaten = coupon // 10
        total += eaten
        coupon = coupon % 10 + eaten
    return total

# 오답
# def solution(chicken):
#     service = chicken // 10
#     coupon = service % 10
#     total = service

#     while True:
#         if service >= 10:
#             service //= 10
#             coupon += service % 10
#             total += service
#         else:
#             break

#     if coupon >= 10:
#         total += (coupon // 10)

#     return total


chicken = 1081
print(solution(chicken))
