# rfile
import dateutil.parser
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy import select
import matplotlib.pyplot as plt
from matplotlib import cbook, dates
#from matplotlib.ticker import Formatter
import mplcursors
# %matplotlib widget
# this gives seperate window qt widget for figures
# %matplotlib qt5
eng = create_engine("mysql://rfile:simple@flatboy/rfile")
myconn = eng.connect()
# get data for sugar
sugeightdays = "SELECT `bsdate`,`bsugar` FROM `sugar` WHERE `bsdate` > DATE_SUB(NOW(), INTERVAL 8 DAY)" # took bsid out so only 1 interger for describe func
sugar8days = pd.read_sql_query(sugeightdays, myconn, parse_dates = "bsdate")
# start setting up figure
mylegend = "7 days stats "
mystats = sugar8days.describe(include='int')
fig3, ax3 = plt.subplots()
plt.ylim(60,150)
ax3.set_xlabel('Date')
plt.title('blood sugar last 8 days')
ax3.annotate([mystats], xy=(200, 380), xycoords='figure points')
plt.setp(ax3.get_xticklabels(), rotation = 90, fontsize=6)
#ax3.set_xticklabels(sugar8days.bsdate, rotation=90, fontsize=6)
plt.grid(b=True, which='both', axis='both', )
fig3.set_figwidth(10)
fig3.set_figheight(10)
lines = ax3.plot(sugar8days.bsdate , sugar8days.bsugar, marker='o', linestyle='dashed' )
mplcursors.cursor(lines) # or just mplcursors.cursor()
#  plt.show()

#blood pressure
bpsevendays = "SELECT `vsigns_bloodpressure`.`bpdate` ,`vsigns_bloodpressure`.`bpsys` AS `systolic`,`vsigns_bloodpressure`.`bpdia` AS `diastolic`,`vsigns_bloodpressure`.`bphr` AS `pulse` from  `vsigns_bloodpressure` WHERE `bpdate` > DATE_SUB(NOW(), INTERVAL 7 DAY)"
bp7days = pd.read_sql_query(bpsevendays, myconn, parse_dates = "bpdate")
x = np.arange(len(bp7days))  # the label locations
width = 0.35  # the width of the bars

# color picker gpick
fig , ax = plt.subplots()
rects1 = ax.bar(x - width/2, bp7days.systolic, width, label='systolic', facecolor='#00388F')
rects2 = ax.bar(x + width/2, bp7days.diastolic, width, label='diastolic', facecolor='#8F5600')
rects3 = ax.bar(x + width, bp7days.pulse, width, label='pulse', facecolor='#638F00')
ax.axhline(y=120, color='#00388F')
ax.axhline(y=80, color='#8F5600')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('120/80 = perfect')
ax.set_title('Blood press 7 days')
ax.set_xticks(x)
ax.set_xticklabels(bp7days.bpdate, rotation=90, fontsize=6)
ax.legend()

ax.bar_label(rects1, label_type='center', color='#EEEED0')
ax.bar_label(rects2, label_type='center')
ax.bar_label(rects3, label_type='center')
plt.rc('xtick', labelsize=6)
fig.set_figheight(10)
mplcursors.cursor(rects3)
mplcursors.cursor(rects2)


plt.show()