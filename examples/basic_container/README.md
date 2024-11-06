# Basic Container Example

This code represents a basic container that converts a parquet file to JSON.
The container runs a corresponding python script that takes two arguements - ``--input`` and ``--output`` with the names of files to read and to write respectively.

To run the container, use the following command for example

```
docker run -v <folder>:/data ghcr.io/gemello-digitale-bologna/gdb-hpc-integration/basic_container:0.1s --input /data/<inputfile> --output /data/<outputfile>
```