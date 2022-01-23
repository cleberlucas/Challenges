def solution(numbers, tgt): 
      numbers.sort()
      nc = numbers[:]
      nlt=[]
      solution=[]
      
      for i,n in enumerate(numbers):          
            if n<tgt:
                  nlt.append(n)
                  nc.pop(nc.index(n))

                  result_sum=[]  
                  for ii,nn  in enumerate(nc):
                        result= ((nlt[i]+nn)*-1)+tgt
                        
                        if (nlt[i]+nn<tgt):
                              result_sum.append(nlt[i]+nn)                    
                              if (result in  nc and nc.index(result)!=ii):
                                          if (sum([n,result, nc[ii]])==tgt and sorted([n,result, nc[ii]]) not in solution) :                     
                                                      solution.append(sorted([n,result, nc[ii]]))                            
      return solution
