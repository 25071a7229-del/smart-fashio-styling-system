# =========================================================
#      SMART FASHION STYLING RECOMMENDATION SYSTEM
# =========================================================

import random

# ================= WELCOME SCREEN =================

print("\n===================================================")
print("        SMART FASHION STYLING SYSTEM")
print("===================================================\n")

# ================= USER INPUT =================

name = input("Enter Your Name : ")
gender = input("Enter Gender (Male/Female) : ")
occasion = input("Enter Occasion (Casual/Party/Formal/Traditional) : ")
favorite_color = input("Enter Favorite Color : ")
weather = input("Enter Weather (Sunny/Rainy/Winter) : ")

print("\n===================================================")
print("Hello,", name)
print("Your Fashion Recommendations Are Ready!")
print("===================================================\n")

# ================= OUTFIT COLLECTIONS =================

# Party Wear
party_male = [
    f"{favorite_color} blazer with black jeans and white sneakers",
    f"{favorite_color} stylish shirt with grey trousers",
    f"{favorite_color} leather jacket with dark blue jeans",
    f"{favorite_color} party wear shirt with black pants",
    f"{favorite_color} printed shirt with slim fit jeans"
]

party_female = [
    f"{favorite_color} western dress with silver heels",
    f"{favorite_color} stylish top with black jeans",
    f"{favorite_color} long gown with matching accessories",
    f"{favorite_color} crop top with white skirt",
    f"{favorite_color} glittery outfit with denim jeans"
]

# Formal Wear
formal_male = [
    f"{favorite_color} formal suit with tie",
    f"{favorite_color} blazer with pencil pants",
    f"{favorite_color} office wear shirt with trousers",
    f"{favorite_color} full sleeve shirt with formal shoes"
]

formal_female = [
    f"{favorite_color} saree with elegant jewellery",
    f"{favorite_color} formal kurti with leggings",
    f"{favorite_color} office wear long frock",
    f"{favorite_color} business outfit with handbag"
]

# Casual Wear
casual_male = [
    f"{favorite_color} casual t-shirt with jeans",
    f"{favorite_color} hoodie with joggers",
    f"{favorite_color} polo t-shirt with shorts",
    f"{favorite_color} sweatshirt with cargo pants"
]

casual_female = [
    f"{favorite_color} casual top with jeans",
    f"{favorite_color} oversized t-shirt with leggings",
    f"{favorite_color} denim jacket with skirt",
    f"{favorite_color} comfortable kurti with jeans"
]

# Traditional Wear
traditional_male = [
    f"{favorite_color} kurta with white pajama",
    f"{favorite_color} sherwani with sandals",
    f"{favorite_color} traditional dhoti outfit",
    f"{favorite_color} ethnic kurta with jeans"
]

traditional_female = [
    f"{favorite_color} silk saree with jewellery",
    f"{favorite_color}
