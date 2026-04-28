default persistent.cg_d2_nsfw1 = False
default persistent.cg_d3_nsfw1 = False
default persistent.cg_d4_nsfw1 = False
default persistent.cg_d5_nsfw1 = False
default nsfwframe = False
default topscars = False
default jump_one = ""
default jump_two = ""
image CG D2_NSFW1 = Composite(
    (1920, 1080),
    (0, 0), "14 Nights With You/images/d2 nsfw/day 2.webp",
    (0, 0), "peffectp",
    (0, 0), "14 Nights With You/images/d1 nsfw/sparkle.webp",
    )
image CG D3_NSFW1 = Composite(
    (1920, 1080),
    (0, 0), "14 Nights With You/images/d3 nsfw/day 3.webp",
    (0, 0), "peffectp",
    (0, 0), "14 Nights With You/images/d1 nsfw/sparkle.webp",
    )
image CG D4_NSFW1 = Composite(
    (1920, 1080),
    (0, 0), "14 Nights With You/images/d4 nsfw/day 4.webp",
    (0, 0), "peffectp",
    (0, 0), "14 Nights With You/images/d1 nsfw/sparkle.webp",
    )
image CG D5_NSFW1 = Composite(
    (1920, 1080),
    (0, 0), "14 Nights With You/images/d5 nsfw/day 5.webp",
    (0, 0), "peffectp",
    (0, 0), "14 Nights With You/images/d1 nsfw/sparkle.webp",
    )
screen warningnsfw:
    style_prefix "popupwhite"

    add "images/bg/other_dark.webp" alpha 0.8 at choice_fade
    add "triangles_light" alpha 0.1
    frame:
        align (0.5,0.5)
        xsize 650
        vbox:
            xalign 0.5
            vbox:
                xalign 0.5
                text "PLEASE READ!" font "fonts/Orbitron-Regular.ttf" size 55 color "#FF66CB"
            vbox:
                text "Due to the way this 18+ scene is written, you will not be able to top Ren. Instead, {u}you{/u} will be the one who is penetrated." font "fonts/Assistant-Regular.ttf" color "#141414" size 25 xalign 0.5 text_align 0.5
                text "\nProceed anyway?" font "fonts/Assistant-Regular.ttf" color "#141414" size 20 xalign 0.5 text_align 0.5
            hbox:
                align (0.5,0.5)
                spacing 90
                textbutton _("YES") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), Jump("".join([jump_one]))] hovered [Play("sound", "audio/ui/click1.ogg")]
                textbutton _("NO") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), Jump("".join([jump_two]))] hovered Play("sound", "audio/ui/click1.ogg")
screen customisensfw:
    modal True

    add "gui/bg/menu_bg_chara.png"
    add "triangles_light"
    if nsfwframe == True:
        frame:
            at slidedown
            style_prefix "popupblack"
            padding (50, 90, 50, 60)
            align (0.23, 0.38)
            xysize (700,600)
            vbox:
                align (0.5,0.5)
                vbox:
                    align (0.5,0.5)
                    vbox align (0.5,0.5)
                    hbox:
                        xalign 0.5
                        text "\n{font=Orbitron-Black.ttf}{size=+10}BODY PREFERENCE{/size}{/font}\nHow would you describe your body?" color "#f8f8f8" size 25 text_align 0.5
                    hbox:
                        xalign 0.5
                        spacing 30
                        textbutton _("feminine") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("body_type", "feminine")] hovered Play("sound", "audio/ui/click1.ogg")
                        textbutton _("ambiguous") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("body_type", "ambiguous")] hovered Play("sound", "audio/ui/click1.ogg")
                        textbutton _("masculine") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("body_type", "masculine")] hovered Play("sound", "audio/ui/click1.ogg")
                    hbox:
                        xalign 0.5
                        text "\n{font=Orbitron-Black.ttf}{size=+10}TOP SURGERY SCARS{/size}{/font}\nThis does nothing (for now)" color "#f8f8f8" size 25 text_align 0.5
                    hbox:
                        xalign 0.5
                        spacing 30
                        textbutton _("no") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("topscars", False)] hovered Play("sound", "audio/ui/click1.ogg")
                        textbutton _("yes") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("topscars", True)] hovered Play("sound", "audio/ui/click1.ogg")
    else:
        frame:
            at slidedown
            style_prefix "popupblack"
            padding (50, 90, 50, 60)
            align (0.23, 0.38)
            xysize (700,600)
            vbox:
                align (0.5,0.5)
                spacing 30
                vbox:
                    align (0.5,0.5)
                    hbox:
                        align (0.5,0.5)
                        text "{font=Orbitron-Black.ttf}{size=+10}Bust Type{/size}{/font}\nHow would you describe your bust?" color "#f8f8f8" size 25 text_align 0.5
                    hbox:
                        align (0.5,0.5)
                        spacing 30
                        textbutton _("breasts") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("bust", "breasts")] hovered Play("sound", "audio/ui/click1.ogg")
                        textbutton _("ambiguous") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("bust", "bust")] hovered Play("sound", "audio/ui/click1.ogg")
                        textbutton _("chest") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("bust", "chest")] hovered Play("sound", "audio/ui/click1.ogg")
                vbox:
                    align (0.5,0.5)
                    hbox:
                        align (0.5,0.5)
                        text "\n{font=Orbitron-Black.ttf}{size=+10}Genitalia Type{/size}{/font}\nHow would you describe your genitalia?" color "#f8f8f8" size 25 text_align 0.5
                    hbox:
                        align (0.5,0.5)
                        spacing 30
                        textbutton _("vagina") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("genitalia", "cooter")] hovered Play("sound", "audio/ui/click1.ogg")
                        textbutton _("ambiguous") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("genitalia", "gnooch")] hovered Play("sound", "audio/ui/click1.ogg")
                        textbutton _("penis") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("genitalia", "bussy")] hovered Play("sound", "audio/ui/click1.ogg")
    frame:
        at slideright
        style_prefix "popupblack"
        padding (50, 90, 50, 60)
        align (0.77,0.25)
        xysize (600,350)
        vbox:
            align (0.5,0.5)
            spacing 10
            xsize 500
            justify True
            text "DLC Symbols" font "Orbitron-Black.ttf" size 35 color "#f8f8f8" text_align 0.5 align (0.5,0.5)
            hbox:
                spacing 20
                add "14NWY symbol" align (0.5,0.5) zoom 1.5
                text "Pink means it's a unique choice from the \"14 Nights With You\" DLC" color "#f8f8f8" size 25 align (0.5,0.5)
            hbox:
                spacing 20
                add "14NWY symbol alt" align (0.5,0.5) zoom 1.5
                text "Red means the choice will involve explicit language and/or content" color "#f8f8f8" size 25 align (0.5,0.5)
    frame:
        at slideright
        style_prefix "popupwhite"
        padding (50, 90, 50, 60)
        align (0.77,0.75)
        xysize (600,350)
        vbox:
            spacing 10
            align (0.5,0.5)
            text "Miscellaneous Features" font "Orbitron-Black.ttf" size 35 color "#141414" text_align 0.5 align (0.5,0.5)
            text "What position suits you best?" color "#141414" size 25 text_align 0.0 align (0.5,0.5)
            hbox:
                xalign 0.5
                spacing 30
                textbutton _("top") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("nsfw_position", "top")] hovered Play("sound", "audio/ui/click1.ogg")
                textbutton _("versatile") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("nsfw_position", "vers")] hovered Play("sound", "audio/ui/click1.ogg")
                textbutton _("bottom") text_style "cutietext" action [Play("sound", "audio/ui/blip.ogg"), SetVariable("nsfw_position", "bottom")] hovered Play("sound", "audio/ui/click1.ogg")
    frame:
        at slideup
        background Frame(["gui/boxes/bubble_black.png"], gui.choice_button_borders)
        padding (50,15,50,15)
        pos (0.6,0.81)
        anchor (1.0,1.0)
        text "This option is still a massive WIP lol" text_align 0.5
    imagebutton auto "gui/ui/back_%s.png" action [Play("sound", "audio/ui/cancel.ogg"), Hide("customisensfw", dissolve)] anchor (0.5, 0.5) pos (0.170, 0.785) hovered Play("sound", "audio/ui/click2.ogg") at amm_button, slideleft
    imagebutton auto "gui/ui/more_%s.png" action [Play("sound", "audio/ui/blip.ogg"), ToggleVariable("nsfwframe")] anchor (0.5, 0.5) pos (0.230, 0.785) hovered Play("sound", "audio/ui/click2.ogg") at amm_button, slideleft
