# Satellite-Ground Contact Simulation

## Sections

### Spacecraft

#### Coordinate System

[CoordinateSystem Doc](http://gmat.sourceforge.net/docs/R2014a/html/CommandSummary.html#N1091D)

EarthMJ2000Eq


#### TLE-set

Keplerian Elements were generated using TLE-Analyzer with ISS orbit

|Abbr   |Parameter                              | Value |
|---    |---                                    | --- |
|SMA    |Semi-Major Axis                        |one-half the length (measured the long way) of the orbit ellipse|6797.329000000002|
|ECC    |Eccentricity|      |0.001533200000000366|
|INC    |Inclination                            |Angle between the orbital plane and the equatorial plane|51.6563|
|RAAN   |Right Ascension of the Ascending Node  |angle measured at the center of the earth, from the vernal equinox to the ascending node|117.7494|
|AOP    |Argument of Perigee                    |Angle between line-of-nodes and line-of-apsides|78.86800000000496|
|TA     |                                       ||320.2378999999949|

[Nomenclature](http://www.amsat.org/amsat/keps/kepmodel.html) 


### Ground Station

- the ground station is modelled at the coordinates of the Loyola campus

### Hardware Components

- a Satellite Antenna, Transmitter, Receiver, and Transponder are created
- a Ground Station Antenna, Transmitter, Receiver are created
- hardware settings still need to be correctly configured

### Physics

#### ForceModels and Propagators

- A Low-Earth Orbit ForceModel and Propagator is configured, with no drag and no relativistic effects

#### Burns

[ImpulsiveBurn Doc](http://gmat.sourceforge.net/docs/R2014a/html/ImpulsiveBurn.html)

- the Cubesat does not have any propulsion systems, so all burn impulse settings are set to zero, leaving only the gravitational force 

### Graphs

#### Default Orbit View


#### Default Ground Track Plot


#### Satellite Altitude Relative To Ground

This graph displays the altitude of the satellite relative to the ground station, using the ground station referenced against the center of the earth



### Report Files

[ReportFile Doc](http://gmat.sourceforge.net/docs/R2014a/html/ReportFile.html)

If a path is not specified, ReportFiles are placed in the GMAT output folder, usually C/Users/**username**/AppData/Local/GMAT/R2014a/output

#### ContactTimes

This report file generates the contact windows between the satellite and the ground station. Contact windows are opened when the altitude of the satellite is above the altitude of the ground station, relative to the ground station reference to the center of the earth. 

#### Satellite Ground Relative State

This report file generates data of the satellites position relative to the ground station. It will eventually be populated by the elevation and azimuth angle, which will be used to direct the antenna.

#### Ephermeris

[EphemerisFile Doc](http://gmat.sourceforge.net/docs/R2014a/html/EphemerisFile.html)

- Filename : this field allows the user to provide the file name and path.
- EphemerisData: this field allows the user to specify what data should be written to the file. For example, if we wanted to write Sat1 orbit ephemeris we might have MyEphemFile.EphemerisData = {Sat1,'OrbitEphemeris'}; Similar for attitude. Default would be orbit if no keyword is provided.
- TimeInterval: Could be "IntegratorTimeSteps" or a numeric value.
- FileFormat: Could be "CCSDS", "SPICE", or "STKefile"
- CoordinateSystem: Any coordinate system created and available in resources.
- EpochFormat: UTCGregorian, TAIGregorian, and so on.
- InterpolationMethod: Lagrange, Hermite/Simpson,....
- InterpolationOrder: A numeric value for interpolation order
- Precision : Precistion to be written to the file

[reference](http://forums.gmatcentral.org/viewtopic.php?f=3&t=103&p=222&hilit=ReportFile+path&sid=e7b1b3b535eeb34d3cb4079989f262ce#p222)
