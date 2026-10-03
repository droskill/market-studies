"""Render the Twitter/OG card (1200x630) for the Weinstein stage-analysis study."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, os

BG='#0f1113'; INK='#eef0f1'; MUT='#9aa0a6'; GRID='#2b2f33'
SAFE='#4d92e8'; CLAIM='#e0603a'; POS='#20b184'; CRIT='#e15a51'

# market-excess forward return by stage (13-week, annualized %)
stages=['Stage 1\nBasing','Stage 2\nAdvancing','Stage 3\nTopping','Stage 4\nDeclining']
xs=[0.6, 2.3, 1.4, 0.4]
cols=[MUT, POS, MUT, MUT]

fig=plt.figure(figsize=(12,6.3),dpi=100); fig.patch.set_facecolor(BG)
ax=fig.add_axes([0.06,0.17,0.58,0.46]); ax.set_facecolor(BG)

x=np.arange(len(stages))
ax.axhline(0,color=GRID,lw=1.2,zorder=1)
ax.bar(x,xs,0.62,color=cols,zorder=3)
for xi,v in zip(x,xs):
    ax.text(xi, v+0.06, f'{v:+.1f}', ha='center', va='bottom',
            color=cols[xi], fontsize=12, fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(stages,color=MUT,fontsize=10.5)
ax.set_ylim(0,2.8); ax.set_yticks([])
for sp in ax.spines.values(): sp.set_visible(False)
ax.tick_params(length=0)
fig.text(0.06,0.075,'market-excess forward return by stage, point-in-time S&P 500 · 1992-2026 · '
         'only Stage 2 (= a rising 30-week MA) beats the market',
         color=MUT,fontsize=10)

fig.text(0.06,0.905,'Is stage analysis just a moving average?',color=INK,fontsize=30,fontweight='bold')
fig.text(0.06,0.815,'Weinstein\'s Stage 2 works because it IS a trend filter. The rest is inert.',
         color=POS,fontsize=15,fontweight='bold')

rx=0.68
fig.text(rx,0.60,'BASING vs TOPPING, FLAT-MA WEEKS',color=MUT,fontsize=10,family='monospace')
fig.text(rx,0.485,'-0.6%',color=CLAIM,fontsize=38,fontweight='bold')
fig.text(rx,0.43,'/yr  (t = -0.5) — the memory adds nothing',color=MUT,fontsize=10)
fig.text(rx,0.325,'0.85 = 0.85',color=SAFE,fontsize=20,fontweight='bold')
fig.text(rx,0.275,'Full Weinstein Sharpe = plain MA filter',color=MUT,fontsize=10)
fig.text(rx,0.175,'+6.3%',color=CRIT,fontsize=20,fontweight='bold')
fig.text(rx,0.125,'/yr survivorship bias in naive',color=MUT,fontsize=10)
fig.text(rx,0.090,'backtests using today\'s members',color=MUT,fontsize=10)

fig.text(0.06,0.028,'901,533 stock-weeks · Norgate point-in-time S&P 500 · Fama-MacBeth · Bento Analytics',
         color=MUT,fontsize=9.5,family='monospace')

out=os.path.join(os.path.dirname(__file__),'og-cover.png')
fig.savefig(out,facecolor=BG); print('wrote',out)
