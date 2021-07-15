# TreeLib
Suppose you are creating documentation of your module. You want make tree of the module. Just like that
<pre>
|----Photon(object)----|
|                      |---__init__(λ,location,direction,spin=(1,0,0),polarization=(1,0))
|                      |---evolve_time(seconds)
|                      |---info()
|
|
|----Beam(object)------|
|                      |---__init__(Photons)
|                      |---info()
|                      |---evolve_time(seconds)
|
|
|----LASER(object)-----|
                       |---__init__(λ,location,direction,intensity)
                       |---fire()

</pre>
You will no longer handle that manually. Now, you can make it automatically.
