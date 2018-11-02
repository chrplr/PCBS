import random

for i in range(1, 51):
    fn = "subj{:02d}.dat".format(i)
    phit = random.uniform(.5, .9)
    pfa = random.uniform(.05, .4)
    data = []
    for t in range(100):
        p = random.randint(1, 3)
        if p == 1:
            if random.uniform(0., 1.) < phit:
                trial = '1Y'
            else:
                trial = '1N'
        else:
            if random.uniform(0., 1.) < pfa:
                trial = '0Y'
            else:
                trial = '0N'
        data.append(trial)
    chaine = ",".join(data)
    f = open(fn, 'w')
    f.write(chaine)
    f.close()




