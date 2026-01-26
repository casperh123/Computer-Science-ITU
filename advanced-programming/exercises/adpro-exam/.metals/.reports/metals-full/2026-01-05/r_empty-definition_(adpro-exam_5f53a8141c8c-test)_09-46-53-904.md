error id: file://<WORKSPACE>/Exam.test.scala:`<none>`.
file://<WORKSPACE>/Exam.test.scala
empty definition using pc, found symbol in pc: `<none>`.
empty definition using semanticdb
empty definition using fallback
non-local guesses:
	 -org/scalactic/TripleEquals.rmse.
	 -org/scalactic/TripleEquals.rmse#
	 -org/scalactic/TripleEquals.rmse().
	 -rmse.
	 -rmse#
	 -rmse().
	 -scala/Predef.rmse.
	 -scala/Predef.rmse#
	 -scala/Predef.rmse().
offset: 740
uri: file://<WORKSPACE>/Exam.test.scala
text:
```scala
/* This file is empty on purpose. It is added and configured if you
 * wanted to add your own tests during the exam. It is not graded and
 * should not be submitted.
 */
package adpro

import org.scalacheck.{Gen, Arbitrary}
import org.scalacheck.Arbitrary.arbitrary
import org.scalacheck.Prop.{forAll, forAllNoShrink}
import org.scalacheck.Prop
import org.scalactic.TripleEquals.*


object ExamSpec
  extends org.scalacheck.Properties("exam-2025"):

  def rmseProperty: Prop =

    given Arbitrary[(LazyList[Double], LazyList[Double])] =
      Arbitrary { 
        Gen.nonEmptyListOf(Gen.choose(1.0, 100.0))
          .map { l => (LazyList(l*), LazyList(l*)) } 
      }

    forAll {(lists: (LazyList[Double], LazyList[Double])) =>
      rm@@se(lists._1, lists._2) > 0
    }

end ExamSpec

// vim:cc=66

```


#### Short summary: 

empty definition using pc, found symbol in pc: `<none>`.