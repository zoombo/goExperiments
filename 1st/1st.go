package main

import "fmt"

func makeEvenGenerator(i uint) func() uint {
	//i := uint(0)
	return func() uint {
		ret := i
		i += 2
		return ret
	}
}
func main() {
	nextEven := makeEvenGenerator(1)
	fmt.Println(nextEven()) // 0
	fmt.Println(nextEven()) // 2
	fmt.Println(nextEven()) // 4
}
