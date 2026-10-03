"""Render the OG/Twitter card (1200x630) for the price-vs-slope trend-signal study."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

BG='#0f1113'; INK='#eef0f1'; MUT='#9aa0a6'; GRID='#2b2f33'
SAFE='#4d92e8'; CLAIM='#e0603a'; POS='#20b184'; CRIT='#e15a51'; PURP='#a142f4'

# long-basket frontier points: (maxDD %, CAGR %, label, color)
pts=[(28.5,8.2,'B&H',MUT),(8.7,6.9,'PRICE',SAFE),(10.1,7.7,'SLOPE',POS),
     (7.6,7.0,'BOTH',CRIT),(8.2,7.3,'GRADED',PURP),(16.6,7.6,'BLEND',CLAIM)]

fig=plt.figure(figsize=(12,6.3),dpi=100); fig.patch.set_facecolor(BG)
ax=fig.add_axes([0.07,0.16,0.52,0.50]); ax.set_facecolor(BG)
for dd,cagr,lab,c in pts:
    ax.scatter(dd,cagr,s=150,color=c,edgecolor=BG,linewidth=1.5,zorder=3)
    dx = -0.9 if lab in ('SLOPE','BOTH','GRADED') else 0.6
    ha = 'right' if dx<0 else 'left'
    ax.annotate(lab,(dd,cagr),xytext=(dx*8,4),textcoords='offset points',
                color=c,fontsize=11,fontweight='bold',ha=ha)
ax.set_xlim(30,5); ax.set_ylim(6.5,8.5)   # invert x: left=worse DD
ax.set_xlabel('max drawdown  (← less risk)',color=MUT,fontsize=10)
ax.set_ylabel('CAGR',color=MUT,fontsize=10)
ax.tick_params(colors=MUT,labelsize=8)
for sp in ax.spines.values(): sp.set_color(GRID)
ax.grid(alpha=0.15)

fig.text(0.07,0.905,'Price, or slope?',color=INK,fontsize=32,fontweight='bold')
fig.text(0.07,0.815,'On a diversified basket, the trend signal you pick is a dial, not an edge.',
         color=POS,fontsize=14.5,fontweight='bold')

rx=0.63
fig.text(rx,0.60,'MA-SLOPE TIMING, 1988-2026',color=MUT,fontsize=10,family='monospace')
fig.text(rx,0.485,'7.7%',color=POS,fontsize=38,fontweight='bold')
fig.text(rx,0.43,'CAGR - 94% of buy & hold (8.2%)',color=MUT,fontsize=10.5)
fig.text(rx,0.325,'-10% vs -29%',color=SAFE,fontsize=20,fontweight='bold')
fig.text(rx,0.275,'max drawdown vs buy & hold',color=MUT,fontsize=10.5)
fig.text(rx,0.175,'3 of 4',color=CRIT,fontsize=20,fontweight='bold')
fig.text(rx,0.125,'decades slope beats price-cross',color=MUT,fontsize=10.5)

fig.text(0.07,0.028,'US multi-asset basket - Norgate + FRED - a Faber extension - Bento Analytics',
         color=MUT,fontsize=9.5,family='monospace')
out=os.path.join(os.path.dirname(__file__),'og-cover.png')
fig.savefig(out,facecolor=BG); print('wrote',out)
