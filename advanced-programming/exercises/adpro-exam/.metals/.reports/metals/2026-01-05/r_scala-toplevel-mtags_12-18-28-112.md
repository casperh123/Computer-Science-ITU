error id: file://<WORKSPACE>/Exam.scala:[1799..1800) in Input.VirtualFile("file://<WORKSPACE>/Exam.scala", "/* Exam: Advanced Programming, by Andrzej Wasowski
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
                   ps: LazyList[Double]): LazyList[Double] = ???
                    

  /* Question 4 */

  def runningRMSEProperty(using arb: Arbitrary[(LazyList[Double], LazyList[Double])]): Prop = 
    forAll {(lists: (LazyList[Double], LazyList[Double])) =>   
      runningRMSE(lists._1, lists._2)
        .take(500)
        .forAll(elem => elem >= 0)
    }

  /* Question 5 */

  def[A: Gen] gen5: Gen[LazyList[A]] =
    

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
")
file://<WORKSPACE>/file:<WORKSPACE>/Exam.scala
file://<WORKSPACE>/Exam.scala:70: error: expected identifier; obtained lbracket


Current stack trace:
java.base/java.lang.Thread.getStackTrace(Thread.java:2451)
scala.meta.internal.mtags.ScalaToplevelMtags.failMessage(ScalaToplevelMtags.scala:1206)
scala.meta.internal.mtags.ScalaToplevelMtags.$anonfun$reportError$1(ScalaToplevelMtags.scala:1192)
scala.meta.internal.metals.StdReporter.$anonfun$create$1(ReportContext.scala:148)
scala.util.Try$.apply(Try.scala:217)
scala.meta.internal.metals.StdReporter.create(ReportContext.scala:143)
scala.meta.pc.reports.Reporter.create(Reporter.java:10)
scala.meta.internal.mtags.ScalaToplevelMtags.reportError(ScalaToplevelMtags.scala:1189)
scala.meta.internal.mtags.ScalaToplevelMtags.methodIdentifier(ScalaToplevelMtags.scala:1132)
scala.meta.internal.mtags.ScalaToplevelMtags.emitTerm(ScalaToplevelMtags.scala:896)
scala.meta.internal.mtags.ScalaToplevelMtags.$anonfun$loop$16(ScalaToplevelMtags.scala:344)
scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.scala:18)
scala.meta.internal.mtags.MtagsIndexer.withOwner(MtagsIndexer.scala:53)
scala.meta.internal.mtags.MtagsIndexer.withOwner$(MtagsIndexer.scala:50)
scala.meta.internal.mtags.ScalaToplevelMtags.withOwner(ScalaToplevelMtags.scala:49)
scala.meta.internal.mtags.ScalaToplevelMtags.loop(ScalaToplevelMtags.scala:344)
scala.meta.internal.mtags.ScalaToplevelMtags.indexRoot(ScalaToplevelMtags.scala:96)
scala.meta.internal.metals.SemanticdbDefinition$.foreachWithReturnMtags(SemanticdbDefinition.scala:83)
scala.meta.internal.metals.Indexer.indexSourceFile(Indexer.scala:546)
scala.meta.internal.metals.Indexer.$anonfun$reindexWorkspaceSources$3(Indexer.scala:677)
scala.meta.internal.metals.Indexer.$anonfun$reindexWorkspaceSources$3$adapted(Indexer.scala:674)
scala.collection.IterableOnceOps.foreach(IterableOnce.scala:630)
scala.collection.IterableOnceOps.foreach$(IterableOnce.scala:628)
scala.collection.AbstractIterator.foreach(Iterator.scala:1313)
scala.meta.internal.metals.Indexer.reindexWorkspaceSources(Indexer.scala:674)
scala.meta.internal.metals.MetalsLspService.$anonfun$onChange$2(MetalsLspService.scala:912)
scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.scala:18)
scala.concurrent.Future$.$anonfun$apply$1(Future.scala:691)
scala.concurrent.impl.Promise$Transformation.run(Promise.scala:500)
java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144)
java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642)
java.base/java.lang.Thread.run(Thread.java:1583)

  def[A: Gen] gen5: Gen[LazyList[A]] =
     ^
#### Short summary: 

expected identifier; obtained lbracket