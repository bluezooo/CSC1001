#func_1()

def func_1():
  #global x_in_func_1
  #global func_2

  x_in_func_1 = 'x_in_func_1'

  print('in func_1')
  print('%s has been used in func_1.'%x)

  def func_2():
    print('in func_2')


x = 'x'

func_1()

print('%s has been used out of func_1.'%x)
#print('%s has been used out of func_1.'%x_in_func_1)

#func_2()

