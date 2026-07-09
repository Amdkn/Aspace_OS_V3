# M_AmPWmkpwA — New AI coding paradiagm - OpenAI Symphony
## Channel: AI Jason
## URL: https://youtu.be/M_AmPWmkpwA
## Date extracted: 2026-06-22
## Duration: ~12:36 (756s)
## Lines: 408
## Chars: 15052

## Transcript (timestamps)

[00:00] So, Open AI just released this
[00:01] open-source repo called Symphony. On the
[00:03] surface level, it looks like a
[00:05] orchestrator that allow you to manage
[00:07] coding agents through ticket tracker
[00:08] like linear, but it is a lot more than
[00:10] just connecting linear. It's a totally
[00:13] different way of interacting with
[00:14] agents. So, the way we use coding agent
[00:16] has shifted a lot for the past few
[00:18] months. From initially just the
[00:19] auto-complete to primarily interactive
[00:21] session with coding agent to now most of
[00:23] us around two or three different
[00:25] sessions in parallel, each working
[00:27] isolated work tree for different
[00:28] features or bug fixing. And then new
[00:30] tooling like Super set or conductor that
[00:32] has been introduced to help you run and
[00:34] manage different interactive coding
[00:36] sessions easier. The problem is that
[00:38] even with those tools, many people,
[00:40] including myself, will feel this burden
[00:42] when we are working on more than like
[00:43] three different sessions cuz we just
[00:45] can't context switch every minute. And I
[00:47] personally have had multiple times
[00:49] sending the wrong instruction to the
[00:50] wrong thread. So, ceiling of how much we
[00:52] can get out from those coding agent is
[00:54] no longer the model capability, but our
[00:57] own attention and cognitive load. And
[00:59] the recent project Symphony is so
[01:00] interesting is that Open AI's
[01:02] engineering team had this realization
[01:03] that the current experience has been
[01:05] orienting around coding session, merge
[01:07] PRs, but in reality for the past
[01:09] decades, software workflow are largely
[01:11] organized around deliverables, things
[01:13] like issues, tasks, tickets, milestones.
[01:15] Engineer leaders have been managing
[01:17] massive amount of tasks across thousands
[01:19] of workers, not by reviewing everyone's
[01:21] PR, but looking at final outcomes using
[01:23] tools like linear and Atlassian. And
[01:25] Open AI's proposed solution is move
[01:27] human up a level. Instead of managing
[01:29] two three interactive sessions, you
[01:31] manage tickets. The agent works at
[01:33] ticket level, report back through the
[01:35] ticket itself, and you stay in the loop
[01:37] without monitoring individual sessions.
[01:38] The ticket tracker becomes state machine
[01:40] itself. And the way Symphony makes this
[01:42] work is almost embarrassingly simple,
[01:44] but very effective. It's a background
[01:46] process. You run it once, point to a
[01:48] workflow file, which we'll talk a bit
[01:49] more, and then it runs forever. Every 30
[01:51] seconds, this background process will
[01:53] glance through your linear board. If it
[01:55] finds any ticket in to-do slots, it will
[01:57] set up an isolated workspace and start
[01:59] agent in that workspace. And the whole
[02:01] system has three key components. One is
[02:03] the scheduler, the background process
[02:05] that is pulling ticket data and set up
[02:07] workspace, manage session life cycle,
[02:09] and a workflow.md file that lives inside
[02:11] your repo. It contains configuration of
[02:13] scheduler and detailed instruction for
[02:15] coding agent to know how to work with
[02:16] those ticketing system. And those
[02:18] external system like linear is a durable
[02:20] state machine for human to interact with
[02:22] agent. And this whole setup is actually
[02:23] very flexible. You don't have to use
[02:25] linear. You don't have to use Code X.
[02:27] You can actually customize to whatever
[02:28] you want. But overall implementation
[02:30] concept is what's interesting. And the
[02:31] most interesting part is this
[02:32] workflow.md file. It basically break
[02:35] down into two parts. The top part is the
[02:36] YAML front matter. It configures
[02:38] scheduler directly, like which linear
[02:40] project it is, what type of ticket it
[02:41] should pick up, where should agent
[02:43] create isolated workspace, and even
[02:45] programmatic hooks to run after it set
[02:47] up the workspace. And this is very
[02:48] useful, so you no longer need to rely on
[02:50] agent to set those things up. As well as
[02:52] how many agents can be run in parallel
[02:54] and specific agent settings. And after
[02:56] that, the bottom half is a markdown
[02:58] file. This is the prompt agent every
[03:00] single turn details rendered in. It's a
[03:03] standard operating procedure for
[03:04] handling tickets in this repo. How
[03:06] should agent plan task? How should agent
[03:08] go validate its work? And what would be
[03:10] considered as done? And when should
[03:11] outreach for human review? And what I
[03:13] love about this design is that the same
[03:15] file just live inside your repo, so it's
[03:17] version controlled and can be changed
[03:19] through normal pull request. And the
[03:20] file itself contains some programmatic
[03:22] rule that controls scheduler and also
[03:24] what an agent does. There's no separate
[03:26] config service, no admin panel, no UI at
[03:28] all. And the team only code base on this
[03:30] workflow. So, when you onboard a new
[03:32] agent capability of adding new step in
[03:34] the process, you just very easily change
[03:36] this markdown file, and the rest will
[03:37] just follow. And this whole system is
[03:39] designed very flexible. You don't have
[03:41] to use Code X, and you don't have to use
[03:43] linear. They have one example
[03:44] implementation in Elixir, which is a
[03:46] programming language. But they have this
[03:48] spec.md file that's detailing how this
[03:50] framework or system is designed. So, you
[03:53] can just drop this file to any coding
[03:55] agent and ask it to build and design a
[03:57] system in any programming language.
[03:59] There are already a lot of different
[04:00] community attempts. Like someone
[04:01] building custom TUI based on the task
[04:03] data. And also another person already
[04:05] rebuilt it to support Cloud Code as
[04:07] agent harness. And I'm going to show you
[04:09] step by step how you can set these
[04:10] things up. But orchestrating agent is
[04:12] only part of the work. As Open AI
[04:14] mentioned, this whole thing only works
[04:16] if your coding agent's environment is
[04:18] set up properly in a way that it can
[04:20] complete tickets end-to-end atomically,
[04:22] which you can call it harness engineer,
[04:23] but fundamentally just whether your
[04:25] environment or code base has been set up
[04:27] in the right way, so agent has
[04:29] everything it needs to complete task
[04:30] end-to-end. And typical things like is
[04:32] the system bootable, so agent can just
[04:34] run a script to get everything set up
[04:36] without spending time to figure that
[04:37] part out. And does the system has a
[04:39] proper documentation structure for
[04:40] different things. And I think most
[04:42] people does have these two things
[04:43] properly set up in your code.md or
[04:45] agent.md file. But the part I think most
[04:47] of team didn't set up is those
[04:48] self-verifying tools. They allow agent
[04:51] to do an end-to-end test after
[04:53] implementing something. And even submit
[04:54] a video recording to prove that it have
[04:57] tested and it's working in the ticket
[04:59] directly just like in their demo. But in
[05:01] the doc, they didn't really mention how
[05:02] they were handling this part. So, I did
[05:04] some research across many major skills.
[05:07] And the best one I found is this
[05:08] Playwright CRI tool. So, I believe many
[05:10] of us are pretty familiar with
[05:12] Playwright MCP, which allow agent to use
[05:14] the browser and do a task, check the
[05:16] logs. But the problem before was that
[05:17] Playwright with MCP setup, it took a
[05:20] huge amount of tokens in context window
[05:21] even when it's not needed. But they have
[05:23] released this Playwright CRI tool
[05:25] alongside agent skill that detailing
[05:27] every single comment. And the most
[05:29] interesting comment is this video
[05:30] recording CRI. So, Playwright allow
[05:32] agent to run commands like video start
[05:35] and video stop to capture browser
[05:36] session into a MP4 or WebM video. They
[05:39] even have some pretty advanced video
[05:41] rendering capability where they can add
[05:43] different chapter on the screen. Like
[05:45] here's one example video where it can
[05:47] record its own session and even add new
[05:49] HTML element on top of the screen to
[05:52] annotate the action the agent took. And
[05:54] then upload session into linear, so you
[05:56] can very easily verify if things
[05:58] actually work. And as far as I know,
[06:00] other tools like Chrome DevTools MCP or
[06:02] agent browser don't have this video
[06:04] capability out of box. So, this is one
[06:06] very important skill that will make your
[06:07] whole experience complete. And
[06:08] meanwhile, there are also other skills
[06:10] that you should add. And I just take one
[06:11] of the repo I have as example. We have
[06:13] this Playwright CRI tool that has a
[06:15] skill as well as a list of reference for
[06:17] agent to know how to like record a video
[06:19] and tracing the debug logs. And we also
[06:21] have a skill here to tell agent how to
[06:23] start server locally. And because ours
[06:25] is pretty straightforward, so it's just
[06:27] a skill file. But sometimes for more
[06:28] complicated things, you can create
[06:30] predefined script as well. So, agent no
[06:32] longer spends cognitive power on those
[06:33] type of stuff. And meanwhile, I also
[06:35] created this linear skill that allow
[06:37] agent to know how to operate linear
[06:38] tickets by using linear API as well as
[06:41] things like upload video evidence of the
[06:43] test. And we actually have more
[06:44] documentations about different parts of
[06:46] system. And in the agent.md or cloud.md
[06:49] file, this is where we have a proper
[06:50] index of different documentation
[06:52] systems, so you can always go and find
[06:53] the relevant information. We also give
[06:55] more detailed debugging skills. For
[06:57] example, we use Grafana to track and
[06:59] store all the logging in production. And
[07:00] we add a relevant Grafana log skill in
[07:03] our repo, so the agent can fetch real
[07:05] production logs for bug fixing. And all
[07:07] those things are try to serve one
[07:08] purpose, which is setting up your code
[07:10] base so that your agent can fix bug,
[07:12] building new features, verify things are
[07:14] working fully atomically end-to-end. I
[07:16] put all skills inside AI Build Club, so
[07:18] you can copy-paste and ask your agent to
[07:20] customize for your own code base. I put
[07:22] the link in the description below, so
[07:23] you can join and access. And once you
[07:25] set this up, even though you don't use
[07:27] Symphony, they're still going to be
[07:28] really useful. But after that, this is
[07:30] where we can start setting up the
[07:31] Symphony, connect to linear, as well as
[07:33] this workflow.md file. So, once you
[07:35] clone the Symphony repo, you'll see
[07:37] folder like this. You'll have this
[07:38] folder of Elixir. So, this is one
[07:40] version implementing Elixir programming
[07:42] language from Open AI. And most of the
[07:44] time, you can just use this Elixir
[07:46] directly. But if you want to customize
[07:47] it to like connect not linear, but
[07:49] connect to Trello or Jira, you can ask
[07:51] coding agent to customize it or even
[07:54] building a different language by
[07:55] pointing to spec.md file. And here's
[07:57] basically what I did in Python folder. I
[07:59] just point to spec.md file and ask it to
[08:02] build a new version in Python. But most
[08:04] of the time, you actually don't need to
[08:05] do that. You can just reuse what Open AI
[08:07] provided. And firstly, you can confirm
[08:09] whether the script is So, you can run
[08:10] script by doing this, which point to the
[08:13] Symphony program that has been built.
[08:14] And run help. So, this should show you
[08:16] the actual command about how to run
[08:18] Symphony. You basically just do Symphony
[08:20] and point to a path to workflow.md file.
[08:22] And by default, you can't just run the
[08:23] Symphony like this. You can run this to
[08:25] bind Symphony command to the specific
[08:28] path. So, just run this. And then you
[08:30] can do Symphony, point to a specific
[08:32] workflow.md file. And by default, it
[08:34] will give you this warning. Then you can
[08:36] add this argument to the command, which
[08:38] will set our Symphony background process
[08:39] like this. It will track all the tasks,
[08:41] show you the project, and next refresh
[08:43] time. It will track a specific linear
[08:45] project you set up every 30 seconds. If
[08:47] there any ticket in to-do, it will pick
[08:49] up and show up in this list. And all
[08:51] those configurations are actually
[08:52] defined in workflow.md file. So, in
[08:54] workflow.md file, at the front matter,
[08:56] there is a project slug. And Symphony
[08:58] script will basically read that
[09:00] metadata,
[09:01] importing information from a specific
[09:02] project. Same thing for all the other
[09:04] configurations, like how frequently it
[09:06] should pull the ticket data, what are
[09:08] things it should do after setting up a
[09:09] new workspace, how many agent can be run
[09:11] at the same time, and the Code X
[09:13] configuration. But once you set up this,
[09:15] it's basically monitoring the specific
[09:16] Symphony repo with Elixir
[09:18] implementation. What we want to do is
[09:20] apply this to your own workspace. It's
[09:22] actually pretty straightforward. You can
[09:24] just open any coding agent like Code X
[09:26] or Cloud Code, point to the spec.md file
[09:28] and say, "I want to set up Symphony for
[09:30] my repo, and we will reuse the Elixir
[09:32] implementation here, and help me build
[09:34] the workflow.md file for my repo." With
[09:36] just one command, coding agent is smart
[09:38] enough to look at your own repo and
[09:41] design a workflow.md file inside there.
[09:43] And this is the one it created for me,
[09:44] including the project slug and API key
[09:47] and all the other configurations. But
[09:49] you do need to set up linear first. If
[09:51] you haven't created linear account yet,
[09:52] just go create a one and then add a new
[09:54] project. And in this project, click on
[09:56] the button here, you can just paste into
[09:59] your coding agent. This thing in the
[10:00] middle here is a project slot, or you
[10:03] can manually paste into the workflow.md
[10:04] file as well. And meanwhile, you need to
[10:06] get a linear API key, which you can get
[10:08] by clicking on settings, security and
[10:10] access, and add a new personal API key
[10:12] here. And once you did that, you should
[10:13] run this command, which will save the
[10:14] linear API key globally on your
[10:16] computer. So, every time when agent try
[10:18] to use linear, it can access any
[10:20] projects you have access to. And there
[10:21] are some configuration you should do,
[10:23] which is status. So, Symphony out-of-box
[10:26] are designed for some specials status
[10:27] control flow, like human review status
[10:30] and also merging status. Once you put a
[10:32] ticket into do, Symphony will
[10:33] automatically pick up and put that in
[10:35] progress and trigger an agent session.
[10:37] And once agent finish the work, it will
[10:38] change to human review status, so that
[10:40] you can review the work. And once
[10:42] finished, you can set the status to be
[10:43] merging, which will trigger the agent
[10:45] automatically raise a PR from this work.
[10:47] And once you did all that, you can do
[10:48] run Symphony past through your
[10:50] workflow.md file, plus this I understand
[10:53] that this will be running without the
[10:55] usual guardrail comment. And now
[10:57] Symphony will be working and picking up
[10:58] all the tickets in your project here. To
[11:00] make it easier, you can also create a
[11:01] new view, set up this board, so that you
[11:03] get this kind of Kanban experience. But
[11:05] to just test, I can just create ticket
[11:07] change the landing page hero copy from
[11:09] your company on autopilot to your AI
[11:11] growth team, and the set up the status
[11:14] to be to do. And this should trigger our
[11:15] agent here. If I go back here, you can
[11:17] see this time it pick up this ticket,
[11:20] and then you can see the agent session
[11:21] show up, and then last agent message
[11:23] here. And depends on your settings, you
[11:25] can also go check this workspace. You
[11:27] can see inside this workspace, it has
[11:29] one workspace per ticket. So, each one
[11:31] is running isolated environment. And
[11:33] this example implementation also has uh
[11:35] kind of web UI dashboard that you can
[11:37] visit, and this will list out similar
[11:39] information you will see in terminal
[11:41] here. Not particularly useful, but I
[11:43] just thought I'd mention this. And you
[11:44] can see after a while, this agent
[11:46] changes ticket to in progress status,
[11:48] which reflect in our linear board as
[11:50] well. And if I click on that, agent made
[11:52] a plan and logged all the steps it did.
[11:55] After a few minutes, the agent check off
[11:57] every single items on the checklist, and
[11:59] upload a video recording to verify
[12:02] things are working. And as a human, I
[12:03] can just very easily see if things are
[12:05] working or not. And once I mark
[12:06] something as merging, it will also
[12:08] create a PR for me. So, this is a whole
[12:09] end-to-end process and how you set
[12:11] things up. It definitely feels like
[12:12] future. If you hit any blockers, I have
[12:14] more detailed step-by-step breakdown, as
[12:16] well as all skills posted in the AI
[12:18] Build Club. Every week, we have workshop
[12:20] to go through those latest learnings and
[12:21] answer any questions. So, if you're
[12:23] interested, you can click on the link
[12:24] below and join our next batch. But this
[12:26] is project Symphony, how it works and
[12:28] what's the implications. If you found
[12:29] this video useful, please give me a
[12:31] subscribe and comment below. Thank you,
[12:32] and I see you next time.
