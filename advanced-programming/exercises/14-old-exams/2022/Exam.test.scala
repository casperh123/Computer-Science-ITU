/* This file is empty on purpose.   It is added, and configured if you
 * wanted to add your own tests during the exam.  It is not graded and
 * should not be submitted.
 */
package adpro

import org.scalacheck.{Gen, Arbitrary}
import org.scalacheck.Arbitrary.arbitrary
import org.scalacheck.Prop.{forAll, forAllNoShrink}
import adpro.PrimesAndLaziness.primesApart
import adpro.ApplesToApples.pickBetter
import adpro.ApplesToApples.bigApple
import adpro.ApplesToApples.smallApple
import adpro.SizedLists.third
import adpro.SizedLists.l2

object Exam2022AutumnSpec
  extends org.scalacheck.Properties("exam-2022"):

  // Q1

  property("A test that always passes (a sanity check)") = 
    forAll { (n: Int) => n == n }

  property("Elements in pairs returned by primesApart differ by n") = 
      val intGen = Gen.choose(0, 20).suchThat(value => value % 2 == 0)

      forAll(intGen) { (n: Int) => 
        primesApart(n).take(5).forAll(value => value._2 - value._1 == n)
      }

  property("betterrApple works") = 
    pickBetter(bigApple, smallApple) == bigApple

  property("better apple infix") = 
    bigApple betterThan smallApple

  property("Test third") = 
    third(l2) == 4
