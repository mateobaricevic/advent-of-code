
file = open("input.txt")
public_keys = file.read().split("\n")[:-1]
public_key_card = int(public_keys[0])
public_key_door = int(public_keys[1])
# public_key_card = 5764801
# public_key_door = 17807724

def getLoopSize(public_key, subject_number):
    value = 1
    count = 0
    while value != public_key:
        value *= subject_number
        value %= 20201227
        count += 1
    return count

loop_size_card = getLoopSize(public_key_card, 7)
loop_size_door = getLoopSize(public_key_door, 7)
# print(loop_size_card, loop_size_door)

def getEncryptionKey(loop_size, public_key):
    value = 1
    for i in range(loop_size):
        value *= public_key
        value %= 20201227
    return value

encryption_key_card = getEncryptionKey(loop_size_card, public_key_door)
encryption_key_door = getEncryptionKey(loop_size_door, public_key_card)

print(encryption_key_card, encryption_key_door)
