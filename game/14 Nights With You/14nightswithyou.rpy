init python:

    persistent.dlc_14nightswithyou = True
    persistent.dlc_14nightswithyou_type = "paid"

default persistent.cg_d1_nsfw1 = False
default persistent.cg_d1_nsfw2 = False
default persistent.cg_d1_nsfw3 = False
default body_type = "ambiguous"
default genitalia = "gnooch"
default bust = "bust"
default sex = "sex"
default parts = "heat"
default hole = "hole"
default length = "length"
default nsfw_position = "bottom"
default first_time = False
default first_penetrated = True
default first_penetrating = True
default first_giving = True
default first_receiving = True
default temp_bottom = False
default first_ren_penetrated = True
default first_ren_penetrating = True
default first_ren_giving = True
default first_ren_receiving = True
label DLC_14NWY:
    if genitalia == "cooter":
        $ sex = "pussy"
        $ parts = "clit"
        $ hole = "cunt"
        $ length = "strap-on"
    if genitalia == "bussy":
        $ sex = "dick"
        $ parts = "balls"
        $ hole = "ass"
        $ length = "cock"
    if genitalia == "gnooch":
        pass
    jump cont
image CG D1_NSFW1 = Composite(
    (1920, 1080),
    (0, 0), "14 Nights With You/images/d1 nsfw/background.webp",
    (0, 0), "peffectp",
    (0, 0), "14 Nights With You/images/d1 nsfw/ren hair [ren_hair].webp",
    (0, 0), "14 Nights With You/images/d1 nsfw/brows 1.webp",
    (0, 0), "d1 nsfw blink1",
    (0, 0), "14 Nights With You/images/d1 nsfw/mouth 1.webp",
    (0, 0), Transform("14 Nights With You/images/d1 nsfw/filter.webp", alpha=0.9),
    (0, 0), "14 Nights With You/images/d1 nsfw/sparkle.webp",
    )
image CG D1_NSFW2 = Composite(
    (1920, 1080),
    (0, 0), "14 Nights With You/images/d1 nsfw/background.webp",
    (0, 0), "peffectp",
    (0, 0), "14 Nights With You/images/d1 nsfw/ren hair [ren_hair].webp",
    (0, 0), "14 Nights With You/images/d1 nsfw/brows 2.webp",
    (0, 0), "14 Nights With You/images/d1 nsfw/blush.webp",
    (0, 0), "d1 nsfw blink2",
    (0, 0), "14 Nights With You/images/d1 nsfw/mouth 2.webp",
    (0, 0), Transform("14 Nights With You/images/d1 nsfw/filter.webp", alpha=0.9),
    (0, 0), "14 Nights With You/images/d1 nsfw/sparkle.webp",
    )
image CG D1_NSFW3 = Composite(
    (1920, 1080),
    (0, 0), "14 Nights With You/images/d1 nsfw/background.webp",
    (0, 0), "peffectp",
    (0, 0), "14 Nights With You/images/d1 nsfw/ren hair [ren_hair].webp",
    (0, 0), "14 Nights With You/images/d1 nsfw/brows 3.webp",
    (0, 0), "14 Nights With You/images/d1 nsfw/blush.webp",
    (0, 0), "14 Nights With You/images/d1 nsfw/sweat.webp",
    (0, 0), "d1 nsfw blink3",
    (0, 0), "14 Nights With You/images/d1 nsfw/mouth 3.webp",
    (0, 0), Transform("14 Nights With You/images/d1 nsfw/filter.webp", alpha=0.9),
    (0, 0), "14 Nights With You/images/d1 nsfw/sparkle.webp",
    )
image d1 nsfw blink1:
    "14 Nights With You/images/d1 nsfw/eyes 1.webp"
    choice 1.0:
        1.5
    choice 1.0:
        4.5
    choice 1.0:
        2.5
    "14 Nights With You/images/d1 nsfw/eyes 0.webp"
    .05
    repeat
image d1 nsfw blink2:
    "14 Nights With You/images/d1 nsfw/eyes 2.webp"
    choice 1.0:
        1.5
    choice 1.0:
        4.5
    choice 1.0:
        2.5
    "14 Nights With You/images/d1 nsfw/eyes 0.webp"
    .05
    repeat
image d1 nsfw blink3:
    "14 Nights With You/images/d1 nsfw/eyes 3.webp"
    choice 1.0:
        1.5
    choice 1.0:
        4.5
    choice 1.0:
        2.5
    "14 Nights With You/images/d1 nsfw/eyes 0.webp"
    .05
    repeat
label DLC_day2_s1:
    n "But then again, we {b}did{/b} sleep together last night, and I still haven't been able to broach the subject with him yet." nointeract
    return
label DLC_day2_s2:
    show ren angry at bpop, rpos
    r "The fuck's your problem, [asshole]?" nointeract
    n "…That was the second time I'd ever heard [ch_ren] swear. Was he usually this accustomed to cussing?" nointeract
    return
label DLC_day2_s3:
    n "Except friends don't spend the night together and get jealous whenever they flirt with someone else." nointeract
    return
label DLC_day2_s4:
    show ren flushed at spop, center
    r "…Y-You've taken a lot more of my firsts than you've realised." nointeract
    return
label DLC_day2_s5:
    n "And there was also the fact that we'd gotten intimate {b}twice{/b} now. Surely that was saying something about my feelings for [ch_ren]." nointeract
    n "He certainly had boyfriend potential, but I still needed to work up the nerve to make it lead towards that direction." nointeract
    n "It's just… He seemed confident in every other aspect though, which was still a bit confusing to me." nointeract
    n "Ah well, just knowing [ch_ren] wanted to spend the entire day with me is enough." nointeract
    n "Rolling onto my side, I reach for the discarded plushie so I can be surrounded by his comforting scent and slowly drift off to sleep." nointeract
    return
label DLC_day2_s6:
    n "Y'know… Despite the fact that we'd gotten intimate {b}twice{/b} now." nointeract
    n "But still… It was nice to fantasise about. {b}He{/b} was certainly nice to fantasise about." nointeract
    n "Rolling onto my side, I reach for the discarded plushie so I can be surrounded by his comforting scent and slowly drift off to sleep." nointeract
    return
label DLC_day2_s7:
    n "And I wasn't talking about getting to know his {b}body{/b} better." nointeract
    n "But still… It was nice to fantasise about. {b}He{/b} was certainly nice to fantasise about." nointeract
    n "Maybe we could get closer in the future? He'd have to actually {b}try{/b} and put the effort in though — because right now, it felt like I was doing all the work." nointeract
    n "Ah well, there was no point in me stressing over something trivial." nointeract
    n "Rolling onto my side, I reach for the discarded plushie so I can be surrounded by his comforting scent and slowly drift off to sleep." nointeract
    return
label DLC_day2_s8:
    n "But I guess I shouldn't be calling him a creep when {b}I{/b} was the one who invited him into bed to have sex. {b}Twice{/b}." nointeract
    n "There was also that break-in that [ch_violet] mentioned yesterday, but [ch_ren] didn't fit their description at all." nointeract
    n "Ah well. I shouldn't be concerning myself over this. I still had that new lock installed, so I doubt they'd want to come back." nointeract
    n "Rolling onto my side, I push those thoughts aside as I reach for the discarded plushie and slowly drift off to sleep." nointeract
    return
label DLC_day3_s1:
    n "Oh. Right. Last night, [ch_ren] and I…" nointeract
    n "I can feel my whole face flush as I recount what we did together last night. Or rather… What {b}he{/b} did." nointeract
    n "Strange. A part of me thought I was going to wake up with [ch_ren] by my side this morning, given his clingy nature that I'd grown all-to-familiar with." nointeract
    n "But still… His lack of presence had me wondering where he might be right now." nointeract
    n "Did he go back to sleep in his own room? Or perhaps he was already awake?" nointeract
    return
label DLC_day3_s2:
    n "I notice the way [ch_ren]'s eyes darken slightly as he rests his hip against the kitchen island." nointeract
    n "He leans down close enough that I could make out the faint marks and blemishes on his cheeks, yet far away to be just out of my reach." nointeract
    show ren smirk at spop, center
    r "Mm… I'm still full from the \"dessert\" I had last night." nointeract
    y "…H-Huh?!" nointeract with vpunch
    show ren neutral at spop, center
    r "You can't be the only one who's allowed to tease people, Angel." nointeract
    return
label DLC_day4_s1:
    n "Muscle memory kicks in, and my immediate reaction is to open the blinds for some much-needed sunshine — but when I glance at my windows, they were already pulled back." nointeract
    n "…Sunlight had been pouring into my room for who knows how long, and I didn't even notice? And when did I open them?" nointeract
    n "Did [ch_ren] open them? And… Wait. Did he leave?" nointeract
    n "I know firsthand that [ch_ren] likes to wake up early, yet even after straining my ears, I couldn't hear him rattling about in my lounge room." nointeract
    n "Admittedly, I thought [ch_ren] would've wanted to stay the night after we…" nointeract
    n "The heat rushes to my face as I recall what we did last night. No, it wouldn't do me any good to think about that first thing in the morning." nointeract
    n "I could always text [ch_ren] later — after all, it was still early, and I didn't want to seem clingy." nointeract
    n "…Would he even think I'm being clingy?" nointeract
    return
label DLC_day4_s2:
    show teo smirk z at spop
    t "C'mon, like you haven't been fooling around with Buttercup. I can practically smell him on you." nointeract
    return
label DLC_day4_s3:
    y "Yeah… I'm pretty sure I placed it on the shelf when we… Y'know." nointeract
    show ren flushed
    n "[ch_ren] seems to blush at that." nointeract
    return
label DLC_day5_s1:
    show ren blushing at bpop
    r "B-Because I'm all for it, trust me! I really like how insatiable you are, but y-your friend is still—" nointeract
    return
label DLC_day5_s2:
    scene ren_loungeroom_night
    play music "audio/bgm/Warmth.ogg" fadein 1 fadeout 1
    show peffect
    with Fade(1.0, 2.0, 1.0)
    n "When I come to, the first thing I notice is the comforting weight of the blanket still covering me on the couch — alongside [ch_ren]'s familiar presence by my side." nointeract
    n "The soft glow emitting from the TV casts a soft light in the otherwise darkened room, and it's then that I realise that the second episode of AoG is currently playing on the screen." nointeract
    n "Damn, did I really doze off long enough for the series to loop? Weren't there at least forty episodes?" nointeract
    n "With a soft groan, I adjust myself into a more comfortable position to survey the rest of my surroundings — only to realise that my movement must've stirred [ch_ren] awake as well." nointeract
    n "Glancing behind me, I immediately notice his sleepy expression and tidy appearance, which means… He must've taken the time to fix both of our clothes at some point during my slumber." nointeract
    n "An appreciative smile pulls at my features — one that [ch_ren] happily returns with his own — before the sound of a tired, drawn-out yawn breaks the silence and ruins the tender moment." nointeract
    n "Turning back around, it's then that I notice [ch_moth] slowly beginning to drift off from their spot on the floor, if the drool coming from the corner of their mouth was any indication." nointeract
    n "It must be bedtime for {b}all{/b} of us." nointeract
    n "But after everything we'd just done, the last thing I wanted to do was leave the warmth of [ch_ren]'s body, but the thought of a comfy bed with plenty of leg room was calling my name." nointeract
    n "I barely have any time to weigh my options, however, as [ch_ren] immediately picks up on my drowsy demeanour and offers to show us to our rooms so that we can rest." nointeract
    scene other_dark
    show peffect
    with dissolve
    n "Eventually, he leaves [ch_moth] and me to settle in for the night, claiming that he has one last matter to take care of." nointeract
    return
label DLC_day5_s3:
    m "[player_fl] was looking for the bathroom earlier. [they!c] needed a mirror to check out all those fresh hickies on [their] neck." nointeract
    show moth blushing at spop
    m "…I wonder how those got there?" nointeract
    return
label DLC_firsttime_menu:
    if persistent.dlc_14nightswithyou_type == "paid":
        if nsfw_position == "top" or nsfw_position == "temp_top":
            if temp_bottom == True:
                if first_penetrated == True:
                    r "U-Um. Actually… Before we continue…" nointeract
                    call DLC_firsttime_penetrated from _call_DLC_firsttime_penetrated
                else:
                    pass
            elif first_penetrating == True:
                call DLC_firsttime_penetrating from _call_DLC_firsttime_penetrating
            else:
                pass
        elif first_penetrated == True:
            r "U-Um. Actually… Before we continue…" nointeract
            call DLC_firsttime_penetrated from _call_DLC_firsttime_penetrated_1
        else:
            pass
    elif persistent.dlc_14nightswithyou_type == "free":
        if first_penetrated == True:
            r "U-Um. Actually… Before we continue…" nointeract
            call DLC_firsttime_penetrated from _call_DLC_firsttime_penetrated_2
        else:
            pass
    else:
        r "U-Um. Actually… Before we continue…" nointeract
        call DLC_firsttime_penetrated from _call_DLC_firsttime_penetrated_3
    return
