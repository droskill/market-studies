"""Render the OG/Twitter card (1200x630) for the high-beta vs low-vol study."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json, os

BG='#0f1113'; INK='#eef0f1'; MUT='#9aa0a6'; GRID='#2b2f33'
SAFE='#4d92e8'; CLAIM='#e0603a'; POS='#20b184'; CRIT='#e15a51'

here = os.path.dirname(__file__)
with open(os.path.join(here, '_dd_data.json')) as f:
    D = json.load(f)

fig=plt.figure(figsize=(12,6.3),dpi=100); fig.patch.set_facecolor(BG)
ax=fig.add_axes([0.07,0.16,0.52,0.50]); ax.set_facecolor(BG)
ax.plot(D['hb_x'], D['hb_y'], color=CLAIM, lw=2.0, zorder=3, label='High-beta decile')
ax.plot(D['lv_x'], D['lv_y'], color=SAFE, lw=1.8, zorder=3, label='Low-vol decile')
ax.axhline(0,color=GRID,lw=1.2)
ax.annotate('Oct 2002: -97.8%', xy=(2002.7,-96), xytext=(2003.3,-56),
            color=CLAIM, fontsize=11, fontweight='bold', ha='left',
            arrowprops=dict(arrowstyle='-', color=CLAIM, lw=1.1))
ax.set_xlim(1994,2026.7); ax.set_ylim(-105,8)
ax.set_ylabel('drawdown from peak',color=MUT,fontsize=10)
ax.tick_params(colors=MUT,labelsize=8.5)
for sp in ax.spines.values(): sp.set_color(GRID)
ax.grid(axis='y',alpha=0.13)
ax.legend(loc='upper left', fontsize=9, facecolor=BG, edgecolor=GRID, labelcolor=INK, framealpha=0.85)

fig.text(0.07,0.905,'Does high beta leading low vol mean anything?',color=INK,fontsize=24.5,fontweight='bold')
fig.text(0.07,0.825,'A real 32-year pattern — a coin flip the moment I tried to trade it.',
         color=POS,fontsize=14,fontweight='bold')

rx=0.63
fig.text(rx,0.60,'SHARPE EDGE, 32 YEARS',color=MUT,fontsize=10,family='monospace')
fig.text(rx,0.49,'+0.31',color=SAFE,fontsize=38,fontweight='bold')
fig.text(rx,0.435,'High-Beta-leading days vs Low-Vol-leading',color=MUT,fontsize=10.5)

fig.text(rx,0.325,'-27.8% vs -14.2%',color=CLAIM,fontsize=19,fontweight='bold')
fig.text(rx,0.275,'2008: Low-Vol-leading days vs High-Beta days',color=MUT,fontsize=10.5)

fig.text(rx,0.165,'51%',color=CRIT,fontsize=22,fontweight='bold')
fig.text(rx,0.115,'overfitting score when I tried to trade it — a coin flip',color=MUT,fontsize=10.5)

fig.text(0.07,0.028,'Synthetic S&P 500 deciles, 1994-2026 - Norgate Data + RealTest - @droskill',
         color=MUT,fontsize=9.5,family='monospace')
out=os.path.join(here,'og-cover.png')
fig.savefig(out,facecolor=BG); print('wrote',out)
