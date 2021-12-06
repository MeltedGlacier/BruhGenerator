import random

# I have never really used Python that much before so forgive me for this code being potentially jank.

# Author:
# MeltedGlacier

# Description:
# Variation of the other one but this time you can
# choose how many bruhs you want. There is no cap.
# Please don't break anything lmao-

# Generates a file called bruh that just has random
# amounts of bruh in it.

target = int(input("How much bruh do you want?"))
output = str("")
count = 0
filenameRand = str(random.randrange(1, 9999))
fileName = str("bruh" + filenameRand + ".txt")

while count < target:
    count = count + 1
    output = output + "Bruh "

f = open(fileName, "x")
f.write(output)
f.close()
