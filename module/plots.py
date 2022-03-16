import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import os

def func(pct, allvals):
            absolute = int(np.round(pct/100.*np.sum(allvals)))
            return "{:.1f}%\n({:d} min)".format(pct, absolute)

def plots():
    path = './records'
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if filename!=".gitkeep":
            if os.path.isfile(f) :
                fig, ax = plt.subplots(figsize=(15, 10), subplot_kw=dict(aspect="equal"))
                file=open('./records/'+filename, 'r')
                ingredients = []
                recipe = []
                for line in file:
                    if(line.split("\t")[0] not in ingredients):
                        ingredients.append((line.split("\t")[0]))
                        recipe.append(30)
                    else:
                        index = ingredients.index(line.split("\t")[0])
                        recipe[index] += 30
    
            data = [x for x in recipe]
            file.close()

            wedges, texts, autotexts = ax.pie(data, radius=1.2, autopct=lambda pct: func(pct, data),
                                        textprops=dict(color="w"))

            ax.legend(wedges, ingredients,
                title="Streamers",
                title_fontsize=20,
                loc=2,
                bbox_to_anchor=(1, 0, 0.5, 1), prop={'size': 20})

            plt.setp(autotexts, size=15, weight="bold")

            ax.set_title(filename[:-4], loc="center", size=30)


            plt.savefig('./plots/'+filename[:-4]+".png")