my_character = {"height":"170cm",
                "age":"24",
                "sex":"male"}

answer = input("height,age or sex")
if answer in my_character:
    result = my_character[answer]
    print(result)
