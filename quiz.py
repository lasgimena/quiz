#categories and library
#easy
easy = [
    ["1. The more you code, the more of me there is. I may be gone for now but you cannot get rid of me forever. What am I?", "a.) A code", "b.) A bug", "c.) A loop", "d.) A secret"],
    ["2. I am a language for everything yet I have no real identity of my own. Good luck trying to compile me. What am I? ", "a.) Algorithm", "b.) Algorihtm", "c.) Pseudocode", "d.) Psuedocode"],
    ["3. As a developer I am your eyes, showing you the result of your code in your language of choice. What am I? ", "a.) A return statement", "b.) A print statement", "c.) A loop statement", "d.) An input statement"],
    ["4. I am fundamental and used to build larger structures. While you will find many different kinds of me, we all just mess with information in different ways. What am I?", "a.) A small structure", "b.) A code structure", "c.) A file structure", "d.) A data structure"],
    ["5. I am your “waiter” for information. What I am?", "a.) A debugger", "b.) A server", "c.) A computer", "d.) A software"],
]
#answers
easy_answers = ["b", "c", "b", "d", "b"]
#average
average = [
    ["1. As a developer, you usually get mad at me because I complain a lot, although I am usually right. What am I?", "a.) A compiler", "b.)  A debugger", "c.) A console", "d.) A terminal"],
    ["2. I am sent before I am ready, I will break before you know it and you cannot find me many places. What am I?", "a.) A sample", "b.) A trial", "c.) A beta release", "d.) A finished product"],
    ["3. I am a simple thing, nothing special. While I have many cousins we are all very similar because we set your project up. What am I?", "a.) A test file", "b.) A debugging file", "c.) A configuration file", "d.) A sample file"],
    ["4. I am pretty focused so I do not do too much. However whatever you wish is my command. What am I?", "a.) A command", "b.) A code", "c.) A request", "d.) A statement"],
    ["5. I have a pulse but no heart, a brain but cannot think and while I can sleep, I usually do not stay asleep for long? What am I?", "a.) A software engineer", "b.) A software", "c.) A monitor ", "d.) A CPU"],
]
#answers
ave_answers = ["a", "c", "c", "a", "d"]
#difficult
difficult = [
    ["1. I catch you and your teammates when you fall and I can be you in a pinch. What am I?", "a.) A developer", "b.) A user", "c.) A project manager", "d.) A tester"],
    ["2. I come small, as small as you can get in fact. With many well-thought-out versions of me I bring stability. What am I?", "a.) A unit test", "b.) A code", "c.) A statement", "d.) A console"],
    ["3. You make me often and you are always messing with me by pushing and pulling me all the time. Do you not have any manners 😠😤? What am I?", "a.) A text", "b.) A code", "a.) A file", "d.) A loop"],
    ["4. I am a shape shifter. You could call me someone who could possess multiple qualities but only has one set of them at any given time. What am I?", "a.) Polymorphism", "b.) Isomerism", "c.) Metamorphism", "d.) Coercion"],
    ["5. I am a red and black structure and often forgotten about after learned. Although you almost always use a different color of me for Christmas. What am I?", "a.) A red-black code", "b.) A red-black test", "c.) A red-black structure", "d.) A red-black tree"],
]
#answers
diff_answers = ["c", "a", "b", "a", "d"]


while True:
    quiz = []   
    points = 0

    categ = input("\nChoose difficulty of quiz [easy, average, difficult] ('exit' to end quiz): ") #input choice
    if categ == "easy":
        quiz = easy
        answer_key = easy_answers
    elif categ == "average":
        quiz = average
        answer_key = ave_answers
    elif categ == "hard":
        quiz = difficult
        answer_key = diff_answers
    elif categ == "exit":
        print("Bye")
        break
    else:
        print("{} is not a valid option!".format(categ))    #if choice is not abcd
        continue

    for i in range(0, len(quiz)):
        qna = quiz[i]
        question = qna[0]   #call question
        print("\n\n{}\n".format(question))

        for choice in range(1, len(qna)):
            print(qna[choice])

        answer = input("\n> ")

        if answer == answer_key[i]:
            points+=1
            print("Correct!")
        else:
            print("Incorrect!")

    print("You got {} points!\n".format(points))
