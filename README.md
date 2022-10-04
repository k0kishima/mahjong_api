# 麻雀API

## 概要

[MahjongRepository/mahjong](https://github.com/MahjongRepository/mahjong) が提供しているモジュールを利用するためのAPIです。

## ローカルでの実行例

Dockerを使う感じはこんな感じです。

```bash
$ git@github.com:k0kishima/mahjong_api.git
$ cd mahjong_api
$ docker run --rm -it -v $PWD:/webapp -w /webapp -p 58000:8000 --network=default python:3.9 bash -c "pip3 install -r requirements.txt && python3 manage.py runserver 0:8000"
```

## APIのインターフェース

### シャンテン数の取得

**リクエスト**

```bash
$ curl http://127.0.0.1:58000/api/hands/234567m12399p234s/shanten | jq
```

**レスポンス**

```json
{
  "shanten": -1
}
```

### 待ち牌の取得


**リクエスト**

```bash
$ curl http://127.0.0.1:58000/api/hands/2367m2399p23456s/shanten_advanceable_tiles | jq
```

**レスポンス**

```json
{
  "shanten_advanceable_tiles": [
    [
      "MAN",
      1
    ],
    [
      "MAN",
      4
    ],
    [
      "MAN",
      5
    ],
    [
      "MAN",
      8
    ],
    [
      "PIN",
      1
    ],
    [
      "PIN",
      4
    ],
    [
      "SOU",
      1
    ],
    [
      "SOU",
      4
    ],
    [
      "SOU",
      7
    ]
  ]
}
```
