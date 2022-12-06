shop_prices = [3000, 2000, 1500000]
user_coupons = [20, 40]

def get_max_discount_price(prices, coupons):
    coupons.sort(reverse=True)      # 오름차순 정렬 .sort() // 내림차순 정렬 .sort(reverse = True) => 1500000, 3000, 2000
    prices.sort(reverse=True)
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price

print(get_max_discount_price(shop_prices, user_coupons))



# 1500000 * 0.6 = 900000
# 3000 * 0.8 = 2400
# 2000
# Total = 904400