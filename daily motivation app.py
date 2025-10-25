import tkinter as tk
import random
import tkinter.font as tkFont

# ------------------------------
# Data: 50 Quotes, 50 Tips, 50 Fun Facts
# ------------------------------

quotes = [
    "Believe in yourself and all that you are.",
    "Success is the sum of small efforts repeated daily.",
    "Your only limit is your mind.",
    "Dream it. Wish it. Do it.",
    "Don’t stop until you’re proud.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream bigger. Do bigger.",
    "Don’t wait for opportunity. Create it.",
    "Sometimes later becomes never. Do it now.",
    "Little things make big days.",
    "It’s going to be hard, but hard does not mean impossible.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Opportunities don’t happen, you create them.",
    "Work hard in silence, let success make the noise.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The key to success is to start before you are ready.",
    "Do something today that your future self will thank you for.",
    "Doubt kills more dreams than failure ever will.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Your limitation—it’s only your imagination.",
    "Don’t wait for motivation. Create discipline.",
    "Don’t be afraid to start over. It’s a chance to rebuild what you want.",
    "Be stronger than your excuses.",
    "Start where you are. Use what you have. Do what you can.",
    "Winners are not people who never fail, but people who never quit.",
    "Hustle until you no longer need to introduce yourself.",
    "Don’t let yesterday take up too much of today.",
    "Act as if what you do makes a difference. It does.",
    "Success is liking yourself, liking what you do, and liking how you do it.",
    "A winner is a dreamer who never gives up.",
    "Discipline is the bridge between goals and accomplishment.",
    "Keep going. Everything you need will come to you at the perfect time.",
    "Your future is created by what you do today, not tomorrow.",
    "Big journeys begin with small steps.",
    "You are capable of more than you know.",
    "Make each day your masterpiece.",
    "Difficult roads often lead to beautiful destinations.",
    "Do not wait to strike till the iron is hot; but make it hot by striking.",
    "Every accomplishment starts with the decision to try.",
    "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart.",
    "With the new day comes new strength and new thoughts.",
    "Happiness is not something ready made. It comes from your own actions.",
    "Fall seven times and stand up eight.",
    "You miss 100% of the shots you don’t take.",
    "Stay positive, work hard, make it happen.",
    "Success usually comes to those who are too busy to be looking for it.",
    "Hardships often prepare ordinary people for an extraordinary destiny."
]

tips = [
    "Break tasks into smaller parts.",
    "Take short breaks while studying.",
    "Write down your goals every morning.",
    "Use a to-do list to stay organized.",
    "Prioritize your most important tasks first.",
    "Set deadlines to avoid procrastination.",
    "Limit social media during work hours.",
    "Work in 25-minute focus intervals (Pomodoro Technique).",
    "Review your progress at the end of the day.",
    "Avoid multitasking — focus on one thing at a time.",
    "Sleep at least 7-8 hours daily.",
    "Drink enough water to stay focused.",
    "Start your day with the hardest task.",
    "Declutter your workspace to boost focus.",
    "Use reminders and alarms to stay on track.",
    "Reward yourself after completing tasks.",
    "Plan tomorrow before going to bed.",
    "Batch similar tasks together.",
    "Use keyboard shortcuts to save time.",
    "Learn to say no to distractions.",
    "Automate repetitive tasks when possible.",
    "Start small if you feel overwhelmed.",
    "Work during your most productive hours.",
    "Avoid perfectionism — done is better than perfect.",
    "Listen to instrumental music while working.",
    "Prepare things you need the night before.",
    "Stand up and stretch every hour.",
    "Check emails only at set times.",
    "Turn off unnecessary notifications.",
    "Keep healthy snacks at your desk.",
    "Write notes instead of keeping everything in your head.",
    "Learn something new every day.",
    "Set realistic daily goals.",
    "Keep a gratitude journal.",
    "Exercise regularly to keep your mind sharp.",
    "Use positive affirmations to stay motivated.",
    "Set weekly review sessions.",
    "Work in a clean and quiet environment.",
    "Take deep breaths when stressed.",
    "Avoid caffeine late in the evening.",
    "Don’t compare your progress with others.",
    "Visualize success before starting your day.",
    "Focus on progress, not perfection.",
    "Learn to delegate tasks when possible.",
    "Stop overthinking — start doing.",
    "Keep a water bottle with you at all times.",
    "Unsubscribe from unnecessary emails.",
    "Limit TV and YouTube binge sessions.",
    "Celebrate small wins every day.",
    "Be consistent — small daily habits create big results."
]

