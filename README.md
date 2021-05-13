# RoastMeBot :speak_no_evil:
 This is a Twitter Bot using the official API made for [Spaguetti Code Fest 2020](https://coredumped.es/2020/ya-esta-aqui-el-spaghetti-code-fest-2020/) from [Core Dumped](https://coredumped.es) in ETSISI (UPM)

## The Concept :thought_balloon:
The idea of the competition was to realise a silly idea and convince the public that is something usefull in their normal life. My idea was a Twitter Bot that roasts you when it's mentioned and detects a keyword. When I submited it, it's content was kinda hardcore, and to avoid problems I removed the original .txt files with the phrases, and replaced it with a example .txt file. If you cannot sleep thinking on what jokes I put, contact me on my social media!

## What you need :computer:
At first, you need a Twitter Developer Account, and you can apply to it clicking [here](https://developer.twitter.com/en), and they will ask you for your purposes with the API and the account itself. Of course you will need Python installed on your computer or whatever you plant to execute this bot. At least the version 3.7 of it. And to finish with the requirements, you will need the [Tweepy](https://www.tweepy.org/) library, that makes the Twitter API work in Python.

## How it works :wrench:
It scans every X secons (you can change it, but the Twitter API has a limit of requests) your bot's timeline and search for a tweet with two requirements: a mention of the bot and a hashtag with a keyword. If a tweet with this conditions is found, it searchs on one .txt file with some funny (or not) phrases, depending on the hashtag (in the original project, if the bot detected #stan, it searched on the 'stan.txt' file for some jokes about the K-Pop fandom); and it replyes the tweet with a ramdom picked phrase of the file. **You don't have to edit the file last_seen_id.txt**

## What can I do? :bow:
You can create your own text files with custom jokes or sentences (remember only one sentence per line) and then change the code to detect the hashtag that makes the bot search into that file.

## Greeatings :heart:
Greatings one more time to Core Dumped and his awesome Spaghetti Code Fest, it was amazing and I learnt a lot during the development of this, being my first "serious" project ever done. Of course thanks to everyone supporting me while I was desperate on the last days, with the deadline getting even and even closer and editing the video that was making for the presentation. I had a mini devlog on Twitter to that was super fun to do.

One more time, thanks to everyone, and every type of feedback is welcome. See you all later!
