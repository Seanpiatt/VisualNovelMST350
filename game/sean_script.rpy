# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sam", color="#00f")
define r = Character("Rowan", color="#f00")
define b = Character("Sam and Rowan", color="#f0f")
define e = Character("Eraser")
define y = Character("You")

# The game starts here.
# Sam and Rowan enter a world wherethey are 2d stick figures with faces (image or drawn?)
# They are first confused and wonder why they are drawn so crudely
# the writer coughs
# they start arguing with the writer about why they are so crude
# They demand they get sent to the next dimension
# I crumple up a piece of paper and throw it at a portal. 
# thus ends the scen
# Define custom transforms
transform far_left:
    xcenter 0.2
    yalign 1.0

transform middle:
    xcenter 0.5
    yalign 1.0

transform far_right:
    xcenter 0.8
    yalign 1.0

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sean
    play sound "page sean.mp3" volume 0.8
    play music "seanbck.mp3" volume 0.1

    # These display lines of dialogue.
    "{i}Just a totally normal piece of paper...{i}"
    show sam talking sean at far_left  
    show rowan happy sean at far_right
    play sound "drawsean.mp3"
    
    s "That portal travel always makes me feel like I want to puke my guts out..."

    show sam happy sean at far_left
    play sound "drawsean.mp3"

    s "..."
    show sam scared sean at far_left
    show rowan sad sean at far_right
    play sound "drawsean.mp3"

    s "WHAT HAPPENED TO MY GUTS???"
    show sam sad sean at far_left
    show rowan scared sean at far_right
    play sound "drawsean.mp3"
    r "Wh-what happened to my limbs...What happened to my 3rd dimension!..."
    r "I-Its like we are drawn on paper or something!"
    show rowan angry sean at far_right
    play sound "drawsean.mp3"
    r "Where the hell did you send us to Sam!?"
    show sam angry sean at far_left
    play sound "drawsean.mp3"
    s "How the hell should I know? It isn't like we can just pick where we go."
    show sam talking sean at far_left
    play sound "drawsean.mp3"
    s "If I could choose I would be SKY DIVING ACROSS 4 CHOCOLATE VOCANOES FIGHTING OFF THE DREADED BROCOLLI!!!"
    show sam happy sean at far_left
    show rowan scared sean at far_right
    play sound "drawsean.mp3"
    r "Maybe it was a good thing we can't choose our destinations..."
    show rowan talking sean at far_right
    play sound "drawsean.mp3"
    r "Can we focus? We need to find a way out of here before something bad happens."
    show rowan happy sean at far_right
    show sam talking sean at far_left
    play sound "drawsean.mp3"
    s "Oh come onnnn. What bad things could possibly happen to us?"
    show rowan scared sean at far_right
    show sam happy sean at middle
    show eraser sean at far_left 
    play sound "drawsean.mp3"
    b "..."
    b ".........."
    show sam scared sean at middle
    play sound "drawsean.mp3"
    b "AAAHHHHHHH"
    
    jump next

label next:
    scene bg sean
    play sound "page sean.mp3" volume 0.8
    b "Huff, puff"
    show sam scared sean at far_left
    show rowan sad sean at far_right
    play sound "drawsean.mp3"
    s "Did we lose that...that monster?"
    show sam sad sean at far_left
    show rowan scared sean at far_right
    play sound "drawsean.mp3"
    r "I am going to need a LOT of therapy after this trip."
    show rowan sad sean at far_right
    show sam talking sean at far_left
    play sound "drawsean.mp3"
    s "Well I don't want to stay here any longer. Lets find a way out. I am going to look over here."
    #stop showing sam
    hide sam talking sean 
    show rowan talking sean at middle
    play sound "drawsean.mp3"
    r "{i}Hmmmm...{i}"
    r "{i} If we are figures on a paper, could that mean someone drew us?{i}"
   
    menu: 
        r "..."
        "Try to be quiet but let out a cough":
            y "...keeuuk.keeuuk"
            
        "Greet them":
            y "uhh hello?"

    r "OMG there is someone here. Sam come back!"
    show rowan happy sean at far_right
    show sam talking sean at far_left
    play sound "drawsean.mp3"
    s "No. Freaking. Way. Look at all those polygons."
    show rowan talking sean at far_right
    show sam happy sean at far_left
    play sound "drawsean.mp3"
    r "Focus Sam."
    r "Hey I am not sure if you will believe us, but we are dimension travelling people and have stumbled upon your world."
    r "Would you mind helping us? We can't do much as stick figures..."
    show rowan happy sean at far_right
    show sam talking sean at far_left
    play sound "drawsean.mp3"
    menu: #giving options to the player
        s "PLEASEEEEE!!! PRETTY PRETTY PLEASEEEEE!!"
        "Agree whole-heartedly":
            y "Of course I can help you"
            jump good_ending
            
        "Agree":
            y "Sure, this seems interesting."
            jump good_ending
        
        "Decline":
            y "Nah I am busy. I got a meeting to get to. Good luck."
            jump bad_ending

