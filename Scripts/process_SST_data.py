import setup
import xarray as xr
import matplotlib.pyplot as plt

setup.dataPath

if __name__ == '__main__':

	#set up variables
	finename = 'HadISST_sst.nc'

	#access SST variable
	sst = data.sst

	#import file
	data = xr.open_dataset(filename)
	mean = data.sst.mean("team")
	print(mean.dims)
	#plotting
	fig = plt.figure[]
	ax = plt.axes(projection= '3d')
	#calculate mean 
	print("the sst mean is ", sst.mean())

	#save other data as variables
	longitude = data.sst.longitude
	latitude = data.sst.latitude
	#print (longitude)
	#print (latitude)

	#access coordinate variable
	#print(data.sst.coords)

	data.mean(dim ="time")

	mean = data.mean("time")
