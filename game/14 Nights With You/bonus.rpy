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
        n "As I fumble around for the strap-on I kept hidden away (for moments such as these) and start to prep for what's about to happen, [ch_ren] makes a sound and pulls away from me with an awkward laugh." nointeract
    else:
        n "As I start to prep for what's about to happen, [ch_ren] makes a sound and pulls away from me with an awkward laugh." nointeract
    r "Um— You should know that I've never had someone else put— I mean, I-I've never… {i}y'know{/i}… back there, before…" nointeract
    r "I mean— Sure, I've {i}experimented{/i} with myself and stuff, but…" nointeract
    r "W-Well, I've never— Not with another person before." nointeract
    n "Wait, was he serious?" nointeract
    n "Almost shyly, [ch_ren] tears his gaze from mine with a crooked smile and a faint dusting of red on his cheeks." nointeract
    r "I just figured you should know." nointeract
    menu:
        "It's my first time doing this":
            $ rem_wahoo = False
            $ first_time = True
            y "You know, it's actually my first time doing something like this, too." nointeract
            r "{size=+10}W-Wait, really?!{/size}" nointeract with vpunch
            r "So then… I'm your first as well?" nointeract
            n "[ch_ren] beams down at me with such a tender and loving expression as his hand shyly starts to travel towards my [length]." nointeract
        "I've done this before":
            $ rem_wahoo = True
            $ first_time = False
            y "Actually… I've done this before." nointeract
            n "For the briefest moment, a frown pulls at [ch_ren]'s features — before he masks it with that familiar, kind-hearted smile I've grown fond of." nointeract
            r "I-I see." nointeract
            r "Then I'd better make this something you won't forget, huh?" nointeract
            r "By the end of this, you won't even remember anyone who came before me." nointeract
            n "With a determined look on [ch_ren]'s face, he slowly reaches for my [length] and gives it an experimental squeeze." nointeract
        "I'm happy to be his first":
            $ rem_wahoo = True
            $ first_time = False
            y "Thanks for telling me. I'm happy I get to be your first, [ch_ren]." nointeract
            r "…M-Me too! I'm glad I get to experience this with you, too!" nointeract
            n "With a bright smile on [ch_ren]'s features, he shyly reaches for my [length] and gives it a few experimental strokes." nointeract
        "It doesn't really matter":
            $ rem_wahoo = True
            $ first_time = False
            y "Right now, all I want to do is be inside of you, [ch_ren]." nointeract
            r "R-Right! Yeah! O-Of course!" nointeract
            r "I, um… I want that too. You have no idea how badly I've— I'll shut up now." nointeract
            n "[ch_ren] looks down at me with an embarrassed expression as his hand shyly starts to travel towards my [length]." nointeract
    return
label DLC_firsttime_giving:
    if persistent.dlc_14nightswithyou_type == "paid" and persistent.dlc_14nwy_comp == False:
        return
    $ first_giving = False
    n "But before I can go any further, I tentatively look back at [ch_ren] with a certain gleam in my eyes." nointeract
    $ choice_style = "box"
    menu:
        "It's my first time doing this":
            $ ren_yippee = False
            y "You should know… I've never actually gone down on someone before." nointeract
            r "R-Really? You've never…?" nointeract
            if first_ren_giving == False:
                pass
            else:
                r "Then… We're the same!" nointeract
            r "Haaaah~ I don't know why hearing that is making me feel so happy…" nointeract
            n "Seeing [ch_ren]'s tender smile gives me all the reassurance and motivation I need to continue." nointeract
        "I've done this before":
            $ rem_yippee = True
            n "[ch_ren] seems to notice my sudden pause and immediately looks down at me with worry in his eyes." nointeract
            r "…Is everything okay, Angel?" nointeract
            y "Oh, yeah. Just fine. It's just… It's been a while since I done something like this." nointeract
            r "I-I see…" nointeract
            n "An emotion I can't quite place seems to wash over [ch_ren] as I watch his brows pull into a frown — before they go back to normal." nointeract
            r "Well, Still. I'm glad you {i}want{/i} to do something like this with me." nointeract
            r "I've never… Y-You're the first person who's ever gone down on me, so I'm glad I get to experience it with you." nointeract
            n "Wow, really? Was he being serious right now?" nointeract
            n "All the more reason for me to make this an {b}extra{/b} memorable experience for him, I guess." nointeract
            n "[ch_ren]'s confession give me all the reassurance and motivation I need to continue." nointeract
    $ choice_style = "default"
    return
label DLC_firsttime_receiving:
    if persistent.dlc_14nightswithyou_type == "paid" and persistent.dlc_14nwy_comp == False:
        return
    $ first_receiving = False
    n "But before [ch_ren] can go any further, I tentatively reach for him in an attempt to get his attention." nointeract
    $ choice_style = "box"
    menu:
        "It's my first time doing this":
            y "You should know… I've never had someone do {i}this{/i} to me before." nointeract
            n "At my words, [ch_ren] seems to halt his actions and look up at me with wide eyes." nointeract
            r "…I-I'm the first person to go down on you like this? H-Haaah~" nointeract
            n "His smile only seems to grow wider as he nuzzles his face closer to my body and presses soft, butterfly kisses against my skin." nointeract
            r "Don't worry, I promise I'll make you feel good! And…" nointeract
            r "Well, I've never actually done this before as well. S-So we're the same." nointeract
            r "Ahh~ This makes me so happy!" nointeract
            n "With a tender smile blooming on [ch_ren]'s face, he picks up where he left off with newfound eagerness." nointeract
        "I've done this before":
            n "[ch_ren]'s gaze immediately flickers to mine with a hint of concern in them." nointeract
            r "…Angel?" nointeract
            y "It's nothing, don't worry." nointeract
            r "I-If you say so…" nointeract
            n "At that, [ch_ren] hesitantly goes back to what he was previously doing — but not before sending me one last worried look." nointeract
            n "When I give him a reassuring smile in return, he takes that as a sign to pick up where he left off with newfound eagerness." nointeract
    $ choice_style = "default"
    return
