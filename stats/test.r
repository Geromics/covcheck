
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

## relative frequency over the average
head(t)
head(t/a)

barplot(t/a)

barplot(log(t/a))


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


case_fatality_rate_of_covid_19_by_age <-
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

cfrbyage <- case_fatality_rate_of_covid_19_by_age

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
 "Italy", "China",   "Spain", "Korea")

cfrbyage.m

## In order to match the plot at Our World in Data, we turn the matrix
## 'upside down'...
cfrbyage.m <-
    cfrbyage.m[ nrow(cfrbyage.m):1, ]




barplot(t(cfrbyage.m), beside=TRUE, horiz=TRUE, col=c(5,6,7,4),
        xlab='Case fatality rate (%)', ylab='Years')

## There is no such thing as 'the average CFR'... However, lets
## pretend there is!
cfronavg <- 0.1


## Odds ratio (below we work with log odds for some reason)
cfrbyage.m / cfronavg

apply(cfrbyage.m / cfronavg, 1, mean)



## We add a very small CFR to allow for 0% CFR conversion to Log Odds
lod <- log(cfrbyage.m + 0.01 / cfronavg)
lod

barplot(t(lod), beside=TRUE, horiz=TRUE,
        col=c(5,6,7,4))


## To add insult to injury, lets average over all four studies...

means <-
    apply(lod, 1, mean)
stdevs <-
    apply(lod, 1, sd)

barplot(rev(means))


## Me no stats good? Unprobable!
barplot(rbind(means+stdevs, means,
              means-stdevs), beside=TRUE)
