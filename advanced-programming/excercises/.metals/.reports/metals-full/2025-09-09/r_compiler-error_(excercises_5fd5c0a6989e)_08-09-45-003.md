error id: 070A509E2380FE501035850AD63641DA
file://<WORKSPACE>/03-option/Exercises.scala
### java.lang.IndexOutOfBoundsException: 0

occurred in the presentation compiler.



action parameters:
offset: 918
uri: file://<WORKSPACE>/03-option/Exercises.scala
text:
```scala
// Advanced Programming, A. Wąsowski, IT University of Copenhagen
// Based on Functional Programming in Scala, 2nd Edition

package adpro.option

import scala.caps.internal

// Exercise 1

trait OrderedPoint
  extends scala.math.Ordered[java.awt.Point]:

  this: java.awt.Point =>

  override def compare(that: java.awt.Point): Int =
    ???

// Try the following (and similar) tests in the repl (sbt console):
//
// import adpro.option.*
// val p = new java.awt.Point(0, 1) with OrderedPoint
// val q = new java.awt.Point(0, 2) with OrderedPoint
// assert(p < q)



// Chapter 3 Exercises

enum Tree[+A]:
  case Leaf(value: A)
  case Branch(left: Tree[A], right: Tree[A])

object Tree:

  // Exercise 2

  def size[A](t: Tree[A]): Int = 
    def internalSize[A](t: Tree[A], acc: Int): Int = t match
      case Leaf(_) => acc + 1
      case Branch(l, r) => internalSize(l, acc) + internalSize(r, acc + 1)
      case Br@@
    internalSize(t, 0)

      
    


  // Exercise 3

  def maximum(t: Tree[Int]): Int = t match
    case Leaf(v) => v
    case Branch(l, r) => maximum(l) max maximum(r)
  

  // Exercise 4

  def map[A, B](t: Tree[A])(f: A => B): Tree[B] = ???

  // Exercise 5

  def fold[A,B](t: Tree[A])(f: (B, B) => B)(g: A => B): B = ???

  def size1[A](t: Tree[A]): Int =  ???

  def maximum1(t: Tree[Int]): Int = ???

  def map1[A, B](t: Tree[A])(f: A => B): Tree[B] = ???




enum Option[+A]:
  case Some(get: A)
  case None

  // Exercise 6

  def map[B](f: A => B): Option[B] = ???

  def getOrElse[B >: A] (default: => B): B = ???

  def flatMap[B](f: A => Option[B]): Option[B] =  ???

  def filter(p: A => Boolean): Option[A] = ???

  // Scroll down for Exercise 7, in the bottom of the file, outside Option

  def forAll(p: A => Boolean): Boolean = this match
    case None => true
    case Some(a) => p(a)

end Option

// Exercise 9

def map2[A, B, C](ao: Option[A], bo: Option[B])(f: (A,B) => C): Option[C] =
  ???

// Exercise 10

def sequence[A](aos: List[Option[A]]): Option[List[A]] =
  ???

// Exercise 11

def traverse[A, B](as: List[A])(f: A => Option[B]): Option[List[B]] =
  ???




// Exercise that are outside the Option companion object

import Option.{Some, None}

def headOption[A](lst: List[A]): Option[A] = lst match
  case Nil => None
  case h:: t => Some(h)

// Exercise 7

def headGrade(lst: List[(String,Int)]): Option[Int] =
  ???

def headGrade1(lst: List[(String,Int)]): Option[Int] =
  ???

// Implemented in the text book

def mean(xs: Seq[Double]): Option[Double] =
  if xs.isEmpty then None
  else Some(xs.sum / xs.length)

// Exercise 8

def variance(xs: Seq[Double]): Option[Double] =
  ???

// Scroll up, to the Option object for Exercise 9

```


presentation compiler configuration:
Scala version: 3.7.2-bin-nonbootstrapped
Classpath:
<WORKSPACE>/.scala-build/excercises_d5c0a6989e/classes/main [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.7.2/scala3-library_3-3.7.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.16/scala-library-2.13.16.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/sourcegraph/semanticdb-javac/0.10.0/semanticdb-javac-0.10.0.jar [exists ], <WORKSPACE>/.scala-build/excercises_d5c0a6989e/classes/main/META-INF/best-effort [missing ]
Options:
-Xfatal-warnings -deprecation -feature -source:future -language:adhocExtensions -Xsemanticdb -sourceroot <WORKSPACE> -Ywith-best-effort-tasty




#### Error stacktrace:

```
scala.collection.LinearSeqOps.apply(LinearSeq.scala:131)
	scala.collection.LinearSeqOps.apply$(LinearSeq.scala:128)
	scala.collection.immutable.List.apply(List.scala:79)
	dotty.tools.pc.InterCompletionType$.inferType(InferExpectedType.scala:94)
	dotty.tools.pc.InterCompletionType$.inferType(InferExpectedType.scala:62)
	dotty.tools.pc.completions.Completions.advancedCompletions(Completions.scala:523)
	dotty.tools.pc.completions.Completions.completions(Completions.scala:122)
	dotty.tools.pc.completions.CompletionProvider.completions(CompletionProvider.scala:139)
	dotty.tools.pc.ScalaPresentationCompiler.complete$$anonfun$1(ScalaPresentationCompiler.scala:194)
```
#### Short summary: 

java.lang.IndexOutOfBoundsException: 0