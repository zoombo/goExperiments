package main
import "fmt"

func main()  {
    // var mainPtr = int(0)
    // *mainPtr = 0
    mainPtr := new(int)

    testF1(mainPtr)
    fmt.Println(*mainPtr)
}

func testF1(mptr *int) {
    *mptr = 100
}