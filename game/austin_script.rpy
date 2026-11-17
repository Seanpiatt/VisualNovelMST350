init python:
    def austin_img(filename, fallback):
        path = "images/" + filename
        if renpy.loadable(path):
            return path
        return fallback

    def austin_audio(channel, filename, **kwargs):
        path = "audio/" + filename
        if renpy.loadable(path):
            renpy.music.play(path, channel=channel, **kwargs)


define austin_sam   = Character("Sam",   color="#ffffff")
define austin_rowan = Character("Rowan", color="#ffffff")
define austin_todo  = Character("Todo",  color="#ffffff")
define austin_mayor = Character("Mayor Copy 2 Final", color="#ffffff")


transform austin_left:
    xcenter 0.17
    yalign 1.0

transform austin_right:
    xcenter 0.83
    yalign 1.0

transform austin_mid:
    xcenter 0.5
    yalign 1.0

transform austin_mid_right:
    xcenter 0.64
    yalign 1.0


image austin_bg car = austin_img("austin_bg_car.png", Solid("#2b2b3a"))

image austin_bg portal = austin_img("austin_bg_portal.png", Solid("#5b2a86"))

image austin_bg arrive = austin_img("austin_bg_arrive.png", Solid("#f5f2e8"))

image austin_bg dimension = austin_img("austin_bg_dimension.png", Solid("#f5f2e8"))

image austin_bg end = austin_img("austin_bg_end.png", Solid("#c9713a"))

image austin_sam happy = "images/austin_sam_happy.png"
image austin_sam sad   = "images/austin_sam_sad.png"
image austin_sam angry = "images/austin_sam_angry.png"

image austin_rowan happy = "images/austin_rowan_happy.png"
image austin_rowan sad   = "images/austin_rowan_sad.png"
image austin_rowan angry = "images/austin_rowan_angry.png"

image austin_todo neutral = "images/austin_stick_neutral.png"
image austin_todo sad     = "images/austin_stick_sad.png"
image austin_todo smile   = "images/austin_stick_smile.png"
image austin_mayor smile  = Transform("images/austin_stick_smile.png", xzoom=-1.0)


default austin_choice = ""


label austin_start:

    scene austin_bg car
    with fade

    $ austin_audio("music", "austin_music_car.mp3", fadein=1.0)

    show austin_sam happy at austin_left
    show austin_rowan sad at austin_right

    "They've been driving forever... Sam's steering with one knee. Rowan's been working on the same postcard for hours."

    $ austin_audio("sound", "austin_sfx_pencil.mp3")

    austin_rowan "Okay. Draft... ...well whatever, I've lost count."

    austin_sam "It says 'Wish You Were Here' on the front. That's like half the work already!"

    show austin_rowan angry

    austin_rowan "It has to sound right. None of them sounded right."

    austin_sam "So... what does this one say?"

    show austin_rowan sad

    austin_rowan "Dear Mom,"

    austin_sam "...And?"

    austin_rowan "That's all I've got. The comma looks weird. Why do we use commas there?"

    austin_sam "Don't stress about it too much. Nobody's ever been mad about getting a postcard."

    austin_rowan "I'll send it when it's ready."

    "Up ahead, the road just stops. It's not a dead end. It looks more like nobody got around to drawing the rest of it."

    jump austin_portal_enter


label austin_portal_enter:

    $ austin_audio("sound", "austin_sfx_portal.mp3")

    scene austin_bg portal
    with Fade(0.2, 0.0, 0.6, color="#ffffff")

    "There's a portal where the road should be. It keeps flickering like it's still loading."

    austin_sam "Is that thing even finished?"

    austin_rowan "Does it matter? You're not slowing down."

    austin_sam "It's probably fine."

    "It was not fine. It also wasn't finished."

    jump austin_arrival


label austin_arrival:

    stop music fadeout 1.0

    scene austin_bg arrive
    with Fade(0.3, 0.3, 1.0, color="#ffffff")

    $ austin_audio("music", "austin_music_dimension.mp3", fadein=1.0)

    "Everything is white. Somebody outlined a whole town in black pen, roofs and windows and everything, and then never came back to colour it in."

    scene austin_bg dimension
    with dissolve

    show austin_sam sad at austin_left
    show austin_rowan sad at austin_right

    austin_sam "Did we break it??? Rowan, I think we broke the universe."

    austin_rowan "Look, there's a sign."

    "WELCOME TO insert town name here. POPULATION: to be determined."

    $ austin_audio("sound", "austin_sfx_gasp.mp3")

    "A crowd shows up. They're all stick figures."

    show austin_mayor smile at austin_mid
    with dissolve

    austin_mayor "Whoa. Look at them. Look at how much detail they have."

    austin_mayor "That one has eyebrows. TWO EYEBROWS!!"

    show austin_sam happy

    austin_sam "Thanks. I grew them myself."

    austin_mayor "I'm the Mayor. Full name is Mayor Copy 2 Final. Welcome to town, Finished Ones."

    austin_rowan "Finished Ones?"

    austin_mayor "You're coloured in. You have clothes. You even have shading."

    austin_sam "HAH! I'm happy you've noticed. I've always said I have great shading."

    show austin_rowan angry

    austin_rowan "You have literally never said that."

    hide austin_mayor
    with dissolve

    jump austin_adventure


