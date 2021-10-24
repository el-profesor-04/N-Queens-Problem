import copy
n=int(input())
start = []
for i in range(n):
    start.append([])
    for j in range(n):
        start[i].append(0)

def goalTest(state):
  queens=0
  for i in state:
    if 1 in i:
      queens+=i.count(1)
  return queens
def crosscheck(i,j,state):
  if i>=j:
    m=i-j
    l=0
    while m!=len(state)-1:
      if state[m][l]==1:
        return False
      m+=1
      l+=1
  else:
    m=0
    l=j-i
    while l!=len(state)-1:
      if state[m][l]==1:
        return False
      m+=1
      l+=1
  if i+j<=len(state)-1:
    m=0
    l=i+j
    while m!=i+j:
      if state[m][l]==1:
        return False
      m+=1
      l-=1
  else:
    m=i+j-len(state)+1
    l=len(state)-1
    while m!=len(state)-1:
      if state[m][l]==1:
        return False
      m+=1
      l-=1
  return True
def movegen(state):
  successors=[]
  i=goalTest(state)
  for j in range(len(state)):
    if isValid(i,j,state):
      tempstate=copy.deepcopy(state)
      tempstate[i][j]=1
      successors.append(list(tempstate))
  return successors
def isValid(i,j,state):
  if 1 in state[i]:
    return False
  elif any([state[k][j]==1 for k in range(len(state))]):
    return False
  elif not crosscheck(i,j,state):
    return False
  else:
    return True
def DepthFirst(state):
  opn=[state]
  while len(opn)!=0:
    for i in opn:
      if goalTest(i)==len(state):
        return i
      else:
        for z in movegen(i):
          if z not in opn:
            opn.append(z)
    return 'Faiure'
print(DepthFirst(start))