#2
/* Write a function of name frame_star that takes as input a string and return a new string that frames it with ********** (10 stars). For example,

print(frame_star('Hello'))

**********
Hello
**********
*/


def frame_star(x) :
  frame_star = "*"*10 + '\n' + x + '\n' + "*"*10
  return frame_star
  
print(frame_star('Hello'))


/*출력 
**********
Hello
**********
*/