label austin_adventure:

    show austin_todo neutral at austin_mid
    with dissolve

    "One of the stick figures walks up. He's wearing a name tag that just says TO-DO."

    austin_sam "Hey, Todo."

    austin_todo "Oh, that's not... actually, yeah. Todo works. That's the most name I've ever had."

    show austin_rowan sad

    austin_rowan "How is that name tag staying on? You don't have a shirt... or a name tag..."

    austin_todo "It's more of an implied sort of thing..."

    austin_todo "Can I ask you guys something? What's it like being done?"

    austin_sam "Honestly it's pretty great. I peaked in third grade and I've been coasting ever since."

    austin_rowan "So what do you all do here?"

    show austin_todo sad

    austin_todo "We wait."

    austin_rowan "For what?"

    austin_todo "To get finished. You can't really start anything when you look like this."

    austin_todo "I've also got a joke. I've been working on it for two hundred years."

    austin_sam "Two hundred years? Okay, let's hear it."

    austin_todo "Oh, no no no. It's not ready. I'll tell it once I'm finished. Once it's perfect."

    "Rowan looks down at the postcard. 'Dear Mom,' and nothing else."

    menu:
        "Rowan looks back at Todo."

        "Tell him the truth about being finished":
            $ austin_choice = "truth"
            jump austin_branch_a

        "Ask to hear the joke anyway":
            $ austin_choice = "joke"
            jump austin_branch_b


label austin_branch_a:

    austin_rowan "Todo, we're not finished either."

    austin_todo "You have eyebrows."

    austin_rowan "I have eyebrows and I've spent six hours on one postcard. I rewrote the word 'Dear' at least fifty times."

    show austin_sam sad

    austin_sam "I don't know how taxes work. I'm just hoping nobody ever asks."

    austin_rowan "Nobody out there is done. We got coloured in and just kept going anyway."

    austin_todo "So when do you get to start stuff?"

    austin_rowan "I think you just start. And it's bad at first."

    show austin_sam happy

    austin_sam "Really bad. Tell the joke, Todo."

    jump austin_climax


label austin_branch_b:

    austin_rowan "Tell it anyway."

    austin_todo "It's a draft."

    austin_rowan "So tell us the draft."

    austin_todo "What if it's bad?"

    austin_sam "Then it's a bad joke and nobody dies. I tell like four of those an hour."

    austin_rowan "He does. I've counted."

    austin_todo "You tell them before they're ready?"

    austin_sam "Todo, I have never been ready for anything in my life."

    jump austin_climax


label austin_climax:

    show austin_todo neutral

    "The whole town leans in. Somewhere a half-drawn bird stops singing."

    austin_todo "Okay. Okay. Why did the stick figure cross the road?"

    austin_rowan "Why?"

    austin_todo "He didn't. The road wasn't finished."

    $ austin_audio("sound", "austin_sfx_badum.mp3")

    "Ba dum. (tss still in development)"

    $ austin_audio("sound", "austin_sfx_crickets.mp3")

    "Nothing. Dead silent."

    stop sound fadeout 0.5

    show austin_sam happy
    show austin_rowan happy

    "Then Sam loses it. Way too hard for a joke that bad."

    show austin_mayor smile at austin_mid_right
    with dissolve

    "Then the Mayor starts laughing. Then everybody. It's the first joke anyone has ever told in insert town name here."

    austin_mayor "Today is officially a holiday! Name of holiday to be decided!"

    hide austin_mayor
    with dissolve

    austin_todo "It needs work. The middle drags."

    austin_rowan "It's two sentences."

    austin_todo "The middle drags."

    austin_rowan "Then tell it again tomorrow. Doesn't matter if it's better or worse. Just tell it."

    show austin_todo sad

    austin_todo "I thought I had to be done before I was allowed to start."

    austin_rowan "I think starting might be how you get done."

    austin_rowan "Maybe... I'm on at least draft nine, so don't quote me."

    show austin_todo smile

    austin_todo "I'm opening a bakery. Who cares if I know anything about baking or food safety."

    austin_sam "That's a health code violation and I fully support it."

    hide austin_todo
    with dissolve

    jump austin_portal_exit


label austin_portal_exit:

    stop music fadeout 1.0

    $ austin_audio("sound", "austin_sfx_portal.mp3")

    scene austin_bg portal
    with dissolve

    "The portal's still flickering where they left it."

    "Todo waves goodbye."

    jump austin_end


label austin_end:

    scene austin_bg end
    with fade

    $ austin_audio("music", "austin_music_car.mp3", fadein=1.0)

    show austin_sam happy at austin_left
    show austin_rowan happy at austin_right

    "Back on the road. The real one, with all the lines filled in."

    if austin_choice == "truth":
        austin_sam "You told a stick figure you don't have your life together. That's growth."

        austin_rowan "You told him about the taxes."

        austin_sam "I panicked."
    else:
        austin_sam "You made a two hundred year old guy perform unfinished material."

        austin_rowan "And he survived."

        austin_sam "Barely. The middle did drag."

    $ austin_audio("sound", "austin_sfx_pencil.mp3")

    "Rowan pulls out the postcard and writes for maybe ten seconds."

    austin_sam "Draft ten?"

    austin_rowan "Draft ten. 'Dear Mom. Sam is driving. We're lost. Things are good. I miss you.'"

    austin_sam "That's the worst one yet."

    austin_rowan "I know. I'm mailing it at the next stop."

    austin_sam "Did you at least fix the comma?"

    show austin_rowan angry

    austin_rowan "Don't."

    "Up ahead, the road starts glowing again."

    austin_sam "Think the next one's finished?"

    show austin_rowan happy

    austin_rowan "Hope not."

    stop music fadeout 1.0

    return