label DLC_firsttime_penetrated:
    $ first_penetrated = False
    r "Y-You should know… I haven't done this with anyone else before…" nointeract
    y "Wait, what?" nointeract
    r "I'm glad I get to experience my first time with someone like you." nointeract
    n "He's looking at me with those eyes again as if I was the one who strung the stars up in the night sky just for him to see. And now here he was, telling me that he'd never done this before?" nointeract
    menu:
        "\"This is my first time as well.\"":
            $ rem_wahoo = False
            $ first_time = True
            r "{size=+10}R-Really?!{/size}" nointeract with vpunch
            r "Then… we're the same?" nointeract
            n "The look of pure, unadulterated happiness washes over his features as I felt the leaking tip of his dick slowly push into me for the first time." nointeract
            r "Ah~ We get to be each other's firsts. I'm so happy!" nointeract
        "\"I've already done this before.\"":
            $ rem_wahoo = True
            $ first_time = False
            n "The look of pure, unbridled jealousy washes over his features before he masks it with a smile, and I {b}finally{/b} feel the leaking tip of his dick slowly enter me." nointeract
            r "Then I'll fuck you better than anyone else you've ever had before me." nointeract
            r "You won't even remember their names by the time I'm done with you." nointeract
        "\"I'm happy I get to be your first.\"":
            $ rem_wahoo = True
            $ first_time = False
            n "He looks as though a giant weight had {b}finally{/b} been lifted off his shoulders, and I felt the leaking tip of his dick slowly enter me." nointeract
            r "Y-Yeah… I wouldn't want to do this with anyone else but you." nointeract
            r "Only you…" nointeract
            r "No one else matters." nointeract
        "\"Does it matter? I just want to feel you.\"":
            $ rem_wahoo = True
            $ first_time = False
            r "N-No, it doesn't. I just wanted you to know…" nointeract
            n "He looks almost dejected for a moment before he masks it with a smile, and I finally felt the leaking tip of his dick slowly enter my hole." nointeract
            r "{i}Hah—!{/i} You're so… tight—" nointeract
    return
label day1_wahooscene:
    show ren smirk at spop, center
    r "Do y'want me to kiss you again? Or do you want… {i}something else?{/i}" nointeract
    n "Where did this confident aura suddenly come from? The moment I showed interest, it was like he became a different person. Not that I was about to complain or anything; this side of him was… insanely attractive." nointeract
    show ren neutral at spop, center
    r "You've gone quiet on me, [ch_angel]. You have to tell me what you want, or I'll stop." nointeract
    y "…I want you, [ch_ren]. {i}Please?{/i}" nointeract
    play music "audio/bgm/Touch Your Heart.ogg" fadein 1 fadeout 1
    hide ren
    show other_dark
    with dissolve
    show peffectp zorder 2
    n "Without missing a beat, [ch_ren]'s large frame obscures my vision as he shifts between my thighs. Both of his arms rest against either side of my head and cage me in, and he stares down at me with an almost predatory gaze." nointeract
    n "He barely allows me a moment to make sense of the new situation before he leans forward to capture my lips in a searing kiss. His large frame engulfs my vision yet again, and I wrap my arms around his neck to pull him even {b}closer{/b} to my body." nointeract
    n "There's a hunger behind his eyes now, almost as if he had been practically {b}yearning{/b} for me all this time. So I lean in for yet another selfish kiss." nointeract
    n "He almost hisses at the contact before deepening it, with one hand coming to caress my cheek once more as the other trails down to my side." nointeract
    n "He kisses with much more fervour now, and I find myself melting into his warm touch. The hand on my side digs deeper into the flesh of my hip before it travels {b}even lower{/b} to tug at the underside of my shirt." nointeract
    n "His eyes seek out mine in the dark to silently ask for permission, and I breathlessly nod my head." nointeract
    n "Almost eagerly, he pulls my shirt up to expose my [bust]." nointeract
    n "The stark coldness of the room finally sinks in and sends a chill down my spine, but I ignore it in favour of feebly tugging at [ch_ren]'s clothes as well." nointeract
    n "He gets the message immediately, hastily tugging his outer sweater off over his head and letting one of the sleeves dangle off of his arm haphazardly. But as I move to take off his white undershirt, he stops me by taking my hand in a gentle hold." nointeract
    r "S-Sorry, can we keep that on? I… Don't feel comfortable taking it off just yet." nointeract
    y "No, that's fine. I get it." nointeract
    n "He barely allows me any time to respond before his lips latch on to my neck instead, and I let out an audible gasp as he bites and sucks on anything he can get his mouth on." nointeract
    n "One nibble in particular has me arching my body into him, and I suddenly became aware of {b}just{/b} how much this had been affecting him yet again." nointeract
    r "{i}Hng—! C-Careful…{/i}" nointeract
    n "He lets out a shaky moan into my ear, and I found myself wanting to hear him make that sound again. And so, almost deviously, I reach a hand down to play with the hem of his jeans." nointeract
    n "I pull at the elastic of his waistband before letting it snap back into place, and [ch_ren]'s response is immediate." nointeract
    n "His hips rut desperately into mine as he whines once more into my ear, and his hands and teeth return to their spot on my body — Only this time, he's biting a little harder and squeezing a little tighter." nointeract
    n "His other hand, however, glides down my sides and makes quick work of my pyjama bottoms, leaving me in nothing but my undergarments." nointeract
    n "I can feel the friction of his jeans {b}even more{/b} against my core now, and I let out a muffled groan at the intense feeling." nointeract
    n "Almost greedily, [ch_ren]'s head shifts back up to swallow my noises with a heated kiss, and his hand busies itself with the elastic of my underwear." nointeract
    n "His blue eyes find mine once more in {b}yet another{/b} silent question, so I guide his hand to where I needed it the most as the answer." nointeract
    r "Fuck, Angel— You're {i}dripping{/i}." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d1_t1 from _call_dlc_14nwy_d1_t1
    else:
        if genitalia == "cooter":
            n "Hearing him swear has me clenching my aching heat around nothing." nointeract
            n "And as if [ch_ren] could sense my neediness, I felt his hand move its attention away from my clit to insert one of his slender fingers into the very place I needed him the most and experimentally wiggle around." nointeract
            n "He starts thrusting his finger now, slowly easing it in and out of me before adding another. My breath hitches in my throat as I throw my head back, once again arching into his addictive touch." nointeract
        elif genitalia == "bussy":
            n "And as if [ch_ren] could sense my neediness, I felt his hand move away from the base of my leaking dick to insert one of his slender fingers into the very place I needed him the most and experimentally wiggle around." nointeract
            n "He starts thrusting his finger now, slowly easing it in and out of me before adding another. My breath hitches in my throat as I throw my head back, once again arching into his addictive touch." nointeract
        else:
            n "Hearing him swear has me clenching my aching hole around nothing." nointeract
            n "And as if [ch_ren] could sense my neediness, I feel him insert one of his slender fingers into the very place I needed him the most and experimentally wiggle around." nointeract
            n "He starts thrusting his finger now, slowly easing it in and out of me before adding another. My breath hitches in my throat as I throw my head back, once again arching into his addictive touch." nointeract
    n "My hips shamelessly rut against [ch_ren]'s hand as they move in tandem with his ministrations." nointeract
    n "Not wanting to be the only one experiencing such pleasure, I reach down to tug at his pants, and he {b}immediately{/b} gets the message to take them off — albeit with a bit {b}too{/b} much enthusiasm." nointeract
    n "[ch_ren] lifts himself from on top of me to cast his jeans off to who-knows-where before returning again with his undivided attention." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d1_t2 from _call_dlc_14nwy_d1_t2
    else:
        n "And as if to make up for temporarily leaving me, he inserts {b}yet another{/b} finger into me, and I feel myself stretching at the sheer size of them." nointeract
        n "Fuck. Just how big {b}was{/b} he if [ch_ren] felt the need to prep me with {b}three{/b} fingers?" nointeract
        n "If I could barely handle this many inside me, would I be able to…?" nointeract
    n "Reaching down, I let out a hitched breath as I take in just how {b}large{/b} his cock was. I mean, it made sense considering his overall size, but still…" nointeract
    n "He felt thick and heavy in my hand, and I could hardly wrap my fingers around it. I gave an experimental squeeze around the tip, and I felt [ch_ren] shiver above me and nuzzle his head into the crook of my neck." nointeract
    y "{i}A-Ah—!{/i}" nointeract
    n "As if responding to my sounds, his mouth moves towards my [bust], and I can't help but arch my back into his searing touch." nointeract
    n "No longer caring about the sounds I make or holding myself back, I keen at [ch_ren]'s ministrations as I desperately cling to his warm skin, quickly feeling that euphoric bliss build up inside me." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d1_t3 from _call_dlc_14nwy_d1_t3
    else:
        r "…Just like that. Keep squeezing around my fingers like that." nointeract
    n "His voice is barely above a whisper, but I hear it nonetheless and feel myself getting closer and closer to the edge." nointeract
    n "I stroke his length with the same fervour now as I shamelessly buck my hips against his hand and seek out what I was desperately looking for." nointeract
    if pronoun == "neutral":
        r "That's it, you're doing so well, baby~ Use my hand to get off." nointeract
    else:
        r "That's it, good [baby]~ Use my hand to get off." nointeract
    r "Ah— {i}Shit—!{/i} I want you to come for me. Can you do that for me, Angel?" nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d1_t4 from _call_dlc_14nwy_d1_t4
    else:
        n "He quickens his pace, and suddenly, my vision goes white. My toes curl as [ch_ren] continues to thrust and scissor his slender digits inside me, and I come with his name on my tongue." nointeract
    r "There you go. Fuck, {i}baby—{/i} You did such a good job." nointeract
    n "I barely hear his words as I lay there almost lifelessly to catch my breath. His hand is still on me, and I feel him scoop up some of my fluids with an embarrassing squelch." nointeract
    n "Then, as if he was the devil incarnate, I watch as he brings his fingers to his lips and practically {b}sucks{/b} on them." nointeract
    r "Mm, you taste just as good as I imagined." nointeract
    y "Nn… Shit, [ch_ren]—" nointeract
    r "Are you alright? That wasn't too much, was it?" nointeract
    y "Not at all… I think I just need a moment." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d1_t5 from _call_dlc_14nwy_d1_t5
    else:
        n "But during my hazed-out state, I came to the realisation that [ch_ren] was {b}still{/b} hard — if his \"subtle\" grinding against my thigh had anything to do with it. So I wrap my legs around his waist and draw him closer." nointeract
    n "He cries out at the sudden contact and doubles over, but quickly catches himself on his forearms before he could crush me with his weight." nointeract
    r "{i}Ah—!{/i} Are you sure, [ch_angel]? We-We don't have to…" nointeract
    n "His timid persona resurfaces once more, and had I not just experienced the best orgasm of my life, I would've been taken aback by the constant whiplash of his personality swings." nointeract
    y "I want to… {i}Please?{/i}" nointeract
    if nsfw_position == "vers":
        $ choice_style = "box"
        menu:
            "I want to penetrate Ren":
                $ nsfw_position = "temp_top"
                pass
            "I want to be penetrated":
                pass
        $ choice_style = "default"
    call DLC_firsttime_menu from _call_DLC_firsttime_menu
    y "Please, [ch_ren]…" nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d1_t6 from _call_dlc_14nwy_d1_t6
    else:
        if genitalia == "cooter":
            n "Apparently, that's all it takes to have him back on me once more, with his hungry mouth and body on mine as his hand moves to line himself up with my aching cunt." nointeract
        else:
            n "Apparently, that's all it takes to have him back on me once more, with his hungry mouth and body on mine as his hand moves to line himself up with my needy hole." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d1_t7 from _call_dlc_14nwy_d1_t7
    else:
        n "[ch_ren] had the decency to go slowly considering his large size, and I find myself clenching around every inch by agonising inch as he enters me." nointeract
        n "I almost forget to breathe as I feel him stretch out my walls, and I unconsciously latch onto his shoulders with my nails to bear the pain." nointeract
        n "Fuuuck… He really was huge. {b}Definitely{/b} bigger than anything else I've ever taken before." nointeract
        n "What felt like hours seemed to pass before [ch_ren] {b}finally{/b} bottoms out inside of me, and he almost seems to double over once more from the sheer pleasure of it all." nointeract
        n "He looks down at me once more with those soft blue eyes of his, and the entire exchange suddenly feels {b}far more{/b} intimate than actually having him inside of me." nointeract
        n "His hand comes to brush away a lone tear from the corner of my eye, and he bends down to give me a chaste kiss on the forehead." nointeract
    n "Surprised by such an innocent gesture, my eyes flutter open once more — and what greets me is a sight that takes my breath away." nointeract
    $ quick_menu = False
    scene other_dark
    show CG D1_NSFW1
    hide screen dayscalendar
    show screen menuwu
    with Fade(1.0, 1.0, 1.0)
    $ persistent.cg_d1_nsfw1 = True
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d1_t8 from _call_dlc_14nwy_d1_t8
    else:
        r "Hah— Look~ I'm finally inside you… You took me so well, Angel." nointeract
    if rem_wahoo == True:
        if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
            call dlc_14nwy_d1_t9 from _call_dlc_14nwy_d1_t9
        else:
            n "Despite his tender words, the sharp thrust of his hips takes me off guard as he begins to move. I can feel the veiny underside of his cock drag against my walls, which sends a wave of pleasure throughout my entire body." nointeract
            r "Does that feel good? You're making such a {i}mess{/i} down there…" nointeract
        r "Hah— Just wait until I'm finished with you~" nointeract
        n "His rough pace doesn't seem to relent as he slams his hips into mine, and the hand that brushed against my skin soon comes to interlock with one of my own." nointeract
        n "Yet again, this started to feel {b}far too{/b} intimate than it should've, but I was too lost in all the pleasure to give it much thought." nointeract
    else:
        if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
            call dlc_14nwy_d1_t10 from _call_dlc_14nwy_d1_t10
        else:
            n "[ch_ren] doesn't move his hips yet, instead choosing to look down at me with soft eyes as I become accustomed to having something inside me for the first time." nointeract
            r "I-Is it uncomfortable? Let me know if it hurts, okay? Just say the word, and we can stop." nointeract
            n "His sincerity touches me as he tries to remain still inside me, but I can tell from his rough expression that he's trying to hold himself back." nointeract
            n "Sure, there was still a little bit of pain — but I reassure him by locking my legs around his waist and pulling him closer." nointeract
            n "At that, I can feel the veiny underside of his cock drag against my walls as he begins to move, sending a wave of pleasure throughout my entire body." nointeract
            n "His gentle pace soon becomes a lot rougher as he experimentally bucks his hips into mine, and the hand that brushed against my skin soon comes to interlock with one of my own." nointeract
        n "Yet again, this is starting to feel far more intimate than it should, but I'm lost in all the pleasure to give it much thought." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d1_t11 from _call_dlc_14nwy_d1_t11
    else:
        r "Look at you, taking my cock with such a lewd expression on your face. {i}Fuck.{/i} Y'feel so good—!" nointeract
    r "It's like you were made for me…" nointeract
    show CG D1_NSFW2
    $ persistent.cg_d1_nsfw2 = True
    r "Like you were made to be {i}mine{/i}." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d1_t12 from _call_dlc_14nwy_d1_t12
    else:
        n "His expression does little to stifle the sensation slowly building between my legs, and I unconsciously clench down around him. [ch_ren] lets out another shaky moan before he effortlessly lifts my hips off of the bed and grinds it along his shaft instead." nointeract
        n "The new position has me seeing stars, and sends my eyes rolling into the back of my head." nointeract
    y "Shit, [ch_ren]! J-Just like that—!" nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d1_t13 from _call_dlc_14nwy_d1_t13
    else:
        if genitalia == "cooter":
            n "My praise only seems to spur him on as he pounds into me with even more vigour now, and the hand that was once intertwined with mine slips between our bodies to stroke my clit." nointeract
        elif genitalia == "bussy":
            n "My praise only seems to spur him on as he pounds into me with even more vigour now, and the hand that was once intertwined with mine slips between our bodies to pump my length once more." nointeract
        else:
            n "My praise only seems to spur him on as he pounds into me with even more vigour now, and the hand that was once intertwined with mine slips between our bodies to play with my nipples once more." nointeract
    show CG D1_NSFW3
    $ persistent.cg_d1_nsfw3 = True
    r "{i}Haah~{/i} F-Fuck— [ch_angel]-!" nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d1_t14 from _call_dlc_14nwy_d1_t14
    else:
        n "Hearing him cry out my name with such {b}neediness{/b} is what finally sends me over the edge once more, and I come undone on his cock with his own name on my lips." nointeract
        n "[ch_ren] isn't far off, it seems, as it only takes a few more thrusts of his hips before he reaches his peak, gripping my waist in a crushing hold as he cries out my own name as well." nointeract
    r "[player_fl]-[player_fl]-[ch_angel]!" nointeract
    n "He seems almost dazed for a moment as he catches his breath, before he doubles over and almost crushes me with the weight of his chest." nointeract
    $ quick_menu = True
    scene angel_bed_night
    hide screen menuwu
    show screen dayscalendar
    show peffectp
    with Fade(1.0, 1.0, 1.0)
    n "At my protest, he lethargically rolls to his side — but not before scooping me into his large arms and bringing me along with him." nointeract
    if nsfw_position == "bottom":
        n "His softening length remains buried deep inside me, but it feels more like a dull sensation at this point as I curl myself into [ch_ren]'s warmth." nointeract
    n "Breathless, sticky, and now perched atop his chest, [ch_ren] and I simply lay there as we take in the afterglow of the moment. What feels like hours seem to pass as I listen to his breathing, and soon enough, I feel my own come to a slow, even pace." nointeract
    n "The hand that was idly stroking up and down my backside soon comes to an eventual halt, and I don't even need to look up to know that he'd already fallen asleep." nointeract
    n "He still has a protective grip on me, though, so I allow the exhaustion to take hold of me and follow [ch_ren] to dreamland." nointeract
    n "After all, we could talk about what had just happened in the morning." nointeract
    $ d1_wahooren = True
    $ rem_wahoo = True
    if nsfw_position == "temp_top":
        $ nsfw_position = "vers"
    if playtest == True:
        jump day2_wahooscene
    else:
        jump day1_ending_good
