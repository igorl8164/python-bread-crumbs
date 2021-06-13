#### Встроенные типы объектов 

`int float str bool list dict tuple set file `

#### Операции над числами

`+ - * / ** // %`

#### Приоритеты операций
слева на право убывает

в порядку убывания

```
()
**
* / // %
+ -
```

Встроенные операции

```python
abs(value)
min(x1, x2, x3, ...)
max(x1, x2, x3, ...)
pow(x, y)
round(float, ndigits)
type(obg)
```

модуль math

ключевые слова 

```python
False class finally is return
None continue for lambda try
True def from nonlocal while 
and del global not with
as elif if or yield
assert else import pass 
break except in rise
```

массовое присвоение 

a=b=c=d=1

множественное присвоение

a, b = 2, 1

ввод данных 

a=input('comment')

int(a)

int('4.5')  ошибка

float('10')  float('2.5')

a, b, c= map(int, input().split(" "))

print(a, sep=' - ', end='\n')

print('xxx %s gghj %s' % (a, b) )

trunc отсечь   floor округление вниз  ceil  округление вверх  модуль math

операторы сравнения >  <  >=  <=  ==  !=  инверсия not  конъюнкция and дизъюнкция or

приоритет not and or

строки ''' kjb '''    """bhvhjvj"""   "klnkjb'bkhv'knjb"    'kn"lkm"lnbnjkb'

concatenate  - сцепление + строк

'lkklk'*3

length()

'j' in 'bhvh'

'' == ''

'jbj'>'m'

ord('b')  код символа

### методы строк

s.upper 

s.lower

s.coutn(sub, start, end)  количество вхождений

s.find(str) найти индекс подстроки или -1 не найдено

s.rfind искать с конца с права

s.index(str)  искать индекс, исключение если не найдено

s.replace(old, new, count) замена в строке

s.isalpha() проверка состоит ли только из букв

s.isdigit() только из цифр

s.rjust(n, 's') расширить строку в право  

s.ljust() влево

s.split() разделить строку

 ' '.join(l)  список в строку с разделителем

s.strip()  удалить справа слева все пробелы и служебные символы '\n'

s.rstrip()  только справа

s.lstrip() только слева

 isupper, islower, isalnum проверки

capitalize  заглавный символ только первого слова

title заглавные первые символы слов 

swapcase инверсия всех букв

startswith, endswith поиск в строке (соответствие на подстроку)

### Служебные символы

```\newline``` продолжение на новой строке

``` \\``` символ обратного слэша

``` \'``` апостроф

``` \"``` кавычка

``` \a``` звонок

``` \b``` забой

``` \f```  перевод формата

``` \v``` новая строка

``` \r``` возврат каретки

``` \t``` горизонтальная табуляция 

``` \v``` вертикальная табуляция

r'string' сырая строка не воспринимает служебные символы

```r'''nnb```

 ```jb''' ```

### Форматирование строк format

```python
""" kljjk {0} lkh bj {1} lnmn
hjkghh g{3} """.format(name, min, balance)
позиционное использование
```

```python
""" kljjk {n} lkh bj {k} lnmn
hjkghh g{b} """.format(n=name, k=min, b=balance)
позиционное именное
```

### F-строка
```python
f""" hello {name} kgghf {d['ky']} """
```



### Списки

bl = [] bl = list() пустой список

``` python
a = [True, 10, 'hello', 5.6, [4, 6, 5]] # пример списка
```

len(a) длинна списка

[12, 14] + ['1', 100] сцепление (сложение) списков

a += ['h', 5] расширение списка

['h', 'l']*5 дублирование списка

`4.5 in [True, 10.2, 5, 100, 4.5, 5.4]` проверка вхождения союзом in

max min sum для списков из чисел

sorted(list)  сортировка по возрастанию

sorted(l, reverse=True) в обратном порядке

[100, 3] > [34, 100, 2]  сравнения списков (поэлементно)

[1, 2, 3]==[1, 2, 3]

a[0] первый элемент

a[-1] последний элемент

a[1:4] срез (последний индекс не включается)

a[2:-1] по пред последний

a[2:999] 

a[2:] со второго и по конец

a[:4] с начало и до минус один

a[:] весь список

a[::2] с шагом

 a[::-1] реверс

a[2] = 10 список изменяемый объект 

a[3:5] = 34, 23

a[2:5] = 23, 34 вставит значения и удалит недостающие до вставке

del a[2]  удалить элемент списка

b = a[:] сохранить копию списка

 append

clear

copy

[]

count

extend

index

in

insert

pop

remove

reverse

sort reverse 

### условия

if  :

​	print()

else:

​	print()

if  :

​	print()

elif:

elif:

elif:

else:

​	print()



### циклы

while

break continue else



i ** 2 <=n:

 

