import random
upperLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', ',', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ';', ':', '<', '>', '?', '/']
allChar = upperLetters + letters + numbers + symbols

print("Chào mừng đến với trình tạo mật khẩu!")
numberOfPassword = int(input("Số lượng kí tự mật khẩu tối thiểu bạn muốn tạo (tối đa 20 kí tự)\n"))
ranNumber = random.randint(1, 10)
numFor = numberOfPassword + ranNumber
if (numFor >= 20): 
    numFor = 20

passwordList = []
passwordList.append(random.choice(upperLetters))
passwordList.append(random.choice(letters))
passwordList.append(random.choice(numbers))
passwordList.append(random.choice(symbols))
numFor -= 4

while (numFor > 0):
    passwordList.append(random.choice(allChar))
    numFor -= 1
random.shuffle(passwordList)

for char in passwordList:
    print(char, end='')



