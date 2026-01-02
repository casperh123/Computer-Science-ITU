error id: file://<WORKSPACE>/Exercises.scala:
file://<WORKSPACE>/Exercises.scala
empty definition using pc, found symbol in pc: 
empty definition using semanticdb
empty definition using fallback
non-local guesses:
	 -l.
	 -l#
	 -l().
	 -scala/Predef.l.
	 -scala/Predef.l#
	 -scala/Predef.l().
offset: 1411
uri: file://<WORKSPACE>/Exercises.scala
text:
```scala
// Advanced Programming, A. Wąsowski, IT University of Copenhagen
// Based on Functional Programming in Scala, 2nd Edition

package adpro.option

// Exercise 1

trait OrderedPoint
  extends scala.math.Ordered[java.awt.Point]:

  this: java.awt.Point =>

  override def compare(that: java.awt.Point): Int =
    ???

// Try the following (and similar) tests in the repl (sbt console):
//
// import adpro.option.*
// val p = new java.awt.Point(0, 1) with OrderedPoint
// val q = new java.awt.Point(0, 2) with OrderedPoint
// assert(p < q)



// Chapter 3 Exercises

enum Tree[+A]:
  case Leaf(value: A)
  case Branch(left: Tree[A], right: Tree[A])

object Tree:

  // Exercise 2

  def size[A](t: Tree[A]): Int = t match
    case Leaf(x) => 1
    case Branch(l, r) => 1 + size(l) + size(r)

  // Exercise 3

  def maximum(t: Tree[Int]): Int = t match
    case Leaf(x) => x
    case Branch(l, r) => maximum(l) max maximum(r)
  

  // Exercise 4

  def map[A, B](t: Tree[A])(f: A => B): Tree[B] = t match
    case Leaf(x) => Leaf(f(x))
    case Branch(l, r) => Branch(map(l)(f), map(r)(f))
  

  // Exercise 5

  def fold[A,B](t: Tree[A])(f: (B, B) => B)(g: A => B): B = t match
    case Leaf(x) => g(x)
    case Branch(l, r) => f(fold(l)(f)(g), fold(r)(f)(g))
  

  def size1[A](t: Tree[A]): Int =
    fold[A, Int](t)((l, r) => l + r + 1)(_ => 1)

  def maximum1(t: Tree[Int]): Int = 
    fold[A, Int](t)((l, r) => @@l max r)(x => x)

  def map1[A, B](t: Tree[A])(f: A => B): Tree[B] = ???




enum Option[+A]:
  case Some(get: A)
  case None

  // Exercise 6

  def map[B](f: A => B): Option[B] = ???

  def getOrElse[B >: A] (default: => B): B = ???

  def flatMap[B](f: A => Option[B]): Option[B] =  ???

  def filter(p: A => Boolean): Option[A] = ???

  // Scroll down for Exercise 7, in the bottom of the file, outside Option

  def forAll(p: A => Boolean): Boolean = this match
    case None => true
    case Some(a) => p(a)

end Option

// Exercise 9

def map2[A, B, C](ao: Option[A], bo: Option[B])(f: (A,B) => C): Option[C] =
  ???

// Exercise 10

def sequence[A](aos: List[Option[A]]): Option[List[A]] =
  ???

// Exercise 11

def traverse[A, B](as: List[A])(f: A => Option[B]): Option[List[B]] =
  ???




// Exercise that are outside the Option companion object

import Option.{Some, None}

def headOption[A](lst: List[A]): Option[A] = lst match
  case Nil => None
  case h:: t => Some(h)

// Exercise 7

def headGrade(lst: List[(String,Int)]): Option[Int] =
  ???

def headGrade1(lst: List[(String,Int)]): Option[Int] =
  ???

// Implemented in the text book

def mean(xs: Seq[Double]): Option[Double] =
  if xs.isEmpty then None
  else Some(xs.sum / xs.length)

// Exercise 8

def variance(xs: Seq[Double]): Option[Double] =
  ???

// Scroll up, to the Option object for Exercise 9

```


#### Short summary: 

empty definition using pc, found symbol in pc: 