
## Taking age data from here:
## https://ourworldindata.org/mortality-risk-covid#case-fatality-rate-of-covid-19-by-age

## The data below is a breakdown of CFR by age group across various
## countries. It shows very large differences of the CFR by age. This
## data is based on the number of confirmed cases and deaths in each
## age group as reported by national agencies.

## The data come from the:

## 1) Chinese Center for Disease Control and Prevention (CDC) as of
##    17th February;

## 2) Spanish Ministry of Health as of 24th March;

## 3) Korea Centers for Disease Control and Prevention (KCDC) as of
##    24th March; and

## 4) Italian National Institute of Health, as presented in the paper
##    by Onder et al. (2020) as of 17th March.17,18


## case_fatality_rate_of_covid_19_by_age
cfrbyage <-
    c(
        0.00, 0.00, 0.00, 0.00, #  0 to  9 years
        0.00, 0.00, 0.20, 0.00, # 10 to 19 years
        0.00, 0.22, 0.20, 0.00, # 22 to 29 years
        0.11, 0.14, 0.20, 0.30, # 30 to 39 years
        0.08, 0.30, 0.40, 0.40, # 40 to 49 years
        0.50, 0.40, 1.30, 1.00, # 50 to 59 years
        1.80, 1.90, 3.60, 3.50, # 60 to 69 years
        6.30, 4.80, 8.00, 12.8, # 70 to 79 years
        13.0, 15.6, 14.8, 20.2  # 80+      years
    )

## Knowing R, there is probably a cleaner way to do this...
cfrbyage.m <- matrix(cfrbyage, 9, byrow=TRUE)
cfrbyage.m

rownames(cfrbyage.m) <- c(
    "0-9",
    "10-19",
    "22-29",
    "30-39",
    "40-49",
    "50-59",
    "60-69",
    "70-79",
    "80+"
)

colnames(cfrbyage.m) <- c(
    "Korea", "Spain", "China", "Italy"
)

cfrbyage.m

## In order to match the plot at Our World in Data, we turn the matrix
## 'upside down' and 'back to front' ...
cfrbyage.m.plot <-
    cfrbyage.m[ nrow(cfrbyage.m):1, ncol(cfrbyage.m):1 ]

barplot(t(cfrbyage.m.plot), beside=TRUE, horiz=TRUE, col=c(5,6,7,4),
        xlab='Case fatality rate (%)', ylab='Years')



## There is no such thing as the 'average CFR'... ... ... Hey! Lets
## pretend there is!
cfronavg <- 0.1


## Calculate the Odds Ratio
cfrbyage.m / cfronavg

## Mean Odds Ratio across all studies
or.mean <-
    apply(cfrbyage.m / cfronavg, 1, mean)
or.mean

or.sd <-
    apply(cfrbyage.m / cfronavg, 1, sd)
or.sd


x <- barplot(or.mean)

my.ylim <-
    c(min(or.mean-or.sd), max(or.mean+or.sd))


barplot(or.mean, ylim=my.ylim)
points(x, or.mean+or.sd)
points(x, or.mean-or.sd)


## Cludge in a log scale...
barplot(log(or.mean+0.01))


## Trying a different way

## We add a very small CFR to allow for 0% CFR conversion to Log Odds
lod <- log((cfrbyage.m + 0.01) / cfronavg)
lod

barplot(t(lod), beside=TRUE, horiz=TRUE,
        col=c(5,6,7,4))


## To add insult to injury, lets average over all four studies...

means <-
    apply(lod, 1, mean)
stdevs <-
    apply(lod, 1, sd)

x <-
    barplot(means, ylim=c(-3, 6))

points(x, means+stdevs)
points(x, means-stdevs, pch=2)


## Me no stats good? Unprobable!
barplot(rbind(means+stdevs, means,
              means-stdevs), beside=TRUE)



## Got the age Odds Ratios above.

## The SNP Odds Ratios are...
baseline.cfr = 0.1

## TT at rs12329760 = 0
rs12329760.tt = 0.146*0 / baseline.cfr

## CT at rs12329760 = 0.146
rs12329760.ct = 0.146*1 / baseline.cfr

## CC at rs12329760
rs12329760.cc = 0.146*2 / baseline.cfr


## CC at rs75603675
rs75603675.cc = 0.148*0 / baseline.cfr
rs75603675.ac = 0.148*1 / baseline.cfr
rs75603675.aa = 0.148*2 / baseline.cfr


## Produce some nice plots...

install.packages("dotwhisker")

library(dotwhisker)
library(broom)
library(dplyr)

m1 <- lm(mpg ~ wt + cyl + disp + gear, data = mtcars)

m1
tidy(m1)

dwplot(m1)
dwplot(tidy(m1))

m1.df <-
    tidy(m1)

m1.df
m1.df$p.value <- 0
m1.df$statistic <- 0

dwplot(m1, style="distribution")

age <- '10-19'
age <- '50-59'
age <- '60-69'

ex1 <- 
    data.frame(
        term=c('age (10-19)', 'rs12329760', 'rs75603675'),
        estimate=c(
            or.mean[age],
            rs12329760.ct,
            rs75603675.ac
        ),
        std.error=c(
            sqrt(or.sd[age]),
            3, 3) 
    )
ex1

dwplot(ex1, style="distribution")
