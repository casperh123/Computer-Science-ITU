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
          (
            acc._1 + math.pow((elems._1 - elems._2), 2), 
            acc._2 + 1
          )
        }
        
    math.sqrt((1.0 / size) * sum)

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
                   ps: LazyList[Double]): LazyList[Double] = 
    def inner(size: Int): Double = 
      val zipped = gs.zip(ps).take(size)

      val sum = zipped.foldLeft(0.0) {(acc, elems) => 
            acc + math.pow((elems._1 - elems._2), 2)
      }
        
      math.sqrt((1.0 / size) * sum)
      
      
    val (size, runnings) = gs.foldLeft(1, LazyList.Empty) { (acc, elem) =>
      (
        acc._1 + 1,
        LazyList.Cons(() => inner(acc._1), () => acc._2)
      )
    }

    runnings


  /* Question 4 */

  def runningRMSEProperty(
    using arb: Arbitrary[(LazyList[Double], LazyList[Double])]): Prop = 
    forAll {(lists: (LazyList[Double], LazyList[Double])) =>   
      runningRMSE(lists._1, lists._2)
        .take(500)
        .forAll(elem => elem >= 0)
    }

  /* Question 5 */

  def gen5[A: Gen]: Gen[LazyList[A]] =
    val gen = summon[Gen[A]]

    LazyList(gen).sequence
    

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
    
    given evidence: Functor[Tree]  = new:
      extension[A](tree: Tree[A])
        def map[B] (f: A => B) : Tree[B] = tree match
            case Leaf => Leaf
            case Branch(value, left, right) => 
              Branch(f(value), left.map(f), right.map(f))

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

  lazy val int: Parser[Int] = regex("[0-9]+".r).map(value => value.toInt)
  lazy val tree: Parser[Tree[Int]] = branch | leaf
  lazy val leaf: Parser[Tree[Int]] = string("()").slice.map(value => Leaf)
  lazy val innerBranch: Parser[Tree[Int]] = 
    (int ** (tree ** tree))
      .map(elems => Branch(elems._1, elems._2._1, elems._2._2))


  lazy val branch: Parser[Tree[Int]] = 
    char('(').slice |* innerBranch *| char(')') 

  lazy val parser = tree

end Parsing
