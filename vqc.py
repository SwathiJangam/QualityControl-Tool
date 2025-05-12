import tkinter as tk     #To create GUI application 
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry   #For selecting of the date from the user
import pandas as pd                #For reading data and analysis
from datetime import datetime      #To convert into time series
import matplotlib.pyplot as plt    #To create plot graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk   #To add plot graph on to the GUI window and to create toolbar to the graphs 
import matplotlib.dates as mdates
from mpl_toolkits.basemap import Basemap    #To create the world map
from matplotlib.figure import Figure
from matplotlib.widgets import RectangleSelector     #To create the box selection in the plot graphs

top=tk.Tk()    # Create a Tkinter application window
top.title("INCOIS")   #Create title to the application window
top.geometry('1536x864')   #To create length and width size of the application window
Label(top,text='VQC Tool',font=("Arial", 30)).place(x=30,y=10)  #create a label with text 'VQC TOOL'
frame1=LabelFrame(top,width=500,height=804,bg='#999999' )      #Grouping and organizing other widgets in application window
frame1.place(x=0,y=60)        #placing the frame on the application window
canvas = tk.Canvas(top,width=1036,height=804)
canvas.place(x=500,y=60)
frame2=Frame(canvas)
frame2.place(x=500,y=60)
Label(frame1,text='Platform :',font=30,bg='#999999').place(x=20,y=20)
options = ["mumbai"]
combobox = ttk.Combobox(frame1, values=options, state='readonly', width=30,justify='center',font=30)
combobox.place(x=130,y=20)
Label(frame1,text='Date Range ',font=30,bg='#999999').place(x=20,y=60)
sd=DateEntry(frame1,selectmode='day',font=45,justify='center',width=12)     #create calendar and selection of date 
sd.place(x=20,y=105)
Label(frame1,text='To',font=45,bg='#999999').place(x=200,y=105)
ed=DateEntry(frame1,selectmode='day',font=45,justify='center',width=12)
ed.place(x=250,y=105)

mapd=pd.read_excel(r"C:\Users\swathi\miniproj\incoisdata.xlsx")
mapd = pd.DataFrame(mapd)
c=Canvas(frame1)     #create of canvas and place map on to that canvas
c.place(x=20,y=250)
fig = plt.Figure(figsize=(4.4, 3.4))
basemap = Basemap(projection='cyl', resolution='l', ax=fig.add_subplot(111))   #create of world map
basemap.ax.set_position([0, 0.08, 0.995, 0.85])     #map dimensions
basemap.drawcoastlines()
basemap.drawcountries()
basemap.drawstates()
canvasm = FigureCanvasTkAgg(fig, master=c)     #importing the map on to the application window
canvasm.draw()


canvasm.get_tk_widget().pack()
toolbar1 = NavigationToolbar2Tk(canvasm, c)
toolbar1.update()

	
df1=pd.read_csv(r"C:\Users\swathi\miniproj\maindata.csv")    #Reading the data from the CSV file
df1 = pd.DataFrame(df1)       # 2 dimensional labeled data structure
df1['date'] = pd.to_datetime(df1['date'], format='%Y-%m-%d')    #conversion of string to time format for dates in data 