label day2_wahooscene:
    scene ren_spareroom_night
    play audio "audio/sfx/movement.ogg"
    play audio "audio/sfx/walking.ogg"
    show ren flushed at spop, center
    show peffectp
    with Fade(1.0, 1.0, 1.0)
    n "Without missing a beat, I pull [ch_ren] into the room by the ends of his shirt, making sure to tug him down and plant a kiss on his inviting lips in the process." nointeract
    show ren neutral at center
    n "He seems surprised for a brief moment — if his wide eyes were any indication — but he quickly recovers by wrapping a large hand around my waist and pulling me closer to his body." nointeract
    n "Pressed flush against his warmth now, I paid no mind to the cold bite of the wind outside his window — alongside the ominous lulls of thunder off in the distance and the streaks of lightning illuminating the dark sky." nointeract
    show ren smirk at center
    n "I somehow felt safe in his embrace, and the way he was pressing hot, fervent kisses against my mouth made me forget all about the muted downpour of rain outside." nointeract
    n "[ch_ren] seemingly felt the same given how he didn't even bat an eye at the flash of lightning — instead appearing content with hoisting my legs around his waist and carrying me towards the edge of the bed. " nointeract
    n "Well, that was rather bold of him." nointeract
    n "I let him take the initiative for the moment as I let my hands aimlessly wander up and down the expanse of his (admittedly large) chest, before settling against the exposed skin just above his grey sweatpants instead." nointeract
    n "My sudden touch seems to pull an audible gasp from [ch_ren] as his lips begrudgingly leave my own to peer down at me instead." nointeract
    show ren blushing at spop, center
    if rem_wahoo == True:
        r "You sure? You want to… A-Again?" nointeract
    else:
        r "Are you sure? Y-You want to…" nointeract
    n "[ch_ren]'s eyes maintain that hopeful sheen to them, though I can tell by his hesitance that he didn't want to instigate anything without my consent." nointeract
    scene black
    hide ren
    show peffectp
    with dissolve
    n "And so, with an affirmative nod, I close my eyes and press my body against his once more as his mouth and teeth playfully return to that sensitive spot on my neck." nointeract
    n "The faint pitter-patter of rain against glass fills the empty silence in the room, before it's replaced by the sounds of us falling onto the mattress in a mess of tangled limbs and fervent kisses." nointeract
    n "The fresh smell of linen and soft sheets fills my senses until it slowly starts to morph into a vague visage of [ch_ren] — with his large frame blocking my view as he slowly crawls on top of me." nointeract
    n "Cherry-tinted lips return once more in the form of frantic kisses and hushed moans as his hands roam up and down my sides in a soothing manner." nointeract
    n "His entire being overwhelms me, and I couldn't help but want to reciprocate his addictive ministrations." nointeract
    n "And so, almost unabashedly, I run my hands down the warm expanse of his chest once more before tugging at the hem of his shirt — indicating that I wanted him to take it off." nointeract
    if rem_wahoo == True:
        n "But just like last time, [ch_ren]'s hand moves to stop me once more." nointeract
        r "Not yet. I still don't… I-I'm sorry, but I don't want to take it off just yet-" nointeract
    else:
        n "But almost unexpectedly, [ch_ren]'s hand moves to stop me once more." nointeract
        r "Um— Sorry, but I don't want to take it off just yet-" nointeract
    y "Hey, it's okay." nointeract
    n "Not wanting to startle him, I gently cup [ch_ren]'s cheek to give him some sort of reassurance." nointeract
    if rem_wahoo == True:
        n "He had been nothing but patient and understanding with me during our last intimate encounter, so it was only fitting for me to return the favour." nointeract
    y "Whatever you're comfortable with, [ch_ren]." nointeract
    n "His eyes seem to soften at my words the moment he hears them, so he sends me a blinding smile in response." nointeract
    n "Large, gentle hands encompass my waist as [ch_ren] shifts his body closer, nuzzling his head into my neck before he speaks once more." nointeract
    r "…Y'too. I only wanna do what you're comfortable with." nointeract
    n "Lifting his head, [ch_ren]'s lips return to mine once again, and I kiss [ch_ren] back with the same amount of desire and ardour." nointeract
    n "I can feel one of his hands chart a path down my side to play with the strings of my (his?) shorts, before teasingly tugging them loose and slipping underneath." nointeract
    n "His hand doesn't go any further than my hip, but the way he touched me felt… {b}different{/b}, somehow." nointeract
    if rem_wahoo == True:
        n "It'd barely been a day since we last did… {b}this{/b} — yet it seem as though [ch_ren] was a completely different person this time. His touch feels more practised and confident now, almost like he wasn't holding himself back anymore." nointeract
        n "His kisses, however, are all too familiar." nointeract
        n "I can practically {b}feel{/b} the adoration and devotion with every press of his lips, and the faint taste of mint brings back those intimate memories shared in the darkness of my bedroom." nointeract
    else:
        n "I've grown used to seeing such a shy and timid [ch_ren] — it almost seems like the person in front of me is a completely different person. His touch feels… confident somehow, almost like he wasn't holding himself back anymore." nointeract
        n "His kisses, however, are all too familiar." nointeract
    r "Actually…" nointeract
    n "His voice is nothing but a whisper against my skin before he draws back slightly to look me in my eyes. I watch on with bated breath as he continues speaking." nointeract
    r "Can we try something… different tonight?" nointeract
    n "[ch_ren]'s timid tone catches me off guard, and I look up only to see him sporting an inquisitive glint in his eyes." nointeract
    n "Curious — and perhaps a little out of breath from the heated make-out session we just shared — I raise an eyebrow at [ch_ren]'s sudden request, but allow him to continue nonetheless." nointeract
    r "Here, lay back." nointeract
    n "With his honeyed voice as soft as his gaze, [ch_ren] gently pulls me towards the end of the bed by my hips." nointeract
    if persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid":
        show CG D2_NSFW1 with dissolve
        $ persistent.cg_d2_nsfw1 = True
    n "A puff of laughter escapes my throat at the sudden motion, before it abruptly morphs into a moan as [ch_ren] situates himself between my thighs instead." nointeract
    n "And despite the heavy tension in the air, I hear something fall from the pillows above my head, which makes me look upwards to see what it was." nointeract
    n "My mind barely has a moment to process the Haruko plushie leaning on its side — did [ch_ren] {b}really{/b} go out of his way to buy this for me? — before he easily hoists my legs over his shoulders and steals my attention once more." nointeract
    n "I watch on with avid curiosity as [ch_ren] shoots me an unreadable grin in return, barely drawing my focus away from his hands as they slowly travel down my sides to hook themselves in the waistband of my shorts." nointeract
    n "Ah. So that was what he had in mind." nointeract
    n "Catching on quickly, I lift my hips to let [ch_ren] remove them alongside my underwear — one of the only particles of clothing left that hadn't been soaked by the rain." nointeract
    n "Now completely bare before him, I felt the urge to turn on my side and hide away from his heavy gaze, but the lustful look in his eyes convinces me to stay put." nointeract
    n "Almost shaking in anticipation, I watch as his hand travels lower and lower until…" nointeract
    y "Ah-!" nointeract
    n "Cold fingertips brush against my inner thigh as [ch_ren] places butterfly kisses against my left ankle." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and first_receiving == True:
        call DLC_firsttime_receiving from _call_DLC_firsttime_receiving
    n "His descent is slow, deliberate, and ardent — before his soft lips meet the space near his fingers. I can feel his mouth move against my skin before my pleasure-filled mind can process his words." nointeract
    r "Just lay back. You don't need to do anything." nointeract
    n "[ch_ren]'s blue eyes shine faintly in the darkness, and I could catch the softest hint of mischief behind them." nointeract
    r "Let me take care of you." nointeract
    if persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid":
        hide CG D2_NSFW1 with dissolve
    n "Squeezing my eyes shut, I feel his lips leave a trail of wet kisses against my skin, closer and closer until—" nointeract
    $ first_ren_giving = False
    n "The next thing I know, I can feel [ch_ren]'s warm mouth pressed flush against the spot where I'm aching the most." nointeract
    if genitalia == "cooter":
        n "A hot tongue darts out to lick a long, wet stripe against my folds, and I have to resist the urge to arch back into his touch." nointeract
        n "His fingers soon join in as they slowly enter my hole, causing my breath to hitch at the sudden sensation." nointeract
        n "They curl and prod against my walls as [ch_ren] shifts slightly to press soft kisses against my stomach and thighs once more, before slowly inching his face closer and closer to where I need him the most." nointeract
        n "The wet tip of his tongue lands on my clit, and I open my eyes in time to watch him eagerly lap up the fluid pooling between my thighs with a debauched grin." nointeract
    elif genitalia == "bussy":
        n "A hot tongue darts out to lick a long, wet stripe along my cock, and I have to resist the urge to arch back into his touch." nointeract
        n "His fingers soon travel south as they slowly enter me, causing my breath to hitch at the sudden sensation." nointeract
        n "They push and prod against my walls as [ch_ren] shifts slightly to press soft kisses against my base and tip once more, before slowly taking my entire length into his mouth." nointeract
        n "The wet tip of his tongue returns once again, and I open my eyes in time to watch him eagerly lap up the fluid dribbling between my thighs with a debauched grin." nointeract
    else:
        n "A hot tongue darts out to lick a wet stripe along my skin, and I have to resist the urge to arch back into his touch." nointeract
        n "His fingers soon join in as they slowly enter me, causing my breath to hitch at the sudden sensation." nointeract
        n "They push and prod against my walls as [ch_ren] shifts slightly to press soft kisses against my stomach and thighs once more, before slowly inching his face closer and closer to where I need him the most." nointeract
        n "The wet tip of his tongue returns once again, and I open my eyes in time to watch him eagerly lap up the fluid pooling between my thighs with a debauched grin." nointeract
    y "[ch_ren]—!" nointeract
    n "I can practically {b}feel{/b} him laugh at my reaction, seemingly pleased with having me watch on with bated breath and clenched muscles." nointeract
    n "And just like that, his mouth goes back to my sensitive parts as his two fingers continue their ministrations inside of me: stretching me out and rubbing against my walls with languid, deliberate motions." nointeract
    n "Another finger soon joins the others, and my thighs unconsciously close around his head at the intrusion." nointeract
    n "[ch_ren] lets out a pleased hum at this, clearly content with being sandwiched between my legs and being so close to my heat." nointeract
    n "He gives a loving nip at my skin to show his appreciation before sinking his head lower and deeper — lapping up my wetness like a man starved." nointeract
    r "I've dreamed about this." nointeract
    r "You taste better than anything I was expecting." nointeract
    n "His words came out as nothing but a mumbled, sticky mess against my skin, bringing on another wave of pleasure that was slowly building inside of me." nointeract
    n "I can feel [ch_ren]'s other hand run up and down my thighs in a soothing manner before gently prying them apart to spread my legs wider." nointeract
    n "Cold air rushes past our bodies and sends a shiver up my spine, and I can feel him readjust himself beneath me before returning to my needy sex with renowned fervour." nointeract
    if genitalia == "cooter":
        n "His mouth is hot against my dripping cunt once more, and I watch as his eyes close in bliss as he moans against my skin." nointeract
    elif genitalia == "bussy":
        n "His mouth is hot against my leaking dick once more, and I watch as his eyes close in bliss as he moans against my skin." nointeract
    else:
        n "His mouth is hot against me once more, and I watch as his eyes close in bliss as he moans against my skin." nointeract
    r "Y'taste divine. Fuck, [ch_angel]… I could stay here forever." nointeract
    n "He sounds serious about his declaration — and the mental image of [ch_ren] on his knees whilst nestled between my thighs emits yet another low whine from me." nointeract
    n "The movement of his fingers only adds to the building sensation, and the sudden addition of his tongue does little to stifle the burning desire inside of me." nointeract
    n "It was starting to become too much for me to keep bottled up, and I have to hold myself back from pulling at the sheets and crying out in pleasure — or, at the very least, stop tugging on [ch_ren]'s hair and shamelessly moan out his name." nointeract
    n "Completely unaware of my inner turmoil, he pushes his digits in deeper now — and in my hazy pleasure, I can faintly make out the metallic feeling of his ring rubbing against my entrance." nointeract
    y "[ch_ren]—!" nointeract
    n "He all but moans against my skin in response as his free hand ghosts along my (still-clothed) stomach to play with my [bust] instead of my thighs." nointeract
    n "He pinches and rolls one of my nipples between his fingers while his tongue delves deeper inside me, and I can barely keep my eyes open as I give in to the hazy pleasure he was giving me." nointeract
    if genitalia == "cooter":
        n "Clenching my eyes shut, I can almost make out [ch_ren] trying to spell his name with his tongue, and I can barely hold myself back from keening out at the budding sensation inside of me." nointeract
    elif genitalia == "bussy":
        n "Clenching my eyes shut, I can almost feel the back of [ch_ren]'s throat as he takes all of me into his mouth, and I can barely hold myself back from keening out at the budding sensation inside of me." nointeract
    else:
        n "Clenching my eyes shut, I can almost feel [ch_ren] reaching the deepest parts of me with his tongue, and I can barely hold myself back from keening out at the budding sensation inside of me." nointeract
    n "Seemingly enjoying all the sounds he pulls from my lips, [ch_ren] looks up from between my thighs and gives me yet {b}another{/b} playful grin." nointeract
    r "That's it. You're doing so well, Angel." nointeract
    r "Buck back against my face if y'want to. Don't be shy." nointeract
    n "At his words, [ch_ren] seems to pick up on my sudden hesitance — if my slight change in body language was anything to go by." nointeract
    r "It's okay; use me to make yourself feel good." nointeract
    n "And with that, [ch_ren] goes back to licking up my wetness like it's his last meal." nointeract
    if genitalia == "cooter":
        n "I can feel him softly moaning against my skin as his nose rubs against my clit — before his tongue joins his fingers once more to stretch me out and make me see stars." nointeract
        n "I couldn't help but do as he says in that moment; shamelessly bucking my hips and bordering on riding his face as [ch_ren] reaches the deepest parts of me with his mouth and hand." nointeract
    elif genitalia == "bussy":
        n "I can feel him softly moaning around my leaking cock as the tip touches the back of his throat — before his fingers curl once more to stretch me out and make me see stars." nointeract
        n "I couldn't help but do as he says in that moment; shamelessly bucking my hips and bordering on fucking his face as [ch_ren] reaches the deepest parts of me with his long fingers." nointeract
    else:
        n "I can feel him softly moaning against my hole as his nose rubs against my skin — before his tongue joins his fingers once more to stretch me out and make me see stars." nointeract
        n "I couldn't help but do as he says in that moment; shamelessly bucking my hips and bordering on riding his face as [ch_ren] reaches the deepest parts of me with his mouth and fingers." nointeract
    n "Soon enough, the pressure becomes too much for me to handle, and I can only cry out his name like a broken record on repeat." nointeract
    y "I-I'm close—!" nointeract
    r "Yeah? It's okay. Come for me, Angel." nointeract
    if genitalia == "cooter":
        n "My voice echoes out into the dark room as my back arches off the bed. Shamelessly riding [ch_ren]'s tongue and fingers; I rock back and forth until the pleasure becomes too much for me to handle." nointeract
        n "His free hand grips my thigh to pull my cunt impossibly close to his mouth and play with my clit, and his ministrations soon speed up to help me reach my peak." nointeract
        n "[ch_ren]'s name continues to fall from my lips like a mantra as I tumble over that blissful edge; tugging on the roots of his hair as I fall into the pit of pleasure below." nointeract
        n "Blinding white floods my vision as I moan out in bliss, my hole tightening and twitching around the large fingers still deep inside me." nointeract
    elif genitalia == "bussy":
        n "My voice echoes out into the dark room as my back arches off the bed. Shamelessly bucking into [ch_ren]'s hot mouth; I rock back and forth until the pleasure becomes too much for me to handle." nointeract
        n "His free hand grips my thigh as he pulls me impossibly close to his mouth, and his ministrations speed up to help me reach my peak." nointeract
        n "[ch_ren]'s name continues to fall from my lips like a mantra as I tumble over that blissful edge; tugging on the roots of his hair as I fall into the pit of pleasure below." nointeract
        n "Blinding white floods my vision as I moan out in bliss, hot ropes of cum erupting inside of [ch_ren]'s mouth as he swallows it all down with a satisfied smile." nointeract
    else:
        n "My voice echoes out into the dark room as my back arches off the bed. Shamelessly riding [ch_ren]'s tongue and fingers; I buck back and forth until the pleasure becomes too much for me to handle." nointeract
        n "His free hand grips my thigh as he pulls me impossibly close to his mouth, and his ministrations speed up to help me reach my peak." nointeract
        n "[ch_ren]'s name continues to fall from my lips like a mantra as I tumble over that blissful edge; tugging on the roots of his hair as I fall into the pit of pleasure below." nointeract
        n "Blinding white floods my vision as I moan out in bliss, my hole tightening and twitching on the large fingers still deep inside me." nointeract
    n "My breath is shaky as I slowly fall back onto the bed to catch my breath, and I can feel [ch_ren] leaving soft kitten licks against my skin as I calm down." nointeract
    n "Slowly, he crawls up from beneath me — but not before adjusting my legs around his waist once more rather than his shoulders." nointeract
    n "Soft, cerulean eyes find mine in the darkness as [ch_ren] places a gentle kiss on my temple, alongside murmurs of praise and reassurance." nointeract
    n "The moment feels soft and tender — just like how he was looking at me — and almost instinctively, I weakly reach for the band of his sweatpants to return the favour." nointeract
    n "But before I can get anywhere near his private parts, [ch_ren] grabs my hand and brings it towards his face instead." nointeract
    y "Here, let me—" nointeract
    r "I-It's okay." nointeract
    y "But you did all the work just now. I wanna return the favour." nointeract
    r "It's okay. Really. As long as you got to feel good, [ch_angel]." nointeract
    n "He repeats himself as he snuggles closer into my side; almost as if he was used to this intimate routine by now." nointeract
    n "Strong arms wrap around my waist as [ch_ren]'s body collapses behind me, carefully pulling me into the warmth of his chest before he starts to draw shapes on my stomach." nointeract
    n "From this position, I can easily make out the outline of his hard-on pressing against my backside — and it did little to ease my conscience." nointeract
    y "[ch_ren]?" nointeract
    r "[ch_angel]." nointeract
    y "{i}[ch_ren].{/i}" nointeract
    n "He lets out a bemused hum behind me, before halting his movements and breathing in my scent." nointeract
    r "Alright. Maybe next time you can return the favour, then." nointeract
    r "B-But… But only if you want to." nointeract
    n "At that, [ch_ren] pulls me even closer into the warmth of his body — if it was even possible, given how inseparable we were right now." nointeract
    r "Ooor… You could let me go down on you again." nointeract
    r "You're my new favourite dessert now. Forget that boardwalk café." nointeract
    n "I couldn't help but laugh at that. It certainly wasn't something I'd imagine [ch_ren] to say, but he seemed to be full of unexpected surprises tonight." nointeract
    n "A comfortable silence soon washes over the both of us, and I can feel [ch_ren] mumble a faint 'getting… sleepy… g'night, Angel.' against my shoulder." nointeract
    n "Well, he certainly seemed to fall asleep quickly." nointeract
    n "Leaving me to my own devices, I idly take in the interior of the dark room until the urge to sleep consumes me." nointeract
    n "The soft patter of rain and thunder still echoes in the distance — coupled with [ch_ren]'s soft breathing — giving me a moment to myself to think." nointeract
    n "How did I feel about [ch_ren]?" nointeract
    $ d2_wahooren = True
    $ rem_yippee = True
    if playtest == True:
        jump day3_wahooscene
    else:
        jump day2_wahooend
