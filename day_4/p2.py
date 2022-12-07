with open('./input.txt', 'r') as f:
    line = f.readline()
    COUNT = 0
    while line:
      g1, g2 = line.strip().split(',')
      g1, g2 = [int(x) for x in g1.split('-')], [int(x) for x in g2.split('-')]
      
      if len(range(max(g1[0], g2[0]), min(g1[1], g2[1])+1)):
        COUNT +=1



      line = f.readline()
    print(COUNT)
    

  