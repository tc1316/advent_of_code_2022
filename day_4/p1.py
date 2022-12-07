with open('./input.txt', 'r') as f:
    line = f.readline()
    COUNT = 0
    while line:
      g1, g2 = line.strip().split(',')
      g1, g2 = [int(x) for x in g1.split('-')], [int(x) for x in g2.split('-')]
      s1, s2 = set(range(g1[0],g1[1]+1)), set(range(g2[0],g2[1]+1))
      if s1.issubset(s2) or s2.issubset(s1):
        COUNT += 1


      line = f.readline()
    print(COUNT)
    

  