/**
 * This file is empty on purpose.   It is added, and configured if you
 * wanted to experiment with tests.
 */

package adpro

import org.scalacheck.{Gen, Arbitrary}
import org.scalacheck.Arbitrary.arbitrary
import org.scalacheck.Prop.{forAll, forAllNoShrink}
import adpro.Q8.checkIfLongerEqThan
import adpro.Q8.checkIfLongerEqThan

import org.scalacheck.{Arbitrary, Gen}
import org.scalacheck.Arbitrary.*
import org.scalactic.Equality

import org.scalacheck.Prop.{forAll, forAllNoShrink}


import fpinscala.answers.laziness.LazyList
import fpinscala.answers.state.*
import fpinscala.answers.monoids.Foldable
import fpinscala.answers.parallelism.Par
import fpinscala.answers.monads.Monad
import fpinscala.answers.laziness.LazyList.empty
import cats.data.Func
import fpinscala.answers.monads.Functor
import fpinscala.answers.testing.Prop.forkProp

object Exam2021AutumnSpec
  extends org.scalacheck.Properties("exam-2021"):

  // Q1

  property("A test that always passes (a sanity check)") = 
    forAll { (n: Int) => n == n }

  given Arbitrary[LazyList[Int]] =
      Arbitrary { Gen.nonEmptyListOf(Gen.choose(1, 100))
        .map { l => LazyList(l*) } }

  property("Q9: Write the test here by replacing 'false' below") =
      forAll {(list: LazyList[Int]) => 
        checkIfLongerEqThan(list.append(list))(2) 
      }
