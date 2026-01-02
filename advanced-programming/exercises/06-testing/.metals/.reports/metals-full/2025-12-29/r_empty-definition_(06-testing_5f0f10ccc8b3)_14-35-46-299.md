error id: file://<WORKSPACE>/Exercises.scala:
file://<WORKSPACE>/Exercises.scala
empty definition using pc, found symbol in pc: 
empty definition using semanticdb
empty definition using fallback
non-local guesses:
	 -org/scalacheck/exceptionList.
	 -org/scalacheck/exceptionList#
	 -org/scalacheck/exceptionList().
	 -org/scalacheck/Prop.exceptionList.
	 -org/scalacheck/Prop.exceptionList#
	 -org/scalacheck/Prop.exceptionList().
	 -lazyList00/exceptionList.
	 -lazyList00/exceptionList#
	 -lazyList00/exceptionList().
	 -LazyList.exceptionList.
	 -LazyList.exceptionList#
	 -LazyList.exceptionList().
	 -exceptionList.
	 -exceptionList#
	 -exceptionList().
	 -scala/Predef.exceptionList.
	 -scala/Predef.exceptionList#
	 -scala/Predef.exceptionList().
offset: 2078
uri: file://<WORKSPACE>/Exercises.scala
text:
```scala
// Advanced Programming, A. Wąsowski, IT University of Copenhagen
// Based on Functional Programming in Scala, 2nd Edition

package adpro.lazyList

import org.scalacheck.*
import org.scalacheck.Prop.*
import org.scalacheck.Arbitrary.arbitrary

import lazyList00.* // uncomment to test the book laziness solution implementation
// import lazyList01.* // uncomment to test the broken headOption implementation
// import lazyList02.* // uncomment to test another version

/* Generators and helper functions */

import LazyList.*

/** Convert a strict list to a lazy-list */
def list2lazyList[A](la: List[A]): LazyList[A] = 
  LazyList(la*)

/** Generate finite non-empty lazy lists */
def genNonEmptyLazyList[A](using Arbitrary[A]): Gen[LazyList[A]] =
  for la <- arbitrary[List[A]].suchThat { _.nonEmpty }
  yield list2lazyList(la)
  
/** Generate an infinite lazy list of A values.
  *
  * This lazy list is infinite if the implicit generator for A never fails. The
  * code is ugly-imperative, but it avoids stack overflow (as Gen.flatMap is
  * not tail recursive)
  */
def infiniteLazyList[A: Arbitrary]: Gen[LazyList[A]] =
  def loop: LazyList[A] =
    summon[Arbitrary[A]].arbitrary.sample match
      case Some(a) => cons(a, loop)
      case None => empty
  Gen.const(loop)

/* The test suite */

object LazyListSpec 
  extends org.scalacheck.Properties("testing"):


  def exceptionList(size: Int): Gen[List[RuntimeException]] =
    Gen.listOfN(size, Gen.const(new RuntimeException("tail was forced")))

  // Exercise 1

  property("Ex01.01: headOption returns None on an empty LazyList") = 
    empty.headOption == None

  property("Ex01.02: headOption returns the head of the stream packaged in Some") =

    given Arbitrary[LazyList[Int]] = Arbitrary(genNonEmptyLazyList[Int])

    forAll { (n: Int) => cons(n,empty).headOption == Some(n) } :| "singleton" &&
    forAll { (s: LazyList[Int]) => s.headOption != None }      :| "random" 

  // Exercise 2

  property("Ex02.01: headOption does not force tail") =
    using Arbitrary[List[RuntimeException]] = Arbitrary(exce@@ptionList())
    
    forAll { (tail: List[RuntimeException])

    }
    
    val list = 1::exceptionList(1).

    list.headOption == Some(1)

  // Exercise 3
  property("Ex03.01: take does not force any heads nor any tails") =
    val list = cons(throw new RuntimeException("Head was forced"), throw new RuntimeException("tail was forced"))

    list.take(1)

    true

  // Exercise 4
  
  // Exercise 5
  
  // Exercise 6
  
  // Exercise 7

  // Exercise 8

  // Exercise 9
 
  // Exercise 10


```


#### Short summary: 

empty definition using pc, found symbol in pc: 