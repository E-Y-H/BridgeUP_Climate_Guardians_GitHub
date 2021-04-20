import setup
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

setup.datapath

if __name__ == '__main__':

        filename = "HadISST_sst.nc"

        data = xr.open_dataset(filename)

        sst = data.sst


plt.figure()
plt.contourf(sst.longitude,sst.latitude,sst.where(sst >= 0).mean(dim="time"), cmap= "cool")
plt.colorbar(label = 'temperature')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.show()

plt.figure(figsize = (20,10))
plt.contourf(atlantic2.longitude,atlantic2.latitude,atlantic2.where(sst >=0).mean(dim="time"), cmap = "cool")
plt.title("The Atlantic")
plt.colorbar(label = 'temperature')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.show()