init $ persistent.dlc_14nwy_ver = "D55426"
label DLC_firsttime_penetrating:
    if persistent.dlc_14nightswithyou_type == "paid" and persistent.dlc_14nwy_comp == False:
        return
    $ first_penetrating = False
    if length == "strap-on":
        n "As I fumble around for the strap-on I kept hidden away (for moments such as these) and start to prep for what's about to happen, [ch_ren] makes a sound and pulls away from me with an awkward laugh."
    else:
        n "As I start to prep for what's about to happen, [ch_ren] makes a sound and pulls away from me with an awkward laugh." 
    r "Um— You should know that I've never had someone else put— I mean, I-I've never… {i}y'know{/i}… back there, before…"
    r "I mean— Sure, I've {i}experimented{/i} with myself and stuff, but…"
    r "W-Well, I've never— Not with another person before." 
    n "Wait, was he serious?" 
    n "Almost shyly, [ch_ren] tears his gaze from mine with a crooked smile and a faint dusting of red on his cheeks."
    r "I just figured you should know." 
    menu:
        "It's my first time doing this":
            $ rem_wahoo = False
            $ first_time = True
            y "You know, it's actually my first time doing something like this, too." 
            r "{size=+10}W-Wait, really?!{/size}"  with vpunch
            r "So then… I'm your first as well?" 
            n "[ch_ren] beams down at me with such a tender and loving expression as his hand shyly starts to travel towards my [length]." 
        "I've done this before":
            $ rem_wahoo = True
            $ first_time = False
            y "Actually… I've done this before." 
            n "For the briefest moment, a frown pulls at [ch_ren]'s features — before he masks it with that familiar, kind-hearted smile I've grown fond of." 
            r "I-I see." 
            r "Then I'd better make this something you won't forget, huh?" 
            r "By the end of this, you won't even remember anyone who came before me." 
            n "With a determined look on [ch_ren]'s face, he slowly reaches for my [length] and gives it an experimental squeeze." 
        "I'm happy to be his first":
            $ rem_wahoo = True
            $ first_time = False
            y "Thanks for telling me. I'm happy I get to be your first, [ch_ren]." 
            r "…M-Me too! I'm glad I get to experience this with you, too!" 
            n "With a bright smile on [ch_ren]'s features, he shyly reaches for my [length] and gives it a few experimental strokes." 
        "It doesn't really matter":
            $ rem_wahoo = True
            $ first_time = False
            y "Right now, all I want to do is be inside of you, [ch_ren]." 
            r "R-Right! Yeah! O-Of course!" 
            r "I, um… I want that too. You have no idea how badly I've— I'll shut up now." 
            n "[ch_ren] looks down at me with an embarrassed expression as his hand shyly starts to travel towards my [length]." 
    return
label DLC_firsttime_giving:
    if persistent.dlc_14nightswithyou_type == "paid" and persistent.dlc_14nwy_comp == False:
        return
    $ first_giving = False
    n "But before I can go any further, I tentatively look back at [ch_ren] with a certain gleam in my eyes." 
    $ choice_style = "box"
    menu:
        "It's my first time doing this":
            $ ren_yippee = False
            y "You should know… I've never actually gone down on someone before." 
            r "R-Really? You've never…?" 
            if first_ren_giving == False:
                pass
            else:
                r "Then… We're the same!" 
            r "Haaaah~ I don't know why hearing that is making me feel so happy…" 
            n "Seeing [ch_ren]'s tender smile gives me all the reassurance and motivation I need to continue." 
        "I've done this before":
            $ rem_yippee = True
            n "[ch_ren] seems to notice my sudden pause and immediately looks down at me with worry in his eyes." 
            r "…Is everything okay, Angel?" 
            y "Oh, yeah. Just fine. It's just… It's been a while since I done something like this." 
            r "I-I see…" 
            n "An emotion I can't quite place seems to wash over [ch_ren] as I watch his brows pull into a frown — before they go back to normal." 
            r "Well, Still. I'm glad you {i}want{/i} to do something like this with me." 
            r "I've never… Y-You're the first person who's ever gone down on me, so I'm glad I get to experience it with you." 
            n "Wow, really? Was he being serious right now?" 
            n "All the more reason for me to make this an {b}extra{/b} memorable experience for him, I guess." 
            n "[ch_ren]'s confession give me all the reassurance and motivation I need to continue." 
    $ choice_style = "default"
    return
label DLC_firsttime_receiving:
    if persistent.dlc_14nightswithyou_type == "paid" and persistent.dlc_14nwy_comp == False:
        return
    $ first_receiving = False
    n "But before [ch_ren] can go any further, I tentatively reach for him in an attempt to get his attention." 
    $ choice_style = "box"
    menu:
        "It's my first time doing this":
            y "You should know… I've never had someone do {i}this{/i} to me before." 
            n "At my words, [ch_ren] seems to halt his actions and look up at me with wide eyes." 
            r "…I-I'm the first person to go down on you like this? H-Haaah~" 
            n "His smile only seems to grow wider as he nuzzles his face closer to my body and presses soft, butterfly kisses against my skin." 
            r "Don't worry, I promise I'll make you feel good! And…" 
            r "Well, I've never actually done this before as well. S-So we're the same." 
            r "Ahh~ This makes me so happy!" 
            n "With a tender smile blooming on [ch_ren]'s face, he picks up where he left off with newfound eagerness." 
        "I've done this before":
            n "[ch_ren]'s gaze immediately flickers to mine with a hint of concern in them." 
            r "…Angel?" 
            y "It's nothing, don't worry." 
            r "I-If you say so…" 
            n "At that, [ch_ren] hesitantly goes back to what he was previously doing — but not before sending me one last worried look." 
            n "When I give him a reassuring smile in return, he takes that as a sign to pick up where he left off with newfound eagerness." 
    $ choice_style = "default"
    return
