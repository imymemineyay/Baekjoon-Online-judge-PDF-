select round(avg(DAILY_FEE),0) as AVERAGE_FEE
from car_rental_company_car
where car_type = "suv"
