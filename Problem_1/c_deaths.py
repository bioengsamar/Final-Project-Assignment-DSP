#  Author:- Anurag Gupta # email:- 999.anuraggupta@gmail.com
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep
from PIL import Image
#### ---- Step 1:- Download data
URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(URL_DATASET, usecols = ['Date', 'Country', 'Deaths'])
#print(df.head(250)) # uncomment this to see output

#### ---- Step 2:- Create list of all dates
list_dates = df['Date'].unique()
#print(list_dates) # Uncomment to see the dates

#### --- Step 3:- Pick 5 countries. Also create ax object
fig, ax = plt.subplots(figsize=(15, 8))
# We will animate for these 5 countries only
list_countries = ['India', 'China', 'US', 'Italy', 'Spain']
# colors for the 5 horizontal bars
list_colors = ['black', 'red', 'green', 'blue', 'yellow']

### --- Step 4:- Write the call back function
# plot_bar() is the call back function used in FuncAnimation class object
def plot_bar(some_date):
    df2 = df[df['Date'].eq(some_date)]
    ax.clear()
    # Only take Confirmed column in descending order
    df3 = df2.sort_values(by = 'Deaths', ascending = False)
    # Select the top 5 Confirmed countries
    df4 = df3[df3['Country'].isin(list_countries)]
#    print(df4)  # Uncomment to see that dat is only for 5 countries
    sleep(0.2)  # To slow down the animation
#   ax.barh() makes a horizontal bar plot.
    return ax.barh(df4['Country'], df4['Deaths'], color= list_colors)


###----Step 5:- Create FuncAnimation object---------
anim = animation.FuncAnimation(fig = fig, func = plot_bar,
                    frames= list_dates, blit=True,
                    interval=20)

### --- Step 6:- Save the animation to an mp4
# Place where to save the mp4. Give your file path instead

path_Gif = r'C:\Users\bisho\Documents\GitHub\sbe309-2020-final-assignment-19_sbe309_20_final\Problem_1\draft\Covid Bars\GIF\Deaths\Deaths_covid2.gif' #this should be changed
#writervideo = animation.FFMpegWriter(fps=60) 
#anim.save(path_mp4, writer=writervideo)

writergif = animation.PillowWriter(fps=10) 
anim.save(path_Gif, writer=writergif)

#path_mp4 = r'C:\Users\bisho\Documents\Python MP4\population_covid2.mp4'  
## my_anim.save(path_mp4, fps=30, extra_args=['-vcodec', 'libx264'])
#anim.save(filename = path_mp4, writer = 'ffmpeg',
#             fps=30,
#             extra_args= ['-vcodec', 'libx264', '-pix_fmt', 'yuv420p'])
plt.show()

#im = Image.open('C:\Users\bisho\Documents\Python MP4\Deaths_covid2.gif')