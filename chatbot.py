def chatbot():
    print("Hiiiiiil, I'm chatbot. Welcome to JSPM hotel")
    while True:
        uinput = input("You: ").lower()
        if "hello" in uinput or "hi" in uinput:
            print("heyy! welcome to our hotel! how can i help you?")
        elif "menu" in uinput:
            print("tea-10 \n pohe-50 \n dosa-68 \n 1dl1-38 \n dhokla-408 \n fafda-20 \nrasgulla-5")
        elif "tea" in uinput:
            print("Tea is a popular beverage made by steeping dried leaves in hot water, offering various flavors and health benefits.")
        elif "pohe" in uinput:
            print("Pohe is a popular Indian breakfast dish made from flattened rice, cooked with spices, peanuts, and vegetables for flavor.")
        elif "dosa" in uinput:
            print("Dosa is a crispy, thin South Indian pancake made from fermented rice and lentil batter, often served with chutney.")
        elif "idli" in uinput:
            print("Idli is a soft, steamed rice and Lentil cake, commonly enjoyed as a breakfast dish with chutney and sambar.")
        elif "dhokla" in uinput:
            print("Dhokla is a steamed, savory snack from Gujarat, made with fermented rice and chickpea flour, often served with chutney.")
        elif "fafda" in uinput:
            print("Fafda is a crispy, savory snack from Gujarat, made from chickpea flour dough, fried and served with spicy chutney.")
        elif "rasgulla" in uinput:
            print("Rasgulla is a popular Bengali sweet made from soft, spongy white cheese balls soaked in sugary syrup, delightfully sweet.")
        elif "bye" in uinput:
            print("goodbye! have a great day and visit again!")
            break
        else:
            print("sorry, i did not get your query, try using the items in the menu :D")

chatbot()