label DLC_day1_library:
    menu:
        "{image=14NWY symbol} He looks like he wants to devour me":
            n "The way he's looking at me… It's almost as if he wants to take a bite out of me." 
            n "There's an almost possessive gleam behind those blue eyes of his which makes it hard to look away — but it's even harder to miss the way they flicker towards my neck before they meet my gaze once more." 
            n "It's almost as if he was trying to map out and memorise every inch of my skin, and the thought alone ignites a flutter of excitement from within me." 
            n "Part of me feels tempted to take a step closer to this stranger just to see how he'd react, but then I remember where I am and what I was initially supposed to be doing." 
            n "Focus, [ch_angel]. You're at work right now. You should be helping this person find a book, not awkwardly ogling them in silence." 
        "{image=14NWY symbol} He looks like he wants me to come closer":
            n "With the way this stranger keeps glancing at me — taking in every inch of me — I can't help but wonder if that was his way of subtly inviting me to come closer." 
            n "As if to test the waters, I take a tentative step in his direction, and he reacts exactly how I expected him to." 
            n "The stranger's eyes widen in surprise as he awkwardly leans against the shelf, and from the corner of my eye, I see his hand twitch in my direction. Was he holding himself back?" 
            n "But just as I'm about to comment on it, I remember where I am and what I was initially supposed to be doing." 
            n "Focus, [ch_angel]. You're at work right now. You should be helping this person find a book, not awkwardly ogling them in silence." 
        "{image=14NWY symbol} He looks like he wants to press me up against the shelf":
            n "There's an unmistakable gleam behind those blue eyes of his, one that speaks louder than words." 
            n "And if the half-lidded look wasn't enough, the twitch in his hand as it reaches for me speaks volumes. But just before the stranger tries to do anything, he abruptly withdraws and goes back to awkwardly picking at the ends of his sleeves." 
            n "The pink-haired stranger can barely meet my gaze now, and his cheeks reveal his embarrassment by turning a deep shade of red — one that reaches all the way to his ears." 
            n "I almost want to comment on them, but then I remember where I am and what I was initially supposed to be doing." 
            n "Focus, [ch_angel]. You're at work right now. You should be helping this person find a book, not awkwardly ogling them in silence." 
        "{image=14NWY symbol} I must be seeing things":
            n "What was I thinking? Besides, I'm at work right now — this was hardly appropriate. From that thought alone, I remember where exactly I am and what I was initially supposed to be doing." 
    n "When I glance back at the stranger with an apologetic look, I notice that his attention has already shifted. Curious, I follow his gaze and suddenly remember what I'm holding in my hands." 
    n "Jeez, how could I forget so easily? But more importantly… Why was he looking at it so intently?" 
    return
label DLC_day1_text:
    rt ".:GKJ"  with vpunch
    rt "I ACCIDENTSLLY HIT SEND ARGHKS SRRY OH GOD SORRY I'M SO SORRY" 
    n "There's a very, very, {b}very{/b} long pause before [ch_ren] replies." 
    rt "…did u mean to send me that? >///<" 
    rt "um. if u want i can send a photo? would u like that?" 
    rt "ahhh but it's rlly dark in my room right now TT_TT besides! i wanted to ask u something actually :3" 
    rt "u see… i was wonderinf if u were free tomorrow? i still wanted to thank u for helping me find that book" 
    return
label DLC_day1_call:
    rcall "{size=+10}S-S-S-Sorry?!{/size}"  with vpunch
    rcall "I… Um… W-Well! Ahah… I'm still wearing the same outfit from earlier." 
    rcall "Oh! But I took off one of my sweaters because it was getting a bit stuffy in y— My… room." 
    n "I was about to ask if the late autumn air didn't bother him — especially at this time of night — but [ch_ren] cuts me off with yet another response." 
    rcall "B-But that's not really an appealing answer, is it?" 
    rcall "Or… Wait. Were you referring to what I'm wearing {i}underneath{/i} my clothes? Because…" 
    rcall "Well, I don't think I can say without feeling embarrassed, ahaha~" 
    rcall "S-Sorry." 
    return
label DLC_day2_cafe:
    n "[ch_ren]'s cheeks are still scarlet red — and he seems almost {b}fidgety{/b} with how his leg keeps bouncing under the table — so I take this opportunity to tease him a bit." 
    n "After all, [ch_ren] doesn't seem to notice the stray pieces of crumbs clinging to his bottom lip yet, which gives me a few mischevious ideas." 
    menu:
        "{image=14NWY symbol} Lean in and lick the crumbs off his lip":
            show ren blushing z at bpop
            r "{size=+10}A-A-Ah!{/size}"  with vpunch
            show ren flushed z at spop
            r "Y-Y-Y-You—!" 
            y "You had some crumbs on your face. I just wanted to help get them off." 
            show ren blushing z at spop
            r "You just licked me… Your tongue touched my—" 
            show ren lovesick z at spop
            r "…Hahahah~" 
            n "Almost immediately, [ch_ren] covers his mouth with the sleeve of his cardigan as his cheeks somehow grow an even {b}darker{/b} shade of red." 
            n "He isn't really subtle with the way he crosses his legs underneath the table, nor the way he clumisly reaches for his drink in an attempt to distract himself with a sip." 
            n "Satisfied with my teasing, I leave [ch_ren] alone and focus my attention back on the plate in front of me." 
        "{image=14NWY symbol} Kiss him in an attempt to remove it":
            show ren blushing z at bpop
            r "—Mn!" 
            n "Just as I anticipated, [ch_ren] tenses up the moment my lips touch his — almost as if he wasn't expecting me to do that — before his eyelids flutter closed and he lets out a dreamy sigh." 
            n "But before the kiss can deepen, I pull away with a satisfied glint in my eyes." 
            y "You had some crumbs on your face. I just wanted to help get them off." 
            show ren flushed z at spop
            r "S-So you… kissed me? Then in that case…" 
            show ren smirk z at spop
            r "Looks like y'got some food on your face, too. Here." 
            n "Before I can respond, [ch_ren] leans in once more and gives me yet another kiss." 
            n "There's hardly anything soft or gentle about this one, and just as I feel his tongue start to curiously prod against my bottom lip, I hear a nearby customer clear their throat in an exasperated manner." 
            n "Ignoring their gaze, I pull away from [ch_ren] with a sheepish smile and watch as he awkwardly shifts in his seat… Before he crosses his legs and pulls the bottom of his cardigan over his lap." 
        "{image=14NWY symbol} Reach up and wipe it off with your finger":
            show ren neutral z at bpop
            r "…" 
            n "Just as I wipe the pieces of cake from his lips, his tongue peeks out and brushes against the tip of my thumb." 
            n "A faux innocent smile is all I get in response, so I decide to amp up my teasing by leaving my finger there and seeing what else [ch_ren] would do." 
            n "Almost immediately, his hand wraps around my wrist as he opens his mouth to suck on my thumb." 
            show ren smirk z at spop
            r "Don't wanna waste any food." 
            y "S-Sure." 
            n "How is that {b}I'm{/b} the one who ended up flustered? With a bewildered look on my face, [ch_ren] pretends nothing happened and goes back to enjoying his cake — though he isn't subtle with the way he shifts in his seat and adjusts his pants." 
            n "Ah. I see." 
        "{image=14NWY symbol} Don't do anything at all":
            show ren sad z at spop
            r "Something wrong?" 
            n "As if noticing what I've been staring at, [ch_ren] brushes his fingers across his face and notices the crumbs." 
            show ren blushing z at spop
            r "O-Oh. Heh, how embarassing." 
            show ren flushed z at spop
            r "All gone now?" 
            n "He looks at me for confirmation, and when I give it, he goes back to eating — but not before attempting to hide his flushed cheeks with the sleeve of his cardigan." 
    return
