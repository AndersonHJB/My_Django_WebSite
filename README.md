# My_Django_WebSite
你好，我是悦创。



在 2021年6月23日，晚上。我决定正式从头到位开发一个属于我自己的 Django 网站。这是这个项目的说明文档，我讲为了编程教育开发一款从头到位的网站。目前预期有一下功能：

- 博客「这也是最基本的功能」
- Python 在线编程
- 少儿编程
- ok 代码作业检查
- 教育内容网站



## 01. 第一阶段：复习

### 1. 新建虚拟环境

```python
python3 -m venv djangoenv
```

### 2. Mac 进入虚拟环境

```python
source djangoenv/bin/activate
```

### 3. 安装 Django

```python
pip3 install django
```

### 4. 新建 Django 项目

```python
django-admin startproject my_blog .
# django-admin.py startproject my_blog
```

### 5. 检测 Django 安装是否成功

```python
python3 manage.py runserver
```

### 6. python manage.py migrate

```python
python manage.py migrate
```

### 7. 新建一个 Django App

```python
python3 manage.py startapp blog
```

### 8. 将 App 添加到 settings.py 里

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'blog',
]
```

