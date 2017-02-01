

function dist(point1, point2){
	//calculates the distance on a hex grid (the hex tiles can be thought of as 3d cubes, thus the z-axis)
	//since distances are discrete, an L1-norm is used (maximum difference in coords along)
	z1 = -(point1[0]+point1[1])
	z2 = -(point2[0]+point2[1])
	return Math.max(Math.abs(point1[0]-point2[0]),Math.abs(point1[1]-point2[1]),Math.abs(z1-z2))
}



function possibilities(location, distance, feasibleSet){

	distances = [100,25,10,5,0,0]

	distmax = distance
	distmin = distances[distances.indexOf(distance)+1]
	temp = []
	if (feasibleSet.length == 0){
		for(var x=0; x<1000; x++){
			for(var y=0; y<1000; y++){
				d = dist(location,[x,y])
				if((d <= distmax) && (d > distmin)){
					feasibleSet.push([x,y])
				}
			}
		}
	}

	for (var i=0; i < feasibleSet.length; i++){
		var x = feasibleSet[i]
		if((dist(x, location) <= distmax) && (dist(x, location) > distmin)){
			temp.push(x)
		}
	}
	return temp

}