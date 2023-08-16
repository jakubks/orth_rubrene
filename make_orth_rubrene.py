import numpy as np

# Number of unit cells in x, y and z dimensions and the output filename

NN = (2,3,3)

groname = 'test_output.gro'

##############################################################################

# Unit cell dimensions at 293 K from O. D. Jurchescu et al. Acta Cryst. (2006)
a = 26.86 /10
b = 7.193 /10
c = 14.433/10

# A few functions to make sure the spacings are correct for .gro file
def rstr(x):

    ans = str(round(x,3))

    if x > 0:
        ans = ' ' + ans

    if len(ans) == 3:
        ans = ans + '0'

    if len(ans) == 4:
        ans = ans + '0'

    if len(ans) == 5:
        ans = ans + '0'

    if x > 9.999:
        if len(ans) == 6:
            ans = ans + '0'

    if ans == '0.0000':
        ans = ' 0.000'

    return ans

def nstr(x):

    ans = str(int(x))

    if len(ans) == 1:
        ans = ' ' + ans

    if len(ans) == 2:
        ans = ' ' + ans

    if len(ans) == 3:
        ans = ' ' + ans

    if len(ans) == 4:
        ans = ' ' + ans

    ans = ans + ' '

    return ans

# Loading the rubrene geometry
core = np.zeros((70,3))
atoms = []
file = open('rubrene_center.gro','r')
lines = file.readlines()
file.close()

for kl in range(70):

    line = lines[kl+2]

    atoms.append(line.split()[0])

    core[kl,0] = float(line.split()[3])
    core[kl,1] = float(line.split()[4])
    core[kl,2] = float(line.split()[5])

vect = np.array([[0,0,0],
                [a,0, 0],
                [0,b, 0],
                [0,0, c],
                [a,b, c],
                [a,b,0],
                [a,0,c],
                [0,b,c],
                [a/2, b/2, 0],
                [a/2,b/2,c],
                [0, b/2, c/2], #10
                [a/2, 0, c/2], #11
                [a, b/2, c/2], #12
                [a/2,b,c/2]]) #13

bvect = np.array([[0,0,0],
                [a/2, b/2, 0],
                [0, b/2, c/2],
                [a/2, 0, c/2]])


###############################################################################

nmol = NN[0] * NN[1] * NN[2] * 4
newgro = open(groname,'w')

# Gotta be careful if any of the coords go above 9.9999 !!!!

newgro.write('crystal \n'+  str(int(70*nmol)) + '\n')


kk = 1 # atom index

for a_i in range(NN[0]):
    for b_i in range(NN[1]):
        for c_i in range(NN[2]):


            for jk in range(70):

                line = lines[jk+2]

                xcord = core[jk,0] +  bvect[0,0] + a_i * a
                ycord = core[jk,1] +  bvect[0,1] + b_i * b
                zcord = core[jk,2] +  bvect[0,2] + c_i * c

                newgro.write(line[0:15])

                newgro.write(nstr(kk))

                if xcord < 10:
                    newgro.write(" ")

                newgro.write(rstr(xcord))
                if ycord > 9.999:
                    newgro.write(" ")
                else:
                    newgro.write("  ")
                newgro.write(rstr(ycord))
                newgro.write("  ")
                newgro.write(rstr(zcord))
                newgro.write("\n")

                kk = kk + 1

##############################--------2----------#############################

for a_i in range(NN[0]):
    for b_i in range(NN[1]):
        for c_i in range(NN[2]):


            for jk in range(70):

                line = lines[jk+2]

                xcord = core[jk,0] +  bvect[1,0] + a_i * a
                ycord = core[jk,1] +  bvect[1,1] + b_i * b
                zcord = core[jk,2] +  bvect[1,2] + c_i * c

                newgro.write(line[0:15])

                newgro.write(nstr(kk))

                if xcord < 10:
                    newgro.write(" ")

                newgro.write(rstr(xcord))
                if ycord > 9.999:
                    newgro.write(" ")
                else:
                    newgro.write("  ")
                newgro.write(rstr(ycord))
                newgro.write("  ")
                newgro.write(rstr(zcord))
                newgro.write("\n")

                kk = kk + 1

##############################--------3----------#############################

for a_i in range(NN[0]):
    for b_i in range(NN[1]):
        for c_i in range(NN[2]):


            for jk in range(70):

                line = lines[jk+2]

                xcord = core[jk,0] +  bvect[2,0] + a_i * a
                ycord = core[jk,1] +  bvect[2,1] + b_i * b
                zcord = -core[jk,2] +  bvect[2,2] + c_i * c

                newgro.write(line[0:15])

                newgro.write(nstr(kk))

                if xcord < 10:
                    newgro.write(" ")
                newgro.write(rstr(xcord))

                if ycord > 9.999:
                    newgro.write(" ")
                else:
                    newgro.write("  ")

                newgro.write(rstr(ycord))
                newgro.write("  ")
                newgro.write(rstr(zcord))
                newgro.write("\n")

                kk = kk + 1

##############################--------4----------#############################

for a_i in range(NN[0]):
    for b_i in range(NN[1]):
        for c_i in range(NN[2]):


            for jk in range(70):

                line = lines[jk+2]

                xcord = core[jk,0] +  bvect[3,0] + a_i * a
                ycord = core[jk,1] +  bvect[3,1] + b_i * b
                zcord = -core[jk,2] +  bvect[3,2] + c_i * c

                newgro.write(line[0:15])

                newgro.write(nstr(kk))
                if xcord < 10:
                    newgro.write(" ")

                newgro.write(rstr(xcord))
                if ycord > 9.999:
                    newgro.write(" ")
                else:
                    newgro.write("  ")
                newgro.write(rstr(ycord))
                newgro.write("  ")
                newgro.write(rstr(zcord))
                newgro.write("\n")

                kk = kk + 1



newgro.write('   ' + str(a*NN[0]) + '   ' + str(b*NN[1]) + '   ' + str(c*NN[2]) + '\n')
newgro.close()

print('Done')
print(f'Orthorhombic crystal of -- {nmol} -- rubrenes was generated.')
