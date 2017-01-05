package main

import (
    "fmt"
    "time"
    "math/rand"
)

func mFoo(nameGr int) {
    for i := 0; i < 10; i++ {
        fmt.Println(nameGr, ":", i)
        amt := time.Duration(rand.Intn(1000))
        time.Sleep(time.Millisecond * amt)
    }
}

func main() {
  //  var rtt [10]int
    for i := range [10]int{0} {
       go mFoo(i)
    }
    var input string 
    fmt.Scanln(&input)
   
}