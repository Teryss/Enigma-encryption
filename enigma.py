def run(text, rotors, R,base, turns):
    I = rotors[0]
    II = rotors[1]
    III = rotors[2]
    I_turn, II_turn = False, False

    #STARTING ROTATION
    for i in range(turns[0]):
        I = rotate_a_rotor(I)
    for i in range(turns[1]):
        II = rotate_a_rotor(II)
    for i in range(turns[2]):
        III = rotate_a_rotor(III)

    output = ''
    for letter in text:
        if letter == ' ':
            output += ' '
        else:
            letter_change = list()
            #HANDLING ROTATION
            I = rotate_a_rotor(I)
            if I[1][0] == I[2][0]:
                I_turn = True
            if I_turn == True and I[1][0] == I[2][1]:
                I_turn = False
                print('rotor 2 rotated')
                II = rotate_a_rotor(II)
            if II[1][0] == II[2][0]:
                II_turn = True
            if II_turn and II[1][0] == II[2][1]:
                II_turn = False
                print("rotor 3 rotated")
                III = rotate_a_rotor(III)
            
            index = base.index(letter)
            #FORWARD ROTORS
            letter_change.append(base[index])
            index = rotor_forward(I, index)
            letter_change.append(base[index])
            index = rotor_forward(II, index)
            letter_change.append(base[index])
            index = rotor_forward(III, index)
            letter_change.append(base[index])
            #REFLECTOR
            index = rotor_forward(R, index)
            letter_change.append(base[index])
            #BACKWARD ROTORS
            index = rotor_backwards(III, index)
            letter_change.append(base[index])
            index = rotor_backwards(II, index)
            letter_change.append(base[index])
            index = rotor_backwards(I, index)
            letter_change.append(base[index])
            
            output += base[index]
    return output


def rotor_forward(rotor, id):
    letter_out = rotor[1][id]
    index_out = rotor[0].index(letter_out)
    return index_out

def rotor_backwards(rotor, id):
    letter_out = rotor[0][id]
    index_out = rotor[1].index(letter_out)
    return index_out

def rotate_a_rotor(rotor):
    temp_base = rotor[0][1:]
    temp_out = rotor[1][1:]

    temp_base += rotor[0][0]
    temp_out += rotor[1][0]

    return [temp_base, temp_out, rotor[2]]