label DLC_day2_rain:
    r "It's really pouring, huh? Here, let's stand over here instead." 
    n "At that, [ch_ren] gently ushers me into the dark alleyway between two buildings." 
    scene other_dark
    hide screen menuwu
    show screen dayscalendar
    show peffectp
    play audio "audio/sfx/movement.ogg"
    $ quick_menu = True
    with Fade(1.0, 1.0, 1.0)
    n "He's quick to press himself against me, likely in an attempt to shield my body from the rain." 
    n "Or perhaps he was just looking for an excuse to be close to me? Either way, [ch_ren]'s actions — and his sudden closesness — got me thinking…" 
    $ choice_style = "box"
    menu:
        "{image=14NWY symbol alt} Press a kiss against his neck":
            n "I'm not sure what comes over me in that moment, but I find myself leaning closer to [ch_ren] and placing a kiss on the exposed spot between the underside of his jaw and neck." 
            r "Ah! Fu—" 
            r "Wh-What are you doing…" 
            n "As if he's acting purely on impulse, [ch_ren] pulls my body {b}even closer{/b} to his own as his large arms wrap around my waist. Hot puffs of air ghost across my shoulder as he tries his best to calm his breathing, but it ultimately seems futile." 
            n "Feeling particularly devious, I place another kiss against the juncture below [ch_ren]'s earlobe, and his reaction is immediate." 
            n "One of his hands squeezes my sides tighter, while the other moves to my leg to lift it up and rest it against his thigh." 
            n "[ch_ren]'s own thigh soon takes up the empty space, and I can feel him not-so-subtly rut himself against me." 
            n "I won't lie, the friction from his jeans feels {b}amazing{/b} — but before I can do anything in return, [ch_ren] cuts me off with a low and husky tone." 
            r "…We really shouldn't be doin' somethin' like this out here." 
            y "{i}You're{/i} the one rubbing yourself against me without a care in the world." 
            r "…" 
            n "[ch_ren] takes in a deep inhale before he presses a kiss of his own against my shoulder and pulls away." 
            if genitalia == "cooter":
                r "You're right. This isn't the place for that. 'N you're soaking wet, Angel." 
                y "…From the rain, right?" 
                n "Even though it's hard to see in this dark alleyway, I still make out the way his eyes narrow as his lips pull into a sly smile." 
                n "As if to tease me even {b}more{/b}, [ch_ren] angles his thigh and purposefully brushes his knee against my core." 
                r "Hmm… Maybe I should check?" 
            elif genitalia == "bussy":
                r "You're right. This isn't the place for that. Besides, you're probably all wet and sticky right now, aren't you?" 
                r "We should continue this at another time. I'd rather you didn't catch a cold." 
                y "…From the rain, right?" 
                n "Even in the dark alleyway, I can see his eyes narrow as his lips pull into a sly smile." 
                n "As if to tease me even {b}more{/b}, [ch_ren] angles his thigh and purposefully brushes it against my growing hard-on." 
                r "Hmm… Maybe I should check?" 
            else:
                r "You're right. This isn't the place for that. Besides, you're probably all wet and sticky right now, aren't you?" 
                y "…From the rain, right?" 
                n "Even in the dark alleyway, I can see his eyes narrow as his lips pull into a sly smile." 
                n "His thigh moves once more, and I feel him press against the spot that's practically {b}aching{/b} to be touched." 
                r "Hmm… Maybe I should check?" 
            n "One of [ch_ren]'s hands starts to move towards my bottoms to undo them, but he seems to hold himself back from going any further." 
            n "His half-lidded eyes find mine in the dark, and when I wordlessly nod my head to give him permission to continue, he doesn't waste a second." 
            n "[ch_ren] fumbles — but only for a moment — before I feel the cold touch of his fingers slide against my skin and push past the elastic of my underwear." 
            if genitalia == "cooter":
                n "Almost immediately, he brushes past my folds and collects my wetness with two of his slender fingers." 
            elif genitalia == "bussy":
                n "Almost immediately, his hand brushes against my dick and wraps around the base before giving it a squeeze." 
            else:
                n "Almost immediately, his hand brushes against the sensitive part of me that's aching the most." 
            y "{i}Ah—!{/i}" 
            n "My voice get muffled by the fabric of [ch_ren]'s cardigan as he leans closer to bury his face in the crook of my neck." 
            r "…Definitely wet." 
            n "His breath is hot against my skin, and it causes goosebumps to form all over my body. Soon enough, I find myself shamelessly arching into his touch in an attempt to feel more." 
            n "A multitude of sighs fall from my lips each time [ch_ren] repeats his actions, and whenever I try to close my thighs to stave off the waves of overwhelming pleasure, he simply nudges them apart with a smug chuckle." 
            r "[ch_angel]…" 
            n "The way [ch_ren] speaks my name with such… {b}tenderness{/b} seems far too innocent compared to the lewd mess he's creating between my legs." 
            if genitalia == "cooter":
                n "It does little to stop me from gripping onto his cardigan every time his fingers brush against my clit and makes me tremble with excitement." 
            elif genitalia == "bussy":
                n "It does little to stop me from gripping onto his cardigan every time his thumb brushes over the tip and makes me tremble with excitement." 
            else:
                n "It does little to stop me from gripping onto his cardigan as each thrum of excitement pulses through my entire body and makes me tremble with excitement." 
            n "And [ch_ren] — observant as ever — immediately picks up on my reactions and responds with a know-it-all grin on his features." 
            r "Are you shaking because it feels good? Or is it the rain?" 
            y "…" 
            n "Too caught up in everything, I barely have it in me to muster a response." 
            n "Yet [ch_ren] seems to take my silence as something to be {b}concerned{/b} about, as he soon draws back and searches for my gaze in the dark. When he notices just how much I've been trembling, a frown pulls at his lips." 
            r "Actually… M-Maybe we shouldn't be doing this here. I wouldn't want you to catch a cold." 
            y "Wha— Are you serious? I'm not shaking because of the rain—" 
            r "Here, don't worry." 
            if genitalia == "cooter":
                n "[ch_ren] cuts me off once again, but I can barely feel annoyed when one of his fingers casually slips past my folds." 
            elif genitalia == "bussy":
                n "[ch_ren] cuts me off once again, but I can barely feel annoyed when his hand is still casually stroking my cock." 
            else:
                n "[ch_ren] cuts me off once again, but I can barely feel annoyed when his hand is still casually rubbing against my sex." 
            if nsfw_position == "vers":
                r "If y'come back to my place, I promise I'll take good care of you. And if you be good f'me, I'll use more than just my hands." 
                r "D'you want that? Think you can behave for that long?" 
            else:
                r "If… I-If you want to come over and stay at my place for the night, I'll make it up to you, I swear." 
                r "I-I promise I'll be good for you." 
                r "And I'll make {i}you{/i} feel good, too. Promise!" 
            r "But first… we should probably find a way to stay dry, huh?" 
            n "Before I can say anything, [ch_ren] removes his hand, fixes my bottoms, and gives me one final, lingering kiss before pulling away fully." 
        "{image=14NWY symbol} Don't do anything":
            n "I watch as Ren looks over his shoulder and scans the area around him." 
    $ choice_style = "default"
    $ rem_yippee = True
    return
label DLC_day3_kitchen:
    n "Quietly sneaking up behind [ch_ren], I wait until he's occupied with his phone once more before I reach for his shirt and slide my hands underneath the soft material." 
    show ren blushing at bpop
    n "He {b}immediately{/b} lets out a sharp breath from the sudden surprise, but… doesn't seem to stop me. Instead, [ch_ren] sets his phone down on the counter and subconsciously leans into my touch." 
    n "A shaky sigh soon follows, and I feel the outlines and grooves of his muscles tense up whenever my fingers brush across them." 
    n "My hands casually roam against his skin — cold at first, though not as cold as his hands — before they wrap around his torso and soak in the warmth it emits." 
    n "Seeing just how far [ch_ren] would let me take this, I glide my fingers upwards across the large expanse of his chest and over his erratic heartbeat… and the next thing I know, they stumble upon something cool, round, and metallic." 
    n "No way— Were those… Did [ch_ren] have…" 
    show ren flushed at bpop
    r "A-Ahem!" 
    n "With bright red cheeks, [ch_ren] reaches for both my wrists and gently pulls my hands from underneath his shirt. Barely a second passes before he turns to me with a flushed smile, and places a few kisses on each of my knuckles." 
    show ren blushing at spop
    r "I-I— Um! I wasn't expecting you to do that so early in the morning." 
    show ren flushed at spop
    r "But— Well… A-Anyway!" 
    return
