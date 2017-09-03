# Work in progress, I have 0 of the assets needed.
# All characters, besides Max, are not mine.

define r = Character("Remy")
define b = Character("Bryce")
define wbr = Character("Written By Remy")
define m = Character("Max")

label start:

    scene black

    wbr "Hey! I'm sorry I'm busy, but meet me at the library at 3:05 PM. I'll see you there, hopefully.      - Remy."

    scene bg_library1
    with Dissolve(1.0)

    "So... this is where Remy wanted me to meet him..."
    
    "Hm? What's that noise?"
    
    show eileen happy
    with Dissolve(1.0)
    
    r "Oh, hey! I'm glad you made it just fine. Any issues making it?"
    
    menu: 
        "Yeah, thanks for not leaving directions.":
            jump choice1_yes
        
        "Nope, just took a bit of walking.":
            jump choice2_no
    
label choice1_yes:
    
    $ menu_flag = True
    
    r "Well, jeez... I'm sorry. I'll make sure to include them next time."
    
    jump choice1_done
label choice1_done:
    
label choice2_no:
    
    $ menu_flag = True
    
    r "Really? That's great! I hope you enjoyed some of the sights here."
    
    jump choice2_done
label choice2_done:
    
    m "I did. I also noticed the ice cream man in the park."
    
    r "Yeah, he's nice. His ice cream is quite delicious, it really helps for the hot days here in the library."
    
    m "So, do you work here?"
    
    r "Yes, sir. I work in sorting out the different books and articles. Sometimes its tiring, but someone needs to do it, right?"

    m "Right. After all, I bet the customers love how you sort the books."
    
    r "Well... it isn't always like that. Sometimes some of the high school students come in to ruin some of the books."
    
    r "And due to my old habits of being clumsy, I get blamed for it..."
    
    m "Hey, don't worry about it. Everyone makes mistakes. Even I do, writing this game."
    
    "Hey, I'm not going to lie."
    
    r "Well... if you say s-"
    
    # I'm going to insert Bryce sliding into frame here, don't worry. - Remy
    
    b "Hey, Max. Nice work today."
    
    m "Thanks. Good afternoon."
    
    r "Good afternoon, Chief. What brings you here today?" 
    
    b "Just getting out of the heat. It's hot as hell today."
    
    m "Amen to that."
    
    b "So, Max, what do you say we go out for a beer?" 
    
    menu:
        
        "Sure.":
            jump choice3_yes
            
        "No thanks.":
            jump choice4_no
label choice3_yes:
    
    $ menu_flag = True
    
    b "I knew you would, you alcoholic!"
    
    m "Who got wasted last time?"
    
    b "Both of us!"
    
    r "Wait, Max, you're leaving?"
    
    m "Yeah, I'll see you later?"
    
    r "Well... I may be busy with work. But I'll call you and let you know."
    
    m "Alright, I'm fine with that."
    
    b "Come on, Max. you coming?"
    
    m "On my way!"
    
    m "See you around, Remy."
    
    r "I'll... see you later." 
    
    show black
    with Dissolve(1.0)
    
    "If you see this, its because I didn't add more than this yet."
    "Try again, try to stay with Remy."
    "Thank you for testing the hard demo."
    
    jump choice3_done
label choice3_done:
    
    jump choice4_yes
label choice4_yes:
    
    b "What, not in the mood to get shitfaced?"
    
    m "Maybe later, I promised the restof the day to Remy."
    
    b "Well, that's understandable. Just know that you still have work tomorrow."
    
    m "Yes, sir."
    
    b "Catch you guys later."
    
    r "Goodbye, chief. Have a wonderful day."
    
    
    
    
    

