/*
Create a function called multiplication_table

takes an integer as input
print a multiplication result (구구단)
and return a list that includes the multiplication results.
For example,

a = multiplication_table(3)

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27

print(a)

[3, 6, 9, 12, 15, 18, 21, 24, 27]
*/

def multiplication_table(x) :
  result = []
  
  for i in range (1,10) :
    m = x * i
    result.append(m)
    print(f'{x} x {i} = {m}')
    
   return result
   
 a = nultiplication_table(3)
 print(a)
 
/* 출력

3 X 1 = 3
3 X 2 = 6
3 X 3 = 9
3 X 4 = 12
3 X 5 = 15
3 X 6 = 18
3 X 7 = 21
3 X 8 = 24
3 X 9 = 27
[3, 6, 9, 12, 15, 18, 21, 24, 27]
*/
