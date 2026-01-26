file://<WORKSPACE>/Exam.scala
### dotty.tools.dotc.ast.Trees$UnAssignedTypeException: type of Ident(intParser) is not assigned

occurred in the presentation compiler.

presentation compiler configuration:


action parameters:
offset: 2749
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

  lazy val intParser[@@]

  lazy val leafParser: Parser[Tree[Int]] = string("()").map(value => Leaf)
  lazy val branchParser: Parser[Tree[Int]] = 
    char('(') |* 

    
        *|



    // for
    //   _ <- char('(')
    //   digit <- regex("[0-9]+".r).map(value => value.toInt)
    //   left <- branchParser
    //   right <- branchParser
    //   _ <- char(')')
    // yield Branch(digit, left, right)

  lazy val parser = ???

end Parsing

```



#### Error stacktrace:

```
dotty.tools.dotc.ast.Trees$Tree.tpe(Trees.scala:74)
	dotty.tools.dotc.util.Signatures$.applyCallInfo(Signatures.scala:207)
	dotty.tools.dotc.util.Signatures$.computeSignatureHelp(Signatures.scala:104)
	dotty.tools.dotc.util.Signatures$.signatureHelp(Signatures.scala:88)
	dotty.tools.pc.SignatureHelpProvider$.signatureHelp(SignatureHelpProvider.scala:53)
	dotty.tools.pc.ScalaPresentationCompiler.signatureHelp$$anonfun$1(ScalaPresentationCompiler.scala:409)
```
#### Short summary: 

dotty.tools.dotc.ast.Trees$UnAssignedTypeException: type of Ident(intParser) is not assigned