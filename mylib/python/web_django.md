# Web Django

-----
### Questions
HttpResponse类和HttpRequest是什么？
为什么视图函数需要一个request参数(django.http.HttpRequest的一个实例)



### Http编码在Python中
```python
def current_datetime(request):
	now = datetime.datetime.now()
	html = '<html><body>It is now %s.</body></html>' % now
	return HttpResponse(html)
```

### 模板
· {{ person_name }}					# 变量
· {% if ordered_warranty %}			# 模板标签
· {% for item in item_list %}