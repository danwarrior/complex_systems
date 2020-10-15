# logistic_map
Plot to show bifurcations in the logistic map

![Logistic Plot](/logistic_map/images/logistic_plot.png)

## Example
```
python logistic_map.py x0 r_min r_max iterations
```
```
python logistic_map.py 0.001 2.5 4 1000
```
<img src="https://render.githubusercontent.com/render/math?math=f(x) = rx(1-x)">

* **x0**: initial condition
* **r_min**: min value for parameter r
* **r_max**: max value for parameter r
* **iterations**: number of time iterations to evolve the system

## Output
The output plot will de saved as **/logistic_map/plot/logistic_plot.png**