label good_ending: 
    scene bg sean
    play sound "page sean.mp3" volume 0.8
    show sam happy sean at far_left
    show rowan happy sean at far_right
    play sound "drawsean.mp3"
    b "Thanks so much!"
    show rowan talking sean at far_right
    play sound "drawsean.mp3"
    r "All we need you to find is the portal. It kinda looks like a wobbly circle with a swarming vortex. Y'know like Rick and Morty?"
    y "{i} You look around and don't notice anything like that near you... or do you mean...{i}"
    show sam talking sean at far_left
    play sound "drawsean.mp3"
    s "I SEE IT, I SEE IT!"
    s "Look right there. {i} tries to point{i}"
    show rowan angry sean at far_right
    play sound "drawsean.mp3"
    b "..."
    r "You know you can't point outside the paper right?"
    show sam angry sean at far_left
    play sound "drawsean.mp3"
    s "Shut up!"
    show sam talking sean at far_left
    show rowan happy sean at far_right
    play sound "drawsean.mp3"
    s "Anwyays its where that naan and veggie plate near you stranger."
    show sam happy sean at far_left
    show rowan happy sean at far_right
    play sound "drawsean.mp3"
    y "Uhh, You mean the spinach dip meant for the company meeting?"
    show sam talking sean at far_left
    play sound "drawsean.mp3"
    s "Yeah Yeah that one!"
    show rowan talking sean at far_right
    show sam happy sean at far_left
    play sound "drawsean.mp3"
    r "I mean I guess we can try it. Ill do anything to breath, eat, and have actual limbs..."
    show rowan happy sean at far_right
    show sam talking sean at far_left
    play sound "drawsean.mp3"
    s "C'mon stranger. Just pick us up and splat us in the dip!"
    show rowan scared sean at far_right
    show sam happy sean at middle
    show eraser sean at far_left
    play sound "drawsean.mp3"
    b "..."
    r "uhh Sam?..."
    show sam scared sean at middle
    play sound "drawsean.mp3"
    s "{i}turns to see{i}"
    b "AAAHHHHHHH!!!"
    menu:
        b "HELP US!"

        "Pick up the eraser":
            y "It is okay guys, this thing won't hurt you when I am around."
        
        "Leave it":
            y "Nah I decided you are both annoying. See ya"
            jump bad_ending
    
    hide eraser sean
    show rowan happy sean at far_right
    show sam happy sean at far_left
    play sound "drawsean.mp3"
    b "Our savior!"
    show rowan talking sean at far_right
    play sound "drawsean.mp3"
    r "Thank you so much for helping us in our journey. It turns out some strangers are kind after all."
    show rowan happy sean at far_right
    show sam talking sean at far_left
    play sound "drawsean.mp3"
    s "Yeah you are the best!"
    show sam happy sean at far_left
    play sound "drawsean.mp3"
    y "Want me to get you outta here now? Into the... spinach dip?"
    show rowan talking sean at far_right
    play sound "drawsean.mp3"
    r "I hope it works... I don't see any other portal close by."
    show rowan happy sean at far_right
    show sam talking sean at far_left
    play sound "drawsean.mp3"
    s "It will work. Trust. Take us to the spinach dip!!"
    "You take paper Sam and Rowan and headon on over to the spinach dip."
    #stop showing rowan and sam
    scene spinachdip sean
    menu: 
        y "{i}How should I do this?{i}"

        "SLAM DUNK":
            play sound "slamsean.mp3"
            "{i}You slam it so hard spinach dip flies across the room in all direction. Your clothes will take weeks to clean everything.{i}"
        
        "Normal":
            play sound "page sean.mp3" volume 0.8
            "{i}You press it normally. Some spinach dip spills over on the plate, but the mess is manageable.{i}"

        "lightly pressed":
            play sound "page sean.mp3" volume 0.4
            "{i}You ever so carefully that nothing is affected. No one will notice that you pressed the paper.{i} "
    scene bg sean
    y "{i}You open the spinached paper and the figures are gone.{i}"
    y "{i}You are left wondering where they will go next.{i}"
    
    return
        
label bad_ending:
    scene bg sean
    play sound "page sean.mp3" volume 0.8
    "{i}They spent years trying to find the way home, but to no avail.{i}"
    "{i}Sam and Rowan had many encounters with the dreaded eraser, and managed to escape each time.{i}"
    "{i}Now they find themselves cornered (specifically the top right of the page.{i}"
  
    show sam sad sean at far_left
    show rowan scared sean at far_right
    r "This is it sam. After all these years, we are just going to end up dying to a bunch of vile erasers."
    show rowan talking sean at far_right
    r "Because we are not making out of this alive. Can I tell you something?"
    show sam talking sean at far_left
    show rowan scared sean at far_right
    s "Yeah. I have something to say too."
    show rowan talking sean at far_right
    r "I love you."
    show sam talking sean at far_left
    s "I love you too."
    "{i}They hug eachother.{i}"
    "All of a sudden, a blinding light comes from both of them. The erasers blinded by the light, hesitate."
    "In that light a green portal appears right in front of them."
    #could talk about how one of them is embarassed. 
    scene greenportal bg
    show sam happy sean at middle
    show rowan happy sean at far_right
    "{i}As they get ready to go, rowan stops.{i}"
    show rowan talking sean at far_right
    r "Did you mean what you said?"
    show rowan happy sean at far_right
    show sam talking sean at middle
    s "Of course I do. I have always felt this way."
    r "{i}smiles{i}"
    #stop showing both of them. 
    hide rowan happy sean 
    hide sam talking sean
    "They both jump in."
    "Where will their adventure lead to next?"
    play sound "page sean.mp3" volume 0.4
    return



    



        