label day3_wahooscene:
    scene black
    play music "audio/bgm/Touch Your Heart.ogg" fadein 1 fadeout 1
    if persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid":
        show CG D3_NSFW1
        $ persistent.cg_d3_nsfw1 = True
    show peffectp
    with Fade(1.0, 2.0, 1.0)
    n "Everything around me goes dark, and suddenly, all my other senses are filled with [ch_ren]." nointeract
    n "The smell of fresh linen and old books greet me as I feel the cold touch of his fingers glide across my skin and gently spin me back around." nointeract
    n "I hear more fabric rustling and [ch_ren]'s breathing grow heavier before I taste his cherry-tinted lips against my own in a slow, ardent kiss." nointeract
    n "But [ch_ren] cruelly pulls away the moment I try to deepen the kiss, and I didn't need to see his face to know that he was probably sporting a playful grin at my sour expression." nointeract
    n "As if to make up for it, [ch_ren]'s larger hands reach for my own and bring them towards the warmth of his chest." nointeract
    n "…His warm, {b}bare{/b} chest." nointeract
    n "Not wanting to waste this opportunity, I carefully run my nails against his skin, taking in the hardness of his muscles and the rivets of his collarbones." nointeract
    n "The bulky muscle mass {b}clearly{/b} wasn't what I was expecting him to hide underneath those soft, cosy-looking sweaters of his — and I have to hold back the urge to move the makeshift blindfold to sneak a peek." nointeract
    n "But I suppose [ch_ren] isn't comfortable with me seeing him without his shirt, so I decide to respect his decision and make do with what he was willing to offer me." nointeract
    y "[ch_ren]…" nointeract
    n "My hands travel lower until they brush over his abdomen, and I can hear him suck in a breath at the sensation." nointeract
    n "His muscles flex and stiffen under my touch before cold fingers wrap around my wrist to guide them towards his face instead." nointeract
    n "Soft kisses are left on the palm of my hands, and I gently cup [ch_ren]'s face as he continues his doting ministrations." nointeract
    n "It doesn't take long before I feel [ch_ren]'s hands ghost against my sides instead — and almost like clockwork, I lift my hips and let him remove the rest of my clothing." nointeract
    n "With the rest of my senses heightened, I feel the rush of cold air brush against my skin before it's replaced by the warmth of [ch_ren]'s body once more." nointeract
    n "My arms eagerly hook themselves over his shoulders, and I feel him pull me closer by my thighs before pressing light kisses against my neck." nointeract
    n "A ticklish sensation runs throughout my entire body as his fingers return to my thighs once more, gently running up and down before inching closer and closer to the place that was yearning for his touch." nointeract
    y "P-Please…" nointeract
    r "Please what? You have t'use your words, Angel." nointeract
    n "His breath tickles my skin as he murmurs into the juncture near my neck, before he drops lower to playfully nip at my [bust]." nointeract
    if persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid":
        hide CG D3_NSFW1 with dissolve
    n "The sensation has me squeezing my eyes shut as I try to fumble around for [ch_ren] in the dark." nointeract
    y "Ah—! Please touch me…" nointeract
    r "…Where?" nointeract
    n "Almost groaning in frustration, I roll my hips against his large hand to get my point across." nointeract
    r "What's that? Want me to stop?" nointeract
    n "Even with the blindfold on, I can still practically make out the sly expression on [ch_ren]'s face. His tone was practically {b}dripping{/b} in smugness, and it takes all my willpower not to take matters into my own hands." nointeract
    n "Letting go of my pride — even if it was for just a moment — I quietly mutter out a response." nointeract
    y "Jeez, [ch_ren]! Just— {i}Please…{/i}" nointeract
    extend " Just touch me. You know where." nointeract
    r "Do I?" nointeract
    y "[ch_ren]!" nointeract
    r "Haha~ I'm sorry. You're just so fun to tease." nointeract
    r "You know I'd never deny you, [ch_angel]." nointeract
    n "At that, I can feel him press a wet kiss against my cheek before he slowly inches his way closer towards my lips." nointeract
    r "…Here?" nointeract
    n "Almost immediately, [ch_ren]'s hand starts to move in tandem with his mouth, and I almost cry out in relief." nointeract
    if genitalia == "cooter":
        n "His touch is light and tentative at first, gently running along my folds and gathering my slick — before he slowly eases two of his fingers inside me." nointeract
    elif genitalia == "bussy":
        n "His touch is light and tentative at first, swiping up some of my leaking precum to use as lube alongside his own spit — before he slowly eases one of his fingers into my hole." nointeract
    else:
        n "His touch is slow at first, gently tracing and prodding my entrance — before he gently eases in one of his fingers." nointeract
    n "I hadn't even noticed how much of a mess I was making down there, but it helped ease the friction once [ch_ren] added another digit inside of me." nointeract
    n "He starts to pump it in and out of me before switching to a slow, deliberate scissoring motion, and it has me keening out." nointeract
    n "It sends a wave of pleasure throughout my body, and I return the favour by reaching out to trace whatever patch of skin my hands can reach." nointeract
    n "It doesn't take long before my hands find his chest and chart a familiar path down towards his navel — before coming into contact with [ch_ren]'s fully erect member." nointeract
    r "A-Ah—!" nointeract
    n "[ch_ren] buckles over in pleasure, and I can feel his head dip into my neck once more before his teeth meet my skin." nointeract
    n "I lean in to press a kiss of my own to the side of his head, and he reacts almost immediately to my touch; pumping his hand with even more vigour and pressing searing kisses to the spot below my earlobe." nointeract
    r "I-I can't wait any longer… Angel, can I—" nointeract
    if nsfw_position == "vers":
        $ choice_style = "box"
        menu:
            "I want to penetrate Ren":
                $ nsfw_position = "temp_top"
                pass
            "I want to be penetrated":
                pass
        $ choice_style = "default"
    call DLC_firsttime_menu from _call_DLC_firsttime_menu_1
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d3_t1 from _call_dlc_14nwy_d3_t1
    else:
        n "He can't seem to concentrate with the way his words come out slurred and needy, so I decide to put him out of his misery by adjusting his cock and lining it up with my entrance." nointeract
        n "He immediately catches on — leaning back onto the couch and spreading my legs further. I almost miss the warmth of his body on mine, but the sudden sensation of his tip teasing my hole draws my attention away." nointeract
        n "With slow, deliberate movements, [ch_ren] gently pushes himself inside of me, and I can barely hold back the sounds of my voice as the stretch of his length fills me up." nointeract
    if d1_wahooren == True:
        if persistent.dlc_14nightswithyou_type == "paid":
            call dlc_14nwy_d3_t2 from _call_dlc_14nwy_d3_t2
        else:
            r "Missed this… Missed being inside of you…" nointeract
        n "[ch_ren] starts to move his hips now as one of his hands seeks out my own. Familiarity blooms inside of me once he entwines our fingers, before it gets replaced with a foggy haze the moment he starts to pick up his pace." nointeract
    else:
        r "We're finally… Haah~ Y'feel so good! This is better than anything I've ever imagined…" nointeract
        n "[ch_ren] starts to move his hips now as one of his hands seeks out my own. Sincerity blooms inside of me once he entwines our fingers, before it gets replaced with a foggy haze the moment he starts to tentatively move his hips." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d3_t3 from _call_dlc_14nwy_d3_t3
    else:
        n "The friction of his cock brushing against my walls practically steals the air from my lungs, and I can't help but arch my back off of the couch." nointeract
    if first_time == True:
        r "Are you okay? You're not in any pain, are you? If you are, tell me and I'll stop." nointeract
        y "Me? What about you?" nointeract
        n "I can feel him smile against my neck before his lips timidly move towards my [bust]." nointeract
        r "I-I… Um… I want to make you feel good too, since this is our first time and all. Is that okay?" nointeract
        r "You don't have to do anything! J-Just let me do all the work." nointeract
    elif d1_wahooren == True:
        r "We've been doing this a lot now, haven't we? You're so addictive, Angel." nointeract
        n "I can feel him smile against my neck before his lips move towards my [bust]." nointeract
        if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
            call dlc_14nwy_d3_t4 from _call_dlc_14nwy_d3_t4
        else:
            r "…No one else has been inside of you since last time, right? Only me?" nointeract
            r "Doesn't really matter anyway. 'M gonna make this [hole] remember my shape." nointeract
    else:
        r "Y-You're so addictive, Angel. I can't get enough of you." nointeract
        n "I can feel him smile against my neck before his lips move towards my [bust]." nointeract
        r "…You won't let anyone else do this with you, right? Only me?" nointeract
        if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
            call dlc_14nwy_d3_t5 from _call_dlc_14nwy_d3_t5
        else:
            r "Doesn't really matter anyway. 'M gonna make this [hole] remember my shape." nointeract
    n "His babbling is bordering on intelligible, and I can barely process his words as all the pleasure fills my brain." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d3_t6 from _call_dlc_14nwy_d3_t6
    else:
        n "All I can focus on is the way [ch_ren]'s cock drives into me as his desperate moans ghost along my skin." nointeract
    r "Only I get to be with you like this… O-Only I can bring you this much pleasure, right?" nointeract
    n "[ch_ren]'s free hand comes to play with my [bust] as his hips roughly buck against my own. The lewd sound of wet skin slapping skin fills the room, accompanied by his insistent ramblings." nointeract
    r "Only me? I'm the only one, aren't I? Tell me…! Ah— F-Fuck!" nointeract
    r "Y'feel so good… Tell me, [ch_angel]—!" nointeract
    n "His grip on my hand tightens and draws me back to the present. In my hazy state, I barely process his unintelligible mumbling before responding with a few words of my own." nointeract
    n "My voice barely comes out louder than a whisper, though I was sure [ch_ren] would hear it, given his close proximity." nointeract
    y "Only {i}you,{/i} [ch_ren]— Just you!" nointeract
    n "I can hear him let out a laugh of relief before his mouth closes on my neck to gently nibble and suck." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d3_t7 from _call_dlc_14nwy_d3_t7
    else:
        n "Leaving another hickey, no doubt — and had I not been getting fucked within an inch of my life — I would've fully noticed the possessive undertones of his actions." nointeract
    r "That's right. Only me. Just like you're the only one f'me, too." nointeract
    r "No one— No one can ever replace you—!" nointeract
    r "Here… Let me reward you for being so honest." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d3_t8 from _call_dlc_14nwy_d3_t8
    else:
        n "Before I can respond, [ch_ren] effortlessly lifts my hips off the couch and {b}fully{/b} sheaths himself inside of me. He sets a brutal pace now, and all I could do was latch onto the throw pillows above my head and let him pound into me." nointeract
        r "No one else could ever compare to you…" nointeract
        r "Y'feel so good too, squeezing my cock like that." nointeract
        n "My legs get thrown over his shoulders, and the new position has me seeing stars." nointeract
        n "I can feel [ch_ren]'s cock drag against my walls, and once his swollen tip hits that particular spot inside me, I can't help but cry out and dig my nails into his arms." nointeract
    n "Pleasure starts to build inside me, and I cast my dignity aside in favour of bucking my hips back in time to meet [ch_ren]'s." nointeract
    r "That's it, keep grinding against me like that." nointeract
    r "You're doing so well. {i}So good{/i} for me." nointeract
    n "His praise only spurs me on, and if I could see his face right now, I know it would be scrunched up in pleasure." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d3_t9 from _call_dlc_14nwy_d3_t9
    else:
        n "[ch_ren]'s voice does little to hide his desire and hunger for me, and he makes it known by bullying his dick into me with reckless abandon." nointeract
    r "You won't do this with anyone else, right? Only me?" nointeract
    r "You'll come to me for this kind of stuff, won't you, Angel?" nointeract
    n "His voice is right beside my ear now, and it sends a shiver up my spine. His tongue soon darts across my skin, creating a wet path from the shell of my ear down to my neck." nointeract
    n "He gently bites down then, drawing another moan from my lips and sending my head spinning. It's slowly becoming too much for me to handle, and I can tell [ch_ren] is enjoying every second of it." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d3_t10 from _call_dlc_14nwy_d3_t10
    else:
        r "Nobody else will fuck you as good as I can." nointeract
        r "Try as much as you want, but it's {i}my{/i} cock that your [hole] will crave." nointeract
        r "Nobody else will fill you up like I can. No one can stretch you full like me." nointeract
    r "I'll make you remember it." nointeract
    n "The lewd sounds coming between our bodies are bordering on {b}obscene{/b} at this point, yet [ch_ren] only seems to add fuel to the fire by softly moaning into my sweaty skin and pressing my back further into the plushness of the couch." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d3_t11 from _call_dlc_14nwy_d3_t11
    else:
        if genitalia == "cooter":
            n "His length is going deeper than ever now, and I throw my head back in ecstatic bliss. And [ch_ren] — ever attentive to my needs — moves one of his hands from the back of my knee and rubs circles against my clit instead." nointeract
        elif genitalia == "bussy":
            n "His length is going deeper than ever now, and I throw my head back in ecstatic bliss. And [ch_ren] — ever attentive to my needs — moves one of his hands from the back of my knee and circles around the tip of my weeping cock." nointeract
        else:
            n "His length is going deeper than ever now, and I throw my head back in ecstatic bliss. And [ch_ren] — ever attentive to my needs — moves one of his hands from the back of my knee and between our bodies to stimulate me down there instead." nointeract
    n "Tears form in the corner of my eyes from all the stimulation and heightened pleasure, but [ch_ren]'s white turtleneck absorbs it all." nointeract
    n "I had half a mind to remove it from my face and glance down at the mess [ch_ren] was creating between our bodies, but I knew better than to do that." nointeract
    n "If he was making me feel this good all because I was listening to his instructions, then who was I to go against him?" nointeract
    r "Are you going to cum, Angel? I want to feel it. Only I get t'feel it." nointeract
    y "Yes! O-Only you!" nointeract
    n "I wasn't sure what I was saying at this point. I was too overwhelmed with how good [ch_ren] felt to care though, so I greedily buck my hips to get more." nointeract
    n "He willingly obliges, leaning down once more to press his mouth against mine in a heated kiss as his free hand roams my body." nointeract
    n "[ch_ren]'s tongue gently prods my lips open, before he deepens the kiss and explores the rest of my body with his fingers." nointeract
    n "Not an inch of my skin was going untouched or unloved by him, and I was loving every second of it." nointeract
    n "One thrust in particular knocks the breath out of me — and from that alone — [ch_ren] was able to tell that I was nearing my end." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d3_t12 from _call_dlc_14nwy_d3_t12
    else:
        if pronoun == "neutral":
            r "That's it. Give it to me. Be good f'me and come on my cock." nointeract
        else:
            r "That's it. Give it to me. Be a good [baby] and come on my cock." nointeract
        r "Y-You own it, don't you? Prove it. Show me who this cock belongs to." nointeract
    n "His words go straight to my core, and I do as he says, wanting nothing more than to please him. And with a few more deep thrusts, [ch_ren] has me tumbling off the edge and into a bottomless pit of pleasure." nointeract
    n "Even though I'm still blindfolded, I see white spots in my vision as my toes curl and my hands grab onto any part of [ch_ren] they can reach." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
        call dlc_14nwy_d3_t13 from _call_dlc_14nwy_d3_t13
    else:
        if genitalia == "cooter":
            n "Something rough and textured brushes against my fingertips, but I pay it no mind as I come all over his length buried deep inside me." nointeract
        elif genitalia == "bussy":
            n "Something rough and textured brushes against my fingertips, but I pay it no mind as I come all over his abdomen." nointeract
        else:
            n "Something rough and textured brushes against my fingertips, but I pay it no mind as I clench around his length and come." nointeract
        n "[ch_ren] seems to have other plans, though, as his hips start to stutter — and before I know it, his strained voice is whimpering into my neck once more as he spills himself inside of me." nointeract
    r "Hah~ A-Angel, I— Ngh!" nointeract
    n "[ch_ren] pulls my body impossibly close to his own and simply holds me there while he tries to catch his breath." nointeract
    if d1_wahooren == True:
        if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
            call dlc_14nwy_d3_t14 from _call_dlc_14nwy_d3_t14
        else:
            n "He doesn't seem to pull out anytime soon though — and much like last time — [ch_ren] remains balls deep inside me as we both melt into the couch." nointeract
    else:
        if persistent.dlc_14nightswithyou_type == "paid" and nsfw_position == "top" or nsfw_position == "temp_top":
            call dlc_14nwy_d3_t15 from _call_dlc_14nwy_d3_t15
        else:
            n "He doesn't seem to detach himself from me though, so we both remain as close as possible while [ch_ren] pulls me closer into the couch." nointeract
    y "…You're heavy." nointeract
    n "My voice comes out hoarse, and I attempt to swat [ch_ren]'s back in hopes of getting him off of me." nointeract
    n "But instead, he languidly rolls to the side and pulls me with him." nointeract
    r "'N you're warm…" nointeract
    n "I would've rolled my eyes at his retort if I wasn't still so dazed. But my eyes were still covered, and I barely had any strength left to move his sweater from my face." nointeract
    n "[ch_ren] seems to pick up on this though (or perhaps he suddenly remembered), because I feel his body shift against mine before his warmth is replaced by my apartment's cold air." nointeract
    n "His fingers trace the side of my jaw before running over my lip, and I resist the urge to playfully lick them." nointeract
    n "All too soon, [ch_ren] moves towards the knot of his turtleneck — but before he removes it, I feel his lips press against mine once more." nointeract
    r "I'm gonna take this off now, Angel, but keep your eyes closed for a little longer." nointeract
    n "I give him a nod, and after a beat of silence, I feel him slowly lift the fabric from my face." nointeract
    n "Even with my eyes still squeezed tight, my surroundings somehow became brighter now that nothing was obscuring it." nointeract
    n "I can hear the sound of fabric moving as [ch_ren] shifts from his spot below me. And before I can protest, his {b}now-clothed{/b} body returns to me once more." nointeract
    r "Kay, you can open 'em now." nointeract
    n "Slowly blinking my eyes open, I let them adjust to the newfound brightness." nointeract
    scene angel_lounge_night
    show peffectp
    show ren smirk z
    with dissolve
    n "But rather than the bleak whiteness of my ceiling, all I can see is [ch_ren]'s adoring gaze boring into mine." nointeract
    n "There's that familiar lovesick expression in his eyes once more, and I can feel his thumb caress my cheek." nointeract
    show ren flushed z at spop, center
    r "H-Hey." nointeract
    y "Hi…" nointeract
    n "His gentle ministrations make me want to fall back asleep for some reason, and before I know it, my eyelids start to grow heavy." nointeract
    n "Doing… {b}this{/b} with [ch_ren] always left me feeling languid and tired (for obvious reasons), and I couldn't stop myself from melting into his embrace." nointeract
    n "Surely he wouldn't mind if I closed my eyes for a few seconds…" nointeract
    scene black
    show peffectp
    with dissolve
    n "As if sensing my fatigue, I hear [ch_ren] let out an endearing chuckle above me before he scoops me into his arms." nointeract
    n "The next thing I know, I'm being lifted from the couch and into the safety of [ch_ren]'s chest instead." nointeract
    n "I already miss the feeling of having him inside me, but the longing soon gets soothed with the comfort of my bedsheets instead." nointeract
    n "…Did [ch_ren] carry me to my bedroom?" nointeract
    n "I can barely keep my eyes open at this point, seemingly happy with reaching for my Haruko plushie to snuggle with instead." nointeract
    n "I can hear [ch_ren] move about my room from somewhere behind me, before I feel the welcoming sensation of a towel clean up the sticky mess between my thighs." nointeract
    n "I let out an appreciative hum at his ministrations — though I was sure it sounded more like a tired sigh — yet [ch_ren] didn't seem to mind." nointeract
    n "Once he's done, I feel him cover my body with the duvet before placing a kiss against the crown of my head." nointeract
    r "…Sleep well, Love." nointeract
    n "His heavy footsteps are the last thing I hear before my consciousness starts to shift from reality and into dreamland." nointeract
    $ d3_wahooren = True
    $ rem_wahoo = True
    if nsfw_position == "temp_top":
        $ nsfw_position = "vers"
    if playtest == True:
        jump day4_wahooscene
    else:
        jump day3_ending_good
