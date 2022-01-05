try:
    fout = open('output.txt', 'w')
except:
    print('Something went wrong.')
line = "This here's the wattle,\n"
fout.write(line)
line = "the emblem of our land.\n"
fout.write(line)
camels = 42
line = 'I have spotted %d camels.\n' % camels
fout.write(line)
camels = 43
line = f'I have spotted {camels} camels.\n'
fout.write(line)
camels = 44
line = 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
fout.write(line)
