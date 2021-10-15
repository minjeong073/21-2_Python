#1
/*
  Create a function called calculator that it takes two variables x,y and calculate following values:

  addition (더하기)
  subtraction (빼기)
  multiplication (곱하기)
  division (나누기)
  floor division (나머지)
  power (거듭제곱)  a^b
*/
 
def calculator(x,y) :
  addition = x+y
  subtraction = x-y
  multiplication = x*y
  division = x/y
  floor_division = x%y
  power = x**y
  
  return addition, subtraction, multiplication, division, floor_division, power
   
 answer = calculator(5,3)
 print(answer)
 
 /* 출력 : 8, 2, 15, 1.6666666667, 2, 125 */
 