label day4_wahooscene:
    scene other_dark
    play music "audio/bgm/Touch Your Heart.ogg" fadein 1 fadeout 1
    play audio "audio/sfx/item.ogg"
    hide ren
    if persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid":
        show CG D4_NSFW1
        $ persistent.cg_d4_nsfw1 = True
    show peffectp
    with dissolve
    n "He looks down at me with wide eyes, but before he can usher out a word, I sink lower on my knees and playfully pull at the waistband of his jeans." nointeract
    n "Or… At least, what I {b}assumed{/b} were his jeans. It was difficult to see anything inside this dark storage closet." nointeract
    r "A-A-A-Angel! You don't… You don't have to—" nointeract
    if d2_wahooren == True:
        y "I'm cashing in that favour now." nointeract
        n "I say with a wink before tasking myself with unbuckling his belt." nointeract
        n "I still haven't forgotten about that night when [ch_ren] went down on me — only to pull me into his arms afterwards and fall asleep without getting off himself. Now, it was his turn." nointeract
    else:
        y "Trust me, [ch_ren], I want to." nointeract
        n "I say with a wink before tasking myself with unbuckling his belt." nointeract
        if rem_wahoo == True:
            n "I won't lie and say that I {b}hadn't{/b} been curious about learning more about what he had going on down there, and especially after our last encounter, I wanted to know just what I was dealing with." nointeract
        else:
            n "I won't lie and say that I {b}hadn't{/b} been curious about learning more about what he had going on down there. Plus, I wanted to know just what I was dealing with." nointeract
    r "[player_fl]-[ch_angel]!" nointeract
    n "[ch_ren]'s voice echoes inside the cramped space, and I can feel his body tense underneath me as I run my hands along his thighs." nointeract
    n "And when I move towards his zipper, I make out the distinct shape of his hard-on straining against the fabric of his jeans." nointeract
    n "Wanting to relieve him, I carefully unzip his pants to free his member." nointeract
    y "Oh…" nointeract
    n "I can't help but let out a surprised sound the moment it springs free — clearly not prepared to be met with something so… big. It's almost daunting having [ch_ren]'s cock so close to my face, and it's {b}then{/b} when reality finally sets in." nointeract
    if rem_wahoo == True:
        n "I had {b}this{/b} inside me? It was almost… unbelievable." nointeract
    else:
        n "…He's {b}huge{/b}. There's absolutely no denying it." nointeract
    if persistent.dlc_14nightswithyou_type == "paid" and first_giving == True:
        call DLC_firsttime_giving from _call_DLC_firsttime_giving
    n "Curiously, I poke at the flared tip to gauge [ch_ren]'s reaction. His reaction is almost immediate with how he practically jumps — letting out a surprised gasp and leaning back onto the shelf the moment I touch him." nointeract
    n "And when I take it a step further and wrap my hand around the head, he all but keens as the air gets sucked out of his lungs as though he was winded." nointeract
    n "Even from down here, I can hear the back of his head thump against one of the shelves as he revels in all the attention I'm giving his member." nointeract
    if hair_length == "bald" or player_hair == "hidden":
        n "And as if to show his gratitude, one of [ch_ren]'s hands moves from the shelf to cup my cheek instead." nointeract
    else:
        n "And as if to show his gratitude, [ch_ren] gently smoothes his hand over my [hair_length] hair." nointeract
    n "His touch is soft and gentle — seemingly a sharp contrast to the throbbing, erect member in front of me right now." nointeract
    if ren_switch >=3:
        n "And even in the darkness, I can make out the faintest blush of pink on his flared tip, the trail of precum dripping down the underside, and the coarse patch of hair covering the base of his cock." nointeract
    else:
        n "And even in the darkness, I can make out the faintest blush of pink on his flared tip, the trail of precum dripping down the underside, and the bare patch of clean-shaven skin at the base of his cock." nointeract
    n "There's also some kind of marking on his left pelvis, but I can barely make out what it is due to the lack of lighting." nointeract
    n "…A tattoo, perhaps? But that was very unlikely given [ch_ren]'s interests and timid demeanour." nointeract
    n "I'm pulled from my thoughts when [ch_ren] lets out a low whine, and it's then that I realise I'd been practically staring at his dick without doing anything. Well… Almost anything." nointeract
    n "I'd been breathing hot air all over his exposed skin, which might explain the faint goosebumps along his thighs and the glassy, dazed-out look in his eyes." nointeract
    n "Seeing him react in such a way… It made me want to see {b}more{/b}." nointeract
    n "I'm so used to seeing [ch_ren] act all shy and bashful around me, so this was honestly a nice — and welcome — change of pace. And so, with determined hands, I reach for his member and try to wrap my fingers around the base — only to fall short." nointeract
    n "But before I have the chance to feel discouraged, one of [ch_ren]'s hands closes around my own and gently coaxes me into stroking his cock; smearing his precum all over the head and down his length." nointeract
    n "The irony of his cock fitting perfectly in his {b}own{/b} hand isn't lost on me, though I find myself getting more and more distracted with the way [ch_ren] uses me to pleasure himself." nointeract
    n "With a steady pace, he guides my hand up and down his shaft and revels in the pure rapture that comes from it, clearly finding bliss in the feeling of my fingers wrapped around his length." nointeract
    n "A heavy sigh falls from his lips the moment I tentatively squeeze the tip a little tighter, before he pulls his hand away and reaches for the shelf once more." nointeract
    r "Keep going… J-Just like that…" nointeract
    n "Feeling bold, I move my face closer and lick a long stripe from the base towards the tip. The taste of salty precum lands on my tongue, and I let out a surprised hum from the intrusion." nointeract
    n "The vibration from my sounds only seems to spur [ch_ren] on as his chest rises and falls with heavy breaths, before one of his hands lifts the hem of his cardigan to see more of my face." nointeract
    n "Wanting to see just how much more of a reaction I can get out of him, I wrap my lips around the flushed tip and give it an experimental suck." nointeract
    n "At that, the faint shadow of [ch_ren]'s adam's apple move as he swallows {b}hard{/b}, and I can tell by the way his fingers curl and flex that he wants to reach out and touch me as well." nointeract
    n "Heh, how cute." nointeract
    n "When I add my tongue to the mix and swirl it around the head, [ch_ren] acts as though his soul practically left his body. He hunches over my form with a low groan, and his eyes whisper for me to continue before he squeezes them shut." nointeract
    r "Please…" nointeract
    n "His voice comes out hoarse — and had I been paying more attention — I would've said it sounded like a whimper." nointeract
    n "All of [ch_ren]'s reactions are bordering on being addictive at this point, and I find myself wanting to hear {b}more{/b} and see what other kinds of sounds I could pull from him." nointeract
    n "It quickly becomes a challenge to see if I can get him to moan {b}my{/b} name instead, and I slowly start to stop caring about someone walking in on us in such a compromising position — Teo and [ch_elanor] be damned." nointeract
    n "All I want to concern myself with are [ch_ren]'s moans, the shape of his cock, and the way it tastes while it touches the back of my throat." nointeract
    n "With a newfound resolve, I try to take him as deep as I can while my free hand strokes what my mouth can't reach." nointeract
    n "And by the looks of it, [ch_ren] seems to be enjoying every second with the way his entire body shakes from above me. Not wanting to disappoint, I continue my ministrations with an eager smile." nointeract
    n "Giving his cock {b}even more{/b} attention now, I lick a wet stripe from the veiny underside to the tip before taking most of it into my mouth once more." nointeract
    n "But instead of another breathy moan or twitch of his thigh like I was expecting, [ch_ren]'s gravelly voice breaks the silence." nointeract
    r "Touch yourself too, [ch_angel]." nointeract
    n "Clearly not expecting him to say anything, my mind barely registers his words — so I look up through my lashes to (vaguely) see the pink-haired man peering down at me with an unreadable look." nointeract
    if genitalia == "cooter":
        r "Your mouth is more than enough f'me. Use your hands to play with your clit." nointeract
    elif genitalia == "bussy":
        r "I want you to stroke your own cock too. Your mouth is more than enough f'me." nointeract
    else:
        r "Your mouth is more than enough f'me. Use your hands to touch yourself." nointeract
    n "Oh. Was that what he had in mind?" nointeract
    n "I won't lie; much like his moans, [ch_ren]'s lewd words also had an effect on me — it was evident with the way it went straight to my core and left me dripping in arousal — but I wanted to focus all of my attention on {b}him{/b} this time." nointeract
    n "He's done nothing but show me so much kindness and patience over the past few days, and it was high time I showed a bit more gratitude." nointeract
    n "So, with a slight smile, I shake my head and go back to lavishing his length with soft kitten licks." nointeract
    y "Nuh-uh. It's all about {i}you{/i} today. Tell me what you need." nointeract
    n "He lets out another low whine at my words — but before he can respond, I quickly cut him off." nointeract
    y "And don't say you want me to touch myself. I wanna show my appreciation towards {i}you{/i}, [ch_ren]." nointeract
    r "…M-Me? {i}Ngh!{/i}" nointeract
    n "It was like I read his mind or something, because he instantly clams up and tries to find something else to say instead. But as I continue to languidly stroke his length with my hands, [ch_ren] seems less and less inclined to respond." nointeract
    if hair_texture == "bald" or hair_texture == "braided" or player_hair == "hidden":
        n "Instead, he simply slumps against the shelf once more as his hands run along my cheeks and jaw in a blissed-out manner." nointeract
    else:
        n "Instead, he simply slumps against the shelf once more as his hands card through my hair in a blissed-out manner." nointeract
    n "Deciding to push a little further, I grip the base of his cock in an attempt to silently draw his attention once more. And it seems to work, given how [ch_ren] lets out a soft moan from the friction and glances down at me with half-lidded eyes." nointeract
    y "…What do {i}you{/i} need, baby?" nointeract
    n "I'm not exactly sure where the affectionate name came from or why I said it, but it seems to do the trick as [ch_ren] practically throws his head back and tenderly cups my jaw." nointeract
    r "Your… Your mouth. I want your mouth on me again. Please?" nointeract
    if genitalia == "cooter":
        r "I'll do whatever you want after… I'll eat you out again if you want! Or press you against the wall 'n fuck you nice and hard—" nointeract
    elif genitalia == "bussy":
        r "I'll do whatever you want after… You can even fuck {i}me{/i} this time— I'll… I'll be good for you!" nointeract
    else:
        r "I'll do anything you want afterwards… I don't care if someone walks in on us right now—" nointeract
    r "Please… I just need to feel your mouth again, and—" nointeract
    n "Without missing a beat, I set back to work. Taking the flushed tip into my mouth once more, I wrap my lips around it and gently suck." nointeract
    n "{b}More{/b} of [ch_ren]'s salty precum lands on my tongue, and I eagerly lap up everything he has to offer me with an impish smile." nointeract
    n "I'm rewarded with more of his addictive sounds, and the moment I run my tongue along one of the more prominent veins on his cock, it was almost as if I activated a switch." nointeract
    n "All of a sudden, [ch_ren] seems all the more eager and chatty now — given how he slightly starts to buck his hips, moan my name, and lose himself in all the pleasure I was giving him." nointeract
    r "Could stay like this forever— Feels {i}soo{/i} good." nointeract
    r "Fuck— The next time I look at those tempting lips of yours, all I'll think about is this moment." nointeract
    r "You, on your knees, with my cock shoved halfway down your throat…" nointeract
    r "Haah~ The thought alone is so… so— {i}Shit{/i}." nointeract
    n "His words do nothing but go straight to my core, and I eagerly pick up the pace in an attempt to hear more of them." nointeract
    n "I hardly ever see this side of [ch_ren], and now that he's given me a taste, I only want more." nointeract
    if d2_wahooren == True:
        if genitalia == "bussy":
            n "Was this how [ch_ren] felt when he was sucking {b}my{/b} cock?" nointeract
        elif genitalia == "cooter":
            n "Was this how [ch_ren] felt when his head was buried between my thighs?" nointeract
        else:
            n "Was this how [ch_ren] felt when he went down on me all those nights ago?" nointeract
    else:
        pass
    n "Without wasting another second, I rest one of my hands on the base of his length once more while the other runs along any exposed skin it can find. His stomach, hips, thighs — anything to make him a shaking, blushing mess above me." nointeract
    n "This time, I try to take as much of [ch_ren]'s cock into my velvety mouth as I can, though it proved difficult given his sheer size." nointeract
    n "It's becoming increasingly more difficult to ignore the dull ache in my jaw from keeping my mouth open for so long, so I instead focus on how [ch_ren] chants my name under his breath over and over again like a mantra." nointeract
    r "[player_fl]-[ch_angel]… [ch_angel]— You're making me feel so— {i}Ah,{/i} [ch_angel]!" nointeract
    n "I can't see his face anymore with how it's thrown back in pure ecstasy, so I settle for watching the sharp rise and fall of his chest instead." nointeract
    y "You look beautiful like this, [ch_ren]." nointeract
    r "…Wh-Wha—? {i}Hng!{/i}" nointeract
    n "At that, he immediately covers his face with one of his sleeves — no doubt to hide his reddening cheeks — as he turns his head away from me." nointeract
    n "…Even with his length out on full display in front of me, calling him beautiful was what made him flustered?" nointeract
    n "Admittedly, I {b}was{/b} having way too much fun teasing [ch_ren] in order to see all his different sounds and reactions, but I figured it was about time to let him have his release." nointeract
    n "Though he must've been getting close already, seeing as he was slowly starting to topple over and his words were beginning to slur." nointeract
    n "At this point, I can barely make out what he's saying outside of my own name and a few occasional moans." nointeract
    if hair_texture == "bald" or hair_texture == "braided":
        n "One of his hands soon slips further down until it reaches my neck, while the other clutches the shelf in a vice-like grip." nointeract
    else:
        n "One of his hands soon finds its way into my hair, while the other clutches the shelf in a vice-like grip." nointeract
    n "I can make out the faintest hint of sweat on his brows — though it disappears from view once [ch_ren] arches his spine and lets out a breathy groan from a particularly hard suck." nointeract
    r "You feel so good… Keep that up 'n I'll cum soon… A-Angel, I—" nointeract
    r "Where do I— Where… Where do you want it?" nointeract
    n "As if to answer, I wrap my lips tighter around his cock and give his thigh a soft squeeze." nointeract
    r "{i}Fuck.{/i}" nointeract
    n "Without any further warning, [ch_ren] doubles over as the feeling of something warm enters my mouth and coats my tongue in his sticky essence." nointeract
    if persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid":
        hide CG D4_NSFW1 with dissolve
    n "Not knowing what to do or whether I should spit out his cum somewhere, I end up swallowing it all with a faint moan of my own." nointeract
    n "The taste is slightly bitter, but I don't seem to mind it that much — especially when I get to see [ch_ren]'s blissed-out expression as he limply slides down to join me on the floor." nointeract
    r "Th-Th… Thank… You…" nointeract
    r "Felt so… s'good… Never came that hard before…" nointeract
    n "His eyes were closed and he was panting like he had just run a marathon, though there was still something so innocent and ethereal about him." nointeract
    n "…How could he look so pretty after shooting his load inside my mouth?" nointeract
    n "Before I have any time to dwell on it, the pink-haired man lets out another winded huff and tears me from my thoughts." nointeract
    n "Once his high finally dies down, [ch_ren] cracks open an eye — no doubt to look for me — as he lethargically extends an arm to pull me closer to his side." nointeract
    n "In all honesty, I find it rather endearing to know how much of a cuddler he was after experiencing… {b}that{/b}. It was almost like I got my normal, shy [ch_ren] back." nointeract
    n "Wanting to indulge him for the moment, I meet [ch_ren] halfway and eagerly lean into his touch — only for him to scoot closer and cup my face once more." nointeract
    n "There's a look of pure, unbridled affection in his eyes as he tenderly brushes his thumb across my cheekbone — but it quickly gets replaced with something more mischievous once his fingers start to dip lower." nointeract
    n "[ch_ren]'s thumb pushes and prods at my lower lip, and I send him a questioning glance to gauge his intentions." nointeract
    r "…Let me see? Please?" nointeract
    n "Let him… See?" nointeract
    extend " {b}Oh.{/b}" nointeract
    n "When I open my mouth, [ch_ren] immediately takes notice of the fact that I swallowed {b}all{/b} of his cum and practically starts salivating at the sight. There's that same lovestruck look in his eyes, and I can't help but feed into it." nointeract
    n "But instead of taking things further like I initially expected, [ch_ren] takes me by surprise by leaning in to press a fervent kiss against my lips." nointeract
    y "Mmph!" nointeract
    n "I let out a faint hum as he guides me into a slow, ardent kiss — before he pulls away with dilated pupils and a dazed expression on his features." nointeract
    n "There's an audible \"thump!\" as [ch_ren] leans against the shelf for the umpteenth time, and I can't resist the urge to perch myself in his lap and press him for answers." nointeract
    y "So? How was it?" nointeract
    r "Y-You must seriously be an angel… 'Swear you just took me to heaven." nointeract
    r "Here, lemme make {i}you{/i} feel good now. I can—" nointeract
    n "I feel [ch_ren]'s hands travel down my sides and reach for my own unbuttoned bottoms, but I gently grab them and pull away." nointeract
    y "I-It's okay. This was more than enough for me." nointeract
    y "Besides, I think we should probably get out of here now. I'm surprised we've been in here for this long without getting interrupted." nointeract
    r "Uh-huh…" nointeract
    n "Glancing up at [ch_ren], I notice how he {b}still{/b} seems dazed and boneless against the shelf as his eyes solely focus on my mouth." nointeract
    n "Holding back my laughter, I begin to tidy up my appearance and help [ch_ren] with his as well." nointeract
    $ d4_wahooren = True
    $ rem_yippee = True
    if playtest == True:
        jump day5_wahooscene
    else:
        jump day4_leavingstoreroom
