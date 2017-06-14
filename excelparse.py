import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def fileToDframe(file, footer, cols, sheet):
    #TODO: Documentation of function and parameters && author signature
    """

    This function reads a .xlsx file and reads a sheet into a pandas DataFrame for further use #

    Example:

    fileToDframe('filename.xls', 110, [0, 3, 4], 1)

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


def plotDframe(dframe, y_list, sec_y, graph_type, title, **ylabel):


    fig, ax = plt.subplots()
    colors = ['blue','purple','green','red']

    for i in y_list:
        ax.plot(dframe['Date'], dframe[i], graph_type, color=colors[len(y_list)-1])


        if len(y_list) == 1:
            ax.set_ylabel(str(i))
        else:
            ax.set_ylabel(ylabel)

        


    if sec_y:

        ax2 = ax.twinx()
        ax2.plot(dframe['Date'], dframe[sec_y], graph_type, color='orange')
        ax2.set_ylabel(str(sec_y))
        ax2.legend(str(sec_y))


    ax.set_xlabel('Time')

    plt.title(title)
    plt.show()


   # ax = plt.plot(dframe[x], dframe[y], '.--')

   # ax2 = ax.twinx()
   # ax2 = plt.plot(dframe[])







# sheet 1 legend
# 0=Date, 3=Precipitation,  4=Qinf_total, 5=Qeffl_recirc, 6=Qinf,7=COD, 8=BOD,
# 11=TSS, 35=O2_section_II, 36=O3_section_III, 42=Q_effluent, 66=Temperature ,79=Fe-dosing A-stage
# sheet 3 legend
# 0=Date, 4=TSS, 23=SRT, 25=HRT
climate_cols = [0, 3, 66] #sheet 1
flow_cols = [0, 6, 79] #sheet 1

climate_footer=110 #TODO: calculate footer on shortest coloumn
flow_footer=91

filename='Data_nieuwveer.xlsx'
size=(10,8)
sheetn=1
x_ax='Date'

sns.plotting_context(font_scale=0.5)
sns.set_style("dark")

df_clim=fileToDframe(filename, climate_footer, climate_cols,sheetn)
df_flow=fileToDframe(filename, flow_footer, flow_cols,sheetn)

yl = df_clim.columns.values.tolist()
yl2 = df_flow.columns.values.tolist()

graph_types = ['.','-','.--']

plotDframe(df_clim,['Precipitation'],'Temperature',graph_types[0], "Climate Data")
#print yl2[1:-1]

#df_clim.plot(x_ax, secondary_y='Temperature',kind='.', mark_right=False)
#if graph_type='point, set scale=float value of your preference
#plotDframe(df_flow, x=yl2[0], y=yl2[1], sec_y=yl2[2], graph_type=gt, title='Flow Rate Data')
#plotDframe(df_flow, x=x_ax, y=y, sec_y=sec_y, graph_type='point', title='Flow Rate Data')
#plotDframe(df_clim, x=x_ax, y=yd, sec_y=yx, graph_type='point', title='Climate Data')







