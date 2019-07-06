a3 = read.csv("/Users/Joy/Desktop/STA302/A3/A3 JOY DATA zhiqian.csv",header=TRUE)

#Regression between Death Rate and the average annual precipitation
lm_fit1 = lm(a3$DEATH.RATE ~ a3$AVP)
summary(lm_fit1)
plot(a3$DEATH.RATE ~ a3$AVP)
abline(lm_fit1)

#Regression between Death Rate and the number of members per household
lm_fit3 = lm(a3$DEATH.RATE ~ a3$MPH)
summary(lm_fit3)
plot(a3$DEATH.RATE ~ a3$MPH)
abline(lm_fit3)

#Regression between Death Rate and the number of years of schooling for persons over 22 m###############
lm_fit4 = lm(a3$DEATH.RATE ~ a3$YSP22)
summary(lm_fit4)
plot(a3$DEATH.RATE ~ a3$YSP22)
abline(lm_fit4)

#Regression between Death Rate and the number of households with fully equipped kitchens
lm_fit5 = lm(a3$DEATH.RATE ~ a3$HFK)
summary(lm_fit5)
plot(a3$DEATH.RATE ~ a3$HFK)
abline(lm_fit5)

#Regression between Death Rate and the number of families with an income less than $3000 ###############
lm_fit6 = lm(a3$DEATH.RATE ~ a3$NFL3)
summary(lm_fit6)
plot(a3$DEATH.RATE ~ a3$NFL3)
abline(lm_fit6)

#correlation between poor family and the number of years of schooling for persons over 22.
cor.test(a3$NFL3,a3$YSP22)


#Regression between Death Rate and the sulfur dioxide pollution index
lm_fit7 = lm(a3$DEATH.RATE ~ a3$SDP)
summary(lm_fit7)
plot(a3$DEATH.RATE ~ a3$SDP)
abline(lm_fit7)

#Mutiple Regression
lm_fit8 = lm(a3$DEATH.RATE ~ a3$AVP + a3$MPH + a3$YSP22 + a3$HFK + a3$NFL3 + a3$SDP + a3$HP + a3$DA)
summary(lm_fit8)
plot(a3$DEATH.RATE ~ a3$AVP + a3$MPH + a3$YSP22 + a3$HFK + a3$NFL3 + a3$SDP + a3$HP + a3$DA)
abline(lm_fit8)


#After removing YSP22 and the number of families with an income less than $3000 
lm_fit9 = lm(a3$DEATH.RATE ~  a3$AVP + a3$MPH+ a3$SDP )
summary(lm_fit9)

anova(lm_fit9,lm_fit8)


#DA
lm_fit12 = lm(a3$DEATH.RATE ~ a3$DA)
summary(lm_fit12)
plot(a3$DEATH.RATE ~ a3$DA)
abline(lm_fit12)

#transformation of DA
a3$trDA = (a3$DA)^(20)
lm_fit13 = lm(a3$DEATH.RATE ~ a3$trDA)
summary(lm_fit13)

#HP
lm_fit11 = lm(a3$DEATH.RATE ~ a3$HP)
summary(lm_fit11)
plot(a3$DEATH.RATE ~ a3$HP)
abline(lm_fit11)


#transformation of HP
a3$trHP = (a3$HP)^(1/10000000)
lm_fit14 = lm(a3$DEATH.RATE ~ a3$trHP)
summary(lm_fit14)




mycor <- function ( data ){
# ------------ put histograms on the diagonal -----------------
panel.hist <- function (x , ...) {
  usr <- par ("usr") ; on.exit ( par ( usr ))
  par ( usr = c( usr [1:2] , 0, 1.5) )
  h <- hist (x , plot = FALSE )
  breaks <- h$ breaks ; nB <- length ( breaks )
  y <- h$ counts ; y <- y/ max (y)
  rect ( breaks [ - nB ] , 0, breaks [ -1] , y , col ="lavender", ...)}
panel.cor <- function (x , y , digits =4 , prefix ="", cex.cor , ...) {
    usr <- par ("usr") ;
    on.exit ( par ( usr ))
    par ( usr = c(0 , 1 , 0 , 1) )
    txt1 <- format ( cor (x ,y) , digits = digits )
    txt2 <- format (cor.test (x ,y)$p.value , digits = digits )
    text (0.5 ,0.5 , paste ("r=",txt1 , "\n P. val =", txt2 ) , cex =0.8)}
pairs (data , lower.panel = panel.cor , cex =0.7 , pch = 21 , bg =" steelblue ", diag.panel = panel.hist , cex.labels = 1.1 , font.labels = 0.9 , upper.panel = panel.smooth )
   }

mycor(a3[,c(9,1:8)])



