# https://cs50.harvard.edu/python/2022/psets/0/faces/

def main():
    user_input = str(input())
    print(convert(user_input))




def convert(smiley_text):
    smiley_text = smiley_text.replace(":)", "🙂")
    smiley_text = smiley_text.replace(":(", "🙁")
    return smiley_text

main()


