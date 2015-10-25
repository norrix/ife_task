# Matplotlib

-----
## pyplot

```python
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (10,8))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212, sharex = ax1)
```

�޸������ǩ
```python
Time = np.arange(N)
ticks = np.arange(1,N,10) # ÿ��10�����ǩ
labels = PriceData.index[ticks]


xticklabels = ax1.get_xticklabels() # set xticklabel invisible
plt.setp(xticklabels, visible=False)
plt.setp(xticklabels, rotation = 30, horizontalalignment='right') # labels��ת�Ƕ�
```

��ͼ�����
```python
ax1.set_title('Price', fontsize = 24)
ax1.plot(Time, Futures1, color = '#0000FF', label = 'Futures1') # Blue
ax1.plot(Time, Futures2, color = '#00FFFF', label = 'Futures2') # Sky Blue
ax1.axhspan(name['lowerlim'], name['upperlim'], facecolor='0.3', alpha=0.3, edgecolor  = None)

ax1.axvline(x = Tindex, linewidth = 1, color='r', linestyle = ':') # һ������
ax1.axvline(x = Tindex, ymin=0.95, linewidth = 2, color='r') # ��ɫ��ʵ��λ��

ax1.grid(True)
```

LEGEND
```python
ax1.legend(framealpha = 0.3, fontsize = 'small', ncol =  3) # transparent, small, horizontal legend 
```

�����
```python
fig.text(0.02, 0.95, text, bbox=dict(facecolor='grey', alpha=0.2), fontsize = 10)
fig.savefig('test.png')
plt.close(fig)
```