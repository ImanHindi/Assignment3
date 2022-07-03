import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
D={'one':pd.Series([1,2,3],index=['A','B','C']),
    'two':pd.Series([1,2,3,4],index=['A','B','C','D'])}

df=pd.DataFrame(D)
df['Three']=pd.Series([1,2,3,4],index=['A','B','C','D'])
df['Four']=df['one']+df['Three']
print(df['Four'].dtype)
print(df['Four'].astype(float))
print(df['Four'].dtype)



#df.replace('')

x=np.array([1,2,3,4,5,6,7,8,9])
y=np.array([43,55,77,88,90,130,270,300,370])
plt.subplot(1,2,1)
plt.plot(x,y)

x1=np.array([1,2,3,4,5,6,7,8,9])
y1=np.array([43,55,77,88,90,130,270,300,370])
plt.subplot(1,2,2)
plt.plot(x1,y1)
#plt.xlabel('time')
#plt.ylabel('temp')
#plt.title('test')
plt.grid(axis='x',color='green',linestyle='--',linewidth=.5)
plt.show()




