"""Render the OG/Twitter card (1200x630) for the bond-rally study."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

BG='#0f1113'; INK='#eef0f1'; MUT='#9aa0a6'; GRID='#2b2f33'
SAFE='#4d92e8'; CLAIM='#e0603a'; POS='#20b184'; CRIT='#e15a51'

# the 2022 inflation shock: total return (%)
cats=['S&P 500','Cash','AGG','IEF','TLT']
vals=[-24.5, 0.9, -14.4, -15.4, -29.3]
cols=[MUT, POS, CLAIM, CLAIM, CRIT]

fig=plt.figure(figsize=(12,6.3),dpi=100); fig.patch.set_facecolor(BG)
ax=fig.add_axes([0.07,0.16,0.52,0.47]); ax.set_facecolor(BG)
x=range(len(cats))
ax.bar(x,vals,color=cols,width=0.66,zorder=3)
ax.axhline(0,color=GRID,lw=1.2)
for i,v in zip(x,vals):
    ax.text(i, v-2.4 if v<0 else v+0.8, ('+' if v>=0 else '')+str(v)+'%',
            color=cols[i],fontsize=10.5,fontweight='bold',ha='center',
            va='top' if v<0 else 'bottom')
ax.set_xticks(list(x)); ax.set_xticklabels(cats,color=MUT,fontsize=9.5)
ax.set_ylim(-34,6)
ax.set_ylabel('total return, 2022',color=MUT,fontsize=10)
ax.tick_params(colors=MUT,labelsize=8)
for sp in ax.spines.values(): sp.set_color(GRID)
ax.grid(axis='y',alpha=0.13)

fig.text(0.07,0.905,'Will bonds finally rally?',color=INK,fontsize=31,fontweight='bold')
fig.text(0.07,0.815,'Three good instincts — carry and insurance, not a coiled spring.',
         color=POS,fontsize=14,fontweight='bold')

rx=0.63
fig.text(rx,0.585,'US TREASURIES, 1962-2026',color=MUT,fontsize=10,family='monospace')
fig.text(rx,0.475,'+0.94',color=SAFE,fontsize=38,fontweight='bold')
fig.text(rx,0.420,'start yield explains the next decade',color=MUT,fontsize=10.5)
fig.text(rx,0.315,'-29%',color=CRIT,fontsize=22,fontweight='bold')
fig.text(rx,0.265,'long bonds in 2022 — worse than stocks',color=MUT,fontsize=10.5)
fig.text(rx,0.165,'24%',color=CLAIM,fontsize=22,fontweight='bold')
fig.text(rx,0.115,'foreign share — a record in $, not fleeing',color=MUT,fontsize=10.5)

fig.text(0.07,0.028,'US Treasuries, yields & TIC flows - Norgate + FRED + Treasury - @droskill',
         color=MUT,fontsize=9.5,family='monospace')
out=os.path.join(os.path.dirname(__file__),'og-cover.png')
fig.savefig(out,facecolor=BG); print('wrote',out)
