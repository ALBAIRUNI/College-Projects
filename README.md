# Assignment 2 Idea

The key concept of encryption is working around dealing with new values produced to insert it in new operations to get nested sequence of opeartions 

* How to Decrypt
An overview points to keep in mind

1 - you have to know that reversing the operations will solve the problem " Why ? " 
Because the main ecryption tool used is XOR and to reverse it use it 

2 - you have to care about order of reversing to keep the values secure from being lost

* Let's Take a closer look

   a = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d)
   b = c ^ F(a ^ F(d) ^ (a | d))
   c = d ^ F(a | F(a) ^ a)
   d = a ^ 31337

   a = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a)
   b = b ^ F(d ^ F(a) ^ (d | a))
   c = a ^ F(d | F(d) ^ d)
   d = d ^ 1337
   
   in reversing orders we will 
   Firstly work with (8,7,6,5) equations then (4,3,2,1)
   
   note //
   working with lower part  (8,7,6,5) equations just reverse without any problem 
   as there are no nested variables : I mean no variable is used after its transformation like equation 7,8
   
*   8     d = d ^ 1337
*   7     a = c ^ (F(d | F(d) ^ d))
*   6     b = b ^ (F(d ^ F(a) ^ (d | a)))
*   5     c = a3 ^ (F(d | F(b ^ F(a)) ^ F(d | b) ^ a))
   
   the Upper Part is different as we use variables after its transformation 
   so we have to keep a version of Pretransformation 
   
   

*         a2 = a

*   4      a = d ^ 31337
*   3      d = c ^ (F(a | F(a) ^ a))
*   2      c = b ^ (F(a ^ F(d) ^ (a | d)))
*   1      b = a2 ^ (F(a | F(c ^ F(d)) ^ F(a | c) ^ d))
  
  note the sequence we used 
