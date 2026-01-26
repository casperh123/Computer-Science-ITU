error id: 353F150696CC78FF50EB1AD548CDEBB9
file://<WORKSPACE>/Exercises.scala
### java.lang.AssertionError: assertion failed: asTerm called on not-a-Term val <none>

occurred in the presentation compiler.



action parameters:
offset: 11302
uri: file://<WORKSPACE>/Exercises.scala
text:
```scala
// Advanced Programming, A. Wąsowski, IT University of Copenhagen
// Based on Functional Programming in Scala, 2nd Edition

package adpro.monad

import org.scalacheck.{Arbitrary, Prop}
import org.scalacheck.Prop.*
import org.scalacheck.Prop.given
import org.scalactic.Equality
import org.scalactic.TripleEquals.*

/***** Part I. Monoid */

trait Monoid[A]:

  def combine(a1: A, a2: A): A
  def empty: A

  // Some Laws for monoids (We place them here like in Parsers)

  object laws:

    /* The instance of Eqaulity type class will be used for equality
     * comparisons.  Normally the default equality is fine, but we need to
     * parameterize to handle endoMonoid (comparisons of functions).  See more
     * comments about that in the test of Ex03.01. */

    def associative(using Arbitrary[A], Equality[A]): Prop =
      forAll { (a1: A, a2: A, a3: A) =>
        combine(combine(a1, a2), a3) === combine(a1, combine(a2, a3))
      } :| "monoid-associative"

    /* The triple equality below (===) uses the eqA instance (by default the
     * same as == but we can override it, which is exploited in the test of
     * Exercise 3) */

    def unit(using Arbitrary[A], Equality[A]): Prop =
      forAll { (a: A) =>
        (combine(a, empty) === a) :| "right-empty" &&
        (combine(empty, a) === a) :| "left-empty"
      } :| "monoid-unit"

    def monoid (using Arbitrary[A], Equality[A]): Prop =
      (associative && unit) :| "monoid-laws"

end Monoid

// AW: A helper function to find a monoid instance easily
def monoid[A: Monoid]: Monoid[A] = summon[Monoid[A]]

val stringMonoid = new Monoid[String]:
  def combine(a1: String, a2: String) = a1 + a2
  val empty = ""

def listMonoid[A] = new Monoid[List[A]]:
  def combine(a1: List[A], a2: List[A]) = a1 ++ a2
  val empty = Nil


// Exercise 1

lazy val intAddition: Monoid[Int] = new Monoid[Int]:
  def combine(a: Int, b: Int): Int = a + b;
  val empty = 0;

lazy val intMultiplication: Monoid[Int] = new Monoid[Int]:
  def combine(a: Int, b: Int): Int = a * b;
  val empty = 1;

lazy val booleanOr: Monoid[Boolean] = new Monoid[Boolean]:
  def combine(a: Boolean, b: Boolean): Boolean = a || b;
  val empty = false

lazy val booleanAnd: Monoid[Boolean] = new Monoid[Boolean]:
  def combine(a: Boolean, b: Boolean): Boolean = a && b;
  val empty = false;


// Exercise 2

// a)

def optionMonoid[A]: Monoid[Option[A]] = new Monoid[Option[A]]:
  def combine(a: Option[A], b: Option[A]): Option[A] = a.orElse(b)

  val empty = None


// b)

def optionMonoidLift[A: Monoid]: Monoid[Option[A]] = new Monoid[Option[A]]:
  def combine(a: Option[A], b: Option[A]): Option[A] =
    val combined = for
      left <- a
      right <- b
    yield summon[Monoid[A]].combine(left, right)
    combined orElse a orElse b
  
  val empty = None;

// Exercise 3

def endoMonoid[A]: Monoid[A => A] = new Monoid[A => A]:
  def combine(a1: A => A, a2: A => A): A => A = 
    a => a1(a2(a))

  val empty = a => a


// Exercise 4 (tests exercises 1-2, written by student)

object MonoidEx4Spec
  extends org.scalacheck.Properties("exerc4"):

  property("Ex04.01: intAddition is a monoid") =
    intAddition.laws.monoid

  property("Ex04.02: intMultiplication is a monoid") =
    intMultiplication.laws.monoid

  property("Ex04.03: booleanOr is a monoid") =
    booleanOr.laws.monoid

  property("Ex04.04: booleanAnd is a monoid") =
    booleanAnd.laws.monoid

  property("Ex04.05: optionMonoid is a monoid") =
    optionMonoid[Int].laws.monoid

  property("Ex04.06: optionMonoidLift is a monoid") =
    given Monoid[Int] = intAddition
    optionMonoidLift[Int].laws.monoid

end MonoidEx4Spec


// Exercise 5

// We implement this as an extension, so that the exercises do not jump back
// and forth in the file. (This naturally belongs to the Monoid trait).

extension [B](mb: Monoid[B])
  def foldMap[A](as: List[A])(f: A => B): B =
    as.foldRight(mb.empty)((elem, acc) => mb.combine(f(elem), acc))


// Exercise 6

/* We implement this as an extension, so that the exercises do not jump back
 * and forth in the file. (This naturally belongs to the Monoid trait).
 *
 * The triple equality (===) uses the Equality instance to check equality
 * (by default the same as == but we can override it). */

extension [A: {Arbitrary, Equality}](ma: Monoid[A])

  def homomorphism[B](f: A => B)(mb: Monoid[B]): Prop =
    ???

  def isomorphism[B: Arbitrary](f: A => B, g: B => A)(mb: Monoid[B]): Prop =
    ???


// Exercise 7 (tests for Exercise 6, written by the student)

object MonoidEx7Spec
  extends org.scalacheck.Properties("exerc7"):

  property("Ex07.01: stringMonoid is isomorphic to listMonoid[Char]") =
    ???


// "Exercise 8 (tests for Exercise 1, written the by student)

object MonoidEx8Spec
  extends org.scalacheck.Properties("exerc8"):

  property("Ex08.01: booleanOr is isomorphic to booleanAnd") =
    ???


// Exercise 9 

def productMonoid[A, B](ma: Monoid[A])(mb: Monoid[B]): Monoid[(A,B)] = new Monoid[(A,B)]:
  def combine(first: (A,B), second: (A,B)) = (ma.combine(first._1, second._1), mb.combine(first._2, second._2)) 
  val empty = (ma.empty, mb.empty)


// Exercise 10 (tests for Exercise 9, written by the student)

object MonoidEx10Spec
  extends org.scalacheck.Properties("exer10"):

  property("Ex10.01: productMonoid(optionMonoid[Int])(listMonoid[String]) gives a monoid") =
    val prodMon = productMonoid(optionMonoid[Int])(listMonoid[String]);
    prodMon.laws.monoid



/* This will be used in the Foldable below: We can get the dual of any monoid
 * just by flipping the `combine`. */

def dual[A](m: Monoid[A]): Monoid[A] = new:
  def combine(x: A, y: A): A = m.combine(y, x)
  val empty = m.empty

/***** Part II. Foldable */

/* The functions foldRight and foldLeft below are little gems for self-study :).
 * They resemble the foldLeft via foldRight exercise from the begining of
 * the course. */

trait Foldable[F[_]]:

  extension [A](as: F[A])

    def foldMap[B](f: A => B)(using mb: Monoid[B]): B

    def foldRight[B](z: B)(f: (A, B) => B): B =
      as.foldMap[B => B](f.curried)(using endoMonoid[B])(z)

    def foldLeft[B](z: B)(f: (B, A) => B): B =
      as.foldMap[B => B](a => b => f(b, a))(using dual(endoMonoid[B]))(z)

    def combineAll(using m: Monoid[A]): A =
      as.foldLeft(m.empty)(m.combine)

end Foldable

// Exercise 11

given foldableList: [A] => Foldable[List] = new Foldable[List]:
  extension[A](as: List[A])
    def foldMap[B](f: A => B)(using mb: Monoid[B]): B = as.map(f).foldRight(mb.empty)((elem, acc) => mb.combine(elem, acc))


// Exercise 12

// Note since Foldable[F] is a given, its extensions for as are visible
// (https://docs.scala-lang.org/scala3/reference/contextual/extension-methods.html)

extension [F[_]: Foldable, A] (as: F[A])
  def toList: List[A] = as.toListF
  def toListF: List[A] = as.foldRight(List.empty) {_::_}


/***** Part III. Functor */

trait Functor[F[_]]:

  extension [A](fa: F[A])
    def map[B](f: A => B): F[B]

  extension [A, B](fab: F[(A, B)])
    def distribute: (F[A], F[B])=
      (fab.map(_._1), fab.map(_._2))

  extension [A, B](e: Either[F[A], F[B]])
    def codistribute: F[Either[A, B]] = e match
      case Left(fa) => fa.map { Left(_) }
      case Right(fb) => fb.map { Right(_) }

  object functorLaws:

    /* The triple equality below (===) uses the Equality instance to check
     * equality (by default the same as == but we can override it). */

    def map[A](using Arbitrary[F[A]], Equality[F[A]]): Prop =
      forAll { (fa: F[A]) => fa.map[A](identity[A]) === fa }

  end functorLaws

end Functor


// Exercise 13

lazy val optionFunctor: Functor[Option] = new Functor[Option]:
  extension [A](option: Option[A])
    def map[B](f: A => B): Option[B] = option.map(f)

// this instance is provided
val listFunctor: Functor[List] = new:
  extension [A] (as: List[A])
    def map[B](f: A => B): List[B] = as.map(f)

object FunctorEx14Spec
  extends org.scalacheck.Properties("exer14"):

  property("Ex14.01: listFunctor satisfies the map law") =
    listFunctor.functorLaws.map[Int]

  // Exercise 14

  property("Ex14.02: optionFunctor satisfies map law (tests Exercise 13)") =
    optionFunctor.functorLaws.map[Int]

end FunctorEx14Spec


/***** Part IV. Monad */

trait Monad[F[_]]
  extends Functor[F]:

  def unit[A](a: => A): F[A]

  extension [A](fa: F[A])
    def flatMap[B] (f: A => F[B]): F[B]

    def map[B](f: A => B): F[B] =
      fa.flatMap[B] { a => unit(f(a)) }

    def map2[B, C](fb: F[B])(f: (A, B) => C): F[C] =
      fa.flatMap { a => fb.map { b => f(a,b) } }

  object monadLaws:

    /* The triple equality below (===) uses the Equality instance to check
     * equality (by default the same as == but we can override it). */

    def associative[A, B, C](using Arbitrary[F[A]], Arbitrary[A => F[B]],
      Arbitrary[B => F[C]], Equality[F[C]]): Prop =
      forAll { (x: F[A], f: A => F[B], g: B => F[C]) =>
        val left = x.flatMap[B](f).flatMap[C](g)
        val right = x.flatMap[C] { a => f(a).flatMap[C](g) }
        (left === right) :| s"left:$left right:$right"
      }

    def identityRight[A](using Arbitrary[F[A]], Arbitrary[A => F[A]], Equality[F[A]]) =
      forAll { (x: F[A], f: A => F[A]) =>
        val result = x.flatMap[A](unit[A])
        (result === x) :| s"got:$result expected:$x" }

    def identityLeft[A: Arbitrary](using Arbitrary[A => F[A]], Equality[F[A]]) =
      forAll { (y: A, f: A => F[A]) =>
        val left = unit[A](y).flatMap[A](f)
        val right = f(y)
        (left === right) :| s"left:$left right:$right"
      }

    def identity[A: Arbitrary](using Arbitrary[F[A]], Arbitrary[A => F[A]],
      Equality[F[A]]): Prop =
      { "identity left: " |: identityLeft[A]  } &&
      { "identity right:" |: identityRight[A] }

    def monad[A: Arbitrary, B, C] (using Arbitrary[F[A]], Arbitrary[A => F[A]],
      Arbitrary[A => F[B]], Arbitrary[B => F[C]]): Prop =
      { "associative:" |: this.associative[A,B,C] } &&
      { "identity:   " |: this.identity[A] }

  end monadLaws

end Monad


// Exercise 15

lazy val optionMonad: Monad[Option] = new Monad[Option]:
  def unit[A](a: => A): Option[A] = Some(a)

  extension[A](option: Option[A])

    def flatMap[B](f: A => Option[B]): Option[B] = 
      for 
        a <- option
        result <- f(a)
      yield result
      

lazy val listMonad: Monad[List] = new Monad[List]:
  def unit[A](a: => A): List[A] = a::List.empty

  extension[A](list: List[A])
    def flatMap[B](f: A => List[B]): List[B] =
      list.flatMap(f)


// Exercise 16 (tests for Exercise 15, written by the student)

object FunctorEx16Spec
  extends org.scalacheck.Properties("exer16"):

  property("Ex16.01: optionMonad is a monad") =
    optionMonad.monadLaws.monad[Int, Int, Int];

  property("Ex16.02: listMonad is a monad") =
    listMonad.monadLaws.monad[List[Int], Int, Int];

end FunctorEx16Spec


// Exercise 17
//
// We do this as an extension to maintain the linear sequence of exercises in
// the file (we would normally place it in the Monad trait).

extension [F[_]](m: Monad[F])
  def sequence[A](fas: List[F[A]]): F[List[A]] =
    fas.foldRight(m.unit(List.empty))((elem, acc) => m.map2(elem)(acc){_::_})


// Exercise 18

extension [F[_]](m: Monad[F])
  def replicateM[A](n: Int, ma: F[A]): F[List[A]] =
    @@???

// Write in the answer below ...
//
// ???


// Exercise 19

extension [F[_]](m: Monad[F])
  def compose[A, B, C](f: A => F[B], g: B => F[C]): A => F[C] =
    ???

```


