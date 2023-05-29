# Medjed Optics

Optical designs for the Medjed system

### A quick note on motivations

The optical design is not designed to reach the absolute lowest cost possible, but rather prioritises the long-term availability of the components and ease of part sourcing. As such, many parts will be sourced from Thorlabs , and supplemented with 3D printed parts where possible. When components are chosen, they will still generally be on the lower-end of parts, as the Medjed is not a high resolution optical system (compared to what one may typically make with Thorlabs parts.)

For more detailed justifications for part choices and focal length, consult the [wiki page](../../Medjed.wiki/optics.md)

### A note on organisation

There are 3 different big assemblies in the origin. This is a bit confusing, but this was the only way to get around the "1 assembly per file" constraint of the `Assembly4` workbench. 

1. `assembly-optical` is the base assembly, which contains the base UV unit of the Photon Ultra.
2. `assembly-optical-stock` is the optical assembly, as used in the photon ultra (i.e. base assembly + lens)
3. `assembly-optical-medjed` is the main optics for the Medjed system.  **🔎 This is the main file to explore.**

