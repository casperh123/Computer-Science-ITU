error id: file://<WORKSPACE>/Exam.scala:`<none>`.
file://<WORKSPACE>/Exam.scala
empty definition using pc, found symbol in pc: `<none>`.
empty definition using semanticdb
empty definition using fallback
non-local guesses:
	 -org/scalacheck/GenExt.gs.unfold.
	 -org/scalacheck/GenExt.gs.unfold#
	 -org/scalacheck/GenExt.gs.unfold().
	 -Arbitrary.gs.unfold.
	 -Arbitrary.gs.unfold#
	 -Arbitrary.gs.unfold().
	 -Prop.gs.unfold.
	 -Prop.gs.unfold#
	 -Prop.gs.unfold().
	 -org/scalactic/TripleEquals.gs.unfold.
	 -org/scalactic/TripleEquals.gs.unfold#
	 -org/scalactic/TripleEquals.gs.unfold().
	 -adpro/option/gs/unfold.
	 -adpro/option/gs/unfold#
	 -adpro/option/gs/unfold().
	 -adpro/lazyList/gs/unfold.
	 -adpro/lazyList/gs/unfold#
	 -adpro/lazyList/gs/unfold().
	 -adpro/state/gs/unfold.
	 -adpro/state/gs/unfold#
	 -adpro/state/gs/unfold().
	 -adpro/monad/gs/unfold.
	 -adpro/monad/gs/unfold#
	 -adpro/monad/gs/unfold().
	 -adpro/parsing/gs/unfold.
	 -adpro/parsing/gs/unfold#
	 -adpro/parsing/gs/unfold().
	 -adpro/parsing/Sliceable.gs.unfold.
	 -adpro/parsing/Sliceable.gs.unfold#
	 -adpro/parsing/Sliceable.gs.unfold().
	 -monocle/gs/unfold.
	 -monocle/gs/unfold#
	 -monocle/gs/unfold().
	 -monocle/syntax/all/gs/unfold.
	 -monocle/syntax/all/gs/unfold#
	 -monocle/syntax/all/gs/unfold().
	 -monocle/function/all/gs/unfold.
	 -monocle/function/all/gs/unfold#
	 -monocle/function/all/gs/unfold().
	 -gs/unfold.
	 -gs/unfold#
	 -gs/unfold().
	 -scala/Predef.gs.unfold.
	 -scala/Predef.gs.unfold#
	 -scala/Predef.gs.unfold().
offset: 1394
uri: file://<WORKSPACE>/Exam.scala
text:
```scala
/* Exam: Advanced Programming, by Andrzej Wasowski
 * IT University of Copenhagen, Autumn 2025: 05 January 2026
 **/
package adpro

import org.scalacheck.{Arbitrary, Gen, Prop}
import org.scalacheck.GenExt.*
import Arbitrary.*, Prop.*
import org.scalactic.TripleEquals.*

import adpro.option.*
import adpro.lazyList.*
import adpro.state.*
import adpro.monad.*
import adpro.parsing.*
import adpro.parsing.Sliceable.*

import monocle.*
import monocle.syntax.all.*
import monocle.function.all.*
import monocle.PLens.lensChoice

object RMSE:

  /* Question 1 */

  def rmse (gs: LazyList[Double],
            ps: LazyList[Double]): Double = 
              val (sum, size) = 
                gs.zip(ps)
                  .foldLeft(0.0, 0) {(acc, elems) => 
                    (acc._1 + (elems._1 - elems._2), acc._2 + 1)
                  }
              

              (1 / size) * math.pow((sum), 2)

  /* Question 2 */

  def rmseProperty: Prop =

    given Arbitrary[(LazyList[Double], LazyList[Double])] =
      Arbitrary { 
        Gen.nonEmptyListOf(Gen.choose(1.0, 100.0))
          .map { l => (LazyList(l*), LazyList(l*)) } 
      }

    forAll {(lists: (LazyList[Double], LazyList[Double])) =>
      rmse(lists._1, lists._2) >= 0
    }

  /* Question 3 */

  def runningRMSE (gs: LazyList[Double],
                   ps: LazyList[Double]): LazyList[Double] = 
                    gs.unf@@old()

  /* Question 4 */

  def runningRMSEProperty: Prop = ???

  /* Question 5 */

  def gen5 = ???

end RMSE

object Lenses:

  /* Question 6 */
  def lens[A]: Lens[Arbitrary[A], Gen[A]] = ???

  /* Which lense laws does this lens satisfy?
   * 1. Put-Get [ ] Yes / [ ] No
   *    ...
   *
   * 2. Get-Put [ ] Yes / [ ] No
   *    ...
   *
   * 3. Put-Put: [ ] Yes / [ ] No
   *    ...
   */

end Lenses

object Monads:

  /* Question 7 */

  enum Tree[+A]:
    case Leaf
    case Branch(value: A, left: Tree[A], right: Tree[A])

    // uncomment
    // given evidence = ???
  end Tree

  /* Question 8 */

  def f8 = ???

end Monads

object Parsing:

  import Monads.Tree
  import Monads.Tree.*

  /* Question 9 */

  lazy val parser = ???

end Parsing

```


#### Short summary: 

empty definition using pc, found symbol in pc: `<none>`.