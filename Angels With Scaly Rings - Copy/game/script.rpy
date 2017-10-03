## Work in progress, I have 0 of the assets needed.
## All characters, besides Max, are not mine.

define r = Character("Remy")
define b = Character("Bryce")
define wbr = Character("Written By Remy")
define m = Character("Max")
define a = Character("Argo")
define h = Character("Heli")
define l = Character("Lucki")
define j = Character("Aoi")

label start:

    scene black

    wbr "Hey! I'm sorry I'm busy, but meet me at the library at 3:05 PM. I'll see you there, hopefully.      - Remy."

    scene bg_library1
    with Dissolve(1.0)

    "So... this is where Remy wanted me to meet him..."
    
    "Hm? What's that noise?"
    
    play music "Morning.mp3" fadeout 1
    queue music "Morning.mp3"
    show remy at center 
    with moveinright
    
    r "Oh, hey! I'm glad you made it just fine. Any issues making it?"
    
    menu: 
        "Yeah, thanks for not leaving directions.":
            jump choice1_yes
        
        "Nope, just took a bit of walking.":
            jump choice2_no
    
label choice1_yes:
    
    $ menu_flag = True
    
    r "Well, jeez... I'm sorry. I'll make sure to include them next time."
    
    r "Did you at least enjoy the walk here?"
    
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
    
    r "Well... if you say so."
    
    show remy left at left
    with move
    
    show bryce at right
    with moveinright
    
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
    "Thank you for testing the demo."
    
    jump choice3_done
label choice3_done:
    
    return
    
    jump choice4_no
label choice4_no:
    
    b "What, not in the mood to get shitfaced?"
    
    m "Maybe later, I promised the rest of the day to Remy."
    
    b "Well, that's understandable. Just know that you still have work tomorrow."
    
    m "Yes, sir."
    
    b "Catch you guys later."
    
    r "Goodbye, chief. Have a wonderful day."
    
    show bryce left at offscreenright 
    with move
    
    r "You didn't promise anything... Are you sure you wanted to stay?"
    
    m "Trust me, there is more to life than drinking your brain cells away."
    
    r "Really? Is that what you humans are like?"
    
    m "Sometimes it is fun to burn brain cells, so..."
    
    m "No."
    
    r "You gave me false hopes, Max."
    
    jump choice4_done
label choice4_done:
    
    r "But... I just need to put this one last box away and we should be fine to roam around at our pleasure. If it isn't a bother, can you put it away for me?"
    
    menu:
      
        "Can do.":
            jump choice5_yes
        
        "Do I need to?":
            jump choice6_no
            
        "You owe me.":
            jump choice7_yat
            
label choice5_yes:

    m "Sure thing, Remy. Just... where do I need to put it?"
    
    r "On top of that shelf. You should be able to reach it... I hope."
    
    show remy left at offscreenleft
    with move
       
    "Hey... this isn't that heavy."
    
    r "You got it, Max? Need any help?" 
    
    m "Nah, it's ok! Thank you for offering, though."
    
    with vpunch
    
    m "And... There we go."
    
    r "Let me see."
    
    show remy left at middle
    with move
    
    r "That's correct! Thanks, Maxy."
    
    r "It's a little hard for me to move things. You know, I'm clumsy."
    
    r "Anyways, I have something to take care of. I'll be quick! Probably, I will be gone for five minutes. I just need to clock out."
    
    r "Feel free to look around while I'm gone!"
    
    show remy at offscreenleft
    with move
    
    jump choice5_done
    
label choice6_no

    r "Seriously? It's only one box."
    
    m "I'm aware. And it's also not my job."
    
    r "You're impossible..."
    
    with vpunch
    
    m "See? It wasn't that bad."
    
    r "..."
    
    m "Oh, cheer up, sourpuss."
    
    r "I'll be back soon. I need to clock out. Stay here."
    
    show remy at offscreenleft 
    with move
    
    jump choice6_done
    
label choice7_yat
    
    m "Sure, but you owe me one."
    
    r "Really? Like what?" 
    
    m "How about dinner? Tonight at your place?"
    
    r "Hm... interesting offer."
    
    r "Alright, dinner it is."
    
    "Why is this box so heavy...? What's in here?"
    
    with vpunch
    
    m "That was... a heavy box. What's in there?"
    
    r "Just a few books, that's all."
    
    r "Anyways, let me leave for a few minutes. I need to clock out, then we can roam around to our pleasure."
    
    r "Feel free to look around the library."
    
    show remy at offscreenleft
    with move
    
    jump choice7_done
    
label choice5_done
label choice6_done
label choice7_done
    
    "Hm... maybe I should get a job in the library."
    
    scene black
    with dissolve(1.0)
    
    "Ten minutes later."
    
    scene bg_library1
    with dissolve(1.0)

    show remy left at middle
    with move
    
    r "Hey, sorry I took so long. New worker here, and he needed to be shown around by me."
    
    m "Hey, it's fine. You do what you need to do."
    
    r "I'm not sure why I was chosen, though."
    
    r "I'm the clumsyist member that works here, and my only purpose is to be a laughing stock, I guess." 
    
    m "Hey, don't say that... People don't laugh at you."
    
    m "And if they do, I'll just kick their shins."
    
    r "You and your shin-kicking..."
    
    m "Hey! It works, doesn't it?" 
    
    r "I guess it does. 
    
    m "So, cutie, where would you like to go?"
    
    r "How about the park?"
    
    m "I swear, you have a fetish with parks..."
    m "Everytime we go out, we always go to the park."
    m "Not like I'm complaining, but it does get a little repetitive."
    
    r "I guess you're right. Where would you like to go?"
    
    
    menu: 
    
        "The park is great!":
              jump choice8_park 
              
        "How about your place?":
              jump choice9_rhome
              
        "I'd like to check out the beach.":
              jump choice10_beach
             
        "Let's swing by Town Square.":
              jump choice 11_tsquare
              
      
    label choice8_park 
    
    m "Well, I have no problem with the park."
    m "Especially at this time of day. Things can be lively there."
    
    r "I know, right? Now is my favorite time to go, read a book, and just relax." 
	r "It's also fun to hang out and simply let all your problems go."
	r "You know... With summer last year." 
	
	m "Yeah, I remember."
	
	r "Yep. And you've seen the issues I have, so now you know why I like this park."
	r "It's, like.... magical."
	
	m "Magic doesn't exist."
	r "Why do you have to be such a downer?"
	m "I'm not a downer, I'm just pointing out the facts."
	r "Lie to yourself sometimes. It makes life more..."
	r "Bearable." 
	
	m "I guess you could be right... Come on, do you want to stand around all day, or actually go to the park?" 
	r "Alright, enough is enough. Let's go!"
