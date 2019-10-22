def mood():
    print("how are you?")
mood()
def my_mood(answear):
    print("My mood today: ")
    print(answear)
resp = input("How are you?")
my_mood(resp)
def my_mood(answear):
    return answear * 2
resp = input("how are you?")
twiced = my_mood(resp)
print("my mood is like", twiced)
