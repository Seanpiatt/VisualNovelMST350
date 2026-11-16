# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character(_("Sam"), color="#ffff00")
define r = Character(_("Rowan"), color="#00ff00")

transform cyan_zoom_fullscreen:
    zoom 5

# The game starts here.

label start:
    scene black screen cyan at cyan_zoom_fullscreen
    show portal cyan
    with fade
    "It's almost as if nothing strange happened just a few seconds ago."

    play music "kulakovka-lo-fi-background-620568 cyan.mp3"
    scene pexels-introspectivedsgn-33295813 cyan:
        zoom 0.7
        yalign 0.5
    with fade
    

    show rowan sad cyan at right with dissolve
    r "My head hurts."

    show sam sad talking cyan at left with dissolve
    s "That's not good."

    show rowan neutral cyan talking
    r "I think I can still keep driving for a bit."

    show sam sad cyan
    s "Are you sure? I'd be happy to take over."

    show rowan sad cyan
    r "..."

    stop music fadeout 1
    scene black screen cyan at cyan_zoom_fullscreen
    with fade

    "Five minutes pass."

    menu:
        s "(Rowan...)"

        "(Ah, it's alright. Your headache doesn't seem to be too bad.)":
            jump relent

        "(I'm getting more worried by the second.)":
            jump intervene

label relent:
    play music "kulakovka-lo-fi-624627 cyan.mp3"
    scene pexels-introspectivedsgn-33295813 cyan:
        zoom 0.7
        yalign 0.5
    with fade

    show rowan neutral cyan at right with dissolve
    r "It's okay Sam. I know that you're concerned."

    show sam sad cyan at left with dissolve
    s "..."

    show rowan neutral talking cyan
    r "I can feel your eyes piercing through my skin."

    show sam sad talking cyan
    s "You aren't even looking at me."

    show rowan neutral cyan
    r "Well, yeah. My eyes belong on the road for now."
    show rowan joy cyan
    r "Hehe."

    show sam joy cyan
    s "I'll try not to disturb you too much."
    show sam stern talking cyan
    s "If I notice something wrong, I WILL make you rest instead."

    show rowan happy talking cyan
    r "Alrighty."

    jump rest_a

label intervene:
    play music "kulakovka-lo-fi-624627 cyan.mp3"
    scene pexels-introspectivedsgn-33295813 cyan:
        zoom 0.7
        yalign 0.5
    with fade

    show sam stern talking cyan at left with dissolve
    s "Okay Rowan. Let me drive."

    show rowan neutral cyan at right with dissolve
    r "..."

    show sam sad talking cyan
    s "Please."
    show sam sad cyan
    s "..."
    show sam sad talking cyan
    s "I don't want you to overexert yourself."

    show rowan sad cyan
    r "..."
    show rowan neutral talking cyan
    r "I understand. Okay then."

    jump rest_b

label rest_a:
    stop music fadeout 1
    scene black screen cyan at cyan_zoom_fullscreen
    with fade

    "Rowan's headache clears up."
    "A few hours pass by, and the sun sets."

    s "I see a bench nearby. Wanna pull over and take a break?"

    r "Sure."

    s "I'll take the wheel after this."

    r "Okay."

    jump bench

label rest_b:
    stop music fadeout 1
    scene black screen cyan at cyan_zoom_fullscreen
    with fade

    "Rowan's headache clears up."
    "A few hours pass by, and the sun sets."

    s "I see a bench nearby. Wanna pull over and take a break?"

    r "zzz..."
    r "...wh- what? Oh. Yeah. Sure, let's do that."

    s "Ah, sorry to wake you up."

    r "No problem, I rested well. I'll take your place after."

    s "Okay."

    jump bench

label bench:
    play music "kulakovka-calm-lo-fi-624643 cyan.mp3"
    scene pexels-thatguycraig000-1503520 cyan:
        zoom 1
        xalign 0.5
        yalign 0.5
    with fade

    show sam happy talking cyan at left with dissolve
    s "Whoa! Look at that!!"

    show rowan happy talking cyan at right with dissolve
    r "What beautiful timing."

    s "Indeed."

    scene black screen cyan at cyan_zoom_fullscreen
    with fade
    "Thirty minutes pass."

    show rowan joy cyan at right with dissolve
    r "I really needed this break."

    show sam joy cyan at left with dissolve
    s "Yeah. I could tell."

    show rowan happy talking cyan
    r "You sound a lot calmer as well."

    show sam happy talking cyan
    s "I suppose so."

    s "Okay then. Should we get going?"

    r "Yeah."

    scene black screen cyan at cyan_zoom_fullscreen
    with fade
    "Sam and Rowan return to continue their drive."
    "That being said..."

    scene grey screen cyan at cyan_zoom_fullscreen
    with fade
    "...a blissful, fleeting memory such as this..."

    scene white screen cyan at cyan_zoom_fullscreen
    with dissolve
    "...may feel unreachable as time goes on."

    scene black screen cyan at cyan_zoom_fullscreen
    show portal cyan
    with fade
    "Another portal awaits their presence."

    jump howe_start
