# Branch


## 冲突

> 几个分支操纵同一个文件

![1559124907852](Branch.assets/1559124907852.png)

`git log --graph --pretty=oneline`——查看分支图

![1559125066544](Branch.assets/1559125066544.png)

## Recursive 策略

> 各分支操纵不同文件

- `git merge 【branch】`——不会快速合并，但是可以自动进行合并并提交，和添加信息

## BUG 分支

1. 先建立一个临时的分支

![1559126444451](Branch.assets/1559126444451.png)

2. 修复完 bug 进行提交

   ![1559126634411](Branch.assets/1559126634411.png)

3. 主动选择 Recursive策略

- `git merge --no-ff -m ‘msg’ 【branch】`——Recursive

![1559126946100](Branch.assets/1559126946100.png)

