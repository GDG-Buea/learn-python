# This program computes the estimated area enclosed by four cities namely: Atlanta, Georgia;
# Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina

import math

latitudeAtlanta = -84.387917
longitudeAtlanta = 33.757222

latitudeOrlando = -81.5197376
longitudeOrlando = 28.3703828

latitudeSavannah = -81.0983
longitudeSavannah = 32.0749

latitudeCharlotte = -80.8449
longitudeCharlotte = 35.05899

averageRadiusOfEarth = 6371.01

A = math.sin(latitudeAtlanta) * math.sin(latitudeOrlando)
B = math.cos(latitudeAtlanta) * math.cos(latitudeOrlando)
C = math.cos(longitudeAtlanta - longitudeOrlando)
distanceAtlanta_Orlando = averageRadiusOfEarth * math.acos(A + B * C)

A1 = math.sin(latitudeOrlando) * math.sin(latitudeSavannah)
B1 = math.cos(latitudeOrlando) * math.cos(latitudeSavannah)
C1 = math.cos(longitudeOrlando - longitudeSavannah)
distanceOrlando_Savannah = averageRadiusOfEarth * math.acos(A1 + B1 * C1)

A2 = math.sin(latitudeSavannah) * math.sin(latitudeCharlotte)
B2 = math.cos(latitudeSavannah) * math.cos(latitudeCharlotte)
C2 = math.cos(longitudeSavannah - longitudeCharlotte)
distanceSavannah_Charlotte = averageRadiusOfEarth * math.acos(A2 + B2 * C2)

A3 = math.sin(latitudeCharlotte) * math.sin(latitudeAtlanta)
B3 = math.cos(latitudeCharlotte) * math.cos(latitudeAtlanta)
C3 = math.cos(longitudeCharlotte - longitudeAtlanta)
distanceCharlotte_Atlanta = averageRadiusOfEarth * math.acos(A3 + B3 * C3)

A4 = math.sin(latitudeCharlotte) * math.sin(latitudeOrlando)
B4 = math.cos(latitudeCharlotte) * math.cos(latitudeOrlando)
C4 = math.cos(longitudeCharlotte - longitudeOrlando)
distanceCharlotte_Orlando = averageRadiusOfEarth * math.acos(A4 + B4 * C4)

sumOfSidesTriangleOne = (distanceCharlotte_Atlanta + distanceAtlanta_Orlando + distanceCharlotte_Orlando) / 2
sumOfSidesTriangleTwo = (distanceOrlando_Savannah + distanceSavannah_Charlotte + distanceCharlotte_Orlando) / 2

areaTriangleOne = math.sqrt(sumOfSidesTriangleOne * (sumOfSidesTriangleOne - distanceCharlotte_Atlanta) *
                            (sumOfSidesTriangleOne - distanceAtlanta_Orlando) *
                            (sumOfSidesTriangleOne - distanceCharlotte_Orlando))

areaTriangleTwo = math.sqrt(sumOfSidesTriangleTwo * (sumOfSidesTriangleTwo - distanceOrlando_Savannah) *
                            (sumOfSidesTriangleTwo - distanceSavannah_Charlotte) *
                            (sumOfSidesTriangleTwo - distanceCharlotte_Orlando))

areaCoveredByCities = areaTriangleOne + areaTriangleTwo


print("The area covered by Atlanta, Georgia; Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina is: ",
      areaCoveredByCities, "m2")

