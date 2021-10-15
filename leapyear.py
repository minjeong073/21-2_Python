year = int(input())

if year%4==0 and year%100!=0 or year%400==0 :
    print(1)
else :
    print(0)
    
    
/*출력

2000 --> 1
1999 --> 0

*/