label DLC_day3_olivia:
    show olivia angry at spop
    o "W-What? You're lying!"  with vpunch
    show olivia frown at spop
    o "There's absolutely {i}no way{/i} someone like him would ever—" 
    show olivia sad at spop
    o "Unless {i}you're{/i} the one who we used to— But you can't be…" 
    y "Sounds like someone is jealous." 
    n "After the way [ch_olivia] carelessly treated me and my feelings the other day, I can't help but let that line slip. Oops." 
    show olivia flushed at bpop
    o "Why would I be jealous?!"  with vpunch
    show olivia frown at bpop
    o "I already have {i}the{/i} Teo Alvarado and an indie-rock drummer wrapped around my finger, what's there for me to be jealous about?" 
    show olivia angry at spop
    o "Well, whatever!" 
    return
label DLC_day3_inviteren:
    show ren blushing at bpop
    r "H-Huh?!"  with vpunch
    n "Almost immediately, [ch_ren] turns his back to me — whether it's out of privacy or embarrassment — and looks down at his pants." 
    n "Amused at how quickly he fell for my bluff, I kick my feet up onto the couch and watch his reactions with a smile on my face." 
    n "He lifts his outer cardigan up a few times — almost as if he wants to be absolutely certain — before he stands up with a huff and repeats the process all over again." 
    n "But when [ch_ren]'s search ends up fruitless, he turns to me with a faux look of betrayal in his eyes." 
    show ren sad at spop
    r "Wait… I-It's not…" 
    play audio "audio/sfx/item.ogg"
    n "He plops himself back onto the couch, crosses his arms, and offers me nothing more than a pout." 
    y "Relaaaax. I just wanted to tease you a little bit." 
    y "You know, you're {i}especially{/i} cute with those blushy cheeks and pouting expression of yours." 
    y "And it's… honestly kind of amusing watching you get riled up over something so small." 
    show ren flushed at spop
    r "…" 
    show ren blushing at spop
    r "Blushy cheeks? …P-Pouting expression?" 
    show ren flushed at spop
    r "…" 
    show ren smirk at spop
    r "Hm. Just wait til I get {i}you{/i} riled up." 
    play audio "audio/sfx/item.ogg"
    show ren smirk z at spop
    n "The next thing I know, [ch_ren] places one of his large hands on the back of the couch for support and leans over me. Because of the close proximity, I can feel the heat radiating from his body and the faint puffs of air that leave his lips." 
    n "His fingers cup my chin as he gently guides my face to look up at him. There's a smug look plastered all over his features, and when he starts to lean even closer, I'm quick to follow." 
    n "But just before our lips could touch, [ch_ren]'s pulling away and reaching for his fork." 
    play audio "audio/sfx/item.ogg"
    show ren neutral at spop
    r "You're not hungry?" 
    y "…Wh-What?" 
    show ren sad at spop
    r "The food. You don't want to eat?" 
    n "Why did he pull away?!" 
    n "As if sensing my bewilderment, [ch_ren] looks back at me with that same smug look from before." 
    show ren smirk at spop
    r "What? Y'can dish it but y'can't take it? Heh…" 
    show ren happy at spop
    r "Y'know, I think you're just as cute with that flushed expression of yours." 
    show ren smirk at spop
    r "Maybe I'll try and see just how much {i}more{/i} flushed and breathless I can make you later. Seeing you pressed against the couch like that has given me a few ideas…" 
    n "At that, [ch_ren] seems to move the conversation along as if nothing happened." 
    return
label DLC_day4_teo:
    if relationship_teo == "fling" and rem_boyfriend == False:
        n "But before I can fumble around in the dark to check, I feel a pair of large hands snake around my waist and pull me into its owner's chest." 
        y "What the {i}fuck{/i} are you doing?" 
        t "What does it look like?" 
        y "I thought you said we weren't going to do anything!" 
        t "We're not. I'm just making sure you're not standing in any fish slime." 
        y "…What? I doubt that's a real thing. And even if it is, why would it be in a {i}closet{/i} of all places— Wait! That's not the point!" 
        y "I know what you're trying to do, Teodore." 
        t "Damn. Not the full name." 
        n "Regardless of my stern tone, Teo continues to press his thumbs into the fabric of my shirt and casually squeeze my sides." 
        t "I've missed hearing you say it." 
        t "Can't forget the way you looked underneath me, either. So desperate and needy for my attention… Moaning out my name like it was going to earn you some kind of reward…" 
        t "Wanna take a walk down memory lane?" 
        y "{i}Teo.{/i} I swear—" 
        t "Aw, you mad, Dollface?" 
        $ choice_style = "box"
        menu:
            "{image=14NWY symbol alt} \"Fine. But only if you help me out.\"":
                t "Need a {i}hand{/i}, do you? Cute." 
                t "Unfortunately for you, I'm not feeling all that generous today, Doll. Especially after experiencing that bratty attitude of yours." 
                n "At that, Teo nudges one of his legs between my thighs and presses upwards. The feeling alone has me taking in a sharp intake of air — and threading my fingers in the material of his shirt with a soft moan." 
                t "If you want more than this, then you're gonna have to beg me." 
                t "Make sure to say my name real sweetly, too." 
                n "Even within the darkness of the closet, I hope Teo can see the venomous scowl I'm sending him." 
                n "But it doesn't last long, because soon he's guiding my hips into a slow rocking motion and sending waves of pleasure through my body." 
                n "Teo's voice comes out low and sultry, and I can feel him press his lips against the shell of my ear before he bites down." 
                t "C'mon, try it. Say {i}'Please, [ch_teo]. Please make me feel good'{/i}, just the way I like it." 
                if nsfw_position == "top" and genitalia == "bussy":
                    t "The way you {i}always{/i} do whenever you're desperate to put your dick inside me." 
                elif nsfw_position == "bottom":
                    t "The way you {i}always{/i} do whenever you're aching to be filled with my cock." 
                else:
                    t "The way you {i}always{/i} do whenever you're hungry for my cock." 
                y "N-Not a chance." 
                t "…You sure?" 
                n "Just as Teo says that, he abruptly pulls away from me with a mocking snicker. All of a sudden, the closet is far too cold and spacious again, and I find myself all alone." 
                y "You asshole—" 
                n "As I take a step back to gather my bearings, I almost end up slipping on something wet." 
                n "What the…?" 
            "{image=14NWY symbol} \"Fuck off, Teo.\"":
                t "Ouch." 
                n "Even in the dark, I don't need to see Teo's expression to know that he's smirking right now; I can practically hear the smug drawl in his voice." 
                n "But my message seems to be clear, as he immediately removes his hands from my body and takes a step back. When I do the same, I almost end up slipping on something wet." 
                n "What the…?" 
        $ choice_style = "default"
        return
    else:
        return
label DLC_day4_ren:
    y "You always seem to be on my mind. When I'm with my friends, when I'm at work, when I'm dreaming…" 
    y "Even late at night, when I'm feeling a little pent up and lonely…" 
    n "I hope [ch_ren] doesn't notice the way my cheeks grow warm as I confess my deepest, darkest secrets with him." 
    y "{i}You{/i} are all I think about during those times." 
    show ren blushing z at spop
    r "…" 
    show ren flushed z at bpop
    r "M-M-Me too! You're all I think about, too!" 
    show ren blushing z at spop
    r "Sometimes… I can't help it. I could be reading a book or watching anime, and all I'll see is you." 
    show ren flushed z at spop
    r "Then the next thing I know, my mind starts to wander, and here I am thinking about all kinds of indecent… {i}things{/i}." 
    if rem_wahoo == True:
        show ren blushing z at spop
        if nsfw_position == "top":
            r "Like… The way you'd look above me while I'm going down on you in the shower… O-Or pressing me against a library shelf while you have your way with me…" 
        elif nsfw_position == "bottom":
            r "Like… The way you'd look on your knees for me while we're in the shower… O-Or pressed against a library shelf with your head thrown back…" 
        else:
            r "Like… The way you'd look on your knees for me while we're in the shower… O-Or pressing me against a library shelf while you have your way with me…" 
        show ren lovesick z at spop
        r "Haa…" 
        show ren blushing z at spop
        r "S-Sometimes I wish you were near so I wouldn't have to use my hand all the time. It doesn't feel the same, and—" 
        show ren flushed z at spop
        r "{size=-6}The thought of you touching my— {i}Ugh.{/i}{/size}" 
        n "[ch_ren] cuts himself off by pressing his forehead against my shoulder." 
        show ren angry z at spop
        r "But just as things start to get good, something {i}always{/i} seems to get in the way and ruin it all. And right now, it's that green-haired loser…" 
    else:
        show ren angry z at spop
        r "But just as things start to get good, something {i}always{/i} seems to get in the way and ruin it all. And right now, it's that green-haired loser…" 
    return
