import enigma

base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#rotors
I = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
II = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
III = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
IV = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
V = 'VZBRGITYUPSDNHLXAWMJQOFECK'
#reflectors
R1 = 'EJMZALYXVBWFCRQUONTSPIKHGD'
R2 = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
R3 = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

rotors = [
    [base, I, ('Q','R')],
    [base, II, ('E','F')],
    [base, III, ('V', 'W')],
    [base, IV, ('J','K')],
    [base, V, ('Z','A')]
]
reflectors = [
    [base, R1],
    [base, R2],
    [base, R3]
]

work_with_inputs = False

if work_with_inputs:
    message = input("Enter a message to encrypt: ").upper()

    rotors_select = input("Which rotors you want to use (ex. 1 3 5): ").split()
    rotors_select = [int(x) - 1 for x in rotors_select]
    rotors_used = [rotors[rotors_select[0]], rotors[rotors_select[1]], rotors[rotors_select[2]] ]

    turns = input("Select rotation of each rotor (from 0 to 25): ").split()
    turns = [int(x) for x in turns]

    reflector_select = int(input("Which reflector you want to use (1-3): ")) - 1

else:
    message = "breaking bad bruh"
    message = message.upper()
    rotors_select = [1,2,1]
    rotors_used = [rotors[x] for x in rotors_select]
    turns = [11,2,23]
    reflector_select = 1

print('Original message: ', message)
encrypted_message = enigma.run(message, rotors_used, reflectors[reflector_select], base, turns)
print('Encrypted: ',encrypted_message)

decrypted_message = enigma.run(encrypted_message, rotors_used, reflectors[reflector_select], base, turns)
print('Decrypted: ',decrypted_message)