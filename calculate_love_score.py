def calculate_love_score(name1, name2):
    num1=0
    num2=0
    love_str1 = 'true'
    love_str2 = 'love'
    count = 0
    for letter in (love_str1):
        # print(letter)
        count=name1.lower().count(letter) + name2.lower().count(letter)
        num1+=count;
        # print(f"{letter.upper()} occurs {count} times")

    # print(f"Total = {num1}")

    count = 0
    for letter in (love_str2):
        count=name1.lower().count(letter) + name2.lower().count(letter)
        num2+=count;
        # print(f"{letter.upper()} occurs {count} times")

    # print(f"Total = {num2}") 
    love_score = f"{num1}{num2}"
    print(love_score)

# calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")