label DLC_day1_library:
    menu:
        "{image=14NWY symbol} He looks like he wants to devour me":
            n "The way he's looking at me… It's almost as if he wants to take a bite out of me." nointeract
            n "There's an almost possessive gleam behind those blue eyes of his which makes it hard to look away — but it's even harder to miss the way they flicker towards my neck before they meet my gaze once more." nointeract
            n "It's almost as if he was trying to map out and memorise every inch of my skin, and the thought alone ignites a flutter of excitement from within me." nointeract
            n "Part of me feels tempted to take a step closer to this stranger just to see how he'd react, but then I remember where I am and what I was initially supposed to be doing." nointeract
            n "Focus, [ch_angel]. You're at work right now. You should be helping this person find a book, not awkwardly ogling them in silence." nointeract
        "{image=14NWY symbol} He looks like he wants me to come closer":
            n "With the way this stranger keeps glancing at me — taking in every inch of me — I can't help but wonder if that was his way of subtly inviting me to come closer." nointeract
            n "As if to test the waters, I take a tentative step in his direction, and he reacts exactly how I expected him to." nointeract
            n "The stranger's eyes widen in surprise as he awkwardly leans against the shelf, and from the corner of my eye, I see his hand twitch in my direction. Was he holding himself back?" nointeract
            n "But just as I'm about to comment on it, I remember where I am and what I was initially supposed to be doing." nointeract
            n "Focus, [ch_angel]. You're at work right now. You should be helping this person find a book, not awkwardly ogling them in silence." nointeract
        "{image=14NWY symbol} He looks like he wants to press me up against the shelf":
            n "There's an unmistakable gleam behind those blue eyes of his, one that speaks louder than words." nointeract
            n "And if the half-lidded look wasn't enough, the twitch in his hand as it reaches for me speaks volumes. But just before the stranger tries to do anything, he abruptly withdraws and goes back to awkwardly picking at the ends of his sleeves." nointeract
            n "The pink-haired stranger can barely meet my gaze now, and his cheeks reveal his embarrassment by turning a deep shade of red — one that reaches all the way to his ears." nointeract
            n "I almost want to comment on them, but then I remember where I am and what I was initially supposed to be doing." nointeract
            n "Focus, [ch_angel]. You're at work right now. You should be helping this person find a book, not awkwardly ogling them in silence." nointeract
        "{image=14NWY symbol} I must be seeing things":
            n "What was I thinking? Besides, I'm at work right now — this was hardly appropriate. From that thought alone, I remember where exactly I am and what I was initially supposed to be doing." nointeract
    n "When I glance back at the stranger with an apologetic look, I notice that his attention has already shifted. Curious, I follow his gaze and suddenly remember what I'm holding in my hands." nointeract
    n "Jeez, how could I forget so easily? But more importantly… Why was he looking at it so intently?" nointeract
    return
label DLC_day1_text:
    rt ".:GKJ" nointeract with vpunch
    rt "I ACCIDENTSLLY HIT SEND ARGHKS SRRY OH GOD SORRY I'M SO SORRY" nointeract
    n "There's a very, very, {b}very{/b} long pause before [ch_ren] replies." nointeract
    rt "…did u mean to send me that? >///<" nointeract
    rt "um. if u want i can send a photo? would u like that?" nointeract
    rt "ahhh but it's rlly dark in my room right now TT_TT besides! i wanted to ask u something actually :3" nointeract
    rt "u see… i was wonderinf if u were free tomorrow? i still wanted to thank u for helping me find that book" nointeract
    return
label DLC_day1_call:
    rcall "{size=+10}S-S-S-Sorry?!{/size}" nointeract with vpunch
    rcall "I… Um… W-Well! Ahah… I'm still wearing the same outfit from earlier." nointeract
    rcall "Oh! But I took off one of my sweaters because it was getting a bit stuffy in y— My… room." nointeract
    n "I was about to ask if the late autumn air didn't bother him — especially at this time of night — but [ch_ren] cuts me off with yet another response." nointeract
    rcall "B-But that's not really an appealing answer, is it?" nointeract
    rcall "Or… Wait. Were you referring to what I'm wearing {i}underneath{/i} my clothes? Because…" nointeract
    rcall "Well, I don't think I can say without feeling embarrassed, ahaha~" nointeract
    rcall "S-Sorry." nointeract
    return
label DLC_day2_cafe:
    n "[ch_ren]'s cheeks are still scarlet red — and he seems almost {b}fidgety{/b} with how his leg keeps bouncing under the table — so I take this opportunity to tease him a bit." nointeract
    n "After all, [ch_ren] doesn't seem to notice the stray pieces of crumbs clinging to his bottom lip yet, which gives me a few mischevious ideas." nointeract
    menu:
        "{image=14NWY symbol} Lean in and lick the crumbs off his lip":
            show ren blushing z at bpop
            r "{size=+10}A-A-Ah!{/size}" nointeract with vpunch
            show ren flushed z at spop
            r "Y-Y-Y-You—!" nointeract
            y "You had some crumbs on your face. I just wanted to help get them off." nointeract
            show ren blushing z at spop
            r "You just licked me… Your tongue touched my—" nointeract
            show ren lovesick z at spop
            r "…Hahahah~" nointeract
            n "Almost immediately, [ch_ren] covers his mouth with the sleeve of his cardigan as his cheeks somehow grow an even {b}darker{/b} shade of red." nointeract
            n "He isn't really subtle with the way he crosses his legs underneath the table, nor the way he clumisly reaches for his drink in an attempt to distract himself with a sip." nointeract
            n "Satisfied with my teasing, I leave [ch_ren] alone and focus my attention back on the plate in front of me." nointeract
        "{image=14NWY symbol} Kiss him in an attempt to remove it":
            show ren blushing z at bpop
            r "—Mn!" nointeract
            n "Just as I anticipated, [ch_ren] tenses up the moment my lips touch his — almost as if he wasn't expecting me to do that — before his eyelids flutter closed and he lets out a dreamy sigh." nointeract
            n "But before the kiss can deepen, I pull away with a satisfied glint in my eyes." nointeract
            y "You had some crumbs on your face. I just wanted to help get them off." nointeract
            show ren flushed z at spop
            r "S-So you… kissed me? Then in that case…" nointeract
            show ren smirk z at spop
            r "Looks like y'got some food on your face, too. Here." nointeract
            n "Before I can respond, [ch_ren] leans in once more and gives me yet another kiss." nointeract
            n "There's hardly anything soft or gentle about this one, and just as I feel his tongue start to curiously prod against my bottom lip, I hear a nearby customer clear their throat in an exasperated manner." nointeract
            n "Ignoring their gaze, I pull away from [ch_ren] with a sheepish smile and watch as he awkwardly shifts in his seat… Before he crosses his legs and pulls the bottom of his cardigan over his lap." nointeract
        "{image=14NWY symbol} Reach up and wipe it off with your finger":
            show ren neutral z at bpop
            r "…" nointeract
            n "Just as I wipe the pieces of cake from his lips, his tongue peeks out and brushes against the tip of my thumb." nointeract
            n "A faux innocent smile is all I get in response, so I decide to amp up my teasing by leaving my finger there and seeing what else [ch_ren] would do." nointeract
            n "Almost immediately, his hand wraps around my wrist as he opens his mouth to suck on my thumb." nointeract
            show ren smirk z at spop
            r "Don't wanna waste any food." nointeract
            y "S-Sure." nointeract
            n "How is that {b}I'm{/b} the one who ended up flustered? With a bewildered look on my face, [ch_ren] pretends nothing happened and goes back to enjoying his cake — though he isn't subtle with the way he shifts in his seat and adjusts his pants." nointeract
            n "Ah. I see." nointeract
        "{image=14NWY symbol} Don't do anything at all":
            show ren sad z at spop
            r "Something wrong?" nointeract
            n "As if noticing what I've been staring at, [ch_ren] brushes his fingers across his face and notices the crumbs." nointeract
            show ren blushing z at spop
            r "O-Oh. Heh, how embarassing." nointeract
            show ren flushed z at spop
            r "All gone now?" nointeract
            n "He looks at me for confirmation, and when I give it, he goes back to eating — but not before attempting to hide his flushed cheeks with the sleeve of his cardigan." nointeract
    return
