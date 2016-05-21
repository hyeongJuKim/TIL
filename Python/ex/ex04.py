# -*- coding: utf-8 -*-

# 자동차 수
cars = 100

# 차에 탈 수 있는 인원
space_in_a_car = 4.0

# 운전사 수
drivers = 30

# 승객원 수
passengers = 90

# 운행되지 않는 차의 수
cars_not_driven = cars - drivers

# 운행되는 차의 수
cars_driven = drivers

# 함께 탈 사람의 수
carpool_capacity = cars_driven * space_in_a_car

# 차마다 타야할 평균 인원 수
average_passengers_per_car = passengers / cars_driven



print "자동차", cars, "대가 있습니다."
print "운전자는", drivers, "명 뿐입니다."
print "오늘은 빈 차가", cars_not_driven, "대일 것입니다."
print "오늘은", passengers, "명 있습니다."
print "함께 탈 사람은", passengers, "명 있습니다."
print "차마다", average_passengers_per_car, "명 정도 씩 타야 합니다." 
