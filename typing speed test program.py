import time

text = "Hi G.SYAM KUMAR " 
print("Type this text as fast as you can: ")
print(text)

input("Press Enter when ready...") 
start_time = time.time() 

typed_text = input() 

end_time = time.time() 

typing_time = end_time - start_time

num_words = len(text.split()) 

typed_words = len(typed_text.split()) 

accuracy = typed_words / num_words * 100 

wpm = typed_words / typing_time * 60 

print("Time taken: {:.2f} seconds".format(typing_time))
print("Accuracy: {:.2f}%".format(accuracy))
print("Words per minute: {:.2f}".format(wpm))
