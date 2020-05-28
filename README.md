# Globeloc

that one true unified global data repository.

## How does it work?

There are multiple parts to this.

1. Client library - pandas/numpy like which lets you create, distribute, gather and compute on spatial data.

2. Server - a Flask REST API that lets you save data, pull down other data and even do remote computation

3. A web app - Github like where you can manage data sets via the UI and browse other contributors data


## Contribute

### Installation

```
git clone https://github.com/fhk/globeloc
cd globeloc
# insert your flavour of virtual env here
conda create -n globeloc python=3.7
conda activate globeloc
pip install -r requirements.txt
``` 

### Client

The client library extends scipy sparse arrays and gives you a way to insert spatial data into them.

These can then be saved, loaded, shared and computed on.

In the simplest case you can parse any file which can be read with geopandas (fiona).

For example:

```
from globeloc.globeloc import GlobeLoc as glc

gdf = glc()
gdf.connect(url="http://127.0.0.1:8080")
#gdf.connect(url="local")
my_unique_data = gdf.parse("./gis_osm_pois_free_1.shp", column="fclass", sub_category="hotel")

response = gdf.save(my_unique_data)

gdf.load("10f2481e-9fce-11ea-89d1-3b195c02ff70")

gdf['hotel'][:] + gdf['park'][:]
```



### Server

The server is a Flask server which is codegened from the swagger.json file.

However, the code gen is only run to add new end points and the other controller must be preserved.

The server lives in the "./api" folder.

To start the server run

```
cd api
python -m swagger_server
```

You can now access the end points on local host port 8080

```
/save
/load
```

However, these are not used directly. Rather the transaction is handled by the client library with the methods of the same name.


### Example Notebooks

There are two notebooks.
```
./notebooks
    globeloc_core.ipynb (1)
    test_lib.ipynb (2)
```

1. Is a exploration of the data and how to store it. This was the R&D that lead to the creation of globeloc.
2. Presents the ways that you can use the library and data store.