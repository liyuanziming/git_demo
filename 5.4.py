print("高铁购票系统欢迎您！")
n=1        #登录次数
while  n<=3 :
    user=input("请输入用户名：")
    pwd=input("请输入密码：")
    if user =='小红'and pwd =='123456':
          print("尊敬的",user,"登录成功!")
          code = input("请输入健康码（绿码/黄码）：")
          if code == "绿码":
              print("请购票，祝您一路旅途顺风！")
              site = ['银川', '吴忠', '庆阳', '永寿西', '礼泉南', '西安北站']
              print("站点信息如下：")
              for i in range(0, 6, 1):
                  print("***", site[i])

              site_start = input("请输入起始站点：")
              site_end = input("请输入终点站：")
              if site_start in site and site_end in site:
                  start = site.index(site_start)
                  end = site.index(site_end)
                  price = abs(start - end) * 10
                  if price <= 20:
                      print("票价为：20元；请扫码，付款！")
                  elif price > 40:
                      print("票价为：40元;请扫码，付款！")
                  else:
                      print("票价为:", price, "元；请扫码，付款！")
              else:
                  print("站点输入有误！")
          else:
              print("黄码禁止购票，谢谢配合！")
          break    #跳出循环，程序结束。
    elif user!= '小红':
          print('已尝试登录',n,"次，用户名不存在，请重新输入! ")
          n=n+1
    else:
          print('已尝试登录',n,'次，密码有误，请重新输入! ')
          n=n+1
else:
         print('登录次数达到3次，登录锁定!')