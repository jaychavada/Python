# QUE: If txt file contain twinkle word or not

f = open("poem.txt")
t = f.read()
if 'twinkle' in t:
    print("Twinkle is Present")
else:
    print("Twinkle is Not Present")
f.close()

# Que: Override highscore.txt if your score > highscore with use of function

def game():
    return 445
score = game()

with open("highscore.txt") as f:
    highscore = int(f.read())

if highscore<score:
    with open("highscore.txt","w") as f:
        f.write(str(score))
        
# QUE: Replace Unusual word with sensor
with open("one.txt") as f:
    content = f.read()

content = content.replace("good","$%@$%@")
with open("one.txt","w") as f:
    content = f.write(content)