label DLC_day2_rain:
    r "It's really pouring, huh? Here, let's stand over here instead." nointeract
    n "At that, [ch_ren] gently ushers me into the dark alleyway between two buildings." nointeract
    scene other_dark
    hide screen menuwu
    show screen dayscalendar
    show peffectp
    play audio "audio/sfx/movement.ogg"
    $ quick_menu = True
    with Fade(1.0, 1.0, 1.0)
    n "He's quick to press himself against me, likely in an attempt to shield my body from the rain." nointeract
    n "Or perhaps he was just looking for an excuse to be close to me? Either way, [ch_ren]'s actions — and his sudden closesness — got me thinking…" nointeract
    $ choice_style = "box"
    menu:
        "{image=14NWY symbol alt} Press a kiss against his neck":
            n "I'm not sure what comes over me in that moment, but I find myself leaning closer to [ch_ren] and placing a kiss on the exposed spot between the underside of his jaw and neck." nointeract
            r "Ah! Fu—" nointeract
            r "Wh-What are you doing…" nointeract
            n "As if he's acting purely on impulse, [ch_ren] pulls my body {b}even closer{/b} to his own as his large arms wrap around my waist. Hot puffs of air ghost across my shoulder as he tries his best to calm his breathing, but it ultimately seems futile." nointeract
            n "Feeling particularly devious, I place another kiss against the juncture below [ch_ren]'s earlobe, and his reaction is immediate." nointeract
            n "One of his hands squeezes my sides tighter, while the other moves to my leg to lift it up and rest it against his thigh." nointeract
            n "[ch_ren]'s own thigh soon takes up the empty space, and I can feel him not-so-subtly rut himself against me." nointeract
            n "I won't lie, the friction from his jeans feels {b}amazing{/b} — but before I can do anything in return, [ch_ren] cuts me off with a low and husky tone." nointeract
            r "…We really shouldn't be doin' somethin' like this out here." nointeract
            y "{i}You're{/i} the one rubbing yourself against me without a care in the world." nointeract
            r "…" nointeract
            n "[ch_ren] takes in a deep inhale before he presses a kiss of his own against my shoulder and pulls away." nointeract
            if genitalia == "cooter":
                r "You're right. This isn't the place for that. 'N you're soaking wet, Angel." nointeract
                y "…From the rain, right?" nointeract
                n "Even though it's hard to see in this dark alleyway, I still make out the way his eyes narrow as his lips pull into a sly smile." nointeract
                n "As if to tease me even {b}more{/b}, [ch_ren] angles his thigh and purposefully brushes his knee against my core." nointeract
                r "Hmm… Maybe I should check?" nointeract
            elif genitalia == "bussy":
                r "You're right. This isn't the place for that. Besides, you're probably all wet and sticky right now, aren't you?" nointeract
                r "We should continue this at another time. I'd rather you didn't catch a cold." nointeract
                y "…From the rain, right?" nointeract
                n "Even in the dark alleyway, I can see his eyes narrow as his lips pull into a sly smile." nointeract
                n "As if to tease me even {b}more{/b}, [ch_ren] angles his thigh and purposefully brushes it against my growing hard-on." nointeract
                r "Hmm… Maybe I should check?" nointeract
            else:
                r "You're right. This isn't the place for that. Besides, you're probably all wet and sticky right now, aren't you?" nointeract
                y "…From the rain, right?" nointeract
                n "Even in the dark alleyway, I can see his eyes narrow as his lips pull into a sly smile." nointeract
                n "His thigh moves once more, and I feel him press against the spot that's practically {b}aching{/b} to be touched." nointeract
                r "Hmm… Maybe I should check?" nointeract
            n "One of [ch_ren]'s hands starts to move towards my bottoms to undo them, but he seems to hold himself back from going any further." nointeract
            n "His half-lidded eyes find mine in the dark, and when I wordlessly nod my head to give him permission to continue, he doesn't waste a second." nointeract
            n "[ch_ren] fumbles — but only for a moment — before I feel the cold touch of his fingers slide against my skin and push past the elastic of my underwear." nointeract
            if genitalia == "cooter":
                n "Almost immediately, he brushes past my folds and collects my wetness with two of his slender fingers." nointeract
            elif genitalia == "bussy":
                n "Almost immediately, his hand brushes against my dick and wraps around the base before giving it a squeeze." nointeract
            else:
                n "Almost immediately, his hand brushes against the sensitive part of me that's aching the most." nointeract
            y "{i}Ah—!{/i}" nointeract
            n "My voice get muffled by the fabric of [ch_ren]'s cardigan as he leans closer to bury his face in the crook of my neck." nointeract
            r "…Definitely wet." nointeract
            n "His breath is hot against my skin, and it causes goosebumps to form all over my body. Soon enough, I find myself shamelessly arching into his touch in an attempt to feel more." nointeract
            n "A multitude of sighs fall from my lips each time [ch_ren] repeats his actions, and whenever I try to close my thighs to stave off the waves of overwhelming pleasure, he simply nudges them apart with a smug chuckle." nointeract
            r "[ch_angel]…" nointeract
            n "The way [ch_ren] speaks my name with such… {b}tenderness{/b} seems far too innocent compared to the lewd mess he's creating between my legs." nointeract
            if genitalia == "cooter":
                n "It does little to stop me from gripping onto his cardigan every time his fingers brush against my clit and makes me tremble with excitement." nointeract
            elif genitalia == "bussy":
                n "It does little to stop me from gripping onto his cardigan every time his thumb brushes over the tip and makes me tremble with excitement." nointeract
            else:
                n "It does little to stop me from gripping onto his cardigan as each thrum of excitement pulses through my entire body and makes me tremble with excitement." nointeract
            n "And [ch_ren] — observant as ever — immediately picks up on my reactions and responds with a know-it-all grin on his features." nointeract
            r "Are you shaking because it feels good? Or is it the rain?" nointeract
            y "…" nointeract
            n "Too caught up in everything, I barely have it in me to muster a response." nointeract
            n "Yet [ch_ren] seems to take my silence as something to be {b}concerned{/b} about, as he soon draws back and searches for my gaze in the dark. When he notices just how much I've been trembling, a frown pulls at his lips." nointeract
            r "Actually… M-Maybe we shouldn't be doing this here. I wouldn't want you to catch a cold." nointeract
            y "Wha— Are you serious? I'm not shaking because of the rain—" nointeract
            r "Here, don't worry." nointeract
            if genitalia == "cooter":
                n "[ch_ren] cuts me off once again, but I can barely feel annoyed when one of his fingers casually slips past my folds." nointeract
            elif genitalia == "bussy":
                n "[ch_ren] cuts me off once again, but I can barely feel annoyed when his hand is still casually stroking my cock." nointeract
            else:
                n "[ch_ren] cuts me off once again, but I can barely feel annoyed when his hand is still casually rubbing against my sex." nointeract
            if nsfw_position == "vers":
                r "If y'come back to my place, I promise I'll take good care of you. And if you be good f'me, I'll use more than just my hands." nointeract
                r "D'you want that? Think you can behave for that long?" nointeract
            else:
                r "If… I-If you want to come over and stay at my place for the night, I'll make it up to you, I swear." nointeract
                r "I-I promise I'll be good for you." nointeract
                r "And I'll make {i}you{/i} feel good, too. Promise!" nointeract
            r "But first… we should probably find a way to stay dry, huh?" nointeract
            n "Before I can say anything, [ch_ren] removes his hand, fixes my bottoms, and gives me one final, lingering kiss before pulling away fully." nointeract
        "{image=14NWY symbol} Don't do anything":
            n "I watch as Ren looks over his shoulder and scans the area around him." nointeract
    $ choice_style = "default"
    $ rem_yippee = True
    return
