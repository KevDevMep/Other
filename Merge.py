import geopandas as gp
import tkinter as tk

def majority(gdf):
    gdf['Majority'] = ''
    for i in range(len(gdf)):
        if gdf['WhitePct'][i] > .5:
            gdf.loc[i, 'Majority'] = "White"
        elif gdf['HispanicPct'][i] > gdf['WhitePct'][i] and gdf['HispanicPct'][i] > gdf['BlackPct'][i] and gdf['HispanicPct'][i] > gdf['AsianPct'][i] and gdf['HispanicPct'][i] > gdf['NativePct'][i] and gdf['HispanicPct'][i] > gdf['PacificPct'][i]:
            gdf.loc[i, 'Majority'] = "Hispanic"
        elif gdf['BlackPct'][i] > gdf['WhitePct'][i] and gdf['BlackPct'][i] > gdf['AsianPct'][i] and gdf['BlackPct'][i] > gdf['NativePct'][i] and gdf['BlackPct'][i] > gdf['PacificPct'][i]:
            gdf.loc[i, 'Majority'] = "Black"
        elif gdf['AsianPct'][i] > gdf['WhitePct'][i] and gdf['AsianPct'][i] > gdf['NativePct'][i] and gdf['AsianPct'][i] > gdf['PacificPct'][i]:
            gdf.loc[i, 'Majority'] = "Asian"
        elif gdf['NativePct'][i] > gdf['WhitePct'][i] and gdf['NativePct'][i] > gdf['PacificPct'][i]:
            gdf.loc[i, 'Majority'] = "Native"
        elif gdf['PacificPct'][i] > gdf['WhitePct'][i]:
            gdf.loc[i, 'Majority'] = "Pacific"
        else:
            gdf.loc[i, 'Majority'] = "Minority"

def geoMerge():
    if filename1.get().strip() == '' or filename2.get().strip() == '':
        print('Files can not be empty')
        pass
        
    try:
        gdf1 = gp.read_file(filename1.get().strip(), use_arrow=True)
        gdf2 = gp.read_file(filename2.get().strip(), use_arrow=True, columns=['DemPct', 'RepPct'])
        gdf2 = gdf2.rename(columns={'DemPct': 'DemPct2', 'RepPct': 'RepPct2'})
        merged = gdf1.merge(gdf2, on='geometry')
        merged['Margin'] = merged['DemPct'] - merged['RepPct']
        merged['Margin2'] = merged['DemPct2'] - merged['RepPct2']
        merged['Swing'] = merged['Margin'] - merged['Margin2']
        majority(merged)
        merged.to_file(f'{tag.get()}_Merged.gpkg', use_arrow=True, driver='GPKG')
        print('Success')
    except:
        print('Error')

root = tk.Tk()
root.config(background='red')
filename1 = tk.StringVar()
filename2 = tk.StringVar()
tag = tk.StringVar()

tk.Label(root, text='File1').grid(row=0, column=0)
tk.Entry(root, textvariable=filename1).grid(row=1, column=0)
tk.Label(root, text='File2').grid(row=2, column=0)
tk.Entry(root, textvariable=filename2).grid(row=3, column=0)
tk.Label(root, text='Tag').grid(row=4, column=0)
tk.Entry(root, textvariable=tag).grid(row=5, column=0)
submit = tk.Button(root, text='Merge', command=geoMerge).grid(row=6, column=0)

root.mainloop()