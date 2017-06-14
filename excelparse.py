import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

__author__ = 'j.k.bakkevig@gmail.com'

def fileToDframe(file, footer, cols, sheet):

    """
    =======================
    Excel file to DataFrame
    =======================

    This function reads a .xlsx file and creates a given sheet from that file into a pandas DataFrame object.
    The file contains the column names and the corresponding cell values to the columns. The specific columns to parse must be given.

    :param file: pathname to a .xlsx file
    :param footer: length between document end and data end, relative to index value Date
    :param cols: which columns to be parsed to the DataFrame, legend below (0-indexed)
    :param sheet: sheet number in .xlsx file (1-indexed)

    :return: pandas DataFrame df

    Example:

    fileToDframe('Data_nieuwveer.xlsx', 110, [0, 3, 66], 1)

    returns df :DataFrame consisting of columns Date (0) , Percipitation (3) and Temperature (66) from sheet 1 in excel file Data_nieuwveer.xlsx

    """
    #TODO: Calculate footer length independtly of given columns

    # Specify datatype during parse to maintain cell value integrity (no decimal points lost)
    datatype = np.float64()

    # Read excel file into excel table
    if file.endswith('xlsx'):
         dt = pd.ExcelFile(file)

    # Parses zero indexed sheet with relevant cols into DataFrame, 7 rows are skipped as per excel document structure
    df=dt.parse(sheetname=(sheet-1), skiprows=7, skip_footer=footer, dtype=datatype, parse_cols=cols)

    # If no values in the cell, interpolate. Used for line plotting
    if df.isnull().values.any() == True:
        df=df.interpolate(method='index')

    # Function returns object(s) DataFrame, for use in seperate plotting function
    return df


def plotDframe(dframe, y_list, sec_y, graph_type, title, **ylabel):

    """
    =====================
    Plot DataFrame values
    =====================

    This function takes a DataFrame object and plots the first column as x-axis and gives the option of plotting
    the other columns on either the same y-axis or seperated on two y-axis depending on variables given.

    :param dframe: DataFrame objected parsed from the fileToDframe function. See fileToDframe documentation.
    :param y_list: List of strings that denote the columns to plot on first y-axis, also works for list of one element
    :param sec_y: Column name to plot on second y-axis
    :param graph_type: What type of plot, graph type are denoted by strings '.', '-', etc
    :param title: Title of the Plot
    :param ylabel: Optional parameter, if several elements in y_list, use this parameter to label the first y-axis appropriately

    :return ax, ax2: Axes objects ax, ax2 for further use to change tick rates etc

    Example:

    plotDframe(dframe, ['Precipitation'], 'Temperature, '.', "Climate Data")

    returns plot of column Precipitation on first y-axis, column Temperature on second y-axis and 'Date' on x-axis.

    """

    # Creating subplots for axis control
    fig, ax = plt.subplots()

    # Plotting colors, only 4 stated as not expecting more than 4 plots on one y-axis
    colors = ['blue','purple','green','red']

    # Setting x-axis to date as no other x-axis is expected in this project #TODO: This may change, make generic solution for adjustable x-axis
    ax.set_xlabel('Date')

    # Iterate over column names to plot on first y-axis
    for i in y_list:
        pplot, = ax.plot(dframe['Date'], dframe[i], graph_type, color=colors[len(y_list)-1])
        # If only one item in y_list, use its column name as y-label
        if len(y_list) == 1:
            ax.set_ylabel(str(i))
        # If multiple items in y_list, use optional parameter ylabel to set specific y-label
        elif len(y_list)>1:
            ax.set_ylabel(ylabel)

    # If any item, plot it on second y-axis
    if sec_y:
        # Share x-axis with ax
        ax2 = ax.twinx()
        # Plot the column of sec_y on y-axis
        splot, = ax2.plot(dframe['Date'], dframe[sec_y], graph_type, color='orange')
        # Set title to column name, as its only one value plotted
        ax2.set_ylabel(str(sec_y))

    # Create handles for legend
    handles=[pplot,splot]
    # Create labels for legend
    labels=[pplot.get_label(),splot.get_label()]
    # Create legend
    plt.legend(handles,labels,loc='upper right')
    # Set title
    plt.title(title)
    # Show figure
    plt.show()

    return ax, ax2

#__SHEET_1_LEGEND__
#
# 0=Date, 3=Precipitation,  4=Qinf_total, 5=Qeffl_recirc, 6=Qinf,7=COD, 8=BOD,
# 11=TSS, 35=O2_section_II, 36=O3_section_III, 42=Q_effluent, 66=Temperature ,79=Fe-dosing A-stage
#
#__SHEET_3_LEGEND__
# 0=Date, 4=TSS, 23=SRT, 25=HRT
#
climate_cols = [0, 3, 66]
flow_cols = [0, 6, 79]

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

graph_types = ['.','-','.--']

plotDframe(df_clim,['Precipitation'],'Temperature',graph_types[0], "Climate Data")