fun_facts = [
    "Bananas are berries, but strawberries are not.",
    "Honey never spoils — archaeologists found 3000-year-old honey still edible.",
    "Octopuses have three hearts.",
    "Sharks existed before trees.",
    "Sloths can hold their breath longer than dolphins.",
    "Wombat poop is cube-shaped.",
    "There’s enough DNA in your body to stretch to the sun and back 600 times.",
    "A day on Venus is longer than a year on Venus.",
    "Koalas have fingerprints almost identical to humans.",
    "Some turtles can breathe through their butts.",
    "Pineapples take about two years to grow.",
    "Water can boil and freeze at the same time.",
    "Butterflies can taste with their feet.",
    "Your stomach gets a new lining every 3 to 4 days.",
    "Sharks are the only fish that can blink with both eyes.",
    "A sneeze travels about 100 miles per hour.",
    "The Eiffel Tower can grow taller in summer due to heat expansion.",
    "Cows have best friends and get stressed when separated.",
    "A group of flamingos is called a 'flamboyance'.",
    "Sea otters hold hands when they sleep to avoid drifting apart.",
    "Your body has more bacteria cells than human cells.",
    "Some cats are allergic to humans.",
    "Pigeons can recognize themselves in mirrors.",
    "Octopuses have blue blood.",
    "An ostrich’s eye is bigger than its brain.",
    "Sharks can live up to 500 years.",
    "A cloud can weigh more than a million pounds.",
    "A giraffe has the same number of neck bones as a human (seven).",
    "Peanuts are not nuts — they’re legumes.",
    "Cows produce more milk when listening to music.",
    "Banana plants are herbs, not trees.",
    "Otters have a special pocket for their favorite rock.",
    "The inventor of the Pringles can is buried in one.",
    "Wombats run surprisingly fast.",
    "The moon has moonquakes.",
    "Some frogs can freeze solid and still live.",
    "Sharks can detect a drop of blood from miles away.",
    "The average person walks the equivalent of five times around the world in a lifetime.",
    "Mosquitoes are attracted more to people who eat bananas.",
    "The fingerprints of a koala are so similar to humans they can confuse crime scenes.",
    "Your taste buds have a lifespan of 10 to 14 days.",
    "The longest hiccup spree lasted 68 years.",
    "The human brain is sometimes more active when asleep than awake.",
    "Ants never sleep.",
    "Penguins propose to each other with a pebble.",
    "Tigers have striped skin, not just striped fur.",
    "An apple floats in water because it is 25% air.",
    "A shrimp’s heart is located in its head.",
    "Rabbits can’t vomit."
]

# ------------------------------
# Function to generate motivation
# ------------------------------

def generate_motivation():
    quote = random.choice(quotes)
    tip = random.choice(tips)
    fact = random.choice(fun_facts)

    quote_label.config(text=f"🌟 Quote: {quote}")
    tip_label.config(text=f"💡 Tip: {tip}")
    fact_label.config(text=f"🤯 Fun Fact: {fact}")

# ------------------------------
# GUI setup
# ------------------------------

root = tk.Tk()
root.title("Daily Motivation Generator")
root.geometry("650x500")
root.config(bg="#f5f5f5")

# Define custom fonts
title_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
content_font = tkFont.Font(family="Helvetica", size=13, weight="bold")

# Title
title = tk.Label(root, text="✨ Daily Motivation Generator ✨", 
                 font=title_font, bg="#f5f5f5", fg="#2c3e50")
title.pack(pady=15)

# Labels
quote_label = tk.Label(root, text="", font=content_font, wraplength=600, bg="#f5f5f5", fg="#333")
quote_label.pack(pady=15)

tip_label = tk.Label(root, text="", font=content_font, wraplength=600, bg="#f5f5f5", fg="#333")
tip_label.pack(pady=15)

fact_label = tk.Label(root, text="", font=content_font, wraplength=600, bg="#f5f5f5", fg="#333")
fact_label.pack(pady=15)

# Button
btn = tk.Button(root, text="✨ Get Motivation ✨", command=generate_motivation, 
                font=("Helvetica", 14, "bold"), bg="#27ae60", fg="white", padx=12, pady=6)
btn.pack(pady=25)

# Run app
root.mainloop()
