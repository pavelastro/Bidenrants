import discord
import os
import random
from keep_alive import keep_alive
from replit import db

client = discord.Client()

# Client prints startup
@client.event
async def on_ready():
  print('{0.user} is alive!'.format(client))
  await client.change_presence(status=discord.Status.online, activity=game)

# Bot Message when joining a new server
@client.event
async def on_guild_join(Guild):
  await Guild.system_channel.send('Hello! I am this server\'s very own, personal Joe Biden. My prefix is `joe`. You can run `joe help` to learn more. By default, I will respond to 1/100 messages. Have a good uhh, you know, the thing!')

# Chance of bot responding to a message, 1/x
response_chance = 100

# On Message
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message:
    responses = [
      "Will you shut up, man? " + message.author.mention, 
      "You ever been to a caucus, " + message.author.mention + "? No you haven’t. You’re a lying dog-faced pony soldier.", "Now we have over 120 million dead from COVID.", 
      "I should not have been so cavalier.", "I shouldn’t have been such a wise guy.", 
      "If you have a problem figuring out whether you’re for me or Trump, then you ain’t black.", 
      "You know, there’s a uh, during World War II, uh, you know, where Roosevelt came up with a thing uh, that uh, you know, was totally different than a, than the, the, it’s called, he called it the, you know, the World War II, he had the war – the War Production Board.",
      "We hold these truths to be self-evident: all men and women are created, by the, you know the, you know the thing.",
      "I may be Irish but I’m not stupid.",
      "You’re full of shit, " + message.author.mention + "!",
      "But we cannot let this – we’ve never allowed any crisis from a Civil War straight through to a pandemic in ‘17, all the way around, ’16, we have never, never let our democracy take second fiddle, we can both have a democracy and elections and at the same time protect the public health.",
      "Poor kids are just as bright and just as talented as white kids.",
      "His mom lived in Long Island for 10 years or so, god rest her soul, and, er, although she’s, wait – your mom’s still alive. It was your dad [who] passed. God bless her soul. I gotta get this straight.",
      "I am a gaffe machine. But by God, what a wonderful thing compared to a guy who can’t tell the truth.",
      "This is a big fucking deal.",
      "Look, John’s last-minute economic plan does nothing to tackle the number one job facing the middle class, and it happens to be, as Barack says, a three-letter word: jobs. J-O-B-S.",
      "If you want to know where Al Qaeda lives, you want to know where Bin Laden is, come back to Afghanistan with me. Come back to the area where my helicopter was forced down, with a three-star general and three senators at 10,500 feet in the middle of those mountains. I can tell you where they are.",
      "I would tell members of my family, and I have, I wouldn’t go anywhere in confined places now. It’s not that it’s going to Mexico, it’s you’re in a confined aircraft when one person sneezes it goes all the way through the aircraft. That’s me. I would not be, at this point, if they had another way of transportation, suggesting they ride the subway.",
      "You need to work on your pecs, " + message.author.mention + ".",
      "You know there’s an old Irish saying, there’s all kinds of old Irish sayings. My grandfather Finnegan, I think he made them up. But uh, it says, may the hinges of our friendship never go rusty. Well, with these two folks that you’re about to meet if you haven’t already, there’s no doubt about them staying oiled and lubricated here, ladies and gentlemen. Now for you who are not full Irish in this room, lubricated has a different meaning for us all.",
      "If John McCain wants to know where the bad guys live, come back with me to Afghanistan. We know where they reside, and it’s not in Iraq.",
      "A man I’m proud to call my friend. A man who will be the next President of the United States – Barack America!",
      "In Delaware, the largest growth of population is Indian Americans, moving from India. You cannot go to a 7/11 or a Dunkin’ Donuts unless you have a slight Indian accent. I’m not joking.",
      "I mean, you got the first mainstream African-American who is articulate and bright and clean and a nice-looking guy. I mean, that’s a storybook, man.",
      "Now is the time to heed the timeless advice from Teddy Roosevelt: ‘Speak softly and carry a big stick.’ I promise you, the president has a big stick.",
      "Why don’t you say something nice instead of being a smartass all the time, " + message.author.mention + "?",
      "No Ordinary American Cares About Their Constitutional Rights.",
      "I never had an interest in being a mayor ’cause that’s a real job. You have to produce. That’s why I was able to be a senator for 36 years.",
      "I think the only reason Clarence Thomas is on the court is because he is black.",
      "When you're appealing to people's fears and anxieties, you can make some gains.",
      "The next person that tells me I'm not religious, I'm going to shove my rosary beads up their ass.",
      "I worked at an all-black swimming pool in the east side of Wilmington, I was involved in what the Negroes, I mean, blacks were thinking, what they were feeling.",
      "It's easy being vice president - you don't have to do anything.",
      "Every single morning since I've been 27 years old, I've got up and someone's handed me a card like the one I have in my pocket with the schedule on it, of all the things I'm gonna do. I don't know what to do if I didn't have that card.",
      "I mean, you got the first mainstream African-American who is articulate and bright and clean and a nice-looking guy. I mean, that's a storybook, man.",
      "Make sure of two things. Be careful - microphones are always hot, and understand that in Washington, D.C., a gaffe is when you tell the truth. So, be careful.",
      "I did not grope the wife of Defense Secretary Ashton Carter or the daughter of Sen. Christopher Coons. I don't put drugs in drinks or give drinks to underage females. And all those photos about me inappropriately touching girls, they are blown-up.",
      "There's never been A day in the last four years I've been proud to be his Vice President. Not a single day.",
      "I agree with " + message.author.mention + " who said about Benghazi: \"We got to preven dis from hapinin agen. \"",
      "Obama and Biden want to raise taxes by a trillion dollars. Guess what? Yes we do.",
      "I get a lot of credit I don't deserve.",
      "How I learned to love the New World Order.",
      "What's four years in our long American history? Remember when I asked that wheelchair-bound politician to \"stand up.\" It turns me off when people say Donald Trump is authentic. Just because he says \"Mexican rapists.\" What about me? I am the real deal.",
      "Guess what, the cheerleaders in college are the best athletes in college. You think, I'm joking, they're almost all gymnasts, the stuff they do on hard wood, it blows my mind.",
      "Well, you know, my shotgun will do better for you than your AR-15, because you want to keep someone away from your house, just fire the shotgun through the door.",
      "President Clinton bankrupted Chrysler so that Italians could buy it to ship jobs overseas to China.",
      "I have never touched Hillary Clinton inappropriately.",
      "I have never touched " + message.author.mention + " inappropriately.",
      "Al Gore invented the Internet.",
      "Folks, I can tell you I've known eight presidents, three of them intimately.",
      "Don't tell me what you value. Show me your budget and I'll tell you what you value.",
      "Almost every great innovation was created by government.",
      "I am a Zionist. You don't have to be a Jew to be a Zionist.",
      "In presidential campaign I released a 65-page file from the Syracuse University College of Law that showed poor grades, back in college, also. If I were plagiarizing consistently, my grades would have been better.",
      "Now that I'm not running, I can appear on Fox. Let the cabinet members do the low-ratings shows on MSNBC.",
      "Remember, no one decides who they're going to vote for based on the vice president. I mean that literally.",
      "Wealthy people are just as patriotic as poor people, I honest to God believe that.",
      message.author.mention + " is a good man, but he doesn't know much about the health care system.",
      "Look, guys, no matter what a girl does, no matter how she's dressed, no matter how much she's had to drink, it's never, never, never, never, never, never, never, never, never, never OK to touch her without her consent.",
      "If I hear one more Republican tell me about balancing the budget, I am going to strangle them.",
      "Hilary Clinton might have been a better pick than me."
      ]
    if random.randint(1, response_chance) == 1:
      await message.channel.send(random.choice(responses))

  if message.content == ('joe help'):
    await message.channel.send('**Commands**\n`joe quote` - Get a random Joe Biden quote\n`joe help` - List of commands and more\n visit my website www.daemonstark.ezyro.com')

  if message.content == ('joe quote'):
    responses = [
      "Will you shut up, man? " + message.author.mention, 
      "You ever been to a caucus, " + message.author.mention + "? No you haven’t. You’re a lying dog-faced pony soldier.", "Now we have over 120 million dead from COVID.", 
      "I should not have been so cavalier.", "I shouldn’t have been such a wise guy.", 
      "If you have a problem figuring out whether you’re for me or Trump, then you ain’t black.", 
      "You know, there’s a uh, during World War II, uh, you know, where Roosevelt came up with a thing uh, that uh, you know, was totally different than a, than the, the, it’s called, he called it the, you know, the World War II, he had the war – the War Production Board.",
      "We hold these truths to be self-evident: all men and women are created, by the, you know the, you know the thing.",
      "I may be Irish but I’m not stupid.",
      "You’re full of shit, " + message.author.mention + "!",
      "But we cannot let this – we’ve never allowed any crisis from a Civil War straight through to a pandemic in ‘17, all the way around, ’16, we have never, never let our democracy take second fiddle, we can both have a democracy and elections and at the same time protect the public health.",
      "Poor kids are just as bright and just as talented as white kids.",
      "His mom lived in Long Island for 10 years or so, god rest her soul, and, er, although she’s, wait – your mom’s still alive. It was your dad [who] passed. God bless her soul. I gotta get this straight.",
      "I am a gaffe machine. But by God, what a wonderful thing compared to a guy who can’t tell the truth.",
      "This is a big fucking deal.",
      "Look, John’s last-minute economic plan does nothing to tackle the number one job facing the middle class, and it happens to be, as Barack says, a three-letter word: jobs. J-O-B-S.",
      "If you want to know where Al Qaeda lives, you want to know where Bin Laden is, come back to Afghanistan with me. Come back to the area where my helicopter was forced down, with a three-star general and three senators at 10,500 feet in the middle of those mountains. I can tell you where they are.",
      "I would tell members of my family, and I have, I wouldn’t go anywhere in confined places now. It’s not that it’s going to Mexico, it’s you’re in a confined aircraft when one person sneezes it goes all the way through the aircraft. That’s me. I would not be, at this point, if they had another way of transportation, suggesting they ride the subway.",
      "You need to work on your pecs, " + message.author.mention + ".",
      "You know there’s an old Irish saying, there’s all kinds of old Irish sayings. My grandfather Finnegan, I think he made them up. But uh, it says, may the hinges of our friendship never go rusty. Well, with these two folks that you’re about to meet if you haven’t already, there’s no doubt about them staying oiled and lubricated here, ladies and gentlemen. Now for you who are not full Irish in this room, lubricated has a different meaning for us all.",
      "If John McCain wants to know where the bad guys live, come back with me to Afghanistan. We know where they reside, and it’s not in Iraq.",
      "A man I’m proud to call my friend. A man who will be the next President of the United States – Barack America!",
      "In Delaware, the largest growth of population is Indian Americans, moving from India. You cannot go to a 7/11 or a Dunkin’ Donuts unless you have a slight Indian accent. I’m not joking.",
      "I mean, you got the first mainstream African-American who is articulate and bright and clean and a nice-looking guy. I mean, that’s a storybook, man.",
      "Now is the time to heed the timeless advice from Teddy Roosevelt: ‘Speak softly and carry a big stick.’ I promise you, the president has a big stick.",
      "Why don’t you say something nice instead of being a smartass all the time," + message.author.mention + "?"
      "No Ordinary American Cares About Their Constitutional Rights.",
      "I never had an interest in being a mayor ’cause that’s a real job. You have to produce. That’s why I was able to be a senator for 36 years.",
      "I think the only reason Clarence Thomas is on the court is because he is black.",
      "When you're appealing to people's fears and anxieties, you can make some gains.",
      "The next person that tells me I'm not religious, I'm going to shove my rosary beads up their ass.",
      "I worked at an all-black swimming pool in the east side of Wilmington, I was involved in what the Negroes, I mean, blacks were thinking, what they were feeling.",
      "It's easy being vice president - you don't have to do anything.",
      "Every single morning since I've been 27 years old, I've got up and someone's handed me a card like the one I have in my pocket with the schedule on it, of all the things I'm gonna do. I don't know what to do if I didn't have that card.",
      "I mean, you got the first mainstream African-American who is articulate and bright and clean and a nice-looking guy. I mean, that's a storybook, man.",
      "Make sure of two things. Be careful - microphones are always hot, and understand that in Washington, D.C., a gaffe is when you tell the truth. So, be careful.",
      "I did not grope the wife of Defense Secretary Ashton Carter or the daughter of Sen. Christopher Coons. I don't put drugs in drinks or give drinks to underage females. And all those photos about me inappropriately touching girls, they are blown-up.",
      "There's never been A day in the last four years I've been proud to be his Vice President. Not a single day.",
      "I agree with " + message.author.mention + " who said about Benghazi: \"We got to preven dis from hapinin agen. \"",
      "Obama and Biden want to raise taxes by a trillion dollars. Guess what? Yes we do.",
      "I get a lot of credit I don't deserve.",
      "How I learned to love the New World Order.",
      "What's four years in our long American history? Remember when I asked that wheelchair-bound politician to \"stand up.\" It turns me off when people say Donald Trump is authentic. Just because he says \"Mexican rapists.\" What about me? I am the real deal.",
      "Guess what, the cheerleaders in college are the best athletes in college. You think, I'm joking, they're almost all gymnasts, the stuff they do on hard wood, it blows my mind.",
      "Well, you know, my shotgun will do better for you than your AR-15, because you want to keep someone away from your house, just fire the shotgun through the door.",
      "President Clinton bankrupted Chrysler so that Italians could buy it to ship jobs overseas to China.",
      "I have never touched Hillary Clinton inappropriately.",
      "I have never touched " + message.author.mention + " inappropriately.",
      "Al Gore invented the Internet.",
      "Folks, I can tell you I've known eight presidents, three of them intimately.",
      "Don't tell me what you value. Show me your budget and I'll tell you what you value.",
      "Almost every great innovation was created by government.",
      "I am a Zionist. You don't have to be a Jew to be a Zionist.",
      "In presidential campaign I released a 65-page file from the Syracuse University College of Law that showed poor grades, back in college, also. If I were plagiarizing consistently, my grades would have been better.",
      "Now that I'm not running, I can appear on Fox. Let the cabinet members do the low-ratings shows on MSNBC.",
      "Remember, no one decides who they're going to vote for based on the vice president. I mean that literally.",
      "Wealthy people are just as patriotic as poor people, I honest to God believe that.",
      message.author.mention + " is a good man, but he doesn't know much about the health care system.",
      "Look, guys, no matter what a girl does, no matter how she's dressed, no matter how much she's had to drink, it's never, never, never, never, never, never, never, never, never, never OK to touch her without her consent.",
      "If I hear one more Republican tell me about balancing the budget, I am going to strangle them.",
      "Hilary Clinton might have been a better pick than me."
      ]
    await message.channel.send(random.choice(responses))



keep_alive()
client.run(os.getenv('TOKEN'))