label DLC_day4_renapartment:
    play audio "audio/sfx/item.ogg"
    show ren flushed z at bpop
    n "Without thinking, I make my way towards [ch_ren] and pull him into a deep kiss." 
    n "His calloused hands move to my face as one of his thumbs gently caresses my cheek, and I soon find myself melting from all his affection." 
    scene other_dark
    show peffectp
    with GlitchDissolve
    n "Before I know what's happening, I feel the welcome intrusion of [ch_ren]'s tongue against my lips, and I eagerly close my eyes and give him access." 
    n "Without breaking the kiss, I feel him gently usher me backwards — until my back hits the counter and I'm boxed in by his arms on either side." 
    n "[ch_ren]'s hands soon move towards my waist and underneath my shirt, but just as he starts to trail them upwards at an agonisingly slow pace, he pulls back with a knowing look on his features." 
    n "When I fully snap out of my daze, I notice that [ch_ren] had already moved back to his previous spot by the sink, but his eyes are still lingering on my body." 
    scene ren_kitchen_day
    show peffect
    show ren smirk at center
    with GlitchDissolve
    r "Don't get me wrong, I love how forward you are, [ch_angel]. But you don't typically do… {i}this{/i} kind of stuff without a reason." 
    n "Damn. He saw right through me." 
    n "Ah, forget it; maybe it was some form of righteousness, but I find myself confessing the truth." 
    return
label DLC_day4_angelapartment:
    n "Raising a brow in [ch_ren]'s direction, I give him a look." 
    menu:
        "{image=14NWY symbol} \"Is there something on my face?\"":
            show ren flushed at bpop
            r "Hm? O-Oh! Uhh… Yes! Here, want me to get it off?" 
            play audio "audio/sfx/item.ogg"
            show ren flushed z at spop
            n "Nodding, I lean closer so that [ch_ren] can remove whatever it is on my face." 
            n "Almost hesitantly, he reaches out and hovers just above my left cheek. But… He doesn't seem to move until I do first — almost as if he's afraid that touching me would scare me off." 
            n "Once I lean into his touch to let him know that it's okay to do so, [ch_ren]'s thumb carefully brushes against my skin in a soothing pattern. But all too quickly, his ghost-like touch turns into him cupping my face entirely." 
            n "His thumb soon drops to my lips, and I feel him gently part them as his breathing starts to pick up." 
            show ren lovesick z
            n "[ch_ren] is staring intently at my mouth now — almost like he's in a trance — and it's {b}then{/b} that I finally understand what's happening." 
            y "There's… nothing on my face, is there?" 
            show ren blushing z at spop
            r "…Huh?" 
            show ren flushed z at bpop
            r "No, I-I mean—! I think I got it, actually! Yep! All gone! Ahahah!" 
            play audio "audio/sfx/item.ogg"
            show ren flushed at spop
            n "He awkwardly pulls away and immediately busies himself with the cameras set out on the table." 
            n "With a knowing look, I leave him be… For now." 
            n "A comfortable silence soon follows, but it's short-lived the moment he clears his throat and speaks once more." 
            show ren sad at spop
            r "Actually… Now that I'm thinking about it…" 
            return
        "{image=14NWY symbol} \"Want to tinker with… something else?\"":
            show ren blushing at bpop
            n "Subtly, I part my thighs ever-so-slightly to get my intentions across." 
            n "In all honesty, I didn't think [ch_ren] would understand my meaning, but with the way he straightens up and casts a sideward glance in my direction, something tells me he knew what I meant." 
            show ren flushed at spop
            r "…" 
            show ren smirk at spop
            r "Don't tempt me." 
            n "He runs a hand up my leg and across my upper thigh — so close to where I'm aching to be touched — before he gives my skin a soft squeeze and pulls away." 
            show ren neutral at spop
            r "I'd rather you be safe from intruders {i}first{/i} before we take things any further." 
            show ren smirk at spop
            r "Besides… Maybe we can test if the cameras work by filming some… {i}stuff{/i}, later." 
            show ren neutral at spop
            r "We gotta make sure it's covering all angles of your apartment 'n all. Wouldn't want a single hiding spot t'go unseen." 
            show ren smirk at spop
            r "…Or flat surface." 
            n "Wait. Did he just suggest—" 
            show ren happy at spop
            r "Just kidding!" 
            n "At that, [ch_ren] goes back to the task at hand as if nothing just happened." 
            n "A comfortable silence soon follows, but it's short-lived the moment he clears his throat and speaks once more." 
            show ren sad at spop
            r "Actually… Now that I'm thinking about it…" 
            return
        "{image=14NWY symbol} Crawl into his lap":
            n "Without wasting another second, I crawl across the couch, situate myself between [ch_ren]'s thighs, and casually rest my arms over his shoulders." 
            play audio "audio/sfx/item.ogg"
            show ren blushing z at bpop
            r "U-Um! Hi…" 
            y "Keep doing what you're doing. Don't mind me." 
            show ren flushed z at spop
            r "I-It's kinda hard {i}not to{/i} when you're sitting on my… Uhh… Y'know—" 
            y "Oh, is {i}that{/i} what that is? I see. I thought you were just hiding a remote in your pocket, or something." 
            show ren blushing z at bpop
            r "Wh-Why would I possibly be hiding a—?!" 
            show ren flushed z at spop
            r "Who does that…? {i}Why{/i} would someone do that? N-Nevermind…" 
            play audio "audio/sfx/item.ogg"
            show ren blushing at spop
            n "Deciding to give [ch_ren] {i}a bit{/i} of breathing room, I lean back so I'm not {b}entirely{/b} all up in his business." 
            n "I'm still nestled — rather smugly — in his lap, though, and he's able to easily reach around me to continue working on setting up the security cameras." 
            n "A comfortable silence soon follows, but it's short-lived the moment [ch_ren] clears his throat and speaks once more." 
            return
        "{image=14NWY symbol} Don't do anything":
            n "He seems to pick up on my confusion and further explains his intentions." 
            return
label DLC_day5_bed:
    show mothphone flushed at bpop
    m "{size=+10}HELLO?!{/size}"  with hpunch
    show mothphone happy at spop
    m "And he looks just like Haruko, too?!" 
    show mothphone blushing at spop
    m "Wait… Is he actually…" 
    y "Submissive and breedable?" 
    show mothphone smirk at spop
    m "I was going to say {i}'Haruko'{/i}, but now I've got to know." 
    show ren sad at spop
    r "Am I… wh-what?" 
    show ren flushed at spop
    r "Well… I-I guess I am, but biologically speaking, I don't think I'm able to be bred—" 
    show mothphone flushed at spop
    m "Not with that attitude. Or is [ch_angel] not trying hard enough?" 
    y "[ch_moth]!" 
    return