label DLC_day3_kitchen:
    n "Quietly sneaking up behind [ch_ren], I wait until he's occupied with his phone once more before I reach for his shirt and slide my hands underneath the soft material." nointeract
    show ren blushing at bpop
    n "He {b}immediately{/b} lets out a sharp breath from the sudden surprise, but… doesn't seem to stop me. Instead, [ch_ren] sets his phone down on the counter and subconsciously leans into my touch." nointeract
    n "A shaky sigh soon follows, and I feel the outlines and grooves of his muscles tense up whenever my fingers brush across them." nointeract
    n "My hands casually roam against his skin — cold at first, though not as cold as his hands — before they wrap around his torso and soak in the warmth it emits." nointeract
    n "Seeing just how far [ch_ren] would let me take this, I glide my fingers upwards across the large expanse of his chest and over his erratic heartbeat… and the next thing I know, they stumble upon something cool, round, and metallic." nointeract
    n "No way— Were those… Did [ch_ren] have…" nointeract
    show ren flushed at bpop
    r "A-Ahem!" nointeract
    n "With bright red cheeks, [ch_ren] reaches for both my wrists and gently pulls my hands from underneath his shirt. Barely a second passes before he turns to me with a flushed smile, and places a few kisses on each of my knuckles." nointeract
    show ren blushing at spop
    r "I-I— Um! I wasn't expecting you to do that so early in the morning." nointeract
    show ren flushed at spop
    r "But— Well… A-Anyway!" nointeract
    return
label DLC_day3_olivia:
    show olivia angry at spop
    o "W-What? You're lying!" nointeract with vpunch
    show olivia frown at spop
    o "There's absolutely {i}no way{/i} someone like him would ever—" nointeract
    show olivia sad at spop
    o "Unless {i}you're{/i} the one who we used to— But you can't be…" nointeract
    y "Sounds like someone is jealous." nointeract
    n "After the way [ch_olivia] carelessly treated me and my feelings the other day, I can't help but let that line slip. Oops." nointeract
    show olivia flushed at bpop
    o "Why would I be jealous?!" nointeract with vpunch
    show olivia frown at bpop
    o "I already have {i}the{/i} Teo Alvarado and an indie-rock drummer wrapped around my finger, what's there for me to be jealous about?" nointeract
    show olivia angry at spop
    o "Well, whatever!" nointeract
    return
label DLC_day3_inviteren:
    show ren blushing at bpop
    r "H-Huh?!" nointeract with vpunch
    n "Almost immediately, [ch_ren] turns his back to me — whether it's out of privacy or embarrassment — and looks down at his pants." nointeract
    n "Amused at how quickly he fell for my bluff, I kick my feet up onto the couch and watch his reactions with a smile on my face." nointeract
    n "He lifts his outer cardigan up a few times — almost as if he wants to be absolutely certain — before he stands up with a huff and repeats the process all over again." nointeract
    n "But when [ch_ren]'s search ends up fruitless, he turns to me with a faux look of betrayal in his eyes." nointeract
    show ren sad at spop
    r "Wait… I-It's not…" nointeract
    play audio "audio/sfx/item.ogg"
    n "He plops himself back onto the couch, crosses his arms, and offers me nothing more than a pout." nointeract
    y "Relaaaax. I just wanted to tease you a little bit." nointeract
    y "You know, you're {i}especially{/i} cute with those blushy cheeks and pouting expression of yours." nointeract
    y "And it's… honestly kind of amusing watching you get riled up over something so small." nointeract
    show ren flushed at spop
    r "…" nointeract
    show ren blushing at spop
    r "Blushy cheeks? …P-Pouting expression?" nointeract
    show ren flushed at spop
    r "…" nointeract
    show ren smirk at spop
    r "Hm. Just wait til I get {i}you{/i} riled up." nointeract
    play audio "audio/sfx/item.ogg"
    show ren smirk z at spop
    n "The next thing I know, [ch_ren] places one of his large hands on the back of the couch for support and leans over me. Because of the close proximity, I can feel the heat radiating from his body and the faint puffs of air that leave his lips." nointeract
    n "His fingers cup my chin as he gently guides my face to look up at him. There's a smug look plastered all over his features, and when he starts to lean even closer, I'm quick to follow." nointeract
    n "But just before our lips could touch, [ch_ren]'s pulling away and reaching for his fork." nointeract
    play audio "audio/sfx/item.ogg"
    show ren neutral at spop
    r "You're not hungry?" nointeract
    y "…Wh-What?" nointeract
    show ren sad at spop
    r "The food. You don't want to eat?" nointeract
    n "Why did he pull away?!" nointeract
    n "As if sensing my bewilderment, [ch_ren] looks back at me with that same smug look from before." nointeract
    show ren smirk at spop
    r "What? Y'can dish it but y'can't take it? Heh…" nointeract
    show ren happy at spop
    r "Y'know, I think you're just as cute with that flushed expression of yours." nointeract
    show ren smirk at spop
    r "Maybe I'll try and see just how much {i}more{/i} flushed and breathless I can make you later. Seeing you pressed against the couch like that has given me a few ideas…" nointeract
    n "At that, [ch_ren] seems to move the conversation along as if nothing happened." nointeract
    return
