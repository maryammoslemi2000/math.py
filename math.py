# گرفتن دو عدد از کاربر
num1 = float(input("عدد اول را وارد کنید: "))
num2 = float(input("عدد دوم را وارد کنید: "))

# انجام چهار عمل اصلی
جمع = num1 + num2
تفریق = num1 - num2
ضرب = num1 * num2

# بررسی اینکه عدد دوم صفر نباشد تا از تقسیم بر صفر جلوگیری شود
if num2 != 0:
    تقسیم = num1 / num2
else:
    تقسیم = "تقسیم بر صفر مجاز نیست"

# نمایش نتایج
print(f"نتیجه جمع: {جمع}")
print(f"نتیجه تفریق: {تفریق}")
print(f"نتیجه ضرب: {ضرب}")
print(f"نتیجه تقسیم: {تقسیم}")