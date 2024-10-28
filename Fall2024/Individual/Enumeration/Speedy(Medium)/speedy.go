package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "crypto/md5"
)

func checkPassword(input string) bool {
    hash := [16]byte{
       0x8f,
       0xcc,
       0xe5,
       0x0f,
       0x39,
       0x2a,
       0x6f,
       0xab,
       0x43,
       0xf3,
       0x0d,
       0x3a,
       0xf6,
       0x09,
       0xd4,
       0xe3,
    }

    key := []byte{47, 69, 82, 74, 80, 47, 54, 58, 48, 58}

    byts := []byte(input)

    inpHash := md5.Sum(byts[0:3])

    if (inpHash != hash) {
        return false
    }

    keyByte := hash[0] & 0x12;

    for index, byt := range byts[3:13] {
        if byt ^ keyByte != key[index] {
            return false
        }
    }
    return true
}

func main() {
        fmt.Println("Enter Your Password:")
        reader := bufio.NewReader(os.Stdin)
        input, err := reader.ReadString('\n')
        if err != nil {
                log.Fatal(err)
        }

    if checkPassword(input) {
        fmt.Println("Correct Password")
        } else {
        fmt.Println("Wrong Password")
                os.Exit(1)
        }
}

