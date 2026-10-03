"""Render the OG/Twitter card (1200x630) for the housing-vs-market study."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

BG='#0f1113'; INK='#eef0f1'; MUT='#9aa0a6'; GRID='#2b2f33'
SAFE='#4d92e8'; CLAIM='#e0603a'; POS='#20b184'; CRIT='#e15a51'

# quarterly drawdown series (from bear_series.csv), 1987-2026
SPX=[(1987.9,-25.1),(1990.7,-15.3),(1994.4,-7.8),(1998.7,-10.3),(2000.9,-13.0),
     (2001.7,-31.4),(2002.7,-46.3),(2003.4,-35.8),(2004.7,-26.6),(2006.4,-16.3),
     (2007.7,-0.3),(2008.9,-41.7),(2009.2,-48.5),(2010.4,-33.5),(2011.7,-27.0),
     (2012.4,-12.1),(2013.2,0.0),(2015.7,-8.9),(2018.9,-14.0),(2020.2,-20.0),
     (2020.9,0.0),(2022.7,-24.8),(2023.2,-13.8),(2024.9,-2.5),(2025.2,-7.1),(2026.4,-1.1)]
HPI=[(1987.9,0.0),(1990.9,-2.0),(1992.2,-2.2),(1995.2,-0.3),(2000.9,0.0),
     (2005.9,0.0),(2007.2,-1.3),(2008.9,-17.4),(2009.9,-20.6),(2011.9,-26.8),
     (2012.2,-26.4),(2013.4,-15.3),(2014.9,-9.8),(2016.4,-1.5),(2018.9,-0.3),
     (2021.9,0.0),(2022.9,-4.5),(2023.4,0.0),(2025.9,-1.4),(2026.4,0.0)]

fig=plt.figure(figsize=(12,6.3),dpi=100); fig.patch.set_facecolor(BG)
ax=fig.add_axes([0.07,0.15,0.52,0.48]); ax.set_facecolor(BG)
ax.axvspan(2007.8,2012.2,color=CLAIM,alpha=0.13,zorder=0)
ax.plot([p[0] for p in SPX],[p[1] for p in SPX],color=SAFE,lw=2.0,label='S&P 500')
ax.plot([p[0] for p in HPI],[p[1] for p in HPI],color=CLAIM,lw=2.4,label='U.S. home prices')
ax.axhline(0,color=GRID,lw=1)
ax.set_xlim(1987,2026.5); ax.set_ylim(-55,4)
ax.set_ylabel('drawdown  (%)',color=MUT,fontsize=10)
ax.tick_params(colors=MUT,labelsize=8)
for sp in ax.spines.values(): sp.set_color(GRID)
ax.grid(alpha=0.13)
ax.text(2010.0,-50,'2008 housing bust',color=CLAIM,fontsize=9,ha='center')
ax.legend(loc='lower left',fontsize=9,facecolor=BG,edgecolor=GRID,labelcolor=INK)

fig.text(0.07,0.905,'Does housing drive the market?',color=INK,fontsize=30,fontweight='bold')
fig.text(0.07,0.815,'Five stock bears, one housing bust — and only 2008 overlaps.',
         color=CLAIM,fontsize=14,fontweight='bold')

rx=0.63
fig.text(rx,0.585,'S&P 500 vs U.S. HOUSING, 1988-2026',color=MUT,fontsize=10,family='monospace')
fig.text(rx,0.475,'+0.22',color=SAFE,fontsize=38,fontweight='bold')
fig.text(rx,0.420,'bull-market ↔ housing correlation (weak)',color=MUT,fontsize=10.5)
fig.text(rx,0.315,'1 of 5',color=CLAIM,fontsize=22,fontweight='bold')
fig.text(rx,0.265,'stock bears came with a housing bust',color=MUT,fontsize=10.5)
fig.text(rx,0.165,'+0.44',color=CRIT,fontsize=22,fontweight='bold')
fig.text(rx,0.115,'stocks ↔ bonds today: no hedge',color=MUT,fontsize=10.5)

fig.text(0.07,0.028,'US stocks, housing & rates - Norgate + FRED (Case-Shiller) - @droskill',
         color=MUT,fontsize=9.5,family='monospace')
out=os.path.join(os.path.dirname(__file__),'og-cover.png')
fig.savefig(out,facecolor=BG); print('wrote',out)
