
def trap(self, input):
    lvolume = [0]
    rvolume = [0]
    lm = 0
    rm = 0
    um = max(input)
    umindex = input.index(um)

    for i in range(1, umindex):
        lm = max(lm, input[i - 1])

        if lm - input[i] >= 0:
            lvolume.append(lm - input[i])
        else:
            lvolume.append(0)

    for i in range(1, len(input) - 1 - umindex):
        rm = max(rm, input[len(input) - i])
        if rm - input[len(input) - 1 - i] >= 0:
            rvolume.append(rm - input[len(input) - 1 - i])
        else:
            rvolume.append(0)

    return sum(lvolume) + sum(rvolume)


