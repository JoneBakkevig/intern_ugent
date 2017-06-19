from excelparse import plotDframe as pdfr
from excelparse import fileToDframe as ftdf
import seaborn as sns


#__SHEET_1_LEGEND__
#
# 0=Date, 3=Precipitation,  4=Qinf_total, 5=Qeffl_recirc, 6=Qinf,7=COD, 8=BOD,
# 11=TSS, 35=O2_section_II, 36=O3_section_III, 42=Q_effluent, 66=Temperature ,79=Fe-dosing A-stage
#
#__SHEET_3_LEGEND__
# 0=Date, 4=TSS, 23=SRT, 25=HRT
#



#
# Parse Parameters
#

climate_cols = [0, 3, 66]
flow_cols = [0, 4, 6, 42,  79]

climate_footer=110
flow_footer=91

filename='Data_nieuwveer.xlsx'
sheetn=1

#
# Graph Parameters
#

graph_types = ['.','-','.--']

sns.plotting_context(font_scale=0.5)
sns.set_style("dark")

#df_clim=ftdf(filename, climate_footer, climate_cols,sheetn)
df_flow=ftdf(filename, flow_footer, flow_cols,sheetn)


#pdfr(df_clim,['Precipitation'],'Temperature',graph_types[0], "Climate Data", None)
pdfr(df_flow, ['Qinf_total','Qinf','Q_effluent'], 'Fe_doseA',graph_types[0], "Flow Rate Data", "Flow")
