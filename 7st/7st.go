package main
import (
    "fmt"
    "time"
    "math/rand"
)

/* 
Принимает время "на которое" нужно залипнуть и возвращает время на которое залипал.
*/
func randSleep(randNum int) int{    
    var sleeper time.Duration       
    sleeper = time.Duration(rand.Intn(randNum))
    time.Sleep(time.Millisecond * sleeper)
    return int(sleeper)
}

/*
Принимает 2 канала по первому передает данные типа "string" а по второму 
время на которое залипал.
*/
func pingerMan(pMan chan string, timeOut chan int) {
    var prevSt int
    for {
        pMan <- "ping"
        timeOut <- prevSt 
        prevSt = randSleep(1000)
    }
}

/*
Принимает 2 канала все что получает из них сразу печатает.
*/
func myPrinter(mPrint chan string, timeIn chan int) {
    for {
        fmt.Println(<- mPrint, <- timeIn)
    }
}
/*
*/
func main() {
    var chM = make(chan string)
    chS := make(chan int)
    
    go pingerMan(chM, chS)
    go myPrinter(chM, chS)

/*
Тут ждем нажатия клавиши. Если этого не сделать или не поставить таймаут, 
достаточный для завершения всех горутин, запущенных из этой функции(тоже горутины), 
то она завершившись убъёт все дочерние горутины(вернее их убъет ОС).
*/
    var input string
    fmt.Scanln(&input) 
}

// Что-то мне C уже не кажется таким уж сложным...
