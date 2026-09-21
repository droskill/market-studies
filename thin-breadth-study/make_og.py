"""Render the OG/Twitter card (1200x630) for the thin-breadth study."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

BG='#0f1113'; INK='#eef0f1'; MUT='#9aa0a6'; GRID='#2b2f33'
SAFE='#4d92e8'; CLAIM='#e0603a'; POS='#20b184'; CRIT='#e15a51'

# forward 12-month S&P 500 total return after an index high, by how thin breadth was
LABELS=['Thinnest\nbreadth\n(<6%)','Broad\nbreadth\n(≥12%)','An ordinary\nday']
VALS=[14.1, 12.4, 12.3]
COLS=[POS, SAFE, MUT]

fig=plt.figure(figsize=(12,6.3),dpi=100); fig.patch.set_facecolor(BG)
ax=fig.add_axes([0.075,0.17,0.50,0.42]); ax.set_facecolor(BG)
x=range(len(VALS))
bars=ax.bar(x,VALS,color=COLS,width=0.62,zorder=3)
ax.axhline(0,color=GRID,lw=1)
ax.set_ylim(0,16.5); ax.set_xlim(-0.6,2.6)
ax.set_xticks(list(x)); ax.set_xticklabels(LABELS,color=MUT,fontsize=9.5)
ax.set_ylabel('forward 12-mo return  (%)',color=MUT,fontsize=10)
ax.tick_params(colors=MUT,labelsize=8,length=0)
for sp in ax.spines.values(): sp.set_color(GRID)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.grid(axis='y',alpha=0.13)
for xi,v,c in zip(x,VALS,COLS):
    ax.text(xi,v+0.5,f'+{v:.1f}',color=c,fontsize=13,fontweight='bold',ha='center')

fig.text(0.075,0.905,'When breadth is thin,',color=INK,fontsize=30,fontweight='bold')
fig.text(0.075,0.818,'what does the market do? Historically: about fine.',
         color=POS,fontsize=14.5,fontweight='bold')

rx=0.635
fig.text(rx,0.585,'AFTER A HIGH ON THE THINNEST BREADTH',color=MUT,fontsize=9.5,family='monospace')
fig.text(rx,0.470,'+14%',color=POS,fontsize=40,fontweight='bold')
fig.text(rx,0.415,'avg 12-mo return — beats an ordinary day',color=MUT,fontsize=10.5)
fig.text(rx,0.310,'80%',color=SAFE,fontsize=23,fontweight='bold')
fig.text(rx,0.258,'positive after the “worst breadth in 100 yrs”',color=MUT,fontsize=10.5)
fig.text(rx,0.158,'0',color=CLAIM,fontsize=23,fontweight='bold')
fig.text(rx,0.106,'breadth rules that beat a 200-day line',color=MUT,fontsize=10.5)

fig.text(0.075,0.028,'S&P 500 breadth & forward returns, 1993-2026 - Norgate Data - @droskill',
         color=MUT,fontsize=9.5,family='monospace')
out=os.path.join(os.path.dirname(__file__),'og-cover.png')
fig.savefig(out,facecolor=BG); print('wrote',out)
