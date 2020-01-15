# Filename:beer.py

price = 2
gaizi = 0
kongping = 0

money = 10

while money >= price:
    result = money / price
    print(result)
    money = money % price
    kongping = money / price
    gaizi = kongping
    while kongping >= 2:
        result = result + kongping / 2
        print(result)
        kongping = kongping % 2 + kongping / 2
        gaizi = gaizi + kongping / 2
    while gaizi >= 4:  # 9G  1P  => 9R
        result = result + gaizi / 4
        print(result)
        kongping = kongping + gaizi / 4
        gaizi = gaizi % 4
        while kongping >= 2:
            result = result + kongping / 2
            print(result)
            kongping = kongping % 2
            kongping = kongping + kongping / 2
            gaizi = gaizi + kongping / 2
        print(result)
        
    
print(result)



