friendly_texts = [
    "Hey! How are you doing today? I hope you're having a great time!",
    "I had a wonderful day at the beach with my friends. The weather was perfect!",
    "Just wanted to say hello and wish you a fantastic day ahead.",
    "My family and I are planning a picnic this weekend. Would you like to join us?",
    "I'm so excited for the upcoming concert. It's going to be amazing!",
    "I wanted to thank you for your kind words. They really made my day.",
    "Let's catch up for coffee sometime. I'd love to hear about your recent adventures.",
    "Hope you're enjoying your vacation. Don't forget to relax and have fun!",
    "I'm hosting a movie night at my place. You're invited! Bring your favorite snacks.",
    "Sending you warm hugs and positive vibes. You're an incredible person!",
    # Add more friendly texts...
]
friendly_texts.extend([
    "It was great catching up with you yesterday. Let's plan another get-together soon!",
    "Wishing you a day filled with smiles and laughter. You deserve all the happiness!",
    "I'm grateful to have you as a friend. You always bring positivity into my life.",
    "Thinking of you and sending you positive energy for a productive day ahead.",
    "Just wanted to check in and see how you're doing. Let me know if there's anything I can do to help.",
    "Congratulations on your recent achievement! You worked hard for it and deserve the recognition.",
    "I appreciate your support and friendship. You're always there when I need someone to talk to.",
    "Let's plan a weekend getaway together. We could use some adventure and relaxation!",
    "Remember to take breaks and prioritize self-care. Your well-being is important to me.",
    "I'm proud of you for pursuing your dreams. Keep going and never give up!",
])
friendly_texts.extend([
    "I hope you're enjoying your day so far! Sending you positive vibes.",
    "Let's plan a game night soon. It's always fun to spend time together.",
    "Just wanted to say thank you for being an amazing friend. I appreciate you!",
    "Remember to take breaks and take care of yourself. You deserve it.",
    "I'm here to support you in whatever you need. You're never alone.",
    "I'm excited to see you this weekend. It's been too long since we last hung out.",
    "Sending you virtual hugs. You're an important part of my life.",
    "You're doing great! Keep up the fantastic work and stay motivated.",
    "I'm grateful for our friendship. It brings so much joy and positivity to my life.",
    "Wishing you a day filled with laughter, love, and beautiful moments.",
])
friendly_texts.extend([
    "Just wanted to send a quick hello and let you know that you're on my mind.",
    "I'm grateful to have you as a friend. Your presence brightens up my days.",
    "Congratulations on your recent success! You deserve all the applause and recognition.",
    "Let's plan a fun day out together soon. We can explore new places and create memories.",
    "I admire your positive attitude and resilience. You inspire me every day.",
    "Thinking of you and hoping that your day is filled with happiness and laughter.",
    "You're an amazing person, and I'm lucky to have you in my life. Thank you for being you.",
    "Just a friendly reminder to always believe in yourself and your abilities. You're capable of great things.",
    "I appreciate your kindness and support. You're a true friend.",
    "Sending you a virtual high-five for all the progress you've made. Keep up the fantastic work!",
])
friendly_texts.extend([
    "I'm so grateful to have you as a friend. You bring so much positivity into my life.",
    "Just wanted to check in and see how you're doing. Let me know if there's anything I can do to support you.",
    "Sending you warm wishes and good vibes for a wonderful day ahead.",
    "Let's plan a movie night soon. We can have popcorn, snacks, and enjoy some great films together.",
    "I believe in you and your abilities. Keep striving for your goals and dreams.",
    "Wishing you a day filled with laughter, love, and all the things that make you happy.",
    "You're not alone. I'm here for you, no matter what you're going through.",
    "Thank you for being such a genuine and caring friend. You make a positive difference in my life.",
    "Let's make time for a coffee date. It's always great to catch up and chat with you.",
    "I'm proud of you and all that you've accomplished. Keep shining brightly!",
])
friendly_texts.extend([
    "Just wanted to say that you're amazing and I'm grateful to have you in my life.",
    "Sending you positive energy and good vibes for a productive and fulfilling day.",
    "Let's plan a fun adventure soon. We can explore new places and create lasting memories.",
    "You have a special place in my heart. Thank you for being such a wonderful friend.",
    "Remember to take time for self-care and prioritize your well-being. You deserve it.",
    "I'm here to support you through thick and thin. You can always count on me.",
    "You bring so much joy and laughter into my life. Thank you for being you.",
    "Congratulations on your recent achievement! You've worked hard for it and deserve the recognition.",
    "Let's plan a virtual hangout soon. We can catch up and share some laughs.",
    "Wishing you a day filled with happiness, love, and all the things that make you smile.",
])
friendly_texts.extend([
    "Just wanted to remind you that you're incredible and capable of amazing things.",
    "Sending you a virtual hug and lots of positive vibes. You're never alone.",
    "Let's plan a cozy movie night with blankets and popcorn. It'll be a fun and relaxing time.",
    "I value our friendship and the bond we share. Thank you for always being there for me.",
    "You have a heart of gold and a smile that brightens the room. Keep shining, my friend.",
    "Congratulations on your new job! Wishing you success and fulfillment in your career.",
    "Let's plan a weekend getaway soon. It'll be a great opportunity to unwind and recharge.",
    "Thank you for being a constant source of support and encouragement. You make a difference in my life.",
    "I believe in your dreams and aspirations. Keep pursuing what sets your soul on fire.",
    "Wishing you a day filled with sunshine, laughter, and beautiful moments to cherish.",
])
friendly_texts.extend([
    "Just wanted to say hi and let you know that you're on my mind. Sending positive vibes your way!",
    "Congratulations on your recent accomplishment! You deserve all the success that comes your way.",
    "Let's plan a fun day out together. We can explore the city, try new restaurants, and have a great time.",
    "Thank you for being an amazing friend. Your presence in my life brings so much joy and happiness.",
    "Remember to take a moment to relax and unwind. Self-care is important, and you deserve it.",
    "I appreciate your kindness and the way you always make others feel special. You're truly a gem.",
    "Wishing you a day filled with laughter, love, and beautiful memories. Enjoy every moment!",
    "You're an inspiration with your determination and passion. Keep chasing your dreams fearlessly.",
    "Let's plan a virtual game night with our friends. It'll be a blast! Get ready for some friendly competition.",
    "Just wanted to check in and see how you're doing. If you need someone to talk to, I'm here for you.",
])


def calculate_word_frequency(text, word):
    words = text.lower()
    word_count = words.count(word.lower())
    total_words = len(words)
    frequency = word_count / total_words
    return frequency
def wordFrequency(listdata,word):
   if word =='' or len(listdata)==0:
      return
   totalFrequency = 0
   for sentence in listdata:
      totalFrequency += calculate_word_frequency(sentence, word)
   return totalFrequency/len(listdata)

word = 'night'
print(f"The frequency of '{word}' in the friendly text is: {wordFrequency(friendly_texts,word)*100}")
