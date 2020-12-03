import pandas as pd
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

Sreg1 = pd.read_csv('Sreg1.csv', header = None,
                    names = ['element', 'node', 'stress in', 'stress out']).drop(columns='element')
Sreg1.sort_values(by=['node'], inplace=True)
Sreg1.drop_duplicates(['node'], inplace=True)
Sreg1.set_index('node')
# Sreg1.reset_index(drop=True, inplace=True)
Sreg1['avg stress'] = Sreg1.iloc[:,2:].mean(axis=1)

Sreg2 = pd.read_csv('Sreg2.csv', header = None,
                    names = ['element', 'node', 'stress in', 'stress out']).drop(columns='element')
Sreg2.sort_values(by=['node'], inplace=True)
Sreg2.drop_duplicates(['node'], inplace=True)
Sreg1.set_index('node')
# Sreg2.reset_index(drop=True, inplace=True)
Sreg2['avg stress'] = Sreg2.iloc[:,2:].mean(axis=1)

Sreg3 = pd.read_csv('Sreg3.csv', header = None,
                    names = ['element', 'node', 'stress in', 'stress out']).drop(columns='element')
Sreg3.sort_values(by=['node'], inplace=True)
Sreg3.drop_duplicates(['node'], inplace=True)
Sreg1.set_index('node')
# Sreg3.reset_index(drop=True, inplace=True)
Sreg3['avg stress'] = Sreg3.iloc[:,2:].mean(axis=1)

Sreg4 = pd.read_csv('Sreg4.csv', header = None,
                    names = ['element', 'node', 'stress in', 'stress out']).drop(columns='element')
Sreg4.sort_values(by=['node'], inplace = True)
Sreg4.drop_duplicates(['node'], inplace=True)
Sreg1.set_index('node')
# Sreg4.reset_index(drop=True, inplace=True)
Sreg4['avg stress'] = Sreg4.iloc[:,2:].mean(axis=1)


nodes = pd.read_csv('nodes.csv', header = None,
                    names = ['node', 'x', 'y', 'z'])


# print(nodes)
# nodes['stress'] = Sreg4.iloc[:,3]
print(Sreg1)
print(Sreg2)
print(Sreg3)
print(Sreg4)
print(nodes)


# nodes.x=pd.to_numeric(nodes.x)
#nodes.y=pd.to_numeric(nodes.y)
#nodes.z=pd.to_numeric(nodes.z)

# nodes.iloc.astype(float)



# nodes.sort_values(by=['x', 'y', 'z'], inplace=True)
# nodes.drop_duplicates(['node'], inplace=True)
# print(nodes.iloc[:,3])
#print(nodes.iloc[:,'y'])


#print(nodes.iloc[:,1])

#Axes3D.plot_wireframe(nodes.iloc[:,1], nodes.iloc[:,2], nodes.iloc[:,3])

#plt.scatter(nodes.iloc[:,3], nodes.iloc[:,2])

#nodes.plot(kind='scatter', x=['z'], y=['y'])
#plt.show()
