error id: file://<WORKSPACE>/Exam.scala:
file://<WORKSPACE>/Exam.scala
empty definition using pc, found symbol in pc: 
empty definition using semanticdb
empty definition using fallback
non-local guesses:
	 -org/scalacheck/GenExt.Branch.
	 -org/scalacheck/GenExt.Branch#
	 -org/scalacheck/GenExt.Branch().
	 -Arbitrary.Branch.
	 -Arbitrary.Branch#
	 -Arbitrary.Branch().
	 -Prop.Branch.
	 -Prop.Branch#
	 -Prop.Branch().
	 -org/scalactic/TripleEquals.Branch.
	 -org/scalactic/TripleEquals.Branch#
	 -org/scalactic/TripleEquals.Branch().
	 -adpro/option/Branch.
	 -adpro/option/Branch#
	 -adpro/option/Branch().
	 -adpro/lazyList/Branch.
	 -adpro/lazyList/Branch#
	 -adpro/lazyList/Branch().
	 -adpro/state/Branch.
	 -adpro/state/Branch#
	 -adpro/state/Branch().
	 -adpro/monad/Branch.
	 -adpro/monad/Branch#
	 -adpro/monad/Branch().
	 -adpro/parsing/Branch.
	 -adpro/parsing/Branch#
	 -adpro/parsing/Branch().
	 -adpro/parsing/Sliceable.Branch.
	 -adpro/parsing/Sliceable.Branch#
	 -adpro/parsing/Sliceable.Branch().
	 -monocle/Branch.
	 -monocle/Branch#
	 -monocle/Branch().
	 -monocle/syntax/all/Branch.
	 -monocle/syntax/all/Branch#
	 -monocle/syntax/all/Branch().
	 -monocle/function/all/Branch.
	 -monocle/function/all/Branch#
	 -monocle/function/all/Branch().
	 -Monads.Tree.Branch.
	 -Monads.Tree.Branch#
	 -Monads.Tree.Branch().
	 -Branch.
	 -Branch#
	 -Branch().
	 -scala/Predef.Branch.
	 -scala/Predef.Branch#
	 -scala/Predef.Branch().
offset: 3012
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
import adpro.Monads.Tree

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

  given Arbitrary[(LazyList[Double], LazyList[Double])] =
      Arbitrary { 
        Gen.nonEmptyListOf(Gen.choose(1.0, 1000.0))
          .map { l => (LazyList(l*), LazyList(l*)) } 
      }

  def rmseProperty: Prop =

    forAll {(lists: (LazyList[Double], LazyList[Double])) =>
      rmse(lists._1, lists._2) >= 0
    }

  /* Question 3 */

  def runningRMSE (gs: LazyList[Double],
                   ps: LazyList[Double]): LazyList[Double] = ???
                    

  /* Question 4 */

  def runningRMSEProperty: Prop = 
    forAll {(lists: (LazyList[Double], LazyList[Double])) =>   
      runningRMSE(lists._1, lists._2)
        .take(500)
        .forAll(elem => elem >= 0)
    }

  /* Question 5 */

  def gen5 =
    ???

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
    
    given evidence: Functor[Tree]  = new:
      extension[A](tree: Tree[A])
        def map[B] (f: A => B) : Tree[B] = 
          def inner(t: Tree[A]) : Tree[B] = t match
            case Leaf => Leaf
            case Branch(value, left, right) => Branch(f(value), inner(left), inner(right))
          
          inner(tree)

  end Tree

  /* Question 8 */

  def f8[Tree[Int]: Functor](tree: Tree[Int]): Tree[Int] = 
    val functor = summon[Functor[Tree]]

    functor.map(tree){(value) => value + 1}

end Monads

object Parsing:

  import Monads.Tree
  import Monads.Tree.*

  /* Question 9 */

  lazy val int: Parser[Int] = regex("[0-9]+".r).slice.map(value => value.toInt)
  lazy val tree: Parser[Tree[Int]] = branch | leaf
  lazy val leaf: Parser[Tree[Int]] = string("()").slice.map(value => Leaf)
  lazy val innerBranch: Parser[Tree[Int]] = 
    (int ** (tree ** tree)).map(B@@ranch(_._1))


  lazy val branch: Parser[Tree[Int]] = 
    for
      _ <- char('(').slice
      digit <- int
      left <- tree
      right <- tree
      _ <- char(')')
    yield Branch(digit, left, right)

    // char('(') |* 
    //   (intParser ** ((tree) ** (tree)))
    //     .map((v, t) => Branch(v, t._1, t._2)) 
    // *| char(')')

  lazy val parser = tree

end Parsing

```


#### Short summary: 

empty definition using pc, found symbol in pc: 