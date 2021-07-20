package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type g struct {
	lon []float64
	lat []float64
	ele []float64
}

func main() {

	dem := os.Args[1] // DEM name

	// If grid file already exists, do not run as this is resource intensive
	if _, err := os.Stat("./input/" + dem + ".csv"); err == nil {
		return
	}

	// Load the ascii file into a large []string object row-wise
	rawData := loadData("./input/" + dem + ".asc")

	// Pass the raw data and get back a map object of the header (top 6 rows)
	header := getHeader(rawData)

	// Create a grid from the header info
	grid := createGrid(header)

	// Map elevations to the coordinates
	eleGrid := mapElevations(grid, rawData)

	// Write to file
	writeGrid(eleGrid, dem)
}

func writeGrid(eleGrid g, dem string) {

	f := "./input/" + dem + ".csv"

	file, err := os.OpenFile(f, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	handleError(err)
	defer file.Close()

	writer := bufio.NewWriter(file)
	for i := range eleGrid.ele {
		if eleGrid.ele[i] > -5000 { // Do not write missing values
			_, _ = writer.WriteString(fmt.Sprintf("%v,%v,%v\n", eleGrid.lon[i], eleGrid.lat[i], eleGrid.ele[i]))
		}
	}
	writer.Flush()
}

func mapElevations(grid g, raw []string) g {

	for i, line := range raw {
		if i > 5 {
			fields := strings.Fields(line) // Each line is split by wihtespace
			for _, field := range fields { // Iterate over each field
				ele, err := strconv.ParseFloat(field, 64) // Convert to float and append
				handleError(err)
				grid.ele = append(grid.ele, ele)
			}
		}
	}
	return grid
}

func createGrid(header map[string]float64) g {

	var coords g // Initiate a struct

	lon := header["xllcorner"]                  // First lon
	for i := 0; i < int(header["ncols"]); i++ { // Iterate over column length
		coords.lon = append(coords.lon, lon) // Append lon
		lon = lon + header["cellsize"]       // Calculate next lon
	}

	lat := header["yllcorner"]                  // First lat
	for i := 0; i < int(header["nrows"]); i++ { // Iterate over row length
		coords.lat = append(coords.lat, lat) // Append lat
		lat = lat + header["cellsize"]       // Calculate next lat
	}

	/*
		Reverse the latitudes as first latitude is lower left corner
		But we will read file from upper left corner
	*/
	for i, j := 0, len(coords.lat)-1; i < j; i, j = i+1, j-1 {
		coords.lat[i], coords.lat[j] = coords.lat[j], coords.lat[i]
	}

	// Create a new struct where lat lons are cross-multiplied creating a lon*lat grid
	var grid g
	for j := 0; j < len(coords.lat); j++ {
		for i := 0; i < len(coords.lon); i++ {
			grid.lon = append(grid.lon, coords.lon[i])
			grid.lat = append(grid.lat, coords.lat[j])
		}
	}
	return grid
}

func getHeader(raw []string) map[string]float64 {

	header := make(map[string]float64) // Use 'make' otherwise cannot append in for loop
	for i, line := range raw {
		if i <= 5 { // Top 6 rows
			var err error
			fields := strings.Fields(line) // Split by whitespace
			// Convert all numbers to floats now, later convert to int where required
			header[fields[0]], err = strconv.ParseFloat(fields[1], 64)
			handleError(err)
		}
	}
	return header
}

func loadData(f string) []string {

	/*
	   Input: Filename
	   Output: []string with each element = 1 row in file
	*/

	file, err := os.Open(f) // Open file
	handleError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	const maxCapacity = 80000
	buf := make([]byte, maxCapacity)
	scanner.Buffer(buf, maxCapacity)

	var raw []string
	for scanner.Scan() {
		raw = append(raw, scanner.Text()) // Each row is a single element in 'raw'
	}
	return raw
}

func handleError(err error) {
	if err != nil {
		fmt.Println("Error:", err)
		os.Exit(1)
	}
	return
}
