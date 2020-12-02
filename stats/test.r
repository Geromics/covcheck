
## Generate some random categorical data
x <- round(rnorm(1000, 100) * 10)

head(x)

barplot(table(x))

t <- table(x)

## Change to frequencies
t <- t/1000

barplot(t)

## Average frequency?
a <- mean(t)
a

## relative frequence over the average
head(t)
head(t/a)

barplot(t/a)

barplot(log(t/a))


## Taking age data from here:
https://ourworldindata.org/mortality-risk-covid#case-fatality-rate-of-covid-19-by-age

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


case_fatality_rate_of_covid_19_by_age <-
    c(
        0.00, 0.00, 0.00, 0.00, #  0     9
        0.00, 0.00, 0.20, 0.00, # 10 to 19
        0.00, 0.22, 0.20, 0.00, # 22 to 29
        0.11, 0.14, 0.20, 0.30, # 30 to 39
        0.08, 0.30, 0.40, 0.40, # 40 to 49
        0.50, 0.40, 1.30, 1.00, # 50 to 59
        1.80, 1.90, 3.60, 3.50, # 60 to 69
        6.30, 4.80, 8.00, 12.8, # 70 to 79
        13.0, 15.6, 14.8, 20.2  # 80 to ... 
    )

cfrbyage <- case_fatality_rate_of_covid_19_by_age

## Knowing R, there is probably a cleaner way to do this...
cfrbyage.m <- matrix(rev(cfrbyage), 9, byrow=TRUE)
cfrbyage.m

rownames(cfrbyage.m) <- c(
    "80+ years",
    "70-79 years",
    "60-69 years",
    "50-59 years",
    "40-49 years",
    "30-39 years",
    "22-29 years",
    "10-19 years",
    " 0- 9 years"
)

colnames(cfrbyage.m) <- c(
 "Italy", "China",   "Spain", "Korea")

cfrbyage.m

barplot(t(cfrbyage.m), beside=TRUE, horiz=TRUE,
        col=c(5,6,7,4))

## There is no such thing as 'the average CFR'... However, lets
## pretend there is!
cfronavg <- 0.1


lod <- log(cfrbyage.m + 0.001 / cfronavg)
lod

barplot(t(lod), beside=TRUE, horiz=TRUE,
        col=c(5,6,7,4))
