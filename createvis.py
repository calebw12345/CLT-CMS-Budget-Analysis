#open the csv file and convert it to a csv list
#Author: Caleb w

#open the excel file and convert it to a manipulatable csv file
import csv
import matplotlib.pyplot
filename = "sep21pub.csv"
fileobject = open(filename)
all_data = csv.reader(fileobject)
dislist = list(all_data)

#iterate through the csv list and pull all of charlotte,orlando,and columbus data
cltData = []
blank=0
for j in range(len(dislist)):
    tempData=[]
    
    if dislist[j][372] == '16740' or dislist[j][372] == '36740' or dislist[j][372] == '18140': 
        
        #Highest level of school acheived (code:peeduca)(row:dt)
        tempData.append(dislist[j][123])

        #DISREGARD THIS ROW. ITS A FILLER ROW TO KEEP INDEXING ON TRACK
        tempData.append(dislist[j][274])
        
        #msa code(code:gtcbsa)(row:ni)
        tempData.append(dislist[j][372])
        
        #Annual income (code:hefaminc)(row:ah)
        tempData.append(dislist[j][33])
        
        #"What is the main reason you dont want to work full time?"  or training(code:pehrrsn2)(row:gg)
        tempData.append(dislist[j][188])
        
         #"What best describes your current situation?"                          (code:pelnfact)(row:hd)
        tempData.append(dislist[j][211])
        
        #"Highest grade of regular school before getting GED?"                (code:pehgcomp)
        tempData.append(dislist[j][143])
        
        cltData.append(tempData)
        
        
    else:
        blank=blank+1
    
    #keep track of the HAC(highest achieved education) of charlotte cps subjects
high1=0
bach1=0
mast1=0
blank1=0


u1=0
for i in range(len(cltData)):
    if cltData[i][2] == '16740':
        
        if cltData[u1][0]=='36' or cltData[u1][0]=='37' or cltData[u1][0]=='38' or cltData[u1][0]=='39':
            high1=high1+1
        if cltData[u1][0]=='40' or cltData[u1][0]=='41' or cltData[u1][0]=='42' or cltData[u1][0]=='43' :
            bach1=bach1+1
        if cltData[u1][0]=='44' or cltData[u1][0]=='45' or cltData[u1][0]=='46' :
            mast1=mast1+1
            
        else:
            
            blank1=blank1+1
    
        u1=u1+1
        
    else:
        u1=u1+1
        
 #keep track of the income of charlotte cps subjects
low1=0
med1=0
hi1=0
blank1=0


u1=0
for i in range(len(cltData)):
    if cltData[i][2] == '16740':
    
    
    
    
    
        if cltData[u1][3]=='1' or cltData[u1][3]=='2' or cltData[u1][3]=='3' or cltData[u1][3]=='4' or cltData[u1][3]=='5' or cltData[u1][3]=='6' or cltData[u1][3]=='7' or cltData[u1][3]=='8' or cltData[u1][3]=='9' or cltData[u1][3]=='10':
            low1=low1+1
        if cltData[u1][3]=='11' or cltData[u1][3]=='12' or cltData[u1][3]=='13' or cltData[u1][3]=='14' :
            med1=med1+1
        if cltData[u1][3]=='15' or cltData[u1][3]=='16':
            hi1=hi1+1
        else:
            blank1=blank1+1
        u1=u1+1
    else:
        u1=u1+1

#keep track of the percent of people in clt surveyed by the cps that don't want to work full time because of school
school1=0


tot1=0
blank1=0
for i in range(len(cltData)):
    if cltData[i][2] == '16740':
        
        if cltData[i][4]=='4':
            school1=school1+1
            tot1=tot1+1
        if cltData[i][4]=='-1' or cltData[i][4]=='':
            blank=blank+1
        
            
        else:
            tot1=tot1+1
answer1=100*(school1/tot1)           
print("%"+str(100*(school1/tot1)))

#keep track of the percent of people in clt surveyed by the cps that define their circumstance primarily as school
sch1=0


