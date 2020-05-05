# Lab5

### Пошаговое затухание (Step-Decay)
 * Оранжевый   
- [x] initial_lrate=0.00001
- [x] drop=0.2
- [x] epoch_drop=10
![step](/graf/step_1.png)
* Синий 
- [x] initial_lrate=0.00001
- [x] drop=0.5
- [x] epoch_drop=5
![step](/graf/step_2.png)
* Красный 
- [x] initial_lrate=0.00001
- [x] drop=0.7
- [x] epoch_drop=2
![step](/graf/step_3.png)
### Сравнение
![compare](/graf/step_compare.png)
На обучающей выборке oранжевый сходится быстрее всех. Точность на валидационной выборке у всех практически одинаковы. Ошибка на валидационной выборке: оранжевый наглядно имеет несколько высоких значений по сравнению с другими, синий и красный ведут себя практически одинаково. 
##### Оптимальный вариант: параметры, соответствующие синему графику
### Экспоненциальное затухание (Exponential Decay)
* Оранжевый
- [x] initial_lrate=0.00001
- [x] k=0.5
![exp](/graf/exp_1.png)
* Синий
- [x] initial_lrate=0.00001
- [x] k=0.1
![exp](/graf/exp_2.png)
* Красный
- [x] initial_lrate=0.0001
- [x] k=0.1
![exp](/graf/exp_3.png)
### Сравнение
![compare](/graf/exp_compare.png)

### Политика “предварительного разогрева” (Warm-Up)
* Оранжевый - Пошаговое затухание  
- [x] initial_lrate=0.00001
- [x] drop=0.5
- [x] epoch_drop=5
* Серый - Экспоненциальное затухание
- [x] initial_lrate=0.0001
- [x] k=0.1
![WarmUp](/graf/warm_up_compare.png)
