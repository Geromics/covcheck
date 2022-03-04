
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