tott1=0
blank1=0
for i in range(len(cltData)):
    if cltData[i][2] == '16740':
        
        if cltData[i][5]=='3':
            sch1=sch1+1
            tott1=tott1+1
        if cltData[i][5]=='-1' or cltData[i][4]=='':
            blank=blank+1
        
            
        else:
            tott1=tott1+1
answer1=100*(sch1/tott1)           
print("%"+str(100*(sch1/tott1)))

 #keep track of the HAC(highest achieved education) of charlotte cps subjects
eight1=0
twelve1=0
u1=0
for i in range(len(cltData)):
    if cltData[i][2] == '16740':
        
        if cltData[i][0]=='1' or cltData[i][0]=='2' or cltData[i][0]=='3' or cltData[i][0]=='4':
            eight1=eight1+1
        if cltData[i][0]=='5' or cltData[i][0]=='6' or cltData[i][0]=='7' or cltData[i][0]=='8' :
            twelve1=twelve1+1
        
            
        else:
            
            blank1=blank1+1
    
        u1=u1+1
        
    else:
        u1=u1+1
        
print(eight1)

 #keep track of the HAC of ORL cps subjects
high=0
bach=0
mast=0
blank=0


u=0
for i in range(len(cltData)):
    if cltData[i][2] == '36740':
    
    
    
    
        if cltData[u][0]=='36' or cltData[u][0]=='37' or cltData[u][0]=='38' or cltData[u][0]=='39':
            high=high+1
        if cltData[u][0]=='40' or cltData[u][0]=='41' or cltData[u][0]=='42' or cltData[u][0]=='43' :
            bach=bach+1
        if cltData[u][0]=='44' or cltData[u][0]=='45' or cltData[u][0]=='46' :
            mast=mast+1
        else:
            blank=blank+1
        u=u+1    
    else:
        u=u+1
print(high,bach,mast)

 #keep track of the income of ORL cps subjects
low=0
med=0
hi=0
blank1=0
u1=0
for i in range(len(cltData)):
    if cltData[i][2] == '36740':
    
    
    
    
    
        if cltData[u1][3]=='1' or cltData[u1][3]=='2' or cltData[u1][3]=='3' or cltData[u1][3]=='4' or cltData[u1][3]=='5' or cltData[u1][3]=='6' or cltData[u1][3]=='7' or cltData[u1][3]=='8' or cltData[u1][3]=='9' or cltData[u1][3]=='10':
            low=low+1
        if cltData[u1][3]=='11' or cltData[u1][3]=='12' or cltData[u1][3]=='13' or cltData[u1][3]=='14':
            med=med+1
        if cltData[u1][3]=='15' or cltData[u1][3]=='16':
            hi=hi+1
        else:
            blank1=blank1+1
        u1=u1+1
    else:
        u1=u1+1
print(low,med,hi) 

#keep track of the percent of people in ORL surveyed by the cps that don't want to work full time because of school
school=0
tot=0
blank1=0
for i in range(len(cltData)):
    if cltData[i][2] == '36740':
        
        if cltData[i][4]=='4':
            school=school+1
            tot=tot+1
        if cltData[i][4]=='-1' or cltData[i][4]=='':
            blank=blank+1
        
            
        else:
            tot=tot+1
answer=100*(school/tot)           
print("%"+str(100*(school/tot)))

#keep track of the percent of people in orl surveyed by the cps that define their circumstance primarily as school
sch=0
tott=0
blank1=0

for i in range(len(cltData)):
    if cltData[i][2] == '36740':
        
        if cltData[i][5]=='3':
            sch=sch+1
            tott=tott+1
        if cltData[i][5]=='-1' or cltData[i][4]=='':
            blank=blank+1
        
            
        else:
            tott=tott+1
answer1=100*(sch/tott)           
print("%"+str(100*(sch/tott)))

