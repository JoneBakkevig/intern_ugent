import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def fileToDframe(file, footer, cols, sheet):
    #TODO: Documentation of function and parameters && author signature
    """

    This function reads a .xlsx file and reads a sheet into a pandas DataFrame for further use #TODO add example

    :param file: pathname to a .xlsx file
    :param footer: length between document end and data end, relative to index value Date
    :param cols: which columns to be parsed to the DataFrame, legend below
    :param sheet: sheet number in .xlsx file
    :return: pandas DataFrame
    """

    # Ensure datatype during parse to maintain cell value integrity
    datatype = np.float64()

    # Read excel file into excel table
    if file.endswith('xlsx'):
         dt = pd.ExcelFile(file)
    # Parses zero indexed sheet with relevant cols into DataFrame
    df=dt.parse(sheetname=(sheet-1), skiprows=7, skip_footer=footer, dtype=datatype, parse_cols=cols)

    if df.isnull().values.any() == True:
        df=df.interpolate(method='index')



    #Function returns object(s) DataFrame, for use in seperate plotting function
    return df


def plotDframe(dframe, x, y, sec_y, graph_type, title):
    #sns.pointplot(x=dframe[x])
    if graph_type == 'point':
        gt = False

    if graph_type == 'line':
        gt = True


    ax = sns.pointplot(x=x, y=y, data=dframe, join=gt, scale=0.25)#parameter needed to adjust scale
    ax.set_xlabel(str(x))
    ax.set_ylabel(str(y))

    if sec_y != None:
        ax2 = ax.twinx()
        sns.pointplot(x=x,y=sec_y,data=dframe,join=gt, scale=0.25, color='orange',ax=ax2)
        ax2.set_ylabel(str(sec_y))

    plt.title(str(title))
    sns.plt.show()

    return ax





#sheet 1 legend
#0=Date, 3=Precipitation, 66=Temperature, 4=Qinf_total, 5=Qeffl_recircu, 6=Qinflow,
#  42=Q_effluent_A, 79=Fe-dosing A-stage, 7=COD, 8=BOD, 11=TSS
climate_cols = [0, 3, 66] #sheet 1
flow_cols = [0, 6, 79] #sheet 1
infl_cols = [0, 7, 8, 11] #Sheet 1
tinfl_cols =[0, 15, 16, 19] #sheet 1
reactr_cols=[0, 23, 25] #sheet 3 date,SRT, HRT
reactr_tss_cols=[0, 4] #sheet 3 date, TSS
oxy_cols=[0,35,36] #sheet 1 date, oxygen II, oxygen III
effl_cols=[0, 33, 43, 47] #sheet 1 SVI, COD, TSS

climate_footer=110 #TODO: calculate footer on shortest coloumn
flow_footer=91
infl_footer=95
reactr_footer=110
reactr_tss_footer=111
effl_footer=96

filename='Data_nieuwveer.xlsx'
size=(10,8)
sheetn=1
x_ax='Date'

sns.plotting_context(font_scale=0.5)
sns.set_style("dark")

df_clim=fileToDframe(filename, climate_footer, climate_cols,sheetn)
df_flow=fileToDframe(filename, flow_footer, flow_cols,sheetn)
# df_inf=fileToDframe(filename, infl_footer, infl_cols,1)
# df_tinfl=fileToDframe(filename, infl_footer, tinfl_cols,1)
# df_reactr=fileToDframe(filename, reactr_footer, reactr_cols,3)
# df_reactr_tss=fileToDframe(filename, reactr_tss_footer, reactr_tss_cols,3)
# df_oxy=fileToDframe(filename,0,oxy_cols,1)
#df_effl=fileToDframe(filename,effl_footer,effl_cols,1)

yl = df_clim.columns.values.tolist()
yl2 = df_flow.columns.values.tolist()

gt = 'point'
#print yl2[1:-1]
df_flow['Qinf']

plt.plot(df_clim[x_ax],df_clim['Precipitation'],'.--')
plt.show()
#df_clim.plot(x_ax, secondary_y='Temperature',kind='.', mark_right=False)
#if graph_type='point, set scale=float value of your preference
#plotDframe(df_flow, x=yl2[0], y=yl2[1], sec_y=yl2[2], graph_type=gt, title='Flow Rate Data')
#plotDframe(df_flow, x=x_ax, y=y, sec_y=sec_y, graph_type='point', title='Flow Rate Data')
#plotDframe(df_clim, x=x_ax, y=yd, sec_y=yx, graph_type='point', title='Climate Data')
#plotDf(df_clim,x_ax,'Temperature',size,'line')
# plotDf(df_flow,x_ax,'Fe_doseA',size)
# plotDf(df_inf,x_ax,None,size)
# plotDf(df_tinfl,x_ax,None,size)
# plotDf(df_reactr,x_ax,'HRT',size)
# plotDf(df_reactr_tss,x_ax,None,size)
# plotDf(df_oxy,x_ax,None,size)
#plotDf(df_effl,x_ax,'TSS',size,'point')

#sns.jointplot(x=x_ax,y=y, data = df_effl, size=10, dropna=True)
#sns.plt.show()

df_clim.plot(x=x_ax,secondary_y='Temperature')





