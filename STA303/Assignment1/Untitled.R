heightt = read.csv("~/Desktop/STA303/Assignment1/assign1data.csv",header=TRUE)
heightM = height[sex == "Male"]
heightF = height[sex != "Male"]
boxplot(heightM,heightF,xlab="Height2230",names = c("Height_Male","Height_Female"))



juries = read.csv("~/Desktop/STA303/Assignment1/juries.csv",header=TRUE)
groupS = PERCENT[JUDGE== "SPOCKS"]
groupNS = PERCENT[JUDGE!= "SPOCKS"]
boxplot(groupS,groupNS,xlab="JUDGE2230",names = c("SPOCKS","OTHERES"))