#keep track of the HAC of columbus cps subjects
high2=0
bach2=0
mast2=0
blank2=0
u2=0
for i in range(len(cltData)):
    if cltData[i][2] == '18140':
    
        if cltData[u2][0]=='36' or cltData[u2][0]=='37' or cltData[u2][0]=='38' or cltData[u2][0]=='39':
            high2=high2+1
        if cltData[u2][0]=='40' or cltData[u2][0]=='41' or cltData[u2][0]=='42' or cltData[u2][0]=='43' :
            bach2=bach2+1
        if cltData[u2][0]=='44' or cltData[u2][0]=='45' or cltData[u2][0]=='46' :
            mast2=mast2+1
        else:
            blank2=blank2+1
        u2=u2+1    
    else:
        u2=u2+1
print(high2,bach2,mast2)

#keep track of the income of columbus cps subjects
low2=0
med2=0
hi2=0
blank1=0
u1=0
for i in range(len(cltData)):
    if cltData[i][2] == '18140':
        if cltData[u1][3]=='1' or cltData[u1][3]=='2' or cltData[u1][3]=='3' or cltData[u1][3]=='4' or cltData[u1][3]=='5' or cltData[u1][3]=='6' or cltData[u1][3]=='7' or cltData[u1][3]=='8' or cltData[u1][3]=='9' or cltData[u1][3]=='10':
            low2=low2+1
        if cltData[u1][3]=='11' or cltData[u1][3]=='12' or cltData[u1][3]=='13' or cltData[u1][3]=='14' :
            med2=med2+1
        if cltData[u1][3]=='15' or cltData[u1][3]=='16':
            hi2=hi2+1
        else:
            blank1=blank1+1
        u1=u1+1
    else:
        u1=u1+1
print(low2,med2,hi2)


#keep track of the percent of people in col surveyed by the cps that don't want to work full time because of school
school2=0
tot2=0
blank1=0
for i in range(len(cltData)):
    if cltData[i][2] == '18140':
        
        if cltData[i][4]=='4':
            school2=school2+1
            tot2=tot2+1
        if cltData[i][4]=='-1' or cltData[i][4]=='':
            blank=blank+1
        
            
        else:
            tot2=tot2+1
answer2=100*(school2/tot2)           
print("%"+str(100*(school2/tot2)))
print(school)


#keep track of the percent of people in cin surveyed by the cps that define their circumstance primarily as school
sch2=0
tott2=0
blank1=0
for i in range(len(cltData)):
    if cltData[i][2] == '18140':
        
        if cltData[i][5]=='3':
            sch2=sch2+1
            tott2=tott2+1
        if cltData[i][5]=='-1' or cltData[i][4]=='':
            blank=blank+1
        
            
        else:
            tott2=tott2+1
answer1=100*(sch2/tott2)           
print("%"+str(100*(sch2/tott2)))


#creates a graph comparing HAC of CLT,ORL,and CIN CPS subjects
majors = ["Highschool or lower","Bachelors","Masters+"]
ci = [high,bach,mast]
c=[high1,bach1,mast1]
co =[high2,bach2,mast2]
b1=matplotlib.pyplot.bar([0,1,2], ci,width=.2,color='red')
b2=matplotlib.pyplot.bar([.5,1.5,2.5], c,width=.2,color='green')
b3=matplotlib.pyplot.bar([.25,1.25,2.25], co,width=.2,color='orange')
matplotlib.pyplot.xlabel("Education Status")
matplotlib.pyplot.ylabel("Number of People")
matplotlib.pyplot.xticks([.25,1.25,2.25], majors)
matplotlib.pyplot.legend((b2,b1,b3),['Charlotte','Orlando','Columbus']);
matplotlib.pyplot.title('Education Status of CPS Participants: Charlotte vs. Orlando vs. Columbus', fontsize=20)
matplotlib.pyplot.show()


