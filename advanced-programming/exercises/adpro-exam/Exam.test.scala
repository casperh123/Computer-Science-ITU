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
import adpro.RMSE.rmse

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
import adpro.Monads.Tree.{Leaf, Branch}
import adpro.Monads.Tree
import adpro.Parsing.parser
import adpro.RMSE.runningRMSEProperty


object ExamSpec
  extends org.scalacheck.Properties("exam-2025"):

  given Arbitrary[(LazyList[Double], LazyList[Double])] =
    Arbitrary { 
      Gen.nonEmptyListOf(Gen.choose(1.0, 1000.0))
        .map { l => (LazyList(l*), LazyList(l*)) } 
    }

  property("rmseProperty is always positive") = 
    forAll {(lists: (LazyList[Double], LazyList[Double])) =>
      rmse(lists._1, lists._2) >= 0
    }

  property("runningRMSE") = 
    runningRMSEProperty

  given evidence: Functor[Tree]  = new:
      extension[A](tree: Tree[A])
        def map[B] (f: A => B) : Tree[B] = tree match
            case Leaf => Leaf
            case Branch(value, left, right) => 
              Branch(f(value), left.map(f), right.map(f))

  property("Tree has map") = 
    forAll(Branch(1, Tree.Leaf, Tree.Leaf)) {(tree: Tree[Int]) =>
      tree.map(identity[Int]) === tree
    }

  property("Tree map increments values") = 
    forAll(Branch(1, Branch(42, Leaf, Leaf), Leaf)) {(tree: Tree[Int]) =>
      tree.map(value => value + 1) === Branch(2, Branch(43, Leaf, Leaf), Leaf)
    }


  property("Tree parser reads tree") = 
    val result = parser.run("(42()())")

    print(result)

    result == Right(Branch(42, Leaf, Leaf))

  property("Tree parser reads tree") = 
    val result = parser.run("()")

    print(result)

    result == Right(Leaf)

  property("Tree parser reads nested tress") = 
    val result = parser.run("(43()(1()()))")

    print(result)

    result == Right(Branch(43, Leaf, Branch(1, Leaf, Leaf)))

  property("Tree parser reads failure") = 
    val result = parser.run("(()()())")

    true

end ExamSpec

// vim:cc=66