label DLC_day4_teo:
    if relationship_teo == "fling" and rem_boyfriend == False:
        n "But before I can fumble around in the dark to check, I feel a pair of large hands snake around my waist and pull me into its owner's chest." nointeract
        y "What the {i}fuck{/i} are you doing?" nointeract
        t "What does it look like?" nointeract
        y "I thought you said we weren't going to do anything!" nointeract
        t "We're not. I'm just making sure you're not standing in any fish slime." nointeract
        y "…What? I doubt that's a real thing. And even if it is, why would it be in a {i}closet{/i} of all places— Wait! That's not the point!" nointeract
        y "I know what you're trying to do, Teodore." nointeract
        t "Damn. Not the full name." nointeract
        n "Regardless of my stern tone, Teo continues to press his thumbs into the fabric of my shirt and casually squeeze my sides." nointeract
        t "I've missed hearing you say it." nointeract
        t "Can't forget the way you looked underneath me, either. So desperate and needy for my attention… Moaning out my name like it was going to earn you some kind of reward…" nointeract
        t "Wanna take a walk down memory lane?" nointeract
        y "{i}Teo.{/i} I swear—" nointeract
        t "Aw, you mad, Dollface?" nointeract
        $ choice_style = "box"
        menu:
            "{image=14NWY symbol alt} \"Fine. But only if you help me out.\"":
                t "Need a {i}hand{/i}, do you? Cute." nointeract
                t "Unfortunately for you, I'm not feeling all that generous today, Doll. Especially after experiencing that bratty attitude of yours." nointeract
                n "At that, Teo nudges one of his legs between my thighs and presses upwards. The feeling alone has me taking in a sharp intake of air — and threading my fingers in the material of his shirt with a soft moan." nointeract
                t "If you want more than this, then you're gonna have to beg me." nointeract
                t "Make sure to say my name real sweetly, too." nointeract
                n "Even within the darkness of the closet, I hope Teo can see the venomous scowl I'm sending him." nointeract
                n "But it doesn't last long, because soon he's guiding my hips into a slow rocking motion and sending waves of pleasure through my body." nointeract
                n "Teo's voice comes out low and sultry, and I can feel him press his lips against the shell of my ear before he bites down." nointeract
                t "C'mon, try it. Say {i}'Please, [ch_teo]. Please make me feel good'{/i}, just the way I like it." nointeract
                if nsfw_position == "top" and genitalia == "bussy":
                    t "The way you {i}always{/i} do whenever you're desperate to put your dick inside me." nointeract
                elif nsfw_position == "bottom":
                    t "The way you {i}always{/i} do whenever you're aching to be filled with my cock." nointeract
                else:
                    t "The way you {i}always{/i} do whenever you're hungry for my cock." nointeract
                y "N-Not a chance." nointeract
                t "…You sure?" nointeract
                n "Just as Teo says that, he abruptly pulls away from me with a mocking snicker. All of a sudden, the closet is far too cold and spacious again, and I find myself all alone." nointeract
                y "You asshole—" nointeract
                n "As I take a step back to gather my bearings, I almost end up slipping on something wet." nointeract
                n "What the…?" nointeract
            "{image=14NWY symbol} \"Fuck off, Teo.\"":
                t "Ouch." nointeract
                n "Even in the dark, I don't need to see Teo's expression to know that he's smirking right now; I can practically hear the smug drawl in his voice." nointeract
                n "But my message seems to be clear, as he immediately removes his hands from my body and takes a step back. When I do the same, I almost end up slipping on something wet." nointeract
                n "What the…?" nointeract
        $ choice_style = "default"
        return
    else:
        return
label DLC_day4_ren:
    y "You always seem to be on my mind. When I'm with my friends, when I'm at work, when I'm dreaming…" nointeract
    y "Even late at night, when I'm feeling a little pent up and lonely…" nointeract
    n "I hope [ch_ren] doesn't notice the way my cheeks grow warm as I confess my deepest, darkest secrets with him." nointeract
    y "{i}You{/i} are all I think about during those times." nointeract
    show ren blushing z at spop
    r "…" nointeract
    show ren flushed z at bpop
    r "M-M-Me too! You're all I think about, too!" nointeract
    show ren blushing z at spop
    r "Sometimes… I can't help it. I could be reading a book or watching anime, and all I'll see is you." nointeract
    show ren flushed z at spop
    r "Then the next thing I know, my mind starts to wander, and here I am thinking about all kinds of indecent… {i}things{/i}." nointeract
    if rem_wahoo == True:
        show ren blushing z at spop
        if nsfw_position == "top":
            r "Like… The way you'd look above me while I'm going down on you in the shower… O-Or pressing me against a library shelf while you have your way with me…" nointeract
        elif nsfw_position == "bottom":
            r "Like… The way you'd look on your knees for me while we're in the shower… O-Or pressed against a library shelf with your head thrown back…" nointeract
        else:
            r "Like… The way you'd look on your knees for me while we're in the shower… O-Or pressing me against a library shelf while you have your way with me…" nointeract
        show ren lovesick z at spop
        r "Haa…" nointeract
        show ren blushing z at spop
        r "S-Sometimes I wish you were near so I wouldn't have to use my hand all the time. It doesn't feel the same, and—" nointeract
        show ren flushed z at spop
        r "{size=-6}The thought of you touching my— {i}Ugh.{/i}{/size}" nointeract
        n "[ch_ren] cuts himself off by pressing his forehead against my shoulder." nointeract
        show ren angry z at spop
        r "But just as things start to get good, something {i}always{/i} seems to get in the way and ruin it all. And right now, it's that green-haired loser…" nointeract
    else:
        show ren angry z at spop
        r "But just as things start to get good, something {i}always{/i} seems to get in the way and ruin it all. And right now, it's that green-haired loser…" nointeract
    return
label DLC_day4_renapartment:
    play audio "audio/sfx/item.ogg"
    show ren flushed z at bpop
    n "Without thinking, I make my way towards [ch_ren] and pull him into a deep kiss." nointeract
    n "His calloused hands move to my face as one of his thumbs gently caresses my cheek, and I soon find myself melting from all his affection." nointeract
    scene other_dark
    show peffectp
    with GlitchDissolve
    n "Before I know what's happening, I feel the welcome intrusion of [ch_ren]'s tongue against my lips, and I eagerly close my eyes and give him access." nointeract
    n "Without breaking the kiss, I feel him gently usher me backwards — until my back hits the counter and I'm boxed in by his arms on either side." nointeract
    n "[ch_ren]'s hands soon move towards my waist and underneath my shirt, but just as he starts to trail them upwards at an agonisingly slow pace, he pulls back with a knowing look on his features." nointeract
    n "When I fully snap out of my daze, I notice that [ch_ren] had already moved back to his previous spot by the sink, but his eyes are still lingering on my body." nointeract
    scene ren_kitchen_day
    show peffect
    show ren smirk at center
    with GlitchDissolve
    r "Don't get me wrong, I love how forward you are, [ch_angel]. But you don't typically do… {i}this{/i} kind of stuff without a reason." nointeract
    n "Damn. He saw right through me." nointeract
    n "Ah, forget it; maybe it was some form of righteousness, but I find myself confessing the truth." nointeract
    return
