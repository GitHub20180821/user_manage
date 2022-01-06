from django.shortcuts import render, redirect
from app01.models import Department

# Create your views here.


def depart_list(request):
    """部门列表"""
    # 获取部门表的数据并渲染到页面中 depart_list.html 中
    # depart_list 返回的是一个queryset 类似于列表 [对象,对象,对象]
    depart_list = Department.objects.all()
    return render(request, "depart_list.html", {'depart_list': depart_list})


def depart_add(request):
    """新建部门"""
    # 1、首先，应该判断请求的方法
    # 因为从部门列表页面点击新建部门 进入新建部门页面 这个功能是通过GET请求实现的
    if request.method == "GET":
        return render(request, "depart_add.html")

    # 2、然后，获取用户POST提交过来的数据
    # 在新建部门页面提交的数据是通过POST提交的
    # 表单中的提交地址action 没有写，默认就提交到当前地址 当前地址就是 depart/add/ 所以依然能执行到本视图函数
    title = request.POST.get("title")  # get("title") 就是前端表单里面的name属性的值

    # 3、然后，把数据存入数据库
    Department.objects.create(title=title)

    # 4、最后 重定向到部门列表页面
    return redirect(to="/depart/list")


def depart_delete(request):
    """删除部门"""
    # http://127.0.0.1:8000/depart/delete/?nid=1
    # 1、获取被删除的ID
    nid = request.GET.get("nid")

    # 2、从数据库删除指定id的记录
    Department.objects.filter(id=nid).delete()

    # 3、重定向回部门列表页面
    return redirect(to="/depart/list")
