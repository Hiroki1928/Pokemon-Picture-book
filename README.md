# Pokemon-Picture-book  

## Overview  
* Pokemon picture book chatbot in Slack  

## Operating environment
* Python 3.7.1(Anaconda)  
* Library  
  * xlrd  
  * slackbot

```
$ pip install slackbot
$ pip install xlrd
```

## Specification  
* When comment "Pokemon" on the bot, it responds randomly pokemon info  
  * Probability is equal

```
@ポケモン ポケモン

@UserName: 
No.41 ズバット(Zubat)
こうもりポケモン
高さ：0.8m 重さ：7.5kg
タイプ１： どく
タイプ２：ひこう
```


* When comment Pokemon name on the bot, the Pokemon information  responds

```
@ポケモン ピカチュウ

@UserName: 
No.25 ピカチュウ(Pikachu)
ねずみポケモン
高さ：0.4m 重さ：6.0kg
タイプ１： でんき
タイプ２：ー
```

* The Pokémon type is first generation, 151 pokemons  

## Execution procedure  
### From local PC  
* Library installation  

```
$ pip install slackbot
$ pip install xlrd
```

* Execute run.py  
* Comment to bot in Slack  

### From Heroku

Push this repository and comment to bot  

## Reference site  
* https://qiita.com/sukesuke/items/1ac92251def87357fdf6  
* https://qiita.com/kunitaya/items/690028e33ba5c666f3e2
* https://note.nkmk.me/python-xlrd-xlwt-usage/