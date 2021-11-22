# Test image for r plot of eye tracking data.

install.packages("png")

library(png)
#Load image
setwd("/mnt/WinLab/Fiza/SensoryImmersion/SensoryFeedbackData/EyeTrackingData/124/000/exports/000/surfaces")
my_image <- readPNG("/home/fiza/Documents/SF_Immersion/cleooverlay.png")

#Load Data
dat <- read.csv("fixations_on_surface_Cleo.csv", header = TRUE)
export <- read.csv("../export_info.csv", header = TRUE)


#Transform data based on AOIs
reelsfixations <- dat[ which(dat$norm_pos_x >= 0.116211 & dat$norm_pos_x <= 0.883789 & dat$norm_pos_y >= 0.161538 & dat$norm_pos_y <= 0.95), ]
winfixations <- dat[ which(dat$norm_pos_x >= 0.661133  & dat$norm_pos_x <= 0.864258 & dat$norm_pos_y >= 0.007692 & dat$norm_pos_y <= 0.136538), ]
creditsfixations <- dat[ which(dat$norm_pos_x >= 0.478516   & dat$norm_pos_x <= 0.648438 & dat$norm_pos_y >= 0.026923 & dat$norm_pos_y <= 0.111538), ]

#Plot CSV

plot(0:1, 0:1, type='n', main="", xlab="", ylab="")

lim <- par()
rasterImage(my_image, 
            xleft=0, xright=1, 
            ybottom=0, ytop=1)
par(bg= 'NA')


points(
  x=dat$norm_pos_x, 
  y=dat$norm_pos_y, 
  type="p", lwd=8, col="grey")

points(
  x=reelsfixations$norm_pos_x, 
  y=reelsfixations$norm_pos_y, 
  type="p", lwd=8, col="magenta")

points(
  x=winfixations$norm_pos_x, 
  y=winfixations$norm_pos_y, 
  type="p", lwd=8, col="cyan")

points(
  x=creditsfixations$norm_pos_x, 
  y=creditsfixations$norm_pos_y, 
  type="p", lwd=8, col="yellow")
