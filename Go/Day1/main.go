package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func ReadFile(fileName string) (nums []int, err error) {
	// Read test file
	data, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}
	// Split input file and convert from byte to string array
	splitArr := strings.Split(string(data[:]), "\n")
	nums = make([]int, 0)
	// Loop through each line
	for _, line := range splitArr {
		// Empty line occurs at the end of the file when we use Split.
		if len(line) == 0 {
			continue
		}
		// 1. Split each line into array
		// 2. Loop through changing string to ints
		currLine := strings.Split(line, " ")
		for _, y := range currLine {
			if y != "" {
				n, err := strconv.Atoi(y)
				if err != nil {
					panic(err)
				}
				nums = append(nums, n)
			}
		}
	}
	// Print information to screen
	fmt.Printf("Test file array size: %d \n", len(nums))
	fmt.Println(nums)
	return nums, nil
}

func main() {
	numsArr, err := ReadFile("test.txt")
	if err != nil {
		panic(err)
	}
	for _, i := range numsArr {
		fmt.Print(i)
		fmt.Print("\n")
	}
}