label day5_wahooscene:
    scene black
    play music "audio/bgm/Touch Your Heart.ogg" fadein 1 fadeout 1
    if persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid":
        show CG D5_NSFW1
        $ persistent.cg_d5_nsfw1 = True
    show peffectp
    with Fade(1.0, 2.0, 1.0)
    r "…Think I've got somethin' in mind." nointeract
    n "His voice startles me, and just as I'm about to respond, the thrilling sensation of [ch_ren]'s hands gliding down my sides halts my train of thought." nointeract
    n "His touch alone is both addictive and electrifying, and the selfish parts of my mind keep screaming out for more." nointeract
    n "And just like I had attempted to do earlier, I feel [ch_ren]'s fingers inch closer and closer towards my core before they stop right at the opening of my bottoms — almost as if to tease me." nointeract
    n "I can feel him lean {b}even closer{/b} now… Until all my senses are taken over by [ch_ren]." nointeract
    r "Is this okay?" nointeract
    n "Almost enthusiastically, I give him my consent by eagerly nodding my head — all while feeling my face heat up as I shamelessly guide his hand closer to where I need him the most." nointeract
    n "And without missing a beat, [ch_ren] responds with just as much enthusiasm as me; deftly undoing the constraints of my bottoms before slipping his hand into my underwear." nointeract
    if genitalia == "cooter":
        n "I have to stifle a moan once I feel the foreign sensation of his fingers running across my folds, and the next thing I know, he's pushing one of them inside and curling inwards." nointeract
        n "Another wave of pleasure wracks through me, and I cling onto [ch_ren]'s upper arm to stop myself from toppling over." nointeract
    elif genitalia == "bussy":
        n "I have to stifle a moan once I feel the foreign sensation of his fingers brushing against my cock, and the next thing I know, he's grabbing it with one hand and giving the tip a small squeeze." nointeract
        n "The other hand swipes some of my precum to use as lube, before he uses a finger to push it inside of my hole." nointeract
        n "Another wave of pleasure wracks through me, and I cling onto [ch_ren]'s upper arm to stop myself from toppling over." nointeract
    else:
        n "I have to stifle a moan once I feel the foreign sensation of his finger running across my hole and the next thing I know, he's pushing it inside and curling inwards." nointeract
        n "Another wave of pleasure wracks through me, and I cling onto [ch_ren]'s upper arm to stop myself from toppling over." nointeract
    r "Feeling good? You're practically leaking all over me, [ch_angel]." nointeract
    r "'N I can feel the way you keep clenching down on my finger. Is that your body asking for more?" nointeract
    n "At that, [ch_ren] inserts {b}yet another{/b} long finger into me. Then another, before he starts pumping them in and out of me at a slow and torturous pace." nointeract
    r "Heh, so greedy." nointeract
    n "There's an unmistakable tinge of mirth in [ch_ren]'s voice, indicating that he's clearly having the time of his life teasing me like this." nointeract
    r "Oh? Don't tell me you're still unsatisfied, even with three fingers inside of you?" nointeract
    r "Guess I'll have t'do something about this, huh?" nointeract
    r "You need something… {i}bigger{/i} to fill you up, right?" nointeract
    n "Before I can respond, [ch_ren] cuts me off by lifting my hips to pull my bottoms all the way down." nointeract
    n "And had I not been so immersed in the way he was practically fingering me without a care in the world, I'm sure I would've felt even an inch of embarrassment for being so… exposed." nointeract
    n "Perhaps it's why I'm so thankful for the privacy the blanket around us provides — or for the fact that it easily muffles all the lewd sounds [ch_ren] was pulling from me." nointeract
    n "But still… I can't seem to comprehend how [ch_moth] still hasn't picked up on what we're doing yet." nointeract
    n "Not that I have much time to dwell on that thought, however, as I soon feel the tip of [ch_ren]'s cock prodding against my [hole]." nointeract
    n "And yet… even after a heartbeat or two, he doesn't seem to go any further than that." nointeract
    n "Before I can twist around to send [ch_ren] a questioning look, I feel a puff of warm air against the top of my head as he rests both of his hands atop my thighs." nointeract
    r "Only if you want to, [ch_angel]." nointeract
    r "If not… Just say the word, and we can stop." nointeract
    n "It's difficult to process [ch_ren]'s words with his hard length pressed against me in such an intimidating manner, but I try my best to ignore it and make sense of the words he's whispering to me." nointeract
    y "…But what about you? I wouldn't want you to—" nointeract
    r "Don't worry about me. This is all about you and what {i}you{/i} want right now." nointeract
    r "Besides, I'm already more than satisfied with holding you in my arms like this." nointeract
    r "As long as you're comfortable, I'm comfortable. We'll go as far as you want to go." nointeract
    n "[ch_ren]'s genuine concern and consideration for me pulls at my heartstrings and fills me with an all-too-familiar warmth. And so, with a newfound resolve, I give [ch_ren] my answer by rolling my hips and leaning further into his embrace." nointeract
    n "He seems to catch on quickly with the way his fingers {b}immediately{/b} inch further up my thighs, but I can tell that there's still the slightest hint of hesitation that's holding him back." nointeract
    r "…You sure?" nointeract
    y "Positive. I wanna do this with you, [ch_ren]." nointeract
    n "He lets out a breathy chuckle at my words before his head dips into the space between my shoulder and neck. I can feel him inhale slightly before his lips start to ghost along the sensitive patch of skin below my earlobe." nointeract
    $ temp_bottom = True
    call DLC_firsttime_menu from _call_DLC_firsttime_menu_2
    $ temp_bottom = False
    if rem_wahoo == True:
        y "Ah!" nointeract
        r "Shh." nointeract
        n "As if to soothe me, [ch_ren] leans forward and places a gentle kiss against my cheek." nointeract
        n "But the chaste action seems a stark contrast to what he's currently doing underneath the blanket — which was to guide my hips lower and lower until I'm sinking down on his length and taking {b}every{/b} agonising inch of it inside me." nointeract
        n "There's an all too familiar burning sensation from the sheer size of him stretching out my walls, but I ignore it in favour of all the pleasure I feel from being so… full." nointeract
    else:
        n "At that, [ch_ren] carefully guides my hips lower and lower until I'm sinking down on his length and taking {b}every{/b} agonising inch of it inside me." nointeract
        n "There's an unfamiliar burning sensation from the sheer size of him stretching out my walls, but I ignore it in favour of all the pleasure I feel from being so… full." nointeract
        r "Y-You feel better than anything I've ever imagined…" nointeract
        r "Haa~ I can't believe we're actually doing this… I thought it would've happeed somewhere a bit more {i}private{/i}, but…" nointeract
        r "Well, I'm not going to complain. You feel {i}amazing{/i}, Angel. I-I'm glad my first time is with you." nointeract
    n "It's almost like a lifetime passes before [ch_ren] is fully sheathed inside of me, but just as I try to move, his hands hold me down and prevent me from squirming out of his reach." nointeract
    n "What was he…? Why didn't [ch_ren] want me to move? Was he still feeling sensitive?" nointeract
    if rem_wahoo == True:
        r "Uh-uh. You're not allowed to move yet. Consider this your punishment for all the teasing you did earlier." nointeract
        y "[ch_ren], you can't be serious—" nointeract
        r "Never been more serious in my entire life." nointeract
        r "In fact, maybe I should just stay like this for a little while longer. You wouldn't mind, right?" nointeract
    else:
        r "As much as I want to consider this your punishment for all the teasing you did earlier…" nointeract
        r "This is still our first time together, and… I-I don't want to move too fast and hurt you." nointeract
        y "[ch_ren], it doesn't hurt that bad—" nointeract
        r "Then this is me making sure you're fully accustomed to my size before we go any further." nointeract
        r "We don't have to rush this." nointeract
        r "Besides, I kind of want to keep you wrapped around me like this for a little while longer. You wouldn't mind, right?" nointeract
    n "I {b}want{/b} to move, yet [ch_ren]'s hands remain firmly around my waist as he casually bucks up into me. All I'm able to do is grind against his dick while he lavishes my neck with endless kisses and love bites." nointeract
    n "His hand doesn't stay idle for long either, as it eventually travels down my stomach to play with my [parts] and make me see stars." nointeract
    n "It soon reaches a point where I have to stifle every gasp and moan, lest I alert [ch_moth] and clue them into what we're currently doing." nointeract
    n "But I can't seem to feel even an {b}ounce{/b} of embarrassment when [ch_ren] is languidly rolling his hips against mine and sending wave after wave of pleasure through my entire body." nointeract
    n "I've never felt so full in my life, and somehow, having [ch_ren] be this close to me felt oddly… intimate." nointeract
    n "His chest is practically {b}glued{/b} to my backside as he leans over my shoulder to observe his ministrations, and having his free hand entwined with my own only makes the moment feel all the more tender." nointeract
    n "Without thinking — or perhaps it's because I'm too far gone in the hazy pleasure of it all — I let my head lull to the side and rest against his shoulder with a soft thump." nointeract
    if genitalia == "cooter":
        n "[ch_ren] wastes no time in turning his attention to the exposed shell of my ear once more, while his other hand goes back to pleasuring my [hole]." nointeract
        n "His fingers feel so good, and I can't help but let out small moans every time he brushes against that sensitive spot inside me. At that, [ch_ren] {b}immediately{/b} perks up with a mischievous glint in his eyes." nointeract
    elif genitalia == "bussy":
        n "[ch_ren] wastes no time in turning his attention to the exposed shell of my ear once more while his other hand goes back to fisting my [sex]." nointeract
        n "His ministrations feel so good, and I can't help but let out small moans every time his thumb brushes against the tip. At that, [ch_ren] {b}immediately{/b} perks up with a mischievous glint in his eyes." nointeract
    else:
        n "[ch_ren] wastes no time in turning his attention to the exposed shell of my ear once more while his other hand goes back to pleasuring my [hole]." nointeract
        n "His fingers feel so good, and I can't help but let out small moans every time he brushes against that sensitive spot inside me. At that, [ch_ren] {b}immediately{/b} perks up with a mischievous glint in his eyes." nointeract
    r "Heh… I wonder if I can make you do that again. Though… Your friend would probably take notice, huh?" nointeract
    r "I wouldn't mind that, actually." nointeract
    r " There's something so… {i}thrilling{/i} about them catching us like this. You, in my lap while you cockwarm me." nointeract
    r "At least then they'd understand that {i}I'm{/i} the only one who can make you feel this good." nointeract
    n "…It almost seems like [ch_ren] is rambling to {b}himself{/b} instead of me." nointeract
    r "Must be gettin' hard for you to focus now, huh? Good, 'cause that's exactly what you do to me." nointeract
    r "Sometimes… Sometimes, I'd watch you while you worked at the library." nointeract
    r "It's always so hard f'me to focus on reading when you're constantly moving about. Y'know, bending down to pick up something or stretching upwards t'place a book on the shelf…" nointeract
    r "Sometimes I'd catch y'scent whenever you'd walk past the aisle I'm in, and then I'd have to resort to relieving myself in the—" nointeract
    r "Hey, are you listening to me?" nointeract
    if genitalia == "bussy":
        n "It's extremely difficult to listen to {b}anything{/b} when all I can focus on is the way [ch_ren]'s hand expertly pumps my [sex] while his cock remains deep inside me." nointeract
    else:
        n "It's extremely difficult to listen to {b}anything{/b} when all I can focus on is the way [ch_ren]'s thick cock feels as it remains buried deep inside me." nointeract
    r "Nothin' to say? Feels {i}that{/i} good, huh? Want more?" nointeract
    y "P-Please." nointeract
    n "That alone seems to do the trick, as [ch_ren] moves one of his hands to my [bust] to play with a nipple." nointeract
    n "I can't help but keen out as I feel him start to move his hips once more, before his soft lips return to the juncture between my shoulder and neck to plant {b}even more{/b} open-mouth kisses." nointeract
    n "Hearing him groan so close to my ear sends goosebumps all over my body, and the brazen part of me silently hopes that he'd do it again." nointeract
    r "Think you've been patient long enough. Time for your reward." nointeract
    y "Hnng!" nointeract
    n "The next thing I know, [ch_ren] starts moving my hips {b}for real{/b} this time — almost like he was using me as his own personal fleshlight — before he bites down on my neck with a moan." nointeract
    n "The only things I can focus on are the way his cock pumps in and out of me, the feeling of his lips against my skin, and the lewd squelching sounds being muffled by the blanket." nointeract
    n "And perhaps it's from the thrill of getting caught, but for some reason, I feel a rush of adrenaline course through me." nointeract
    if rem_wahoo == True:
        n "It's so unlike anything else I've felt before — especially compared to the last time I'd gotten intimate with [ch_ren]. I mean, the very first time we'd done something like this, it was in the privacy of my own room. But this? This was completely different." nointeract
        n "And on a completely different level." nointeract
    else:
        n "This euphoric feeling [ch_ren] is currently giving me is so unlike anything else I've experienced before. And on a completely different level." nointeract
    n "[ch_ren] must be on a similar wavelength as me, as every so often, I catch him sneaking glances in [ch_moth]'s direction with a familiar glint in his eyes." nointeract
    n "Was he making sure we wouldn't get caught, or…" nointeract
    n "Did he {b}want{/b} [ch_moth] to turn around and catch us in the act?" nointeract
    n "I wonder if—" nointeract
    r "Think they'd want photos of Haruko doing somethin' indecent like this?" nointeract
    r "I know I would. Seems fair, don't you think? I mean, you have all those photos of {i}me{/i} at the beach…" nointeract
    r "Shouldn't I have photos of {i}you{/i} like this? Spread out and bouncing on my cock like your life depends on it?" nointeract
    r "Hehe~ just kidding." nointeract
    r "Besides… Photos can't compare to having the real deal right in front of me." nointeract
    r "Bein' able to fuck you like this {i}definitely{/i} beats doing it with my hand." nointeract
    r "It's the same for you, right? D'you like doing it with me the most? You know you can come to me anytime. I'd never deny you." nointeract
    n "As he says that, the tip of [ch_ren]'s length brushes against that sensitive spot inside of me, which has me throwing my head back as I keen out." nointeract
    n "My hips shamelessly move out of their own volition at this point, and I meet every single one of [ch_ren]'s thrusts as he bucks up into me with reckless abandon. Soon enough, I can feel myself slowly inching closer and closer to my peak." nointeract
    if persistent.dlc_14nightswithyou == True and persistent.dlc_14nightswithyou_type == "paid":
        hide CG D5_NSFW1 with dissolve
    n "My eyes squeeze shut the moment [ch_ren] pulls me down {b}fully{/b} onto his cock, and I begin to see stars the moment his thighs are flush against my own as he ruts his length inside of me." nointeract
    n "The next thing I know, the warmth of his seed spills inside of me as I find my own release shortly after." nointeract
    n "With one final, satisfied sigh, my body languidly slumps against [ch_ren]'s embrace as I hear him chuckle from somewhere above me." nointeract
    n "My eyes feel droopy all of a sudden, and I end up drifting off in [ch_ren]'s arms." nointeract
    $ d5_wahooren = True
    $ rem_wahoo = True
    if playtest == True:
        $ renpy.full_restart()
        jump main_menu_screen
    else:
        jump day5_renevening
return