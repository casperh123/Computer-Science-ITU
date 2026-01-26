/* This file is empty on purpose.   It is added, and configured if you
 * wanted to add your own tests during the exam.  It is not graded and
 * should not be submitted.
 */
package adpro

import org.scalacheck.{Gen, Arbitrary}
import org.scalacheck.Arbitrary.arbitrary
import org.scalacheck.Prop.{forAll, forAllNoShrink}
import adpro.Streaming.fViaRec
import adpro.solution.Streaming.fViaFold
import adpro.Parsing.longestLine
import adpro.parsing.Sliceable.run
import adpro.Parsing.allLinesTheSame
import adpro.RL.Q
import adpro.RL.qGen
import adpro.RL.qZero
import adpro.RL.update

object ExamSpec
  extends org.scalacheck.Properties("exam-2023-autumn"):
  import adpro.laziness.LazyList

  given arb[A: Arbitrary]: Arbitrary[LazyList[A]] =
    val l = summon[Arbitrary[List[A]]].arbitrary
    val la = l.map { value => LazyList(value*)}
    Arbitrary(la)

  property("fViaRec compiles") = 
    forAll { (list: LazyList[Int]) =>
      fViaRec(list)
      true
    }

  property("fViaFold compiles") = 
    forAll { (list: LazyList[Int]) =>
      fViaRec(list)
      true
    }

  property("fViaRec equals fViaFold") = 
    forAll { (list: LazyList[Int]) =>
      fViaRec(list) == fViaFold(list)
    }

  property("Longest Line found 5") =
    val line = "1,2,3 , 5,4 \n42,42"
    longestLine.run(line).getOrElse(0) == 5 

  property("Longest Line found 10") =
    val line = "1,2,3 , 5,4 \n42,42,1,1,1,1,1,1,1,1"
    longestLine.run(line).getOrElse(0) == 10

  property("Equal Length lines") = 
    val line = "1,2 \n 5,4 \n4,4"
    allLinesTheSame.run(line).getOrElse(false) == true

  property("Not equal Length lines") = 
    val line = "1,2 , 5,4 \n4,4,5"
    allLinesTheSame.run(line).getOrElse(true) == false 

  property("00 Null update on null table 2x3") = 
    val table = qZero(2, 3)
    val updatedTable = update(table, 0, 0)(0.0, 0.0)

    table == updatedTable

  property("01 Null update on null table 2x3") = 
      val genState = Gen.choose(0, 1)
      val genAction = Gen.choose(0,2)

      forAll(genState, genAction, qGen(2,3)) {(state: Int, action: Int, table: Q[Int, Int]) =>
        val reward = table(state)(action)
        val updatedTable = update(table, state, action)(reward, 0.0)

        table == updatedTable
      }

end ExamSpec

object NullUpdatesSpecObj
  extends RL.NullUpdatesSpec(update = RL.update, "studentrl") {}
