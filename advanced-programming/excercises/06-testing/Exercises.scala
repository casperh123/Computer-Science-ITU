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

  // Exercise 1

  property("Ex01.01: headOption returns None on an empty LazyList") =
    empty.headOption == None

  property("Ex01.02: headOption returns the head of the stream packaged in Some") =

    given Arbitrary[LazyList[Int]] = Arbitrary(genNonEmptyLazyList[Int])

    forAll { (n: Int) => cons(n,empty).headOption == Some(n) } :| "singleton" &&
      forAll { (s: LazyList[Int]) => s.headOption != None }      :| "random"

  // Exercise 2

  property("Ex02.01: headOptions does not force the tail of a list") =

    val list = cons(1, throw new RuntimeException("Tail was forced"))

    list.headOption == Some(1)

  // Exercise 3

  property("Ex03.01: take does not force any heads nor any tails of the lazy list it manipulates") =

    val list = cons(
      throw new RuntimeException("Head was forced"),
      throw new RuntimeException("Tail was forced")
    )

    val takenList = list.take(1)

    true

  // Exercise 4
  property("Ex04.01: take(n) does not force the (n+1)st head ever") =
    val list = cons(
      1, cons(
        2,
        cons(
          throw new RuntimeException("n+1 head was forced"),
          empty
        )
      )
    )

    val evaluatedSize = list.take(2).foldRight(0)((elem, acc) => acc + 1)

    evaluatedSize == 2

// Exercise 5

  property("Ex05.01: l.take(n).take(n) == l.take(n) for any lazy list s and any n") =

    given Arbitrary[LazyList[Int]] = Arbitrary(infiniteLazyList[Int])
    given Arbitrary[Int] = Arbitrary(Gen.chooseNum(0, 10000))


    forAll { (list: LazyList[Int], n: Int) =>
      list.take(n).take(n).toList == list.take(n).toList
    }


// Exercise 6

  property("Ex06.01: l.drop(n).drop(m) == l.drop(n+m) for any n, m") =

    given Arbitrary[LazyList[Int]] = Arbitrary(genNonEmptyLazyList[Int])
    given Arbitrary[Int] = Arbitrary(Gen.chooseNum(0, 10))

    forAll { (list: LazyList[Int], n: Int, m: Int) =>
      list.drop(n).drop(m).toList == list.drop(n + m).toList
    }

// Exercise 7

  property("Ex07.01: l.drop(n) does not force any of the dropped elements (heads)") =
    val list = cons(
    throw new RuntimeException("Head was forced"), cons(
      throw new RuntimeException("Head was forced"),
        cons(
          1,
          empty
        )
      )
    )

    val listWithDroppedElements = list.drop(2)
    listWithDroppedElements.toList.size == 1

// Exercise 8

  property("Ex08.01: l.map(identity) == l for any lazy list l") =
    given Arbitrary[LazyList[Int]] = Arbitrary(genNonEmptyLazyList[Int])

    forAll { (list: LazyList[Int]) => list.map(identity).toList == list.toList}

// Exercise 9

  property("Ex09.02: map terminates on infinite lazy lists") =
    given Arbitrary[LazyList[Int]] = Arbitrary(infiniteLazyList[Int])

    forAll { (list: LazyList[Int]) =>
      list.map(identity)
      true
    }

// Exercise 10

