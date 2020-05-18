# Lab 4

#### Выбор  максимально возможного темпа обучения
* Оранжевый - lr=0.01
* Синий - lr=0.001
* Красный - lr=0.0001
* Голубой -  lr=0.00001
![lr](/graf/lr.png)
Так как при lr=0.00001 принимает наименьшее значение из всех значений функций потерь, то это значение выбрано как  максимально возможный темп обучения
##  Горизонтальное отражение
![flip](/graf/flip.png)
## Поворот на случайный угол
* Красный 30
* Синий 45
* Оранжевый 60
![rotate](/graf/rotate.png)
На обучающей выборке все три эксперимента ведут себя практически одинаково. На валидационных графиках выделяется оранжевый.
##### Оптимальный параметр - угол поворота 60
## Изменение яркости и контраста
 * Оранжевый   
- [x] tf.image.random_brightness(image, 0.5, seed=None)
- [x] tf.image.random_contrast(image, lower=0.2, upper=1.2 seed=None)
* Синий 
- [x] tf.image.random_brightness(image, 0.4, seed=None)
- [x] tf.image.random_contrast(image, lower=0.1, upper=1.1 seed=None)
* Красный 
- [x] tf.image.random_brightness(image, 0.6, seed=None)
- [x] tf.image.random_contrast(image, lower=0.3, upper=1.3 seed=None)
![contrast](/graf/contrast.png)
### Сравнение
![zoom](/graf/zoom_contrast.png)
На обучающей выборке все три эксперимента ведут себя практически одинаково. Разброс по точности у всех на валидационной выборке практически одинаковый. На графиках  валидационной точности видно, что сеть обучается.
Оранжевый на обучающей выборке сходится быстрее всех.
##### Оптимальный параметр - параметры, соответсвующие оранжевому графику

## Использование случайного участка изображения
* Розовый - размер участка  300 х 300
* Голубой - размер участка  400 х 400
* Бирюзовый - размер участка  500 х 500
![crop](/graf/crop.png)
Бирюзовый на обучающей выборке сходится быстрее всех. Розовый и голубой сходятся медленно, чем бирюзовый. На валидационных графиках все ведут себя практически одинаково.
##### Оптимальный параметр - размер участка 500 х 500

## Использование всех оптимальных параметров

![all](/graf/all.png)


