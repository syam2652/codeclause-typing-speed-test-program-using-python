import time

def typing_test():
    print("Welcome to the typing test!")
    time.sleep(1)
    print("You will be presented with a sentence to type.")
    time.sleep(1)
    print("Type the sentence exactly as it appears and press enter.")
    time.sleep(1)
    print("Let's begin!")
    time.sleep(1)
    sentence = "The quick brown fox jumps over the lazy dog."
    print(sentence)
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    accuracy = sum([1 for i, c in enumerate(user_input) if c == sentence[i]]) / len(sentence)
    words_per_minute = len(user_input) / (elapsed_time / 60) / 5
    print(f"Your accuracy was {accuracy * 100:.2f}%.")
    print(f"You typed at {words_per_minute:.2f} words per minute.")
    
typing_test()