label DLC_day4_angelapartment:
    n "Raising a brow in [ch_ren]'s direction, I give him a look." nointeract
    menu:
        "{image=14NWY symbol} \"Is there something on my face?\"":
            show ren flushed at bpop
            r "Hm? O-Oh! Uhh… Yes! Here, want me to get it off?" nointeract
            play audio "audio/sfx/item.ogg"
            show ren flushed z at spop
            n "Nodding, I lean closer so that [ch_ren] can remove whatever it is on my face." nointeract
            n "Almost hesitantly, he reaches out and hovers just above my left cheek. But… He doesn't seem to move until I do first — almost as if he's afraid that touching me would scare me off." nointeract
            n "Once I lean into his touch to let him know that it's okay to do so, [ch_ren]'s thumb carefully brushes against my skin in a soothing pattern. But all too quickly, his ghost-like touch turns into him cupping my face entirely." nointeract
            n "His thumb soon drops to my lips, and I feel him gently part them as his breathing starts to pick up." nointeract
            show ren lovesick z
            n "[ch_ren] is staring intently at my mouth now — almost like he's in a trance — and it's {b}then{/b} that I finally understand what's happening." nointeract
            y "There's… nothing on my face, is there?" nointeract
            show ren blushing z at spop
            r "…Huh?" nointeract
            show ren flushed z at bpop
            r "No, I-I mean—! I think I got it, actually! Yep! All gone! Ahahah!" nointeract
            play audio "audio/sfx/item.ogg"
            show ren flushed at spop
            n "He awkwardly pulls away and immediately busies himself with the cameras set out on the table." nointeract
            n "With a knowing look, I leave him be… For now." nointeract
            n "A comfortable silence soon follows, but it's short-lived the moment he clears his throat and speaks once more." nointeract
            show ren sad at spop
            r "Actually… Now that I'm thinking about it…" nointeract
            return
        "{image=14NWY symbol} \"Want to tinker with… something else?\"":
            show ren blushing at bpop
            n "Subtly, I part my thighs ever-so-slightly to get my intentions across." nointeract
            n "In all honesty, I didn't think [ch_ren] would understand my meaning, but with the way he straightens up and casts a sideward glance in my direction, something tells me he knew what I meant." nointeract
            show ren flushed at spop
            r "…" nointeract
            show ren smirk at spop
            r "Don't tempt me." nointeract
            n "He runs a hand up my leg and across my upper thigh — so close to where I'm aching to be touched — before he gives my skin a soft squeeze and pulls away." nointeract
            show ren neutral at spop
            r "I'd rather you be safe from intruders {i}first{/i} before we take things any further." nointeract
            show ren smirk at spop
            r "Besides… Maybe we can test if the cameras work by filming some… {i}stuff{/i}, later." nointeract
            show ren neutral at spop
            r "We gotta make sure it's covering all angles of your apartment 'n all. Wouldn't want a single hiding spot t'go unseen." nointeract
            show ren smirk at spop
            r "…Or flat surface." nointeract
            n "Wait. Did he just suggest—" nointeract
            show ren happy at spop
            r "Just kidding!" nointeract
            n "At that, [ch_ren] goes back to the task at hand as if nothing just happened." nointeract
            n "A comfortable silence soon follows, but it's short-lived the moment he clears his throat and speaks once more." nointeract
            show ren sad at spop
            r "Actually… Now that I'm thinking about it…" nointeract
            return
        "{image=14NWY symbol} Crawl into his lap":
            n "Without wasting another second, I crawl across the couch, situate myself between [ch_ren]'s thighs, and casually rest my arms over his shoulders." nointeract
            play audio "audio/sfx/item.ogg"
            show ren blushing z at bpop
            r "U-Um! Hi…" nointeract
            y "Keep doing what you're doing. Don't mind me." nointeract
            show ren flushed z at spop
            r "I-It's kinda hard {i}not to{/i} when you're sitting on my… Uhh… Y'know—" nointeract
            y "Oh, is {i}that{/i} what that is? I see. I thought you were just hiding a remote in your pocket, or something." nointeract
            show ren blushing z at bpop
            r "Wh-Why would I possibly be hiding a—?!" nointeract
            show ren flushed z at spop
            r "Who does that…? {i}Why{/i} would someone do that? N-Nevermind…" nointeract
            play audio "audio/sfx/item.ogg"
            show ren blushing at spop
            n "Deciding to give [ch_ren] {i}a bit{/i} of breathing room, I lean back so I'm not {b}entirely{/b} all up in his business." nointeract
            n "I'm still nestled — rather smugly — in his lap, though, and he's able to easily reach around me to continue working on setting up the security cameras." nointeract
            n "A comfortable silence soon follows, but it's short-lived the moment [ch_ren] clears his throat and speaks once more." nointeract
            return
        "{image=14NWY symbol} Don't do anything":
            n "He seems to pick up on my confusion and further explains his intentions." nointeract
            return
label DLC_day5_bed:
    show mothphone flushed at bpop
    m "{size=+10}HELLO?!{/size}" nointeract with hpunch
    show mothphone happy at spop
    m "And he looks just like Haruko, too?!" nointeract
    show mothphone blushing at spop
    m "Wait… Is he actually…" nointeract
    y "Submissive and breedable?" nointeract
    show mothphone smirk at spop
    m "I was going to say {i}'Haruko'{/i}, but now I've got to know." nointeract
    show ren sad at spop
    r "Am I… wh-what?" nointeract
    show ren flushed at spop
    r "Well… I-I guess I am, but biologically speaking, I don't think I'm able to be bred—" nointeract
    show mothphone flushed at spop
    m "Not with that attitude. Or is [ch_angel] not trying hard enough?" nointeract
    y "[ch_moth]!" nointeract
    return
label DLC_day5_stall:
    $ choice_style = "default"
    menu:
        "{image=14NWY symbol} \"Maybe you should…\"":
            show ren blushing z at bpop
            n "At that, [ch_ren]'s cheeks practically glow bright red." nointeract
            show ren flushed z at spop
            r "B-But you're already changed…" nointeract
            y "Why do you sound so disappointed, you pervert?" nointeract
            show ren blushing z at bpop
            r "{size=+10}…!{/size}" nointeract with vpunch
            show ren flushed z at bpop
            r "N-N-N-NO! No, I didn't— I wasn't— I just meant…" nointeract
            show ren blushing z at bpop
            r "{size=-6}Ughhh… What I would give to have the ground swallow me up right now.{/size}" nointeract
            show ren flushed z at spop
            r "I-I take back what I said. I didn't mean to—" nointeract
            y "Relax, [ch_ren]. I'm only teasing you." nointeract
            show ren blushing z at spop
            r "…Oh. Ahah~" nointeract
            show ren flushed z at spop
            r "…" nointeract
            show ren blushing z at spop
            r "But if you {i}wanted{/i} to get undressed, I wouldn't m—" nointeract
        "{image=14NWY symbol} \"Can I watch you get changed instead?\"":
            play audio "audio/sfx/item.ogg"
            play audio "audio/sfx/shoes alt.ogg"
            show ren flushed at bpop
            n "Almost immediately, [ch_ren]'s head snaps up and he almost drops his bag. He nearly slams himself into the wall behind him as well, but manages to catch his footing just in time." nointeract
            show ren blushing at bpop
            r "Y-Y-Y-Y-You want to—?! I mean— But that's—!" nointeract
            y "Is that a no?" nointeract
            show ren flushed at spop
            r "I don't mind, but… Well, you see, no one's really seen me without a shirt on before, and… And—" nointeract
            n "I can practically see the steam rising from [ch_ren]'s head as he tries to come up with something to say. Taking pity on him, I decide to put him out of his misery." nointeract
            y "Hey, it's okay. I'm only teasing." nointeract
            show ren blushing at spop
            r "…Oh. Ahah~" nointeract
            show ren flushed at spop
            r "…" nointeract
            show ren blushing at spop
            r "Y'know, I was going to suggest watching me take my pants off instead, but…" nointeract
            y "Wait. Are you serious—" nointeract
        "{image=14NWY symbol} \"Are you blushing again?\"":
            show ren blushing z at bpop
            r "…!" nointeract
            show ren flushed z at spop
            r "N-N-No! …Maybe?" nointeract
            y "I'll be the judge of that." nointeract
            n "Stumbling my way through the dimly lit area, I reach out towards [ch_ren] and cup his face with my hands. His own immediately reach for my wrists — not to pull them away — but to hold onto." nointeract
            y "Yeah, they're warm, alright. That's about a nine on the [ch_ren]-blush-o-meter." nointeract
            show ren blushing z at spop
            r "You have a scale for that?" nointeract
            y "Mhm! Exclusive to you." nointeract
            show ren smirk z at spop
            r "So… No one else has a scale? Just me?" nointeract
            y "Yes?" nointeract
            show ren happy z at spop
            r "…" nointeract
            show ren smirk z at spop
            r "Hey, d'you think you could touch me a little lower—" nointeract
        "{image=14NWY symbol} \"Alright then. Thank you, [ch_ren].\"":
            show ren neutral z at spop
            r "Mm! Of course!" nointeract
            show ren happy z at spop
            r "If you want, I can—" nointeract
    $ choice_style = "box"
    return
