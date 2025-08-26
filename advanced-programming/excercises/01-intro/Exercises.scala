// Advanced Programming, A. Wąsowski, IT University of Copenhagen
// Based on Functional Programming in Scala, 2nd Edition

package adpro.intro

object MyModule:

  def abs(n: Int): Int =
    if n < 0 then -n else n

  // Exercise 1

  def square(n: Int): Int =
    n * n

  private def formatAbs(x: Int): String =
    s"The absolute value of ${x} is ${abs(x)}"

  val magic: Int = 42
  var result: Option[Int] = None

  @main def printAbs: Unit =
    assert(magic - 84 == magic.-(84))
    println(formatAbs(magic - 100))

end MyModule

// Exercise 2 requires no programming

// Exercise 3
def fib(n: Int): Int =
  @annotation.tailrec
  def inner_fib(i: Int, acc: Int, current: Int): Int =
    if i <= 1 then acc
    else inner_fib(i - 1, current, current + acc)
  inner_fib(n, 0, 1)

// Exercise 4

def isSorted[A](as: Array[A], ordered: (A, A) => Boolean): Boolean =
  @annotation.tailrec
  def recIsSorted[A](index: Int): Boolean =
    if index >= (as.length - 1) then true
    else if (ordered(as(index), as(index + 1))) recIsSorted(index + 1)
    else false
  recIsSorted(0)


// Exercise 5

def curry[A, B, C](f: (A, B) => C): A => (B => C) =
  ???

def isSortedCurried[A]: Array[A] => ((A, A) => Boolean) => Boolean =
  ???

// Exercise 6

def uncurry[A, B, C](f: A => B => C): (A, B) => C =
  ???

def isSortedCurriedUncurried[A]: (Array[A], (A, A) => Boolean) => Boolean =
  ???

// Exercise 7

def compose[A, B, C](f: B => C, g: A => B): A => C =
  ???
