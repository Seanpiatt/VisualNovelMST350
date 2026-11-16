# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sam")
define r = Character("Rowan")
define m = Character("Mysterious Artist")


# audio sourced from https://www.myinstants.com/en/instant/minecraft-villager-sound/
# and https://www.chosic.com/download-audio/54471/ 
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg portal howe
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Sam and Rowan step out the portal, into the great unknown!"

    "or was unknown, until Sam recognized their current dimension..."

    show sam sigh howe at left
    s "Well Rowan, we really outdid ourselves this time."

    play sound "minecraft-villager-sound-effect-Howe.mp3"
    show rowan thinking howe at right
    r "Where in the world are we?"

    r "And why is everything completely white"

    s "We've ended up in Nowhere, the place between Something and Nothing"

    s "Some people would call this a Sanctuary of Endless Peace"

    s "I'd call it **BORING**"

    "Clearly, Sam was not a big fan of the Sanctuary of Endless Peace Dimension"

    r "Well surely it can't be alllllll boring, is there anyone around?"

    s "*sigh* well at the very least we can cope and take a look around first maybe there's something to do, or at least another portal taking us somewhere new"

    "Sam and Rowan explore this great unknown, filled with just enough of Something to not be Nothing"

    play sound "minecraft-villager-sound-effect-Howe.mp3"

    show rowan i spy howe at right

    r "Hey Sam look over there!"

    scene bg hill howe

    "As Rowan is the first to scale a small hill, he spots Something, or something less Nothing than everything else in Nowhere"

    play sound "vine-boom-sound-effect-Howe(chosic.com).mp3"

    show sam surprised 1 howe at left

    s "Oh yippee, wait is that a person??"

    "They spy an individual drawing all over the pure white ground"

    "The individual raises their head upon hearing the cries from the two daring adventures"

    show mysterious figure howe

    m "Whoa! Hello strangers, wasn't expecting guests on my canvas so soon! I would have prepared some tea"

    play sound "vine-boom-sound-effect-Howe(chosic.com).mp3"
    show sam surprised 2 howe at left

    "Sam, safe to say, was incredibly confused."

    show rowan thinking howe at right

    r "Hello chap, we were actually looking for signs of civilization, know any places nearby?"

    "The mysterious artist chuckled"

    m "Sorry to disappoint, but I've been around the block for the past 500 years, haven't seen any until you guys showed up!"

    play sound "vine-boom-sound-effect-Howe(chosic.com).mp3"
    show sam surprised 3 howe at left

    "Sam was now, safe to say, completely flabbergasted"

    r "Did you say 500 years? How are you still sane? or alive for that matter?"

    "The artist smiled"

    m "The world works in *mysterious* ways young fella, but I've been working on my masterpiece! Too bad I didn't get to finish before my first guests, but here's a little teaser, what do you think?"

    "Sam and Rowan finally noticed what's the artist has been doing along the ground"

    scene bg beach howe
    play sound "vine-boom-sound-effect-Howe(chosic.com).mp3"
    queue sound "vine-boom-sound-effect-Howe(chosic.com).mp3" volume 0.75
    queue sound "vine-boom-sound-effect-Howe(chosic.com).mp3" volume 0.5
    show sam surprised 4 howe at left

    show rowan i spy howe at right
    r "I'd say it's definitely Something, ay Sam?"

    menu:
        "What does Sam say to the artist?"

        "Talk about the how masterfully he stroked the paint(a lie, Sam has no idea how painting goes)":
            s "Incredible strokes! It's almost like I can feel the movement of the paint from my eyes"

        "give the default response(Something Sam would definitely say)":
            s "It's uhhh incredible!"
    show mysterious figure howe
    m "I sure am glad that you think that way lads. At the very least, this world is my oyster, and I've decided to give it a makeover"

    "Sam and Rowan were truely inspired by the man's devotion to his craft"

    "Sam knew that this universe was empty and so the odds of someone seeing their work was extremely rare and yet..."

    "and Rowan knew that 500 years of work with no payoff requires unbreakable resolve and yet the artist stands showing their work!"

    scene bg portal howe

    "After saying their goodbyes (and enjoying a nice cup of tea with the artist), the two would continue their journey, with newfound inspiration!"

    # This ends the game.

    return
