# the following algorithm is for 
# finding the closest pair of points using the 
# divide and conquer algorithm

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
x=np.random.randn(20)
print(x)
y=np.random.randn(20)
#y=np.random.random(-3,3,8)
print(y)
coordinates=[]
for i in range(len(x)):
    coordinates.append((x[i],y[i]))
# we will sort the coordinates in coordinates of x
coordinates.sort()
print(coordinates)

# let x = 0 be the spiting point
# the following problem will be solved 
# using the divide and conquer approach


# for x<0 this is the minimum distance
distance_for_x_lt_0={}
i=0

while(coordinates[i][0]<0):
	for j in range(len(x)):
		if(coordinates[j][0]<0 and i!=j and j>i):
			distance_for_x_lt_0[((coordinates[i][0],coordinates[i][1]),
			(coordinates[j][0],coordinates[j][1]))]=((
			(coordinates[i][0]-coordinates[j][0])**2+
			(coordinates[i][1]-coordinates[j][1])**2
			)**0.5)
			
			# distance_for_x_lt_0.append((
			# (coordinates[i][0]-coordinates[j][0])**2+
			# (coordinates[i][1]-coordinates[j][1])**2
			# )**0.5)
	i+=1
#print(distance_for_x_lt_0)
# for key in distance_for_x_lt_0:
	# print ('value is ',distance_for_x_lt_0[key])
	# print ('key is  is ',key)
key1=min( distance_for_x_lt_0)
print('minimum distance when x<0 is ', min( distance_for_x_lt_0))
print('minimum distance value x<0 is ', distance_for_x_lt_0[key1])
#----------------
# for x>0 this is the minimum distance
distance_for_x_gt_0={}
i=i+1
while(coordinates[i][0]>0):
	for j in range(len(x)):
		if(coordinates[j][0]>0 and i!=j and j>i):
			distance_for_x_gt_0[((coordinates[i][0],coordinates[i][1]),
			(coordinates[j][0],coordinates[j][1]))]=((
			(coordinates[i][0]-coordinates[j][0])**2+
			(coordinates[i][1]-coordinates[j][1])**2
			)**0.5)
	i+=1
	if(i==len(x)):
		break
#-
key2=min( distance_for_x_gt_0)
print('minimum distance coordinates when x>0 is ', min( distance_for_x_gt_0))
print('minimum distance value x<0 is ', distance_for_x_gt_0[key2])

minimua1={}
#minimum among the left and right half of the origin
if(distance_for_x_lt_0[key1]>distance_for_x_gt_0[key2]):
	minimua1[key2]=distance_for_x_gt_0[key2]
else:
	minimua1[key1]=distance_for_x_lt_0[key1]

print('minima is')	
print(minimua1)
# now that minimum coordinate is found we can find 
# if there are any coordinate which are in the minimum box near the origin 
# if there are no coordinates then we juust ignore
# else we will have to consider them as well

# this can maximum have 6 values inside itemswhich will make it easier to find in O(n)
newMinima={}
for i in range(len(x)):
	if coordinates[i][0]>0 and coordinates[i][0]<=min([distance_for_x_lt_0[key1],distance_for_x_gt_0[key2]]):
		newMinima[((coordinates[i][0],coordinates[i][1]),
			(coordinates[j][0],coordinates[j][1]))]=((
			(coordinates[i][0]-coordinates[j][0])**2+
			(coordinates[i][1]-coordinates[j][1])**2
			)**0.5)

			
print('new minima in x',newMinima)
print (' if new minima is a null set {} then we conclude')
print('  minimua1 is the shortest pair of coordinates that we have ')

# this is the plot of points
plt.plot(x,y,'*')
plt.show()