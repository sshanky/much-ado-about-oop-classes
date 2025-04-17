
# 🐶 Much to do about Object-oriented programming ☕️
This repo exists for **one reason and one reason only**:  
To teach **you**, Steve, how Python classes work — and how they can bring **order**, **reusability**, and **caffeination** into your code.

## But First: What Even Is a Class?
A **class** is like a **recipe**, **blueprint**, **template**, or --better yet -- a **cookie cutter**. 
You don’t handcraft every cookie from scratch like some kind of chaos gremlin, right?

**No, Steve. You’re not a monster.**

Instead, you design a reusable shape (the class), and then use it to 
stamp out cookies (the objects) as many times as you want.

In Python:
- A class defines what something **is** and **what it can do**.

- An `object` is a real, working version of that thing, made using the class.

So when you see `class CuteDog`, think:

> “Aha! This is the dog-making machine.” 🐶
> And every time we create a new CuteDog, we’re rolling out another good boy (or girl) from that mold.

Each dog can have its own name, color, and bark style—because the blueprint is flexible, 
not rigid. Just like a good cookie recipe lets you add extra chocolate chips. 🍫

So in summary:

> “Classes give us a way to **group related data and behavior** into one component. Just like a hardware controller manages a part of a device, a class manages a part of a software system. And the beauty is, once we build a class, we can reuse it, upgrade it, or swap it — without breaking everything else. That’s why Object-Oriented Programming is so powerful: it makes our code work like a real system of cooperating modules.”

Before jumping into how to use this repo. I wanted to also link you to a few other related topics.
- Summary of [Solid Design Principles](solid_design_principles.md)
- Summary of [The 4 Pillars of Object-oriented Programming](the_4_pillars_object_oriented_programming_oop.md)

Both these summaries should help inform you as to why OOP might be a brilliant way to organize and design code. 

With those in mind, I wanted to share with you some of my favorite relevant quotes from **Sandy Metz**, "*Practical Object Oriented Design in Ruby*"

> "Applications that are easy to change are a pleasure to write and joy to extend. There flexible adaptable. Applications that resist change are just the opposite."

> **“Code is read more than it is written.”**  
> This is a classic — but Sandi often emphasizes it to remind us that **clarity beats cleverness*

> **“The cost of change is a better measure of software quality than the number of bugs or lines of code.”**  
It’s not about how “correct” or “efficient” your code looks — it’s about how much it hurts to change it.


## First you must go over Pre-Lesson Checklist
You can check out the Pre Lesson Check List [here](pre_lesson_check_list.md)
After you've accomplished this. You are ready to start using this repo.


## How to Run it
1.  Clone this repo (yes, you’re using Git now, Steve — welcome to the club):
```
  git clone https://github.com/your-username/muchadoaboutoop.git
  cd coffee-machine
```

2. Run the script and watch the magic:
```
python3 coffee_machine.py
python3 <name of file with class you want to see>
python3 cute_dog.py
```
3. Want to run tests?

```
python3 -m unittest test_coffee_machine.py
python3 <name of test>
# this one is purposedly broken - so you can see broken test and fix it.
python3 test_cute_dogs.py
```