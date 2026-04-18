import random
print("Hello there and welcome to the Chrys Ultimate Afican Quiz Game.")
print("The game is simple:you are given a name of a country and you have to enter the country's capital.\nDont add the accents.\nIf it is wrong"
"you are told the correct answer and if you are right you are congratulated and the game continues."
"\nYou can leave anytime you want and your score would be shown to you")
african_countries={"algeria":"algiers","angola":"luanda","benin":"porto novo","botswana":"gaborone","burkina faso":"ouagadougou",
"burundi":"gitega","cabo verde":"praia","cameroon":"yaounde","central africa republic":"bangui",
"chad":"n'djamena","comoros":"moroni","republic of congo":"brazzaville","congo DRC":"kinshasa",
"cote divoire":"yamoussoukro","djibouti":"djibouti","egypt":"cairo","equatorial guinea":"malabo",
"eritrea":"asmara","estwatini":"mbabane","ethiopia":"addis ababa","gabon":"libreville","gambia":"banjul",
"ghana":"accra","guinea":"conakry","guinea bissau":"bissau","kenya":"nairobi","lesotho":"maseru",
"liberia":"monrovia","libya":"tripoli","madagascar":"antananarivi","malawi":"lilongwe","mali":"bamako",
"mauritania":"nouakchott","mauritius":"port louis","morocco":"rabat","mozambique":"maputo",
"namibia":"windhoek","niger":"niamey","nigeria":"abuja","rwanda":"kigali","sao tome and principe":"sao tome",
"senegal":"dakar","seychelles":"victoria","sierra leone":"freetown","somalia":"mogadishu",
"south africa":"pretoria","south sudan":"juba","sudan":"khartoum","tanzania":"dodoma","togo":"lome",
"tunisia":"tunis","uganda":"kampala","zambia":"lusaka","zimbabwe":"harare"}
game_start=int(input("Enter 1 to start game and 2 to end and view score\n"))
correct_answers=0
total_answers=0
while True:
    country,capital=random.choice(list(african_countries.items()))
    if game_start==1:
        your_country=input(f"Enter the capital of {country.title()}\n").lower()
        if african_countries[country].strip()==your_country.strip():
            correct_answers+=1
            total_answers+=1
            print("Congrats,that is correct. Moving to the next one....")
        else:
            print(f"Wrong,Geography left the chat.The correct answer is: {african_countries[country].title()}.  Moving on...")
            total_answers+=1
    if game_start==2 or your_country=="2":
        if correct_answers>=total_answers/2:
            print(f"You got {correct_answers} out of {total_answers}. Well done.\nThanks for trying the Chrys Ultimate African Quiz.")
            break
        else:
            print(f"You got {correct_answers} out of {total_answers}. Not good at all.\nThanks for trying the Chrys Ultimate African Quiz.")
            break