row = int(input('enter the number of rows '))

# full star
# for i in range(1, row+1):
#     print(' '*(row-i)+'*'*(2*i-1))
'''
    *
   ***
  *****
 *******
*********
'''

# hollow triangle
for i in range(1, row+1):
    print(' ' * (row - i) + '*' + ' ' * (2 * i - 3) + '*' * (i != 1), end='\n' + '*' * (i == row and row * 2-1))
'''
Output 10
         *
        * *
       *   *
      *     *
     *       *
    *         *
   *           *
  *             *
 *               *
*                 *
******************** 
'''