package main
import "fmt"

////////////////////////__new_Type__////////////////////////
type unit struct {
    name string
}
////////////////////////__methods_of_new_Type__////////////////////////
func (mSss *unit) prtName() {
    fmt.Println("Name is", mSss.name)
}
////////////////////////__End_methods_of_new_Type__////////////////////////

/////////////////////////////////////////////////////////////
////////////////////////__Main_Func__////////////////////////
/////////////////////////////////////////////////////////////
func main() {

    type myTestType struct {
        myUnit1 unit
        i int
    }

    var newTT = new(myTestType)
    newTT.myUnit1.name = "Dmitry"
    newTT.myUnit1.prtName()

    type myTestType2 struct {
        unit
    }
    var newTT2 myTestType2
    newTT2.unit.name = "Nikoly"
    newTT2.unit.prtName()

    type myTestType3 struct {
        myUnit2 unit
        zZz int
    }
    newTT3 := myTestType3{zZz: 10}
    newTT3.myUnit2.name = "Sergio"
    newTT3.myUnit2.prtName()

}