presentation compiler configuration:
Scala version: 3.7.2-bin-nonbootstrapped
Classpath:
<WORKSPACE>/.scala-build/09-monad_e8211e4050/classes/main [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.7.2/scala3-library_3-3.7.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scalacheck/scalacheck_3/1.19.0/scalacheck_3-1.19.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scalactic/scalactic_3/3.2.19/scalactic_3-3.2.19.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.16/scala-library-2.13.16.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-sbt/test-interface/1.0/test-interface-1.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/sourcegraph/semanticdb-javac/0.10.0/semanticdb-javac-0.10.0.jar [exists ], <WORKSPACE>/.scala-build/09-monad_e8211e4050/classes/main/META-INF/best-effort [missing ]
Options:
-Xfatal-warnings -deprecation -feature -source:future -language:adhocExtensions -Xsemanticdb -sourceroot <WORKSPACE> -release 17 -Ywith-best-effort-tasty




#### Error stacktrace:

```
scala.runtime.Scala3RunTime$.assertFailed(Scala3RunTime.scala:8)
	dotty.tools.dotc.core.Symbols$Symbol.asTerm(Symbols.scala:186)
	dotty.tools.dotc.core.Definitions.ObjectClass(Definitions.scala:325)
	dotty.tools.dotc.core.Definitions.ObjectType(Definitions.scala:329)
	dotty.tools.dotc.core.Definitions.AnyRefAlias(Definitions.scala:428)
	dotty.tools.dotc.core.Definitions.syntheticScalaClasses(Definitions.scala:2231)
	dotty.tools.dotc.core.Definitions.syntheticCoreClasses(Definitions.scala:2244)
	dotty.tools.dotc.core.Definitions.init(Definitions.scala:2260)
	dotty.tools.dotc.core.Contexts$ContextBase.initialize(Contexts.scala:920)
	dotty.tools.dotc.core.Contexts$Context.initialize(Contexts.scala:545)
	dotty.tools.dotc.interactive.InteractiveDriver.<init>(InteractiveDriver.scala:41)
	dotty.tools.pc.CachingDriver.<init>(CachingDriver.scala:30)
	dotty.tools.pc.ScalaPresentationCompiler.$init$$$anonfun$1(ScalaPresentationCompiler.scala:129)
```
#### Short summary: 

java.lang.AssertionError: assertion failed: asTerm called on not-a-Term val <none>