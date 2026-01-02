error id: 070A509E2380FE501035850AD63641DA
file://<WORKSPACE>/Exercises.scala
### java.lang.IndexOutOfBoundsException: 1

occurred in the presentation compiler.



action parameters:
offset: 3667
uri: file://<WORKSPACE>/Exercises.scala
text:
```scala
// Advanced Programming, A. Wąsowski, IT University of Copenhagen
// Based on Functional Programming in Scala, 2nd Edition

package adpro.adt

import java.util.NoSuchElementException
import scala.annotation.tailrec

enum List[+A]:
  case Nil
  case Cons(head: A, tail: List[A])


object List: 

  def head[A] (l: List[A]): A = l match
    case Nil => throw NoSuchElementException() 
    case Cons(h, _) => h                                                                                                                                                                                                                                       
  
  def apply[A] (as: A*): List[A] =
    if as.isEmpty then Nil
    else Cons(as.head, apply(as.tail*))

  def append[A] (l1: List[A], l2: List[A]): List[A] =
    l1 match
      case Nil => l2
      case Cons(h, t) => Cons(h, append(t, l2)) 

  def foldRight[A, B] (l: List[A], z: B, f: (A, B) => B): B = l match
    case Nil => z
    case Cons(a, as) => f(a, foldRight(as, z, f))
    
  def map[A, B] (l: List[A], f: A => B): List[B] =
    foldRight[A, List[B]] (l, Nil, (a, z) => Cons(f(a), z))

  // Exercise 1 (is to be solved without programming)

  // Exercise 2

  def tail[A] (l: List[A]): List[A] = l match
    case Nil => throw NoSuchElementException()
    case Cons(x, xs) => xs
  

  // Exercise 3
  
  @tailrec
  def drop[A] (l: List[A], n: Int): List[A] = l match
    case l if n <= 0 => l
    case Nil => throw NoSuchElementException()
    case Cons(x, xs) => drop(xs, n - 1)
  

  // Exercise 4

  def dropWhile[A] (l: List[A], p: A => Boolean): List[A] = l match
    case Nil => Nil
    case Cons(x, xs) if p(x) => dropWhile(xs, p)
    case l => l
  

  // Exercise 5
 
  def init[A] (l: List[A]): List[A] = l match
    case Nil => throw NoSuchElementException()
    case Cons(x, xs) if xs == Nil => Nil
    case Cons(x, xs) => Cons(x, init(xs))
  
    

  // Exercise 6

  def length[A] (l: List[A]): Int = 
    foldRight(l, 0, (elem, acc) => acc + 1)

  // Exercise 7

  @tailrec
  def foldLeft[A, B] (l: List[A], z: B, f: (B, A) => B): B = l match
    case Nil => z
    case Cons(x, xs) => foldLeft(xs, f(z, x), f)

  // Exercise 8

  def product (as: List[Int]): Int = 
    foldLeft(as, 1, (acc, elem) => acc * elem)

  def length1[A] (as: List[A]): Int = 
    foldLeft(as, 0, (acc, elem) => acc + 1)

  // Exercise 9

  def reverse[A] (l: List[A]): List[A] = 
    foldLeft(l, Nil, (acc, elem) => Cons(elem, acc))
 
  // Exercise 10

  def foldRight1[A, B] (l: List[A], z: B, f: (A, B) => B): B =
    foldLeft(reverse(l), z, (a, b) => f(b, a))
  
  
  // Exercise 11

  def foldLeft1[A, B] (l: List[A], z: B, f: (B, A) => B): B = ???
 
  // Exercise 12

  def concat[A] (l: List[List[A]]): List[A] = 
    foldLeft(l, Nil, (acc, elem) => List.append(acc, elem))
  
  // Exercise 13

  def filter[A] (l: List[A], p: A => Boolean): List[A] = 
    foldRight(l, Nil, (elem, acc) => if p(elem) then Cons(elem ,acc) else acc)
 
  // Exercise 14

  def flatMap[A,B] (l: List[A], f: A => List[B]): List[B] = 
    foldRight(l, Nil, (elem, acc) => List.append(f(elem), acc))

  // Exercise 15

  def filter1[A] (l: List[A], p: A => Boolean): List[A] =
    flatMap(l, (elem) => if p(elem) then List(elem) else Nil)

  // Exercise 16

  def addPairwise (l: List[Int], r: List[Int]): List[Int] = (l, r) match
    case (Nil, _) => Nil
    case (_, Nil) => Nil
    case (Cons(x, xs), Cons(y, ys)) => Cons(x + y, addPairwise(xs, ys))

  // Exercise 17

  def zipWith[A, B, C] (l: List[A], r: List[B], f: (A,B) => C): List[C] = (l, r) match
    case (Nil, _) => Nil
    case (_, Nil) => Nil
    case (Cons(x, xs), Conse(y, y@@))
  

  // Exercise 18

  def hasSubsequence[A] (sup: List[A], sub: List[A]): Boolean = ???

```


presentation compiler configuration:
Scala version: 3.7.2-bin-nonbootstrapped
Classpath:
<WORKSPACE>/.scala-build/02-adt_0f10ccc8b3/classes/main [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.7.2/scala3-library_3-3.7.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.16/scala-library-2.13.16.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/sourcegraph/semanticdb-javac/0.10.0/semanticdb-javac-0.10.0.jar [exists ], <WORKSPACE>/.scala-build/02-adt_0f10ccc8b3/classes/main/META-INF/best-effort [missing ]
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

java.lang.IndexOutOfBoundsException: 1