# create a Matplotlib figure	
figure = plt.Figure(figsize=(10.6, 7.4), dpi=100)
ax1,ax2,ax3= figure.subplots(3, sharex=True)
a,=ax1.plot(df1.date,df1.meantemp, marker='o',alpha=0.5)      #plotting of data in the graph
b,=ax2.plot(df1.date,df1.meanpressure,marker='o',alpha=0.5)
d,=ax3.plot(df1.date,df1.humidity,marker='o',alpha=0.5)
line = FigureCanvasTkAgg(figure, master=frame2)          #importing of graph onto the GUI application window
def onselect(eclick, erelease):     #creation of function with name onselect
    rs2.set_visible(False)     #To keep the box selection visible or not on the graph 
    rs3.set_visible(False)
    rs1.set_visible(False)
    global xmin, xmax, ymin, ymax
    xmin, xmax = sorted([eclick.xdata, erelease.xdata])     #To get ranges of the x-axis and y-axis from the box selection
    ymin, ymax = sorted([eclick.ydata, erelease.ydata])
    xmind= mdates.num2date(xmin)                            #conversion of dates
    xmaxd=mdates.num2date(xmax)
    date_string = xmind.strftime('%Y-%m-%d %H:%M:%S')
    date_string1 = xmaxd.strftime('%Y-%m-%d %H:%M:%S')
    xmind = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    xmaxd = datetime.strptime(date_string1, '%Y-%m-%d %H:%M:%S')
    df1['date'] = df1['date'].dt.to_pydatetime()
    selected_data = df1[(df1['date'] >= xmind) & (df1['date'] <= xmaxd) & (df1['meantemp'] >= ymin) & (df1['meantemp'] <= ymax)]
    a.set_data(df1['date'], df1['meantemp'])
    ax1.draw_artist(a)
    def red(): 
        ax1.scatter(selected_data['date'], selected_data['meantemp'], color='red', s=30)
        df1.loc[selected_data.index,'flag']=4
        df1.to_csv(r'C:\Users\swathi\miniproj\maindata.csv' , index=False)
        ax1.relim()
        ax1.autoscale_view()
        line.draw()
    def blue():   
        ax1.scatter(selected_data['date'], selected_data['meantemp'], color='blue', s=30)
        df1.loc[selected_data.index,'flag']=3
        df1.to_csv(r'C:\Users\swathi\miniproj\maindata.csv' , index=False)
        ax1.relim()
        ax1.autoscale_view()
        line.draw()
    def green():   
        ax1.scatter(selected_data['date'], selected_data['meantemp'], color='green', s=30)
        df1.loc[selected_data.index,'flag']=2
        df1.to_csv(r'C:\Users\swathi\miniproj\maindata.csv' , index=False)
        ax1.relim()
        ax1.autoscale_view()
        line.draw()
    def yellow():    
        ax1.scatter(selected_data['date'], selected_data['meantemp'], color='yellow', s=30)
        df1.loc[selected_data.index,'flag']=1
        df1.to_csv(r'C:\Users\swathi\miniproj\maindata.csv' , index=False)
        ax1.relim()
        ax1.autoscale_view()
        line.draw()
    #def delete():
       # csv_file_path= r'C:\Users\91934\maindata.csv'
    #    df = pd.read_csv(csv_file_path) 
    #    df = df[df['flag'] != 4]
   #     df.to_csv(csv_file_path, index=False)
    button = tk.Button(frame1, text="   4   ",command=red).place(x=40,y=670)
    button = tk.Button(frame1, text="   3   ",command=blue).place(x=120,y=670)
    button = tk.Button(frame1, text="   2   ",command=green).place(x=200,y=670)
    button = tk.Button(frame1, text="   1   ",command=yellow).place(x=280,y=670)
    #button = tk.Button(frame1,text="Delete",command=delete).place(x=130,y=720)
#create of box selection for the graphs			
rect = plt.Rectangle((0,0), 0, 0, alpha=0.2, facecolor='blue', edgecolor='red', visible=False)
ax1.add_patch(rect)
rs = RectangleSelector(ax1, onselect, button=[1],minspanx=5, minspany=5, spancoords='pixels',interactive=True)
def delete():
     csv_file_path= r'C:\Users\swathi\miniproj\maindata.csv'
     df = pd.read_csv(csv_file_path) 
     df = df[df['flag'] != 4]
     df.to_csv(csv_file_path, index=False)
