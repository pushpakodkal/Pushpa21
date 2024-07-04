import numpy as np
import matplotlib.pyplot as plt
days=["jul-5","jul-6","jul-7","jul-8","jul-9","jul-10","jul-11","jul-11","jul-12","jul-12"]
temperature=[21,21,29,26,28,29,29,31,30,30]
Humidity=[28,28,28,28,28,29,29,28,27,26]
ypos=np.arange(len(days))
plt.bar(ypos-0.2,temperature,color="pink",width=0.4)
plt.bar(ypos+0.2,Humidity,color="g",width=0.4)
plt.xticks(ypos,temperature)
plt.xlabel("No of Days")
plt.ylabel("Temperature")
plt.title("Weather forecasting")
plt.legend(loc="upper right")
