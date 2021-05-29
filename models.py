# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime


# 用户表，作基类表
class User(models.Model):
    user_id = models.AutoField(primary_key=True)  # 会自动生成？
    user_name = models.CharField(max_length=32, blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    user_phone = models.CharField(max_length=11, blank=True, null=True)
    login_pwd = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'user0'


# 部门
class Depart(models.Model):
    dep_id = models.AutoField(primary_key=True)
    dep_name = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'depart'


# 员工的基类表
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    # dep_id = models.CharField(max_length=3, blank=True, null=True)
    staff_salary = models.FloatField(blank=True, null=True)
    staff_phone = models.CharField(max_length=11, blank=True, null=True)
    login_pwd = models.CharField(max_length=16, blank=True, null=True)
    dep = models.ForeignKey(to=Depart, on_delete=models.CASCADE, null=True)  # 级联

    class Meta:
        db_table = 'staff'


# 商品表单
class Goods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=50)
    brand = models.CharField(max_length=16, null=True)
    size = models.CharField(max_length=16, null=True)
    goods_type = models.CharField(max_length=10, null=True)
    rel_date = models.DateTimeField(blank=True, null=True)
    rel_price = models.FloatField(blank=True, null=True)
    material = models.CharField(max_length=32, null=True)
    goods_des = models.CharField(max_length=50, null=True)
    style = models.CharField(max_length=16, null=True)
    img_path = models.CharField(max_length=64, null=True)

    class Meta:
        db_table = 'goods'


class Goods_price(models.Model):
    detail_id = models.AutoField(primary_key=True)
    goods = models.OneToOneField(to=Goods, on_delete=models.CASCADE, null=True)
    min_ask_fast = models.FloatField(blank=True, null=True)
    max_bid = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'goods_price'


# ER图里没有，用于查询物流单号与对应的物流信息
class SendCompany(models.Model):
    log_send = models.AutoField(primary_key=True)
    log_detail = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'send_c'


