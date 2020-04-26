def sideways_triangle(size):
  for i in range(1, size+1):
    print('#'*i)
  for i in range(size - 1, 0, -1):
    print('#'*i)

sideways_triangle(5)
