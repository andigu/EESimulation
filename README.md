#Simulation of the Path of a Photon

Created from an idealized model of a surface, with the following assumptions:
* Light enters the cover layer at every angle with equal intensity
* The surface is composed entirely of a grid of identical right cones with a base diameter b and a height h. This 
gives rise to surface roughness: cones with a larger h/b ratio will cause the R value of the surface to increase. 
The b and h themselves do not affect the outcome of the simulation, only the h/b ratio is relevant. Thus, for 
brevity’s sake, this ratio is labelled r. Taking the cross section of any part on the surface will result in a row 
of identical isosceles triangles – these triangles will have an identical r to the r value of every cone.
* Snell’s law is obeyed, where the index of refraction of air n<sub>air</sub>=1 and the index of refraction of the 
acrylic n<sub>acrylic</sub>=1.49
* Every point at which the light enters the surface, part of the beam is reflected outwards. If the beam carried 
energy E before entering, it will have (1-ρ)E after, where ρ is the reflectance of acrylic. ρ for clear acrylic is 
typically  given as 4%. 

Using geometry and Snell's law, the path of any given beam of light was predicted. The math behind this method is shown
in _entrance.pdf_ and _exit.pdf_. 

To get a visual representation of the light diffraction phenomena, use `draw.py`. To purely obtain data, use 
`calculate.py`.
