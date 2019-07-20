# Workspace

![1559117744154](Workspace.assets/1559117744154.png)

## 增

- `git add 【file…or dir…】`——工作区→暂存区

![1559118367326](Workspace.assets/1559118367326.png)

- `git checkout -b 【branch】`——创建一个新的分支，并切换

![1559123002253](Workspace.assets/1559123002253.png)

## 查

- `git status`——显示状态变化

![1559118403204](Workspace.assets/1559118403204.png)

- `git diff HEAD -- 【file】`——工作区对比版本库内容不同

![1559121865361](Workspace.assets/1559121865361.png)

## 改

- `git reset –-hard HEAD~【版本号】`——版本回退

> 先是两次提交，版本回退到第一版

![1559119544008](Workspace.assets/1559119544008.png)

- `git reset –-hard 【版本id】`——版本切换

> 再回退到版本二

![1559119823572](Workspace.assets/1559119823572.png)

- `git checkout -- 【file】`——丢弃工作区的改动

> 丢弃改动删除的又回来了

![1559122341857](Workspace.assets/1559122341857.png)

- `git checkout 【branch】`——切换分支

![1559123162346](Workspace.assets/1559123162346.png)

## 删

- 

## 合并

- `git merge 【branch】`——快速合并分支*Fast-forward*

![1559123499716](Workspace.assets/1559123499716.png)