button = tk.Button(frame1,text="Delete",command=delete).place(x=130,y=720)
def onselect2(eclick, erelease):
    rs.set_visible(False)
    rs3.set_visible(False)
    rs1.set_visible(False)
    global xmin, xmax, ymin, ymax
    xmin, xmax = sorted([eclick.xdata, erelease.xdata])
    ymin, ymax = sorted([eclick.ydata, erelease.ydata])
    xmind= mdates.num2date(xmin)
    xmaxd=mdates.num2date(xmax)
    date_string = xmind.strftime('%Y-%m-%d %H:%M:%S')
    date_string1 = xmaxd.strftime('%Y-%m-%d %H:%M:%S')
    xmind = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    xmaxd = datetime.strptime(date_string1, '%Y-%m-%d %H:%M:%S')
    df1['date'] = df1['date'].dt.to_pydatetime()
    selected_data = df1[(df1['date'] >= xmind) & (df1['date'] <= xmaxd) & (df1['meanpressure'] >= ymin) & (df1['meanpressure'] <= ymax)]
    b.set_data(df1['date'], df1['meanpressure'])
    ax2.draw_artist(b)
    def red():   
        ax2.scatter(selected_data['date'], selected_data['meanpressure'], color='red')
        df1.loc[selected_data.index,'flag']=4
        df1.to_csv(r'C:\Users\swathi\miniproj\maindata.csv' , index=False)
        ax2.relim()
        ax2.autoscale_view()
        line.draw()
    def blue(): 
        ax2.scatter(selected_data['date'], selected_data['meanpressure'], color='blue') 
        df1.loc[selected_data.index,'flag']=3
        df1.to_csv(r'C:\Users\swathi\miniproj\maindata.csv' , index=False)
        ax2.relim()
        ax2.autoscale_view()
        line.draw()
    def green():
        ax2.scatter(selected_data['date'], selected_data['meanpressure'], color='green')
        df1.loc[selected_data.index,'flag']=2
        df1.to_csv(r'C:\Users\swathi\miniproj\maindata.csv' , index=False)
        ax2.relim()
        ax2.autoscale_view()
        line.draw()
    def yellow():   
        ax2.scatter(selected_data['date'], selected_data['meanpressure'], color='yellow')
        df1.loc[selected_data.index,'flag']=1
        df1.to_csv(r'C:\Users\swathi\miniproj\maindata.csv' , index=False)
        ax2.relim()
        ax2.autoscale_view()
        line.draw()
    button = tk.Button(frame1, text="   4   ",command=red).place(x=40,y=670)
    button = tk.Button(frame1, text="   3   ",command=blue).place(x=120,y=670)
    button = tk.Button(frame1, text="   2   ",command=green).place(x=200,y=670)
    button = tk.Button(frame1, text="   1   ",command=yellow).place(x=280,y=670)
			
rect2 = plt.Rectangle((0,0), 0, 0, alpha=0.2, facecolor='blue', edgecolor='red', visible=False)
ax2.add_patch(rect2)
rs2 = RectangleSelector(ax2, onselect2, button=[1],minspanx=5, minspany=5, spancoords='pixels',interactive=True)

def onselect3(eclick, erelease):
    rs.set_visible(False)
    rs2.set_visible(False)
    rs1.set_visible(False)
    global xmin, xmax, ymin, ymax
    xmin, xmax = sorted([eclick.xdata, erelease.xdata])
    ymin, ymax = sorted([eclick.ydata, erelease.ydata])
    xmind= mdates.num2date(xmin)
    xmaxd=mdates.num2date(xmax)
    date_string = xmind.strftime('%Y-%m-%d %H:%M:%S')
    date_string1 = xmaxd.strftime('%Y-%m-%d %H:%M:%S')
    xmind = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    xmaxd = datetime.strptime(date_string1, '%Y-%m-%d %H:%M:%S')
    df1['date'] = df1['date'].dt.to_pydatetime()
    selected_data = df1[(df1['date'] >= xmind) & (df1['date'] <= xmaxd) & (df1['humidity'] >= ymin) & (df1['humidity'] <= ymax)]
    d.set_data(df1['date'], df1['humidity'])
    ax3.draw_artist(d)
    def red():
        ax3.scatter(selected_data['date'], selected_data['humidity'], color='red')
        df1.loc[selected_data.index,'flag']=4
        df1.to_csv(r'C:\Users\swathi\miniproj\maindata.csv' , index=False)
        ax3.relim()
        ax3.autoscale_view()
        line.draw()
    def blue():
        ax3.scatter(selected_data['date'], selected_data['humidity'], color='blue')
        df1.loc[selected_data.index,'flag']=3
        df1.to_csv(r'C:\Users\swathi\miniproj\maindata.csv' , index=False)
        ax3.relim()
        ax3.autoscale_view()
        line.draw()
    def green(): 
        ax3.scatter(selected_data['date'], selected_data['humidity'], color='green')
        df1.loc[selected_data.index,'flag']=2
        df1.to_csv(r'C:\Users\swathi\miniproj\maindata.csv' , index=False)
        ax3.relim()
        ax3.autoscale_view()
        line.draw()
    def yellow():  
        ax3.scatter(selected_data['date'], selected_data['humidity'], color='yellow')
        df1.loc[selected_data.index,'flag']=1
        df1.to_csv(r'C:\Users\swathi\miniproj\maindata.csv' , index=False)
        ax3.relim()
        ax3.autoscale_view()
        line.draw()
    button = tk.Button(frame1, text="   4   ",command=red).place(x=40,y=670)
    button = tk.Button(frame1, text="   3   ",command=blue).place(x=120,y=670)
    button = tk.Button(frame1, text="   2   ",command=green).place(x=200,y=670)
    button = tk.Button(frame1, text="   1   ",command=yellow).place(x=280,y=670)
			