label DLC_day5_kitchen:
    n "I don't know what compels me to do this, but I reach for [ch_ren]'s belt and pull him closer to me." nointeract
    n "He doesn't seem to mind at all — in fact, it's as though all his sadness washes away the moment I reach for him, and instead gets replaced with something more tender." nointeract
    show ren neutral z at spop
    r "…Angel?" nointeract
    show ren smirk z at spop
    r "You know your friend is standing nearby, right?" nointeract
    show ren neutral z at spop
    r "And they're looking at you like you've just done something crazy." nointeract
    y "I {i}did{/i} just reach for your crotch area…" nointeract
    n "[ch_ren] only seems to let out an amused laugh at my words before leaning closer." nointeract
    show ren smirk z at spop
    r "You're so insatiable. I s'pose it's a good thing that I'm into it, huh?" nointeract
    return
label dlc_14nwy_d1_t1:
    n "Hearing him swear sends a wave of pleasure through my body." nointeract
    n "And as if [ch_ren] could sense my neediness, I feel him reach below to experimentally play with my [parts]." nointeract
    n "He gently runs his fingers across before he applies more pressure. My breath hitches in my throat as I throw my head back, once again arching into his addictive touch." nointeract
    return
label dlc_14nwy_d1_t2:
    n "I don't miss the small bottle of lube in one of [ch_ren]'s hands once he returns — no doubt something he fished from his pockets — but it soon becomes an afterthought the moment he leans closer and gives me a slow kiss." nointeract
    n "While he busies himself with opening the lid and smearing some of the liquid onto his fingers, I take it upon myself to make {b}him{/b} feel good as well." nointeract
    return
label dlc_14nwy_d1_t3:
    r "…Just like that. Use me to pleasure yourself." nointeract
    return
label dlc_14nwy_d1_t4:
    n "He quickens his pace, and suddenly, my vision goes white. My toes curl as [ch_ren] continues to tease my [parts] and [sex], and I come with his name on my tongue." nointeract
    return
label dlc_14nwy_d1_t5:
    n "But during my hazed-out state, I came to the realisation that [ch_ren] was {b}still{/b} hard — if his \"subtle\" grinding against my side had anything to do with it. So I nudge his thighs apart and beckon him closer." nointeract
    return
label dlc_14nwy_d1_t6:
    n "Apparently, that was all it took to have him back on me once more, with his hungry mouth on mine as his hand moves to line up my [length] with his lubed hole." nointeract
    return
label dlc_14nwy_d1_t7:
    n "Considering how [ch_ren] has apparently never done something like this before, he decides to take things nice and slow." nointeract
    n "I watch in awe as he tries to take every inch inside of his tight hole with a blissed out look on his face." nointeract
    if length == "strap-on":
        n "I almost forget to breathe as the base of my strap-on deliciously rubs against one spot in particular, and I unconsciously latch onto his thighs to anchor myself." nointeract
        r "A-Ah… I haven't taken anything as big as this before…" nointeract
    else:
        n "I almost forget to breathe as I feel his walls clench around my [length], and I unconsciously latch onto his thighs to anchor myself." nointeract
        r "A-Ah… I haven't taken anything as big as you before…" nointeract
    n "What felt like hours seemed to pass before [ch_ren] {b}finally{/b} bottoms out on my [length], and he almost seems to double over once more from the sheer pleasure of it all." nointeract
    n "He looks down at me once more with those soft blue eyes of his, and the entire exchange suddenly feels {b}far more{/b} intimate than actually having me inside of him." nointeract
    n "[ch_ren]'s hand moves to tenderly cup my cheek, before he bends down to give me a chaste kiss on the forehead." nointeract
    return
label dlc_14nwy_d1_t8:
    r "Hah— Look~ You're finally inside me… You feel {i}amazing{/i}, Angel." nointeract
    return
label dlc_14nwy_d1_t9:
    n "Despite [ch_ren]'s tender words, the sudden movement of his hips takes me off guard as he starts to ride my length." nointeract
    n "But my pleasure isn't far from his thoughts, it seems, as he's quick to reach down and play with my [parts], which sends a wave of excitement throughout my entire body." nointeract
    r "Y-You're making such a {i}mess{/i} out of me…" nointeract
    return
label dlc_14nwy_d1_t10:
    n "[ch_ren] doesn't lift his hips yet, instead choosing to look down at me with soft eyes as he adjusts to having something inside him for the first time." nointeract
    r "I-Is it uncomfortable? Let me know if anything hurts, okay? Just say the word, and we can stop." nointeract
    n "His sincerity touches me as he tries to remain still atop of me, but I can tell from his rough expression that he's trying to hold himself back." nointeract
    n "[ch_ren] seems to be in the {b}slightest{/b} bit of pain — judging by the sweat that forms near his brows — so I reassure him by running my hands along his thighs and pulling him closer." nointeract
    n "At that, [ch_ren] seemingly finds enough confidence to move." nointeract
    n "But my pleasure isn't far from his thoughts, it seems, as he's quick to reach down and play with my [parts] — which sends a wave of excitement throughout my entire body." nointeract
    n "His tentative pace soon changes as he experimentally grinds himself on my [length], and the hand that brushed against my skin soon comes to interlock with one of my own." nointeract
    return
label dlc_14nwy_d1_t11:
    r "Look at you, laying there with such a lewd expression on your face. {i}Fuck.{/i} You're making me feel so good right now…!" nointeract
    return
label dlc_14nwy_d1_t12:
    n "His expression does little to stifle the sensation slowly building between my legs, and I unconsciously thrust my hips upwards. [ch_ren] lets out another shaky moan before he effortlessly reaches for my [parts] to stimulate me further." nointeract
    n "The sensation has me seeing stars, and sends my eyes rolling into the back of my head." nointeract
    return
