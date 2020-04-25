![](images/logo.png)

## Get started

Have you ever wondered why trees look like this?

We were inspired by the <a href="https://www.youtube.com/watch?v=WTh-gNZxTM8" target="_blank">foo52ru channel</a> and decided to simulate the evolution of trees. To do this, we use genetic algorithms and the PyGame library.

To start simulation, run this command:

``` python3 main.py ```

### Command line arguments
```
-o : folder name to save genom  |  default TreesGenoms

-i : genome conservation frequency  |   default None

-t : initial number of trees   |   default 10

--cli : non_gui mode  |  default False

--step_mode : step mode    | default False

--width  :  screen width    

--height : screen height

--pixel_size : pixels size 
```


### Examples

``` python3 ./main.py -t 20  -i 100  --width 1200 --height 1000 -o test ```

``` python3 ./main.py  -t 10 --cli --step_mode --pixel_size 15 ```

``` python3 ./main.py -t 20    --width 1200 --height=1000 ```

## Video about the project
[![](https://img.youtube.com/vi/9t3mAgyzeZM/0.jpg)](https://www.youtube.com/watch?v=9t3mAgyzeZM)

## License
<a href="http://opensource.org/licenses/MIT">MIT</a>

All rights belong to their respective owners
