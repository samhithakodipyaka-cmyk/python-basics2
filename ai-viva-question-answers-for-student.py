def ai_viva_generator(topic):
    questions = {
        "ai": [
            ("What is Artificial Intelligence?",
             "Artificial Intelligence is the ability of a machine to mimic human intelligence."),
            
            ("What are the types of AI?",
             "The types of AI are Narrow AI, General AI, and Super AI."),
            
            ("What is Machine Learning?",
             "Machine Learning is a subset of AI that allows systems to learn from data."),
            
            ("What is Deep Learning?",
             "Deep Learning is a type of Machine Learning using neural networks."),
            
            ("Give one real-world example of AI.",
             "Chatbots, voice assistants, and recommendation systems are examples of AI.")
        ],

        "python": [
            ("What is Python?",
             "Python is a high-level, interpreted, and easy-to-learn programming language."),
            
            ("Why is Python used in AI?",
             "Python has simple syntax and powerful AI libraries like NumPy and TensorFlow."),
            
            ("What is a variable?",
             "A variable is used to store data values."),
            
            ("What is a function?",
             "A function is a block of code that performs a specific task."),
            
            ("What is indentation?",
             "Indentation is used to define blocks of code in Python.")
        ]
    }

    topic = topic.lower()

    if topic in questions:
        print("\nAI VIVA QUESTIONS AND ANSWERS\n")
        for q, a in questions[topic]:
            print("Q:", q)
            print("A:", a)
            print("-" * 40)
    else:
        print("Topic not found. Available topics: AI, Python")


# Main Program
print("AI VIVA QUESTION GENERATOR")
print("Available Topics: AI, Python")

user_topic = input("Enter topic name: ")
ai_viva_generator(user_topic)
