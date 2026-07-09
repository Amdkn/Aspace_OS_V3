---
video_id: B95cu7seTm8
url: https://www.youtube.com/watch?v=B95cu7seTm8
title: Make ANY Model Think Like Fable in Minutes
channel: Mark Kashet
duration: 9:38
views: 8k
language: en
ingested_at: 2026-06-14
status: ok
source: LLM_Wiki_A0
domain: L1 Life_OS / Hand-off
tags: [#wiki #hygiene #backfill]
date: 2026-06-14
type: source
---

# Make ANY Model Think Like Fable in Minutes

**Chaîne** : Mark Kashet
**URL** : https://www.youtube.com/watch?v=B95cu7seTm8
**Durée** : 9:38
**Vues** : 8k

## Transcript brut (concaténé)

So, if you feeling the withdrawal
effects of not using Fable 5, or even
the FOMO of not having the chance to
play with it before we lost it, then the
last few days have definitely been
rough. We had a taste, a glimpse of what
a super intelligent, PhD level scientist
looks like living in your editor. Now, I
can't help you get the power of Fable
back, because that power lies in the raw
model itself. But, I've hacked a way
that you can use your existing Claude
and Codex models, and just get them to
behave a lot more like Fable in just a
few steps. And you can even apply what
I'm about to show you to your
open-source models to get them to be
that much more functional. So, if you
want the second best thing until we get
our super intelligence back, then let's
dive in. All right, so the average
person doesn't know that the majority of
your conversations, whether they're
Codex or Claude code, live in what are
called JSONL files on your computer. And
they're basically these behemoth files
that are full of tool calls, metadata.
And within this metadata is a series of
gold that you can mine. And this file is
one example of one session full of said
metadata. You can see right here, these
are all my MCP tool calls. But, within
here you can also find things like the
prompts that you've sent to a model, as
well as what the model responded with,
and how it actually planned out its
tasks, along with the tool calls it
made. So, what you can do is have Claude
code parse through all of your
conversations to go from something like
this to something like this, where you
have a full playbook that you can give
pretty much any model, whether it's
open-source or close-source, and have it
either injected at the beginning of a
session using something like a hook, or
you refer to it in the middle of the
session to get that model to behave that
much more like Fable did. Now, like you
would have seen, the majority of that
file was pretty much irrelevant to us.
And while you could theoretically load
hundreds of JSONL files within a
conversation, you're going to
unnecessarily bloat it with information
that doesn't help you at all. So, what
you can do is, and I'll show you in a
second how you can do this in a
terminal, is ask Claude code to build a
series of scripts to already
preemptively parse through and only
distill the information that matters and
takes that information and then analyze
it for all the behavioral differences
between different models. And this
process would allow you to go from
thousands of lines to only a fraction of
that. And that fraction is what we can
feed these language models. And the
trick here is that all of these files
actually tag which model sent which
response. So we can filter down
something like Opus 4.8 conversations
against Fable 5 conversations to see the
disparity of how they behaved, what
tools they called, how they planned out
their sessions, and try to imitate the
delta. Now before I hop into the
terminal, what if you barely had a
chance to even have conversations with
Fable? You'd have no data to actually
analyze to begin with. What you could do
is go to this link in Hugging Face and
there are a series more like it where
people have actually open-sourced their
sessions that they've had with Fable 5.
So you can go through them and do the
exact same exercise even though it's not
your specific information or your
specific projects. And no need to
screenshot the link, I'll make it
available along with a few other things
in the second link down below. Now
popping into the terminal, I'm going to
walk you through the handful of prompts
that you can use to get to that
synthesis file that you can use however
you want. So in this case we can start
off with asking how many JSONL files do
we have from all of our sessions? And I
asked this to see what is the blast
radius. How many files do we have in the
entire universe of our usage? Now one
key caveat here is only a small fraction
of those would be Fable 5. So I'm just
trying to get a sense for how many so I
can then tell it to focus on that
specific filter. So in our case we have
close to 3,000 JSONL files across all of
our projects. Then once you understand
that, you can send a prompt just like
this. So you could basically say the
bloat in these files is the tool
results, the full file contents, and
command output that get echoed back into
context. Key thing, write me a small
Python script, you can name it whatever
you want, that takes a Claude code
session file and strips all the
lightweight transcript. So, leave me
with things like the timestamps, which
model it was, what did I ask for, and
what did the actual assistant respond
with. If you're trying this for the
first time, have it just do one specific
file, so you can make sure that it's the
exact format they're expecting. And once
it parses through, it will give you this
resulting file. You can take a peek at
it, and like I said, make sure it's what
you're expecting. So, in my case, I
redacted some information, some personal
information, but then it leaves you with
the transcript, the back and forth
between you and the agent. And you can
also add different metadata, like all
the tool calls, like you can see here.
Here are exactly what tools it executed
in what order. You can see this is the
assistant and that specific model. So,
you can easily then go to the next step,
which is parse the model-based
conversations that matter. So, then you
can send a prompt like this, where we
basically tell it that every single
conversation has this artifact that's
called message model, which we just saw
right now. Pull every turn that came
from Claude Fable 5, the exact model
name, out of my whole history across all
of my projects into one combined corpus.
So, basically, create a full playbook of
every single conversation that I had
using this model and all of the preamble
or the context around that conversation.
And on top of that, you can ask it to do
some synthesis. So, I say, "Give me the
behavioral patterns as real measured
numbers, not just impressions." So,
something that is tangible versus just
an intangible objective look at the
quality of the conversation. Now, since
we created a sample script before, it's
way faster to go from that point to this
point, where we have that completed file
that has all the artifacts across all
10,000 records, and then you can see all
the volume of messages. It walks through
and breaks down the numbers around tool
use, the order of work. So, one thing
that you'd want to emulate using Opus or
Codex or even your open-source models is
how disciplined Fable seemed to be
around using the right tools at the
right time. And you can learn a lot from
its rhythms. You can even see its
working rhythm here is being analyzed.
This transitions between using different
bash commands, chaining different steps,
the way it read and edited files,
everything seemed to be a little bit
more elegant and a little bit more
refined and precise from something like
Opus. And once you have that, this is
the key distinction. Depending on
whatever model you used alongside Fable
before Fable came out, let's say it's
Opus 4.8, it could be Opus 4.7 or even
Haiku. You can say, "Now run the exact
same behavioral read against insert name
of model here and put the two side by
side. Show me the distance between their
rhythm, the tool call cadence, the
action sequences, and the ratios like
reads before edits and tests after
edits." So we're trying to emulate the
entire structure of how Fable executed
things. Once you get that full
breakdown, it'll go and basically edit
its script and it will come back with an
overall summary like you can see here.
So you can see this is the side-by-side
compare
of Fable 5 and Opus 4.8 on your specific
computer. Again, if you don't have
enough history to have enough training
data for this Fable analysis, you could
use that open-source example I showed
you earlier.
And when you go to the bottom here, if
we scroll back up, you can see that for
very similar problems, there were many
more turns taken by Opus 4.8. A lot of
times it doesn't think before it acts as
much as Fable. So a lot of these, again,
we can't change cuz they come from the
model weights itself. But if you can
implore or elicit Opus to think that
much longer or plan a little bit longer
to be a lot more thoughtful, you still
won't get Fable 5 performance, but you
can get a much stronger Opus execution.
Once you finish the analysis, ask it to
distill all of its core findings of how
Opus could act more like Fable in
something like a playbook file. And what
you could do is you can open a brand new
session and refer to said file by
tagging it, or you could actually attach
it to a hook. so you could tag the
Claude Code Guide agent, and let's say
we go into a brand new terminal session,
and we spin this up.
Like I said, you could just bring the
file in and drag and drop it, or you
could say, "I want to use the learnings
from name of file."
Let's call it .md.
And I want it always injected
at session start. So, in this case, you
could say CC
the Claude Code Guide agent right here,
and I could say, "Attach a hook at the
session start event to always inject
this into context." Now, alternatively,
you could turn this into a skill. You
could turn it into a series of lines in
your Claude MD that are already auto
injected in every session. There are
different ways to go about integrating
this that really depend on your
day-to-day workflow. But, the bottom
line is you can improve the performance
of all of your models by giving it
something like this playbook. And to
make it easier for you, I will give you
my playbook as well. If you want to skip
this whole process and just take the
synthesis of what I've observed through
my Claude Code sessions. And that's
pretty much it. So, we can't clone the
power of Fable 5, but you can do a few
things to at least improve the models
that you currently have in the meantime
while we wait for all this play out.
Like I said before, you'll be able to
find all the prompts I walked you
through along with that link to that
open-source data set, along with that
little guide I showed you right now in
the second link down below. If you
always want to be on the front foot with
things like Claude Code and Codex and
agentic workflows in general, then check
out the first link down below for my
early adopters community. They already
got a preview of this trick before I put
it all together. So, if you always want
to be ahead of the game, then make sure
to check that out. And for the rest of
you, if you found this helpful, I'd
super appreciate a like and comment on
the video. Helps the reach, helps the
channel, and I'll see you in the next
one.


