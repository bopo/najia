# 快速上手

## 使用最快的服务器

```shell
python -m najia bestip -vv
```

## 离线数据读取

```python
from najia import Najia

params = [2, 2, 1, 2, 0, 2]
result = Najia(2).compile(params=params, date='2019-12-25 00:20').render()
```