label DLC_day5_stall:
    $ choice_style = "default"
    menu:
        "{image=14NWY symbol} \"Maybe you should…\"":
            show ren blushing z at bpop
            n "At that, [ch_ren]'s cheeks practically glow bright red." 
            show ren flushed z at spop
            r "B-But you're already changed…" 
            y "Why do you sound so disappointed, you pervert?" 
            show ren blushing z at bpop
            r "{size=+10}…!{/size}"  with vpunch
            show ren flushed z at bpop
            r "N-N-N-NO! No, I didn't— I wasn't— I just meant…" 
            show ren blushing z at bpop
            r "{size=-6}Ughhh… What I would give to have the ground swallow me up right now.{/size}" 
            show ren flushed z at spop
            r "I-I take back what I said. I didn't mean to—" 
            y "Relax, [ch_ren]. I'm only teasing you." 
            show ren blushing z at spop
            r "…Oh. Ahah~" 
            show ren flushed z at spop
            r "…" 
            show ren blushing z at spop
            r "But if you {i}wanted{/i} to get undressed, I wouldn't m—" 
        "{image=14NWY symbol} \"Can I watch you get changed instead?\"":
            play audio "audio/sfx/item.ogg"
            play audio "audio/sfx/shoes alt.ogg"
            show ren flushed at bpop
            n "Almost immediately, [ch_ren]'s head snaps up and he almost drops his bag. He nearly slams himself into the wall behind him as well, but manages to catch his footing just in time." 
            show ren blushing at bpop
            r "Y-Y-Y-Y-You want to—?! I mean— But that's—!" 
            y "Is that a no?" 
            show ren flushed at spop
            r "I don't mind, but… Well, you see, no one's really seen me without a shirt on before, and… And—" 
            n "I can practically see the steam rising from [ch_ren]'s head as he tries to come up with something to say. Taking pity on him, I decide to put him out of his misery." 
            y "Hey, it's okay. I'm only teasing." 
            show ren blushing at spop
            r "…Oh. Ahah~" 
            show ren flushed at spop
            r "…" 
            show ren blushing at spop
            r "Y'know, I was going to suggest watching me take my pants off instead, but…" 
            y "Wait. Are you serious—" 
        "{image=14NWY symbol} \"Are you blushing again?\"":
            show ren blushing z at bpop
            r "…!" 
            show ren flushed z at spop
            r "N-N-No! …Maybe?" 
            y "I'll be the judge of that." 
            n "Stumbling my way through the dimly lit area, I reach out towards [ch_ren] and cup his face with my hands. His own immediately reach for my wrists — not to pull them away — but to hold onto." 
            y "Yeah, they're warm, alright. That's about a nine on the [ch_ren]-blush-o-meter." 
            show ren blushing z at spop
            r "You have a scale for that?" 
            y "Mhm! Exclusive to you." 
            show ren smirk z at spop
            r "So… No one else has a scale? Just me?" 
            y "Yes?" 
            show ren happy z at spop
            r "…" 
            show ren smirk z at spop
            r "Hey, d'you think you could touch me a little lower—" 
        "{image=14NWY symbol} \"Alright then. Thank you, [ch_ren].\"":
            show ren neutral z at spop
            r "Mm! Of course!" 
            show ren happy z at spop
            r "If you want, I can—" 
    $ choice_style = "box"
    return
label DLC_day5_kitchen:
    n "I don't know what compels me to do this, but I reach for [ch_ren]'s belt and pull him closer to me." 
    n "He doesn't seem to mind at all — in fact, it's as though all his sadness washes away the moment I reach for him, and instead gets replaced with something more tender." 
    show ren neutral z at spop
    r "…Angel?" 
    show ren smirk z at spop
    r "You know your friend is standing nearby, right?" 
    show ren neutral z at spop
    r "And they're looking at you like you've just done something crazy." 
    y "I {i}did{/i} just reach for your crotch area…" 
    n "[ch_ren] only seems to let out an amused laugh at my words before leaning closer." 
    show ren smirk z at spop
    r "You're so insatiable. I s'pose it's a good thing that I'm into it, huh?" 
    return
label dlc_14nwy_d1_t1:
    n "Hearing him swear sends a wave of pleasure through my body." 
    n "And as if [ch_ren] could sense my neediness, I feel him reach below to experimentally play with my [parts]." 
    n "He gently runs his fingers across before he applies more pressure. My breath hitches in my throat as I throw my head back, once again arching into his addictive touch." 
    return
label dlc_14nwy_d1_t2:
    n "I don't miss the small bottle of lube in one of [ch_ren]'s hands once he returns — no doubt something he fished from his pockets — but it soon becomes an afterthought the moment he leans closer and gives me a slow kiss." 
    n "While he busies himself with opening the lid and smearing some of the liquid onto his fingers, I take it upon myself to make {b}him{/b} feel good as well." 
    return
label dlc_14nwy_d1_t3:
    r "…Just like that. Use me to pleasure yourself." 
    return
label dlc_14nwy_d1_t4:
    n "He quickens his pace, and suddenly, my vision goes white. My toes curl as [ch_ren] continues to tease my [parts] and [sex], and I come with his name on my tongue." 
    return
label dlc_14nwy_d1_t5:
    n "But during my hazed-out state, I came to the realisation that [ch_ren] was {b}still{/b} hard — if his \"subtle\" grinding against my side had anything to do with it. So I nudge his thighs apart and beckon him closer." 
    return
label dlc_14nwy_d1_t6:
    n "Apparently, that was all it took to have him back on me once more, with his hungry mouth on mine as his hand moves to line up my [length] with his lubed hole." 
    return
label dlc_14nwy_d1_t7:
    n "Considering how [ch_ren] has apparently never done something like this before, he decides to take things nice and slow." 
    n "I watch in awe as he tries to take every inch inside of his tight hole with a blissed out look on his face." 
    if length == "strap-on":
        n "I almost forget to breathe as the base of my strap-on deliciously rubs against one spot in particular, and I unconsciously latch onto his thighs to anchor myself." 
        r "A-Ah… I haven't taken anything as big as this before…" 
    else:
        n "I almost forget to breathe as I feel his walls clench around my [length], and I unconsciously latch onto his thighs to anchor myself." 
        r "A-Ah… I haven't taken anything as big as you before…" 
    n "What felt like hours seemed to pass before [ch_ren] {b}finally{/b} bottoms out on my [length], and he almost seems to double over once more from the sheer pleasure of it all." 
    n "He looks down at me once more with those soft blue eyes of his, and the entire exchange suddenly feels {b}far more{/b} intimate than actually having me inside of him." 
    n "[ch_ren]'s hand moves to tenderly cup my cheek, before he bends down to give me a chaste kiss on the forehead." 
    return
label dlc_14nwy_d1_t8:
    r "Hah— Look~ You're finally inside me… You feel {i}amazing{/i}, Angel." 
    return
label dlc_14nwy_d1_t9:
    n "Despite [ch_ren]'s tender words, the sudden movement of his hips takes me off guard as he starts to ride my length." 
    n "But my pleasure isn't far from his thoughts, it seems, as he's quick to reach down and play with my [parts], which sends a wave of excitement throughout my entire body." 
    r "Y-You're making such a {i}mess{/i} out of me…" 
    return
label dlc_14nwy_d1_t10:
    n "[ch_ren] doesn't lift his hips yet, instead choosing to look down at me with soft eyes as he adjusts to having something inside him for the first time." 
    r "I-Is it uncomfortable? Let me know if anything hurts, okay? Just say the word, and we can stop." 
    n "His sincerity touches me as he tries to remain still atop of me, but I can tell from his rough expression that he's trying to hold himself back." 
    n "[ch_ren] seems to be in the {b}slightest{/b} bit of pain — judging by the sweat that forms near his brows — so I reassure him by running my hands along his thighs and pulling him closer." 
    n "At that, [ch_ren] seemingly finds enough confidence to move." 
    n "But my pleasure isn't far from his thoughts, it seems, as he's quick to reach down and play with my [parts] — which sends a wave of excitement throughout my entire body." 
    n "His tentative pace soon changes as he experimentally grinds himself on my [length], and the hand that brushed against my skin soon comes to interlock with one of my own." 
    return
