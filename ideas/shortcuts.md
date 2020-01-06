对于字符串的动态规划问题，一般来说采用二维数组dp，且可以按照下面的方式构建数组
```py
                i 
    1 1
    0 1 1 
    0 0 1 1
    0 0 0 1 1
    0 0 0 0 1 1
   j

   # or
                i 
    1 1 1 1 1 1
    0 1 1 1 1 1 
    0 0 1 1 1 1
    0 0 0 1 1 1
    0 0 0 0 1 1
   j
```
`i`为字符串首， `j`为字符串尾

```python
dp = [[0] * i + [1, 1] for i in range(leng)]

# or
dp = [[0] * i + [1] * (leng - i + 1) for i in range(leng)]
```

这样dp中的每个元素`dp[j][i]`代表`s[i:j+1]`的字符串的属性，即从第i个位置到第j个位置的所有元素。

**PS：**
1. 遍历顺序通常为Z字型，所以外循环为j，内循环为i
2. `dp`的取值为`dp[j][i]`而不是`dp[i][j]`，注意顺序