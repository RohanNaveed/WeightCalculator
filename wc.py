weight = input("Weight: ")
weight = int(weight)
L = weight * 0.45
K = weight * 2.20
final_weight = input('(L)bs or (K)g ').upper()
if final_weight == 'L':
    print(f'You are {L} kilograms')
elif final_weight == 'K':
    print(f'You are {K} pounds')