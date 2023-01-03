#اعداد الطالب علي الشناعة 
##الرجاء الانتباه عند الادخال عند طلب عدد الارقام الصحيحة والمكان الصحيح او الارقان
#الصحيحة والمكان الخاطئ لانه ييؤثر غلى الحل فا بععض الحالات اطلب عددالرقمين 
#او اطلب فقط الرقم عدد الصحيح في المكان الصحيح او فقط عددالرقم الصحيح  في المكان الخاطئ

from experta import *# استيراد المكاتب بايثون
from random import randint


print("hi how are you?")
print("I am experta !")
print("you need to think about a random code containing 4 digits.")
print(" the 4 digits have to all be different and can only be numbers from 1 to 9")

start=input("are you ready? [y-n]")
class Correct(Fact):#  الرقم الحقيقة   مكون من اربع مراتب 
    A = Field(int)# المرتبة الاولى 
    B = Field(int)#الثانية 
    C = Field(int)#الثالثة 
    D = Field(int)# المرتبة الرابعة 

class Current(Fact):# الرقم الحالي الذي تتم معالجته
    a = Field(int)#الاول 
    b = Field(int)#الثاني 
    c = Field(int)#الثالث
    d = Field(int)# الرابع 
class state(Fact):# حقيقة الحالة التي تعبر عن تغير الدخل من المستخدم 
    correct_place_new = Field(int)#  عدد الارقام الصحيحة في المكان الصحيح الجديد
    correct_place_old= Field(int)#عدد الارقام الصحيحة في المكان الصحيح القديم 
    wrong_place_new= Field(int)#عدد الارقام الصحيحة في المكان الخاطئ الجديد
    wrong_place_old = Field(int)#عدد الارقام الصحيحة في المكان الخاطئ القديمc
class active(Fact):# مجموعة الارقام الغير ظاهرة والتي من الممكن ان تكون من الرقم الصحيح 
    e = Field(int)
    f = Field(int)
    j = Field(int)
    h= Field(int)
    i= Field(int)