label dlc_14nwy_d1_t11:
    r "Look at you, laying there with such a lewd expression on your face. {i}Fuck.{/i} You're making me feel so good right now…!" 
    return
label dlc_14nwy_d1_t12:
    n "His expression does little to stifle the sensation slowly building between my legs, and I unconsciously thrust my hips upwards. [ch_ren] lets out another shaky moan before he effortlessly reaches for my [parts] to stimulate me further." 
    n "The sensation has me seeing stars, and sends my eyes rolling into the back of my head." 
    return
label dlc_14nwy_d1_t13:
    n "My praise only seems to spur him on as his hand {b}and{/b} hips start to move more fervently, and [ch_ren] practically starts to lose himself to the pleasure." 
    return
label dlc_14nwy_d1_t14:
    if genitalia == "bussy":
        n "Hearing him cry out my name with such {b}neediness{/b} is what finally sends me over the edge once more, and I come inside [ch_ren] with his own name on my lips." 
    else:
        n "Hearing him cry out my name with such {b}neediness{/b} is what finally sends me over the edge once more, and I come undone with [ch_ren]'s own name on my lips." 
    n "[ch_ren] isn't far off, it seems, as it only takes him a few more seconds of shamelessly riding my [length] before he reaches his peak." 
    n "One of his hands grip my bedsheets in a crushing hold as he cries out my own name as well." 
    return
label dlc_14nwy_d3_t1:
    r "I-I already applied some lube earlier, but if you need me to, I can—" 
    r "That is— U-Um…" 
    r "Do you want me to suck you off before I— Before {i}we{/i}—" 
    n "[ch_ren] can't seem to concentrate with the way his words come out slurred and needy, so I decide to put him out of his misery by reaching for my [length] instead and lining it up with his hole." 
    n "He immediately catches on — lifting his hips and spreading his thighs further. I almost miss the warmth of his body on mine, but the sudden sensation of [ch_ren] hovering over my tip draws my attention away." 
    if length == "strap-on":
        n "With slow, deliberate movements, [ch_ren] gently lowers himself, and I can barely hold back the sounds of my voice as the base of my [length] rubs against my sex." 
    else:
        n "With slow, deliberate movements, [ch_ren] gently lowers himself, and I can barely hold back the sounds of my voice as his walls squeeze around [length]." 
    return
label dlc_14nwy_d3_t2:
    if nsfw_position == "top" or nsfw_position == "temp_top":
        r "Missed this… Missed having you inside me…" 
    else:
        r "Missed this… Missed doing this with you…" 
    return
label dlc_14nwy_d3_t3:
    if length == "strap-on":
        n "The pleasurable feeling coming from the inner side of my [length] practically steals the air from my lungs, and I can't help but lift my hips off of the couch and buck into [ch_ren] for even {b}more{/b} friction." 
    else:
        n "The pleasurable feeling of his walls squeezing around my [length] practically steals the air from my lungs, and I can't help but lift my hips off of the couch and buck into [ch_ren]." 
    return
label dlc_14nwy_d3_t4:
    r "…You haven't done this with anyone else since last time, right? Only me?" 
    r "Doesn't really matter anyway. Gonna make sure {i}I'm{/i} the only one y'wanna fuck from now on." 
    return
label dlc_14nwy_d3_t5:
    r "Doesn't really matter anyway. Gonna make sure {i}I'm{/i} the only one y'wanna fuck from now on." 
    return
label dlc_14nwy_d3_t6:
    n "The next thing I know, [ch_ren]'s hungry mouth and body are on mine once more as he reaches down to play with my [parts]." 
    return
label dlc_14nwy_d3_t7:
    n "Leaving another hickey, no doubt — and had I not been fucking [ch_ren] within an inch of his life — I would've fully noticed the possessive undertones of his actions." 
    return
label dlc_14nwy_d3_t8:
    n "Before I can respond, [ch_ren] {b}fully{/b} sheaths my [length] inside of his tight hole and starts to grind his hips. But just as he lets out a moan from the friction, he starts to move once more." 
    n "[ch_ren] sets a brutal pace now, and all I could do was latch onto the throw pillows above my head and let him ride me to completion." 
    r "No one else could ever compare to you…" 
    r "Y'feel so good too, filling me up 'n leaving me full." 
    n "[ch_ren] spreads his thighs even more before he returns his attention back towards my [bust], which has me seeing stars." 
    n "I can feel his hole squeeze around my [length], and once my tip hits that particular spot inside of him, [ch_ren] can't help but cry out and reach for my [parts] once more." 
    return
label dlc_14nwy_d3_t9:
    n "[ch_ren]'s voice does little to hide his desire and hunger for me, and he makes it known by bouncing on my [length] with reckless abandon." 
    return
label dlc_14nwy_d3_t10:
    r "Nobody else will make you feel as good as me." 
    if length == "strap-on":
        r "And there's nobody else who can take you as well as I can." 
        r "Though it's not like they'll even get the chance to try." 
    else:
        r "Try as much as you want, but it's {i}my{/i} hole that your [length] will crave." 
        r "Nobody else can take you as well as I can. They won't even get the chance to try." 
    return
label dlc_14nwy_d3_t11:
    if genitalia == "cooter":
        n "The pleasure is almost too much to bear, and I throw my head back in ecstatic bliss. And [ch_ren] — ever attentive to my needs — continues to rubs circles against my clit instead." 
    elif genitalia == "bussy":
        n "His length is going deeper than ever now, and I throw my head back in ecstatic bliss. And [ch_ren] — ever attentive to my needs — moves one of his hands from my [bust] to stroke my weeping cock instead." 
    else:
        n "His length is going deeper than ever now, and I throw my head back in ecstatic bliss. And [ch_ren] — ever attentive to my needs — moves one of his hands from my [bust] to stimulate my sex instead." 
    return
label dlc_14nwy_d3_t12:
    if length == "cock":
        r "That's it. Give it to me. Be good f'me and come inside my ass." 
    else:
        r "That's it. Give it to me. Be good f'me and come as hard as you can." 
    r "C'mon, [ch_angel]. Show me who I belong to, who makes you feel this good." 
    return
label dlc_14nwy_d3_t13:
    n "Something rough and textured brushes against my fingertips, but I pay it no mind as as I feel [ch_ren]'s teeth on my shoulder and come." 
    n "[ch_ren] seems to have other plans, though, as his hips start to stutter — and before I know it, his strained voice is whimpering into my neck once more as he spills himself on both our stomachs." 
    return
label dlc_14nwy_d3_t14:
    if length == "cock":
        n "He doesn't seem to remove himself from my [length] though — and much like last time — I remain balls deep inside him as we both melt into the couch." 
    else:
        n "He doesn't seem to detach himself from me though — and much like last time — we both remain as close as possible while [ch_ren] pulls me closer into the couch." 
    return
label dlc_14nwy_d3_t15:
    if length == "cock":
        n "He doesn't seem to remove himself from my [length] though, and I remain balls deep inside him as we both melt into the couch." 
    else:
        n "He doesn't seem to remove himself from my [length] though, so we both remain as close as possible while [ch_ren] pulls me closer into the couch." 
    return
label dlc_14nwy_d5_t1:
    $ jump_one = "day5_wahooscene"
    $ jump_two = "day5_renevening"
    call screen warningnsfw with dissolve
return