# 交易表,用来表示订单买卖方交易，系统如何匹配买家和卖家？先进先出？
class Trade(models.Model):
    trade_id = models.AutoField(primary_key=True)
    # goods_id = models.ForeignKey(to=Goods, on_delete=models.CASCADE, null=True)
    # trade_type = models.IntegerField(null=True)  # 表示交易状态，0买卖方缺一方、1买卖方已匹配
    pay_id = models.IntegerField(null=True)  # 对应售卖表单和购买表单，但没有设置外键
    trade_status = models.CharField(max_length=16, null=True)
    ask_id = models.IntegerField(null=True)
    log_send = models.OneToOneField(to=SendCompany, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'trade'


# 卖家表
class Seller(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE, null=True)
    id_card = models.CharField(max_length=18, null=True)
    valid = models.IntegerField(null=True)  # 信誉评级

    class Meta:
        db_table = 'seller'


# 卖家售卖表单
class AskTran(models.Model):
    ask_id = models.AutoField(primary_key=True)
    goods_id = models.ForeignKey(to=Goods, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    trade_id = models.OneToOneField(to=Trade, on_delete=models.CASCADE, null=True) #
    ask = models.FloatField(null=True)  # ask 是出价
    sell_mode = models.CharField(max_length=8, blank=True, null=True)
    ask_status = models.CharField(max_length=16, blank=True, null=True)
    time = models.DateTimeField(default=datetime.now, blank=True, null=True)
    # ple_price = models.FloatField(blank=True, null=True)
    del_phone = models.CharField(max_length=11, blank=True, null=True)
    del_addr = models.CharField(max_length=64, blank=True, null=True)
    del_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'ask_tran'


# 买家购买订单
class BuyGood(models.Model):
    pay_id = models.AutoField(primary_key=True)
    goods_id = models.ForeignKey(to=Goods, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    trade_id = models.OneToOneField(to=Trade, on_delete=models.CASCADE, null=True)
    del_addr = models.CharField(max_length=64, blank=True, null=True)
    del_ph = models.CharField(max_length=11, blank=True, null=True)
    del_name = models.CharField(max_length=32, blank=True, null=True)
    order_mode = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    time = models.DateTimeField(default=datetime.now, blank=True, null=True)
    paid_money = models.FloatField(blank=True, default=0)

    class Meta:
        db_table = 'buy_good'


# 仓库
class Warehouse(models.Model):
    ware_id = models.AutoField(primary_key=True)
    ware_telephone = models.CharField(max_length=20, null=True)
    ware_cap = models.IntegerField(null=True)
    ware_store = models.IntegerField(null=True)
    attr = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'warehouse'


# 物流处理人员
class SendStaff(models.Model):
    staff = models.OneToOneField(to=Staff, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'send_staff'


# 鉴定人员
class AppStaff(models.Model):
    staff = models.OneToOneField(to=Staff, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'app_staff'


# 财务人员
class FinStaff(models.Model):
    staff = models.OneToOneField(to=Staff, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'fin_staff'


# 售后人员
class AfterServerStaff(models.Model):
    staff = models.OneToOneField(to=Staff, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'after_server_staff'


# 现金流水表单
class CashFlow(models.Model):
    flash_rec_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(to=FinStaff, on_delete=models.CASCADE, null=True)
    cash_type = models.CharField(max_length=8, blank=True, null=True)
    time = models.DateTimeField(datetime.now, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'cash_flow'


# 收入流水
class IncomeFlow(models.Model):
    flash_rec_id = models.OneToOneField(to=CashFlow, on_delete=models.CASCADE, null=True)
    in_source = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'income_flow'


# 支出流水
class OutFlow(models.Model):
    flash_rec_id = models.OneToOneField(to=CashFlow, on_delete=models.CASCADE, null=True)
    to_where = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        db_table = 'out_flow'


# 售后过程
class AfterServer(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    after_server_staff_id = models.ForeignKey(to=AfterServerStaff, on_delete=models.CASCADE, null=True)
    describe = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(datetime.now, blank=True, null=True)

    class Meta:
        db_table = 'after_server'


# 退货
class BackGoodsTran(models.Model):
    pay_id = models.OneToOneField(to=BuyGood, on_delete=models.CASCADE, null=True)
    flash_rec_id = models.ForeignKey(to=OutFlow, on_delete=models.CASCADE, null=True)
    log_send = models.OneToOneField(to=SendCompany, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'back_goods_tran'


# 卖家往仓库发货
class SellerSend(models.Model):
    seller_id = models.OneToOneField(to=AskTran, on_delete=models.CASCADE, null=True)
    log_send = models.OneToOneField(to=SendCompany, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'seller_send'


# 卖家已完成订单
class CpltSale(models.Model):
    ask_id = models.ForeignKey(to=AskTran, on_delete=models.CASCADE, null=True)
    state = models.CharField(max_length=8, blank=True, null=True)
    time = models.DateTimeField(default=datetime.now, blank=True, null=True)

    class Meta:
        db_table = 'cplt_sale'


# 平台鉴定订单,,这里可能少个买家的id外键
class PltApp(models.Model):
    ask_id = models.OneToOneField(to=AskTran, on_delete=models.CASCADE, null=True)
    staff_id = models.ForeignKey(to=AppStaff, on_delete=models.CASCADE, null=True)
    app_fdbc = models.CharField(max_length=16, blank=True, null=True)
    buyer_opin = models.CharField(max_length=4, blank=True, null=True)
    img_path = models.CharField(max_length=64, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'plt_app'


# 买家已完成订单
class FinishOrder(models.Model):
    pay_id = models.OneToOneField(to=BuyGood, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'finish_order'


# 用户消息，有user_id作为外键
class msg(models.Model):
    msg_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, null=False)
    msg_content = models.CharField(max_length=30, blank=True, null=True)