class guesser(KnowledgeEngine):# تكوين محرك الاستدلال جديد 

    @DefFacts()# وضع القيم الابتدائية 
    def startup(self):
             
            
        yield Correct (A=0,B=0,C=0,D=0)   # الرقم الحقيقي غير معروف لذلك نكون القيمة الابتدائية =0 
        yield state (correct_place_new=0)# القيم الابتداائية للحال=0
        yield state (correct_place_old=0)
            
    @Rule(NOT(state(correct_place_new=-1)),# مادام العددالارقام الصحيحة لايساوي -1
    NOT(Current(a=W())))
    def SET_Current(self):# تعين قيم عشوائية  للرقم الحالي المعالج
        l1=[randint(1,9),randint(1,9),randint(1,9),randint(1,9)]
        for i in l1:# التاكد ان لايوجد اعداد مكررة 
            i=randint(1,9)
        for i in range(len(l1)) :
             for j in range(len(l1)):
                if(i!=j):
                    if(l1[j]==l1[i]):
                        l1[j]=randint(1,8)+1
        l2=[]
       
        for i in range(1,10):
            if i  not in l1:
                l2.append(i)

        self.declare(Current(a=l1[0]))# التصريح عن القيم العشوائية للرقم الحالي 
        self.declare(Current(b=l1[1]))
        self.declare(Current(c=l1[2]))
        self.declare(Current(d=l1[3]))
        self.declare(active(e=l2[0]))
        self.declare(active(f=l2[1]))
        self.declare(active(j=l2[2]))
        self.declare(active(h=l2[3]))
        self.declare(active(i=l2[4]))
    @Rule(Current(a=MATCH.a),Current(b=MATCH.b),Current(c=MATCH.c),Current(d=MATCH.d),
    active(e=MATCH.e),active(f=MATCH.f),active(j=MATCH.j),active(h=MATCH.h),active(i=MATCH.i),
    # للقاعدة قسمان القسم الاول هو الشروط والقسم الثاني هو ما يتم تنفيذه
    )
    def show_current(self,a,b,c,d,e,f,j,h,i) :# القاعدة الاساسية التي تعالج المدخلات 

        current=[a,b,c,d]# الرقم الحالي 
        correct=[0,0,0,0]# الارقام المكتشفة من الرقم المخفي 
        acvtive=[e,f,j,h,i]# مجموعة الارقام التي من الممكن ان تكون من الرقم الحقيقي 
        wrong=[]# مصفوفة تحتوي على الارقام الخاظئة 
        print("Is number   %s ?" % (current))# عرض الرقم الحالي 
        print("corrent number   %s ?" % (correct))#عرض الرقم الصحيح
        print("wrong number   %s ?" % (wrong))#الارقام الصحيحة في مكان خاطئ
        print("active number   %s ?" % (acvtive))
        correct_place_new=int(input("correct number in correct place  "))#سؤال الاعب عن عدد الارقام الصحيحة في المكان الصحيح
        wrong_place_new=int(input("correct number in wrong place  "))#في المكان الخاطئ
        correct_place_init=correct_place_new# اسناد القيم الجديدة للقديمة 
        wrong_place_init=wrong_place_new
        while(correct_place_new!=-1):#المستخدم لم يدخل -1 كرر
            for index in range(len(current)):# عالج كل الارقام 
                m=index % 4# عدم خروج المؤشر خارج نطاق المصفوفة 
                
                if(correct[index]==0):# الرقم لم يكتشف 
                    for j in range(len(acvtive)) :# عالج جميع الارقام الممكنة
                        z=j % len(acvtive)# # عدم خروج المؤشر خارج نطاق المصفوف
                        if acvtive[j] !=0 :# الرقم لم يعالج اي انه لم تحدد حالته
                            
                            
                                mid=current[index]  #حفظ قيمة الرقم الحالي 
                                current[index]=acvtive[j]# بدل قيمة الرقم الحالي باولرقم ممكن 
                                print("Is number   %s ?" % (current))
                                print("corrent number   %s ?" % (correct))
                                print("wrong number   %s ?" % (wrong))
                                print("active number   %s ?" % (acvtive))
                                correct_place_init=correct_place_new#  الحالة الحالية حفظ 
                                wrong_place_init=wrong_place_new
                                correct_place_new=int(input("correct number in correct place  "))
                                wrong_place_new=int(input("correct number in wrong place  "))
                               #اذا كان عدد الارقام الصحيحة قد زاد 
                                if(correct_place_new-correct_place_init==1):#اذا كان عدد 
                                        #الرقم الممكن الحالي هو رقم صحيح عدل قيمة مصفوفة الارقام الصحيحة 
                                        correct[index]=current[index]
                                        
                                #ذا كان عدد الارقام الصحيحة قد نقص #        
                                if(correct_place_new-correct_place_init==-1):
                                    #القيمة السابقة هي الصحيحة 
                                    current[index]=mid
                                    correct[index]=mid
                                    
                                 #  اذا حصل التغيير    في  القيم الصحيحة في المكان الخاطئ وزاد
                                if(wrong_place_new-wrong_place_init==1):
                                     #ضيف القيمة الحالية الى مصفوفة الارقام الخاطئة 
                                    if (acvtive[j] not in wrong):
                                        #تحقق ان الرقم ليس موجود
                                        wrong.append(acvtive[j])
                                   
                                        
                                    
                                        
                                        
                                 #اذا قل القيم الصحيحة في المكان الخاظئ  
                                if(wrong_place_new-wrong_place_init==-1):
                                    #ضيف القيمة السابقة الى المصفوفة الارقام الصحيححة في المكان الخاطئ
                                    if (mid not in wrong):
                                        wrong.append(mid)
                                # اذا كان لدينا تساوي فنحن امام احتمالين 
                                # ما الرقمين صحيحين في مكان خاطئ او ان الرقمين خاطئين
                                # للمعالجة نقوم بتبديل رقمين الحالي والسابق 
                                # اذا زاد الفرق اي ان الرقمين صحيحين في مكان خاطئ
                                # او اذا لم يتغير ان الرقمين خاطئين     
                                         
                                       
                                  #في حال عدم التعيير   
                                if(wrong_place_new-wrong_place_init==0):
                                    
                                    mid2=current[m+1]#حفظ القيم السابقة 
                                    current[m+1]=mid# بدل الرقم الموجاور بالقيمة العدد السابق
                                    print("Is number   %s ?" % (current))
                                    print("corrent number   %s ?" % (correct))
                                    print("wrong number   %s ?" % (wrong))
                                    print("active number   %s ?" % (acvtive))
                                    #ادخل قيمة التغيير 
                                    wrong_place_new=int(input("correct number in (((((((wrong )))))) place  "))
                                    #اذا زاد  عدد الارقام الصحيحة في المكان الخطئ
                                    if(wrong_place_new-wrong_place_init==1):
                                        #ضيف الرقمين الى الاعداد الصحيحة في المكان الخاطئ
                                        #بعد التاكد من عدم وجودها
                                        if (acvtive[j] not in wrong):
                                           wrong.append(acvtive[j])
                                           
                                           
                                        if (mid not in wrong):    
                                            wrong.append(mid)
                                            for a in range(len(acvtive)):
                                                if mid==acvtive[a]:
                                                    #اسناد قيمة 0 اي ان العدد معالج
                                                    acvtive[a]=0

                               #اسناد القيمة صفر اي ان العدد معالج      
                                acvtive[j]=0
                 #اجعل قيمة الحالية التي تم اكتشاف قيمة العدد الصحيح في مرتبتها تساوي ذلك العدد                   
                if (correct[index] !=0):
                     current[index]=correct[index]
                for n in wrong:#حذف الاعداد المعالجة 
                    if(n==0):
                        wrong.remove(n)
                if(wrong):#عند وجود اعداد في مصفوفة الاعداد الصحيحة في المكان الخاطئ
                       
                        
                        for i in range(len(correct)):# على جميع مراتب العدد الصحيح
                            if correct[index]==0:# في حال كان هناك عدد غير مكتشف 
                                for j in wrong:#على جميع قيم الاعداد ليست في المكان الصحيح
                                    if j!=0:# في حال كان العدد غير مكتشف 
                                        mid=current[index]# حغظ القيم السابقة 
                                        current[index]=j# للعدد الخاطئ اسناد القيمة الحالية 
                                        
                                        correct_place_init=correct_place_new
                                        print("Is number   %s ?" % (current))
                                        print("corrent number   %s ?" % (correct))
                                        #تفحص التغيرات
                                        correct_place_new=int(input("correct number in correct place  "))
                                        if(correct_place_init<correct_place_new):
                                                correct[index]=j
                                        # اذا زاد عدد الاعداد الصحيحة في المكان الصحيح
                                        current[index]=mid
                                        if (correct[index] !=0):# عدل قيم الاعداد الصحيحة
                                            current[index]=correct[index]
                                        


if (start=="y" or start=="Y"):
    
    engine=guesser()# انشاء كائن من نوع محرك استدلال 
    engine.reset() # اعادة تعينها    
    engine.run()  # تشغيل محرك الاستدلال                  
   
else :
    print("okay, see you later")