#creates a bar chart that shows income distribution of CPS subjects in CLT,ORL,and COL
majors = ["39k or lower","39k-100k","100k+"]
ci = [low,med,hi]
c=[low1,med1,hi1]
co =[low2,med2,hi2]
b1=matplotlib.pyplot.bar([0,1,2], ci,width=.2,color='red')
b2=matplotlib.pyplot.bar([.5,1.5,2.5], c,width=.2,color='green')
b3=matplotlib.pyplot.bar([.25,1.25,2.25], co,width=.2,color='orange')
matplotlib.pyplot.xlabel("Annual Income Classification")
matplotlib.pyplot.ylabel("Number of People")
matplotlib.pyplot.xticks([.25,1.25,2.25], majors)
matplotlib.pyplot.legend((b2,b1,b3),['Charlotte','Orlando','Columbus']);
matplotlib.pyplot.title('Annual Income of CPS Participants: Charlotte vs. Orlando vs. Columbus', fontsize=15)
matplotlib.pyplot.show()


#creates a pie chart that shows the percentage of CPS subjects in ORL who answered that they dont work due to school
import matplotlib.pyplot
majors = ["%27.58 dont work full time due to school","%72.42 dont work full time due to other"]#,"Charlotte: %30.43","Columbus: %24.13"
num_students=[(100*(school/tot)),100-(100*(school/tot))]
matplotlib.pyplot.pie(num_students, labels = majors)
matplotlib.pyplot.title('Percent of CPS Subjects in ORL that Dont Work Due to School',fontsize=20)
matplotlib.pyplot.show()


#creates a pie chart that shows the percentage of CPS subjects in COL who answered that they dont work due to school
majors = ["%24.13 dont work full time due to school","%75.87 dont work full time due to other"]
num_students=[(100*(school2/tot2)),100-(100*(school2/tot2))]
matplotlib.pyplot.pie(num_students, labels = majors)
matplotlib.pyplot.title('Percent of CPS Subjects in COL that Dont Work Due to School',fontsize=20)
matplotlib.pyplot.show()


#creates a pie chart that shows the percentage of CPS subjects in CLT who answered that they dont work due to school
majors = ["%30.43 dont work full time due to school","%69.57 dont work full time due to other"]
num_students=[(100*(school1/tot1)),100-(100*(school1/tot1))]
matplotlib.pyplot.pie(num_students, labels = majors)
matplotlib.pyplot.title('Percent of CPS Subjects in CLT that Dont Work Due to School',fontsize=20)
matplotlib.pyplot.show()


#creates a pie chart that shows the percentage of CPS subjects in ORL who answered that their primary focus in life is school
import matplotlib.pyplot
majors = ["%34.58 identify their current circumstance as primarily school focused","%65.42 Identify their current circumstance as other focuses"]
num_students=[(100*(sch/tott)),100-(100*(sch/tott))]
matplotlib.pyplot.pie(num_students, labels = majors)
matplotlib.pyplot.title('Percent of CPS Subjects in ORL Identify Their Current Circumstance as "School Focused"',fontsize=20)
matplotlib.pyplot.show()


#creates a pie chart that shows the percentage of CPS subjects in CLT who answered that their primary focus in life is school
majors = ["%33.02 identify their current circumstance as primarily school focused","%66.98 Identify their current circumstance as other focuses"]
num_students=[(100*(sch1/tott1)),100-(100*(sch1/tott1))]
matplotlib.pyplot.pie(num_students, labels = majors)
matplotlib.pyplot.title('Percent of CPS Subjects in CLT Identify Their Current Circumstance as "School Focused"',fontsize=20)
matplotlib.pyplot.show()


#creates a pie chart that shows the percentage of CPS subjects in COL who answered that their primary focus in life is school
majors = ["%34.14 identify their current circumstance as primarily school focused","%65.86 Identify their current circumstance as other focuses"]
num_students=[(100*(sch2/tott2)),100-(100*(sch2/tott2))]
matplotlib.pyplot.pie(num_students, labels = majors)
matplotlib.pyplot.title('Percent of CPS Subjects in COL Identify Their Current Circumstance as "School Focused"',fontsize=20)
matplotlib.pyplot.show()

