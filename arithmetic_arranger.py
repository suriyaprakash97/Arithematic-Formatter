def arithmetic_arranger(problems,ans=False):
  prob_count = len(problems)
  #number of lines in output.
  line1=''
  line2=''
  line3=''
  line4=''
  #Error condition-1: too many problems.
  if prob_count > 5:
    return "Error: Too many problems."
  #Trying other scenarios in the problem.
  for i in problems:
    #Error Condition-2: Operator must be '+' or '-'.
    if i.find('*') != -1 or i.find('%') != -1 or i.find('/') != -1:
      return "Error: Operator must be '+' or '-'."
    #Error Condition-3: Numbers must only contain digits.
    a = i.split()
    try:
      int(a[0])
      int(a[2])
    except:
      return "Error: Numbers must only contain digits."
    #Error Condition-4: Numbers cannot be more than four digits. 
    if (len(a[0]) > 4) or (len(a[2]) > 4):
      return "Error: Numbers cannot be more than four digits."
    #Calculate the Answer
    if a[1] == '+':
      answer = int(a[0])+int(a[2])
    else:
      answer = int(a[0])-int(a[2])
    #identify the length for formatter
    maxlen = max(len(a[0]),len(a[2]))
    #padline length calculator
    pad1 = maxlen-len(a[0])
    pad2 = maxlen-len(a[2])
    #assemble single problem in lines
    ln1 = ' '*2+' '*pad1+a[0]
    ln2 = (a[1]+' ')+' '*pad2+a[2]
    ln3 = '-'*len(ln1)
    ln4 = ' '*(len(ln1)-len(str(answer)))+str(answer)
    #append to final lines
    line1+=ln1+' '*4
    line2+=ln2+' '*4
    line3+=ln3+' '*4
    line4+=ln4+' '*4
  # form the final result
  if ans:
    formatted = line1.rstrip()+'\n'+line2.rstrip()+'\n'+line3.rstrip()+'\n'+line4.rstrip()
  else:
    formatted = line1.rstrip()+'\n'+line2.rstrip()+'\n'+line3.rstrip()
  #return the final result
  return formatted