label dlc_14nwy_d1_t13:
    n "My praise only seems to spur him on as his hand {b}and{/b} hips start to move more fervently, and [ch_ren] practically starts to lose himself to the pleasure." nointeract
    return
label dlc_14nwy_d1_t14:
    if genitalia == "bussy":
        n "Hearing him cry out my name with such {b}neediness{/b} is what finally sends me over the edge once more, and I come inside [ch_ren] with his own name on my lips." nointeract
    else:
        n "Hearing him cry out my name with such {b}neediness{/b} is what finally sends me over the edge once more, and I come undone with [ch_ren]'s own name on my lips." nointeract
    n "[ch_ren] isn't far off, it seems, as it only takes him a few more seconds of shamelessly riding my [length] before he reaches his peak." nointeract
    n "One of his hands grip my bedsheets in a crushing hold as he cries out my own name as well." nointeract
    return
label dlc_14nwy_d3_t1:
    r "I-I already applied some lube earlier, but if you need me to, I can—" nointeract
    r "That is— U-Um…" nointeract
    r "Do you want me to suck you off before I— Before {i}we{/i}—" nointeract
    n "[ch_ren] can't seem to concentrate with the way his words come out slurred and needy, so I decide to put him out of his misery by reaching for my [length] instead and lining it up with his hole." nointeract
    n "He immediately catches on — lifting his hips and spreading his thighs further. I almost miss the warmth of his body on mine, but the sudden sensation of [ch_ren] hovering over my tip draws my attention away." nointeract
    if length == "strap-on":
        n "With slow, deliberate movements, [ch_ren] gently lowers himself, and I can barely hold back the sounds of my voice as the base of my [length] rubs against my sex." nointeract
    else:
        n "With slow, deliberate movements, [ch_ren] gently lowers himself, and I can barely hold back the sounds of my voice as his walls squeeze around [length]." nointeract
    return
label dlc_14nwy_d3_t2:
    if nsfw_position == "top" or nsfw_position == "temp_top":
        r "Missed this… Missed having you inside me…" nointeract
    else:
        r "Missed this… Missed doing this with you…" nointeract
    return
label dlc_14nwy_d3_t3:
    if length == "strap-on":
        n "The pleasurable feeling coming from the inner side of my [length] practically steals the air from my lungs, and I can't help but lift my hips off of the couch and buck into [ch_ren] for even {b}more{/b} friction." nointeract
    else:
        n "The pleasurable feeling of his walls squeezing around my [length] practically steals the air from my lungs, and I can't help but lift my hips off of the couch and buck into [ch_ren]." nointeract
    return
label dlc_14nwy_d3_t4:
    r "…You haven't done this with anyone else since last time, right? Only me?" nointeract
    r "Doesn't really matter anyway. Gonna make sure {i}I'm{/i} the only one y'wanna fuck from now on." nointeract
    return
label dlc_14nwy_d3_t5:
    r "Doesn't really matter anyway. Gonna make sure {i}I'm{/i} the only one y'wanna fuck from now on." nointeract
    return
label dlc_14nwy_d3_t6:
    n "The next thing I know, [ch_ren]'s hungry mouth and body are on mine once more as he reaches down to play with my [parts]." nointeract
    return
label dlc_14nwy_d3_t7:
    n "Leaving another hickey, no doubt — and had I not been fucking [ch_ren] within an inch of his life — I would've fully noticed the possessive undertones of his actions." nointeract
    return
label dlc_14nwy_d3_t8:
    n "Before I can respond, [ch_ren] {b}fully{/b} sheaths my [length] inside of his tight hole and starts to grind his hips. But just as he lets out a moan from the friction, he starts to move once more." nointeract
    n "[ch_ren] sets a brutal pace now, and all I could do was latch onto the throw pillows above my head and let him ride me to completion." nointeract
    r "No one else could ever compare to you…" nointeract
    r "Y'feel so good too, filling me up 'n leaving me full." nointeract
    n "[ch_ren] spreads his thighs even more before he returns his attention back towards my [bust], which has me seeing stars." nointeract
    n "I can feel his hole squeeze around my [length], and once my tip hits that particular spot inside of him, [ch_ren] can't help but cry out and reach for my [parts] once more." nointeract
    return
label dlc_14nwy_d3_t9:
    n "[ch_ren]'s voice does little to hide his desire and hunger for me, and he makes it known by bouncing on my [length] with reckless abandon." nointeract
    return
label dlc_14nwy_d3_t10:
    r "Nobody else will make you feel as good as me." nointeract
    if length == "strap-on":
        r "And there's nobody else who can take you as well as I can." nointeract
        r "Though it's not like they'll even get the chance to try." nointeract
    else:
        r "Try as much as you want, but it's {i}my{/i} hole that your [length] will crave." nointeract
        r "Nobody else can take you as well as I can. They won't even get the chance to try." nointeract
    return
label dlc_14nwy_d3_t11:
    if genitalia == "cooter":
        n "The pleasure is almost too much to bear, and I throw my head back in ecstatic bliss. And [ch_ren] — ever attentive to my needs — continues to rubs circles against my clit instead." nointeract
    elif genitalia == "bussy":
        n "His length is going deeper than ever now, and I throw my head back in ecstatic bliss. And [ch_ren] — ever attentive to my needs — moves one of his hands from my [bust] to stroke my weeping cock instead." nointeract
    else:
        n "His length is going deeper than ever now, and I throw my head back in ecstatic bliss. And [ch_ren] — ever attentive to my needs — moves one of his hands from my [bust] to stimulate my sex instead." nointeract
    return
label dlc_14nwy_d3_t12:
    if length == "cock":
        r "That's it. Give it to me. Be good f'me and come inside my ass." nointeract
    else:
        r "That's it. Give it to me. Be good f'me and come as hard as you can." nointeract
    r "C'mon, [ch_angel]. Show me who I belong to, who makes you feel this good." nointeract
    return
label dlc_14nwy_d3_t13:
    n "Something rough and textured brushes against my fingertips, but I pay it no mind as as I feel [ch_ren]'s teeth on my shoulder and come." nointeract
    n "[ch_ren] seems to have other plans, though, as his hips start to stutter — and before I know it, his strained voice is whimpering into my neck once more as he spills himself on both our stomachs." nointeract
    return
label dlc_14nwy_d3_t14:
    if length == "cock":
        n "He doesn't seem to remove himself from my [length] though — and much like last time — I remain balls deep inside him as we both melt into the couch." nointeract
    else:
        n "He doesn't seem to detach himself from me though — and much like last time — we both remain as close as possible while [ch_ren] pulls me closer into the couch." nointeract
    return
label dlc_14nwy_d3_t15:
    if length == "cock":
        n "He doesn't seem to remove himself from my [length] though, and I remain balls deep inside him as we both melt into the couch." nointeract
    else:
        n "He doesn't seem to remove himself from my [length] though, so we both remain as close as possible while [ch_ren] pulls me closer into the couch." nointeract
    return
label dlc_14nwy_d5_t1:
    $ jump_one = "day5_wahooscene"
    $ jump_two = "day5_renevening"
    call screen warningnsfw with dissolve
return