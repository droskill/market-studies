"""Render the Twitter/OG card (1200x630) for the Hindenburg Omen study."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, os

BG='#0f1113'; INK='#eef0f1'; MUT='#9aa0a6'; GRID='#2b2f33'
SAFE='#4d92e8'; CLAIM='#e0603a'; POS='#20b184'; CRIT='#e15a51'

# forward SPY return after a Hindenburg signal, by horizon (%)
hz=['5d','10d','20d','40d','60d','120d']
fr=[-0.16,-0.17,-0.68,0.16,0.62,3.03]
cols=[CLAIM if v<0 else POS for v in fr]

fig=plt.figure(figsize=(12,6.3),dpi=100); fig.patch.set_facecolor(BG)
ax=fig.add_axes([0.06,0.17,0.58,0.46]); ax.set_facecolor(BG)

x=np.arange(len(hz))
ax.axhline(0,color=GRID,lw=1.2,zorder=1)
ax.bar(x,fr,0.60,color=cols,zorder=3)
for xi,v in zip(x,fr):
    ax.text(xi, v+(0.10 if v>=0 else -0.10), f'{v:+.2f}', ha='center',
            va='bottom' if v>=0 else 'top',
            color=cols[xi], fontsize=11.5, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(hz,color=MUT,fontsize=11)
ax.set_ylim(-1.1,3.5); ax.set_yticks([])
for sp in ax.spines.values(): sp.set_visible(False)
ax.tick_params(length=0)
fig.text(0.06,0.075,'average SPY return after a signal, by trading-day horizon · '
         'red for ~a month, then the market\'s drift wins',
         color=MUT,fontsize=10)

fig.text(0.06,0.905,'Does the Hindenburg Omen work?',color=INK,fontsize=30,fontweight='bold')
fig.text(0.06,0.815,'A mild one-month chill — not the crash siren it\'s famous for.',
         color=POS,fontsize=15,fontweight='bold')

rx=0.68
fig.text(rx,0.60,'NEXT 20 DAYS, AFTER A SIGNAL',color=MUT,fontsize=10,family='monospace')
fig.text(rx,0.485,'-0.68%',color=CLAIM,fontsize=38,fontweight='bold')
fig.text(rx,0.43,'/20d  vs +0.95% baseline — real, but mild',color=MUT,fontsize=10)
fig.text(rx,0.325,'19% vs 9%',color=CRIT,fontsize=20,fontweight='bold')
fig.text(rx,0.275,'>15% drop in 60d, 3+ cluster — 81% false alarm',color=MUT,fontsize=10)
fig.text(rx,0.175,'0.78 > 0.66',color=SAFE,fontsize=20,fontweight='bold')
fig.text(rx,0.125,'cash-20d overlay Sharpe beats buy & hold,',color=MUT,fontsize=10)
fig.text(rx,0.090,'and a shallower drawdown (-49.8 vs -55.2%)',color=MUT,fontsize=10)

fig.text(0.06,0.028,'214 signals · S&P 1500 breadth · SPY total return · 1995-2026 · Norgate Data',
         color=MUT,fontsize=9.5,family='monospace')

out=os.path.join(os.path.dirname(__file__),'og-cover.png')
fig.savefig(out,facecolor=BG); print('wrote',out)
