package com.lielamar.a;

import com.lielamar.b.Inner;
import com.lielamar.b.Inner2; 

public class HelloWorld {

    public static void main(String[] args) {

        System.out.println("Hello, World");     

        Inner myInner = new Inner(); 
        myInner.myInner(); 

        Inner2 myInner2 = new Inner2();
        myInner2.myInner(); 

    }

}