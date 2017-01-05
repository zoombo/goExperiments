package main
import "fmt"

func swap(x *int, y *int) {
    // var tmp int = *x // тоже работает но с warning
    var tmp int
    tmp = *x 
    *x = *y
    *y = tmp
}
func main() {
    /*
    var x int // так тоже верно 
    var y int // так тоже верно :)
    */
    x := int(0)
    y := int(0)
    y = 5
    swap(&x, &y)
    fmt.Println("x = ", x)
    fmt.Println("y = ", y)
}