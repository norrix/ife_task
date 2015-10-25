# Pandas

-----
## Numpy
percentile
```python
ptl = np.percentile(dataAllNP, [90,80,70,60,50,40,30,20,10], interpolation = 'higher')
```


-----
## DataFrame

sort
```python
DF = DF.sort(columns = 'id')
```

add a column # 'axis = 0' => column but when we concat we use 'axis = 1'
```python
nameTag = pd.DataFrame(nameTag, columns = ['nameTag'])
ConfigTag = pd.concat([Config, nameTag], axis = 1).sort(columns = 'nameTag')
# Sometimes we use 'ignore_index = True'
ConfigTag.iloc[0]
```

broadcast
```python
Config.ix[:,:2].applymap(addSuffix) # For elementwise operations

```