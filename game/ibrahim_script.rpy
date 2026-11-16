# Ibrahim's dimension: The Moon
# Assets: see game/images/links_ibrahim.txt
# Reuses Sean's characters (s, r, b, y) and positions (far_left, middle, far_right).

label ibrahim_start:

    # Portal in
    scene black
    "They float down to the cheesy surface of the moon from the portal in the air."

    # Beat 1: Arrival
    scene bg moon ibrahim
    show sam scared ibrahim at far_left
    show rowan scared ibrahim at far_right
    s "I CAN'T BREATHE!! There is barely any air in here"
    r "Huh... very odd.. I think we seem to be fine. Must be because of the portal."
    show sam talking ibrahim at far_left
    s "I think we are far from our planet"
    show rowan talking ibrahim at far_right
    r "Oh look! I see Earth from here."
    s "The floor looks quite cheesy too.."

    # Beat 2: The problem / funny moment
    show sam happy ibrahim at far_left
    s "Let me try grabbing a scoop of this."
    show rowan scared ibrahim at far_right
    r "This is not cheese, sam.. we are on the Moon"
    s "Here goes nothing!!"
    "Sam grabs a bite but then spits out dust, to his surprise"
    show rowan angry ibrahim at far_right
    r "I warned you! Listen to me next time."
    show sam happy ibrahim at far_left
    s "Well, I don't regret it. Sometimes it doesn't hurt to live a little."

    # Beat 3: Player choice
    show rowan talking ibrahim at far_right
    menu:
        r "Hey, you! Settle this for us. Should we take risks out here, or play it safe?"

        "Live a little":
            y "Live life in the present, always."
            show sam happy ibrahim at far_left
            s "Wise words! Could not have said it better myself."
            show rowan angry ibrahim at far_right
            r "Hmph.."
            show rowan happy ibrahim at far_right
            r "I guess it was funny that you did go for it.."

        "Play it safe":
            y "You should protect yourself so you can live more later.."
            show rowan happy ibrahim at far_right
            r "Absolutely."
            show sam scared ibrahim at far_left
            s "Hmmm.."
            s "Fine.. I will try my best to be more careful from now on.."

    # Beat 4: Find the portal and leave
    show sam talking ibrahim at far_left
    show rowan happy ibrahim at far_right
    s "There it is! The portal!"
    r "I almost didn't see it there. Seems to be very submerged within the floor.."
    b "Let's get some fresh air and get out of here!!"

    scene black
    "They jump through the portal in the crack of the floor."
    "Where will their adventure lead to next?"

    return