rect3 = plt.Rectangle((0,0), 0, 0, alpha=0.2, facecolor='blue', edgecolor='red', visible=False)
ax3.add_patch(rect3)
rs3 = RectangleSelector(ax3, onselect3, button=[1],minspanx=5, minspany=5, spancoords='pixels',interactive=True)



def onselect1(eclick, erelease):
    rs.set_visible(False)
    rs3.set_visible(False)
    rs2.set_visible(False)
    global xmmin, xmmax, ymmin, ymmax
    xmmin, xmmax = sorted([eclick.xdata, erelease.xdata])
    ymmin, ymmax = sorted([eclick.ydata, erelease.ydata])
    indices = (mapd['longitude'] >= xmmin) & (mapd['longitude'] <= xmmax) & (mapd['latitude'] >= ymmin) & (mapd['latitude'] <= ymmax)
    def red():
        basemap.scatter(mapd.loc[indices, 'longitude'], mapd.loc[indices, 'latitude'], c='red', edgecolors='red')
        fig.canvas.draw_idle()
    def blue():
        basemap.scatter(mapd.loc[indices, 'longitude'], mapd.loc[indices, 'latitude'], c='blue', edgecolors='blue')
        fig.canvas.draw_idle()
    def green():
        basemap.scatter(mapd.loc[indices, 'longitude'], mapd.loc[indices, 'latitude'], c='green', edgecolors='green')
        fig.canvas.draw_idle()
    def yellow():
        basemap.scatter(mapd.loc[indices, 'longitude'], mapd.loc[indices, 'latitude'], c='yellow', edgecolors='yellow')
        fig.canvas.draw_idle()
    button = tk.Button(frame1, text="   4   ",command=red).place(x=40,y=670)
    button = tk.Button(frame1, text="   3   ",command=blue).place(x=120,y=670)
    button = tk.Button(frame1, text="   2   ",command=green).place(x=200,y=670)
    button = tk.Button(frame1, text="   1   ",command=yellow).place(x=280,y=670)
			
rect1 = plt.Rectangle((0,0), 0, 0, alpha=0.2, facecolor='blue', edgecolor='red', visible=False)
basemap.ax.add_patch(rect1)
rs1 = RectangleSelector(basemap.ax, onselect1, button=[1],minspanx=5, minspany=5, spancoords='pixels',interactive=True)


def main():
	sdate=sd.get()       #getting dates from the user
	edate=ed.get()
	ssdate=datetime.strptime(sdate,'%m/%d/%y')
	eedate=datetime.strptime(edate,'%m/%d/%y')
	ax1.set_xlim(ssdate, eedate)     #setting the limits of the x-axis in the graph plot
	ax2.set_xlim(ssdate, eedate)
	ax3.set_xlim(ssdate, eedate)
	ax1.set_ylabel("Temperature(celsius)")    #setting the label to the y-axis in the graph plot
	ax2.set_ylabel("Pressure(pascal)")
	ax3.set_ylabel("Humidity(grams/m3)")
	ax3.set_xlabel("Time-series")
	basemap.scatter(mapd['longitude'], mapd['latitude'])   #plotting the data on to the map
	fig.canvas.draw_idle()
	canvasm.get_tk_widget().pack()
	line.draw()
	line.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
	#scrollbar = ttk.Scrollbar(top, orient=tk.VERTICAL, command=canvas.yview)
	#canvas.configure(yscrollcommand=scrollbar.set)
	canvas.create_window((0, 0), window=frame2, anchor='nw')

	#scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
	toolbar.update()		
	toolbar.pack( side=tk.TOP,fill=tk.X)
	
toolbar = NavigationToolbar2Tk(line, frame2)     #create toolbar for the graphs and it useful for zoom in and out 
toolbar.pack_forget()	
			
button = tk.Button(frame1, text="Plot",font=30,command=main).place(x=20,y=155)   #create of button in the application window and on click it runs main function

top.mainloop()