# Web Django

-----
### Questions
HttpResponse���HttpRequest��ʲô��
Ϊʲô��ͼ������Ҫһ��request����(django.http.HttpRequest��һ��ʵ��)



### Http������Python��
```python
def current_datetime(request):
	now = datetime.datetime.now()
	html = '<html><body>It is now %s.</body></html>' % now
	return HttpResponse(html)
```

### ģ��
�� {{ person_name }}					# ����
�� {% if ordered_warranty %}			# ģ���ǩ
�� {% for item in item_list %}