package main
import "fmt"

func main() {
    x := 1.5
    square(&x)
    fmt.Println(x)
}

func square(rtt *float64) {
    *rtt = *rtt * *rtt
}