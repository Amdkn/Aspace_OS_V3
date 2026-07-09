---
source: youtube-transcript-api A3 (Saru LD02 watch history)
date: 2026-06-21
type: transcript
domain: L2_Business_OS
video_id: RChO5deJ_fE
topic: mark_kashef_claudex
description: "You Can Make Claude + Codex Plan Together â€” Mark Kashef"
tags: [#youtube, #transcript, #video_RChO5deJ_fE, #mark_kashef_claudex]
---

# Transcript brut — Mark Kashef /Claudex (RChO5deJ_fE)

## Metadata
- **Title** : You Can Make Claude + Codex Plan Together. Here's How.
- **Author** : Mark Kashef
- **Channel** : UCHkzp52CldSPZqU5T49mOnA
- **URL** : https://youtu.be/RChO5deJ_fE
- **Fetched** : 2026-06-21 via `mcp__transcript-api__get_youtube_transcript`
- **Format** : text
- **Send metadata** : true

## Transcript (verbatim)

[0.08s] Everyone loves building way more than
[2.08s] planning, but the truth is the more time
[4.0s] you spend specking and planning, the
[6.24s] less time you spend going back and forth
[8.559s] with something like Cloud Code. And I
[10.24s] don't use things like the / Ultra plan
[12.639s] because it becomes very/ ultra
[14.639s] expensive. But if you do want to bring
[16.16s] your Robin to your Claude Code Batman,
[18.48s] then you can use what I'll show you in
[20.08s] this video, which is called /Claudeex.
[22.56s] And this is basically a loop where you
[24.32s] can either start with a cloud code plan
[26.24s] that you audit in multiple rounds with
[28.08s] codecs or you can have them
[29.439s] interchangeably work together. So in
[31.279s] this video I'm going to walk you through
[32.559s] how it works and by the end I'm going to
[34.719s] actually give it to you. So if that
[36.399s] sounds like a plan then let's dive in.
[38.079s] In my last video I walked you through
[39.68s] how to use the native OpenAI plugin to
[42.559s] do something like /codeex and use any
[45.28s] one of these various commands here. And
[47.2s] while this is awesome, it doesn't give
[48.8s] you the ability to automate a workflow
[50.96s] where you can actually put this dynamic
[52.559s] duo together and have them plan in
[54.559s] unison. You're still technically driving
[56.48s] every single move. So the whole point
[57.92s] of/cloudex is this is meant to change
[60.239s] all of that. All you have to do is do
[62.559s] plan and then we do a space here. You
[65.36s] can tell it how many rounds of back and
[67.2s] forth you want to go through. Now, in
[68.799s] this case, I have it start with a clawed
[70.64s] codebased plan, and then I have Codeex
[73.2s] go over the plan three different times.
[75.68s] Depending on what it is that you're
[76.96s] trying to put together, you could make
[78.32s] this one round, two rounds, or if you
[80.4s] have the token budget, you can go for
[82.0s] five rounds. So, you could theoretically
[83.6s] do dash-3 for three rounds and say
[86.08s] something like build me a clone of to-d
[88.96s] doist, the to-do list app. And then it
[91.36s] would go together and put together a
[93.04s] plan from Claude through a plan.mmd
[95.2s] file. Then it would have Codeex audit
[97.36s] it, look for flaws, patch the flaws,
[99.6s] then go back to Claude, see if it's
[101.6s] revised it, and then go back to Codeex
[103.52s] and look for any additional flaws it
[105.439s] didn't get in its first pass. So this is
[107.52s] the 50,000 ft view of how it works. The
[110.0s] first thing that happens is that Claude
[111.6s] drafts a plan, then Codeex reviews said
[113.92s] plan and then comes up with its finding
[116.079s] and where it thinks it could be better.
[117.68s] Then Claude reads the findings and
[119.36s] integrates it into its original plan.
[121.2s] And then finally, Claudex asks, did we
[123.759s] reach the desired number of rounds to go
[126.079s] through revision? On average from
[127.6s] testing it so far, it seems that two to
[129.52s] three rounds is sufficient to get the
[131.36s] 8020 of the planning bugs. So, if you
[133.76s] were to take an X-ray machine, this is
[135.52s] what /Cloudex would look like behind the
[137.76s] scenes. Step one is where you'd add what
[139.76s] it is that you're trying to build or
[141.36s] whatever you're trying to add on to what
[142.959s] already exists. And after you send that
[144.72s] off, this will initiate a script. It's
[146.64s] called a bash script. This will
[148.239s] essentially execute the initialization
[150.319s] of the loop. So if you put no rounds, it
[152.879s] will default to three different rounds.
[154.48s] And if you have a prompt, it will take
[156.4s] said prompt and then it will add it to
[158.08s] what's called a YAML file. This
[160.08s] essentially like a notepad or a sticky
[161.92s] note that keeps track of how many rounds
[164.239s] this will go for, what is the main
[165.84s] prompt we're optimizing for, and what is
[167.599s] the end state we're going for. And once
[169.2s] we have the prompt, this will kick off
[170.72s] step number two, which is essentially
[172.879s] initializing this script. It's called a
[174.72s] bash script. What it's doing behind the
[176.4s] scenes is it's taking the prompt and
[178.16s] then putting together a file. This file
[180.64s] is called a YAML file. This will specify
[183.44s] what it is that we're building or doing,
[185.36s] how many rounds we've set, and what
[187.599s] round are we currently in. Now, step
[189.28s] four is the magic piece that lets us all
[191.36s] work together. So, Cloud Code has these
[193.36s] things built in called hooks. One of
[195.519s] them is called a stop hook. This
[197.28s] essentially forces claude code to stop
[199.519s] and take a look at the state file to
[201.519s] make sure it's on track and it knows
[203.28s] exactly where we are and how many more
[205.44s] rounds it needs to go and invoke the
[207.519s] codeex plugin. So you can think of this
[209.44s] as a bouncer that tells claude code
[211.519s] either okay you can leave or wait we
[214.319s] have to do something else. If it decides
[215.84s] we have to do something else this is
[217.2s] where it's going to invoke the codeex
[218.879s] command line interface to go and
[220.56s] actually get codeex's opinion on your
[222.56s] existing plan. And then last but not
[224.08s] least you get all the findings from
[225.519s] codeex. This is then fed to cloud code
[227.92s] to internalize and see which parts of
[230.08s] its existing plan should it edit. Now,
[232.239s] I've only shown you the plan function,
[234.08s] but I also have a few others. So, I'm
[235.76s] going to walk you through exactly what
[237.28s] these do in case you want to take my
[239.28s] code, edit it to your own
[240.48s] specifications, and know exactly how
[242.159s] they work. So, when you do slash review,
[243.92s] codeex will just audit what you have so
[246.0s] far and give you written commentary
[247.84s] about it. It won't auto change your
[249.76s] plan. It won't edit anything, and it
[251.599s] won't tell Claude Code to do anything
[253.599s] other than provide an asset. The cancel
[255.92s] command acts as an emergency break where
[258.239s] if you see it steering off of course or
[260.639s] you feel like your initial plan wasn't
[262.639s] good enough or wasn't deserving of the
[264.479s] token burn it was about to go through
[266.16s] then you can just gracefully stop it and
[268.0s] restart. And then you have / rollback
[270.56s] which is meant to be the equivalent of a
[272.32s] nuclear cleanup. So if you've started a
[274.24s] plan and you've canceled it and you feel
[276.32s] like you want to wipe the slate clean
[277.84s] completely you can use this function
[279.68s] that's way more involved than the
[281.44s] emergency break. So the TLDDR is that
[283.68s] the two ways you can use Claudeex is
[285.36s] either to create a brand new project
[286.88s] from scratch or you can grill an
[289.199s] existing plan. And one additional thing
[290.96s] that I've done that I haven't shown you
[292.32s] in the demo is I also injected an ask
[294.56s] user input tool. This is essentially the
[296.639s] very mechanism that claude code can
[298.8s] provoke a series of multiple choice
[300.479s] questions. So if you put a very vague
[302.8s] plan, it will ask you for more feedback
[304.8s] before it even goes into this loop. And
[306.8s] by the way, I'm holding myself back
[308.4s] purposefully to not go full nerd mode to
[310.639s] make this as accessible as possible. But
[312.479s] if you want to actually learn exactly
[314.0s] how I built this step by step and learn
[316.56s] all of the plumbing involved to do
[318.32s] something like this on your own, I have
[319.759s] a dedicated brand new module that I've
[321.52s] added to our living course all about how
[323.919s] to use this and how to build on it. So,
[325.44s] if that interests you, then check it
[326.639s] out. Now, this is what it looks like in
[328.24s] the wild. Imagine you're trying to build
[330.08s] a special web page where it's not just a
[332.08s] web page. It's a web page that can also
[334.24s] track what everyone's doing, record
[336.32s] sessions on that web page of where
[338.16s] people are clicking, where they're
[339.44s] spending their most time. And you didn't
[341.039s] want to use a third-party service and
[342.96s] pay for that as well. So, this is a more
[345.039s] tricky task that I wrote a scope for and
[348.16s] architecture for. Let's be honest, I had
[350.16s] AI write it for me. And it walks through
[352.08s] the diagram of exactly what the scope of
[354.639s] this entire build is. Now, what it is is
[357.199s] less important. I more want to show you
[359.039s] how you would use this. So you do
[360.8s] /claudex plan in this case you don't
[362.96s] have to specify rounds three it does it
[364.8s] by default and I would just say plan the
[366.8s] pulse page build using and then I would
[369.36s] tag the files at scope MD and then at
[372.96s] architecture MD. This will automatically
[375.28s] force claude code to read these before
[377.68s] it does anything else. And then you can
[379.199s] see the flow from here. It will write
[380.72s] the plan and this is the claude code
[382.479s] version of that plan. And then as you
[384.24s] scroll down, you will see it ran three
[386.4s] different stop hooks and then it stops
[388.16s] it exactly where it needs to. And then
[390.319s] as you scroll through, you'll see that
[392.0s] the plan is updating. Every time you see
[394.08s] a red, that is a deletion from the plan.
[396.4s] Every time you see a green, that is an
[397.919s] addition from the plan. And that
[399.68s] addition is provoked by something like
[401.44s] codeex. So, as you go through, this will
[403.44s] go down endlessly because it goes very
[406.4s] deep in terms of checking every single
[408.56s] part of the plan, double-checking if
[410.4s] it's thoughtful enough and if it's
[411.919s] thought of the second order and the
[413.28s] third order consequences. And after it
[415.199s] takes its 15 to 20 minutes to go back
[417.12s] and forth, we get to something like this
[419.039s] where it says, "Round three, hard stop
[421.039s] reached. All 10 findings by codeex have
[423.68s] been actually integrated into the plan."
[425.599s] And it walks you through all the
[426.96s] details. And if we compare the
[429.12s] robustness here, we have one tab that
[431.599s] goes through the execution just using
[433.599s] Claudeex and one that uses only Claw to
[436.479s] create the plan. And you'll notice right
[438.08s] away without getting into the trenches
[439.919s] and the details, you have all five
[441.919s] phases here. And it is way more detailed
[444.96s] than what I'm about to show you. So this
[446.639s] is number one, and this is the one only
[448.96s] from Claude. You'll even notice visibly
[451.84s] that the phases are a little bit more
[454.0s] frail in terms of what they're going to
[455.28s] be doing when you go through the details
[457.36s] depending on what it is. You could even
[459.039s] use this by the way for creating things
[460.4s] like assets like PowerPoints, Excel
[462.479s] files, docx, whatever you want. The
[464.8s] whole point of this is that you have a
[466.24s] much richer planning mode so that by the
[468.639s] time you actually execute, you won't
[470.4s] theoretically oneshot something, but you
[472.72s] can increase the likelihood that you
[474.16s] will get the same thing done in less
[475.759s] steps. And that's pretty much it. So, as
[477.919s] promised, I will give this slash command
[479.919s] to you so you can take it, break it,
[482.16s] change it to your specifications, and
[483.919s] use it to get even better planning.
[485.759s] You'll find the link to the GitHub along
[487.44s] with a guide on how to use it in the
[489.52s] second link in the description below,
[490.96s] completely free. If you want to go
[492.319s] infinitely deeper and see exactly how
[494.08s] you could have built this for yourself,
[495.599s] how you can build on top of it, and in
[497.599s] general become a master of cloud code
[499.919s] and codecs, then check out the first
[501.68s] link in description below, and I'll see
[503.28s] you in my early A adopters community.
[504.96s] For the rest of you, if you enjoyed the
[506.24s] video, I'd super appreciate a like and a
[508.24s] sub on the channel. And if you feel so
[510.0s] pulled to do so, a comment on the video
[511.84s] would really help the reach."