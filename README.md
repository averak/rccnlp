# rccnlp

[![PyPi](https://badge.fury.io/py/rccnlp.svg)](https://pypi.python.org/pypi/rccnlp/)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

RCC 自然言語処理班で使うツールキットです。

## 実行環境

- Python 3

## インストール

```sh
$ pip install rccnlp
```

## 使い方

### センチメント分析
```python
from rccnlp.sentiment import Analyzer
analyzer = Analyzer()

analyzer.analyze('天国で待ってる。')
# => [1.0]
analyzer.analyze('遅刻したけど楽しかったし嬉しかった。すごく充実した！')
# => [0.3333333333333333, 1.0]

analyzer.count_polarity('遅刻したけど楽しかったし嬉しかった。すごく充実した！')
# => [{'positive': 2, 'negative': 1}, {'positive': 1, 'negative': 0}])
analyzer.count_polarity('そこにはいつもと変わらない日常があった。')
# => [{'positive': 0, 'negative': 0}]

analyzer.analyze_detail('お金も希望もない！')
# => [{'positive': [], 'negative': ['お金-NEGATION', '希望-NEGATION'], 'score': -1.0}])
analyzer.analyze_detail('お金がないわけではない')
# => [{'positive': ['お金'], 'negative': [], 'score': 1.0}]
```
