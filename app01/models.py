from django.db import models

# Create your models here.


class Department(models.Model):
    """部门表
    verbose_name="部门名称" 主要是用于注解 方便知道字段的含义
    id django会自动创建，不需要我们再去定义
    """
    # id = models.AutoField(verbose_name="ID", primary_key=True)
    # id = models.BigAutoField(verbose_name="ID", primary_key=True)
    title = models.CharField(verbose_name="部门名称", max_length=32)


class UserInfo(models.Model):
    """员工表
    max_digits=10 表示数字总长度是10位，
    decimal_places=2 表示保留2位小数
    models.SmallIntegerField 表示小整型
    """
    name = models.CharField(verbose_name="员工姓名", max_length=32)
    pwd = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")

    # 思考？ 员工表中应该要存入其对应的部门
    # 怎么存？ 新建一个专门存部门的字段？ 可以但不推荐   存入部门名称或部门ID？ 可以且推荐
    # 正确的应该是新建一个字段，用于存入部门对应的ID, 并且部门ID应该有约束，即只能存入部门表里面存在的ID，不能乱存
    # 那怎么约束呢？  使用 models.ForeignKey() 即可

    # 无约束 不推荐
    # depart_id = models.BigIntegerField(verbose_name="部门ID")

    # 1、有约束 推荐
    #   - to 表示与哪张表关联
    #   - to_field, 表示与表中的哪个字段关联(哪一列)  目的是，以后就只能写关联的那一列的值
    # 2、注意，在定义ForeignKey时，虽然这里字段名定义的是 depart， 但是django会自动让其变成 depart_id
    # 3、部门表被删除
    # 3.1、级联删除 on_delete=models.CASCADE  即2个表存在关联数据时，其中1个被删除，其关联的数据也会被删除
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)
    # 3.2、置空  即2个表存在关联数据时，其中1个被删除，其关联的数据被置空
    # depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    # 总结：写法就是选3.1或3.2都可以

    # 性别怎么存？ 当然可以直接存男或女，但是为了节省存储资源 我们可以直接存数字来表示 比如1表示男 2表示女
    # 但是，我们不知道1代表男，2代表女，所以我们需要在django中做个约束 如下： 这样以后就只能传1或者2
    gender_choices = (
        (1, "男"),
        (2, "女")
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)