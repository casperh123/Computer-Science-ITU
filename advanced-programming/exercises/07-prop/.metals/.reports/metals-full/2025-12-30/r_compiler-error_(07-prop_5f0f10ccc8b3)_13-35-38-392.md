error id: FB79C624F5F9DD27FA8C2F02FDEB430F
file://<WORKSPACE>/Exercises.scala
### java.lang.AssertionError: assertion failed

occurred in the presentation compiler.



action parameters:
uri: file://<WORKSPACE>/Exercises.scala
text:
```scala
// Advanced Programming, A. Wąsowski, IT University of Copenhagen
// Based on Functional Programming in Scala, 2nd Edition

package adpro.prop

import adpro.state.*

val TODO = 42

// Exercise 1

lazy val rng1: RNG = 
  RNG.Simple(42)

// Exercise 2
lazy val (x, rng2): (Int, RNG) = 
  rng1.nextInt
lazy val y = 
  val (value, next) = rng2.nextInt
  value

// Exercise 3

object Exercise_3:

  import org.scalacheck.Prop.{forAll, forAllNoShrink}

  // Use this generator explicitly in the two properties
  val intList =
    org.scalacheck.Gen.listOf(org.scalacheck.Gen.choose(0, 100))
      .suchThat (_.nonEmpty)

  // The properties are put into a function taking `minimum` as argument to
  // allow the teachers to test them with different mutants of `minimum`.


  def p1Min (minimum: List[Int] => Int): org.scalacheck.Prop =
    org.scalacheck.Prop.forAll(intList) { (list: List[Int]) =>
      list.contains(minimum(list))
    }

  def p2Min (minimum: List[Int] => Int): org.scalacheck.Prop =
    org.scalacheck.Prop.forAll(intList) {(list: List[Int]) =>
      val minVal = minimum(list)
      list.forall(element => minVal <= element)
    }

end Exercise_3

// Exercise 4

object Exercise_4:

  // This implementation of Prop is only used in Exercise 4
  trait Prop:
    self => // TODO remove
    def check: Boolean

    infix def && (that: Prop): Prop =
      new Prop:
        def check: Boolean =
          self.check && that.check

end Exercise_4

opaque type Gen[+A] = State[RNG, A]

object Gen:

  extension [A](g: Gen[A])
    // Let's convert generator to streams of generators
    def toLazyList (rng: RNG): LazyList[A] =
      LazyList.unfold[A,RNG](rng)(rng => Some(g.run(rng)))

  // Exercise 5
  def choose(start: Int, stopExclusive: Int): Gen[Int] =
    State { rng =>
      val (n, next) = rng.nextInt
      val mod = stopExclusive - start
      val positive = if (n < 0) -(n + 1) else n
      (start + positive % mod, next)
  }


  // Exercise 6

  def unit[A] (a: =>A): Gen[A] =
    State(s => (a, s))

  def boolean: Gen[Boolean] =
    State {s => RNG.boolean(s)}

  def double: Gen[Double] =
    State(s => 
      val (value, nextRng) = s.nextInt
      val (secondValue, finalRng) = nextRng.nextInt

      (value / secondValue.toDouble, finalRng)  
    )

  // Exercise 7

  extension [A](self: Gen[A])

    def listOfN(n: Int): Gen[List[A]] =
      val generators = List.fill(n)(self)

      State.List.fill(n)(self)generators)

  // Exercise 8

  // Write here ... ???

  // Exercise 9

  extension [A](self: Gen[A])

    def flatMap[B](f: A => Gen[B]): Gen[B] =
      ???

    // It will be convenient to also have map (uses flatMap)
    def map[B](f: A => B): Gen[B] =
      self.flatMap { a => unit(f(a)) }


  // Exercise 10

  extension [A](self: Gen[A])
    def listOf(size: Gen[Int]): Gen[List[A]] =
      ???


  // Exercise 11

  extension [A](self: Gen[A])
    def union (that: Gen[A]): Gen[A] =
      ???

end Gen

import Gen.*

object Exercise_12:

  // Exercise 12 (type classes, givens, using, summon)

  // Choose one of the following templates, but note only listOfN and
  // listOf are tested (so rename if you use another than the first)

  def listOfN[A: Gen](n: Int): Gen[List[A]] =
    ???

  def listOfN_[A: Gen]: Int => Gen[List[A]] =
    ???

  def listOfN__ [A](n: Int)(using genA: Gen[A]): Gen[List[A]] =
    ???

  // Choose one of the following templates, but note only listOfN and
  // listOf are tested (so rename if you use another than the first)

  def listOf[A: Gen](using genInt: Gen[Int]): Gen[List[A]] =
    ???

  def listOf_[A] (using genInt: Gen[Int], genA: Gen[A]): Gen[List[A]] =
    ???

end Exercise_12


// (Exercise 13)
// Read the code below (and/or Section 8.1.6). You will find the
// exercise in the bottom of this fragment, marked with ??? as usual.

opaque type TestCases = Int
opaque type FailedCase = String
opaque type SuccessCount = Int
opaque type MaxSize = Int

def TestCases(n: Int): TestCases = n
def FailedCase(s: String): FailedCase = s
def SuccessCount(n: Int): SuccessCount = n
def MaxSize(n: Int): MaxSize = n

/** The type of results returned by property testing. */
enum Result:
  case Passed
  case Falsified(failure: FailedCase, successes: SuccessCount)

  def isFalsified: Boolean = this match
    case Passed => false
    case Falsified(_, _) => true

end Result

import Result.{Passed, Falsified}

opaque type Prop = (MaxSize, TestCases, RNG) => Result

def randomLazyList[A](g: Gen[A])(rng: RNG): LazyList[A] =
  LazyList.unfold(rng)(rng => Some(g.run(rng)))

def buildMsg[A](s: A, e: Exception): String =
  s"test case: $s\n" +
  s"generated an exception: ${e.getMessage}\n" +
  s"stack trace:\n ${e.getStackTrace.mkString("\n")}"

def forAll[A](as: Gen[A])(f: A => Boolean): Prop =
  (max, n, rng) =>
    randomLazyList(as)(rng)
      .zip(LazyList.from(0))
      .take(n)
      .map { (a, i) =>
             try if f(a) then Passed else Falsified(a.toString, i)
             catch case e: Exception => Falsified(buildMsg(a, e), i) }
      .find(_.isFalsified)
      .getOrElse(Passed)

def forAllNotSized[A] = forAll[A]

extension (self: Prop)
  infix def && (that: Prop): Prop = (maxSize, tcs, rng) =>
    ???

  infix def || (that: Prop): Prop = (maxSize, tcs, rng) =>
    ???

  def apply(maxSize: MaxSize, tcs: TestCases, rng: RNG): Result =
    self(maxSize, tcs, rng)

// Exercise 14

/** The type of generators bounded by size */
opaque type SGen[+A] = Int => Gen[A]

extension [A](self: SGen[A])
  def apply(n: Int): Gen[A] = self(n)

extension [A](self: Gen[A])
  def unsized: SGen[A] =
    ???

// Exercise 15

extension [A](self: Gen[A])
  def list: SGen[List[A]] =
    ???

// A sized implementation of prop, takes MaxSize to generate
// test cases of given size.
//
// The code below also contains the `run` method for Prop - which
// provides a simple way to execute tests. Needed in the final
// exercise below.

object SGen:

  object Prop:

    def forAll[A](g: SGen[A])(f: A => Boolean): Prop =
      (max, n, rng) =>
        val casesPerSize = (n.toInt - 1)/max.toInt + 1
        val props: LazyList[Prop] =
          LazyList.from(0)
            .take((n.toInt min max.toInt) + 1)
            .map { i => forAllNotSized(g(i))(f) }
        val prop: Prop =
          props.map[Prop](p => (max, n, rng) =>
            p(max, casesPerSize, rng)).toList.reduce(_ && _)
        prop(max, n, rng)

  extension (self: Prop)
    def run(
      maxSize: MaxSize = 100,
      testCases: TestCases = 100,
      rng: RNG = RNG.Simple(System.currentTimeMillis)): Boolean =

      self(maxSize, testCases, rng) match
      case Result.Falsified(msg, n) =>
        println(s"\u001b[34m! Falsified after $n passed tests:\n $msg [message from our Prop framework]")
        false
      case Result.Passed =>
        println(s"\u001b[34m+ OK, passed $testCases tests. [message from our Prop framework]")
        true

end SGen

// Exercise 16

// Use this generator explicitly in the two properties
val nonEmptyList: SGen[List[Int]] =
  (n: Int) => Gen.choose(-100, 100).listOfN(n max 1)

object Exercise_16:

  import SGen.*

  // The properties are put into a function taking `minimum` as argument to
  // allow the teachers to test them with different mutants of `minimum`.

  def p1Min(minimum: List[Int] => Int): Prop =
    ???

  def p2Min(minimum: List[Int] => Int): Prop =
    ???

end Exercise_16

// vim:cc=80:conceallevel=1

```


presentation compiler configuration:
Scala version: 3.7.2-bin-nonbootstrapped
Classpath:
<WORKSPACE>/.scala-build/07-prop_0f10ccc8b3/classes/main [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.7.2/scala3-library_3-3.7.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scalacheck/scalacheck_3/1.19.0/scalacheck_3-1.19.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.16/scala-library-2.13.16.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-sbt/test-interface/1.0/test-interface-1.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/sourcegraph/semanticdb-javac/0.10.0/semanticdb-javac-0.10.0.jar [exists ], <WORKSPACE>/.scala-build/07-prop_0f10ccc8b3/classes/main/META-INF/best-effort [missing ]
Options:
-Xfatal-warnings -deprecation -feature -source:future -language:adhocExtensions -Xsemanticdb -sourceroot <WORKSPACE> -Ywith-best-effort-tasty




#### Error stacktrace:

```
scala.runtime.Scala3RunTime$.assertFailed(Scala3RunTime.scala:11)
	dotty.tools.dotc.core.Types$RefinedType.<init>(Types.scala:3215)
	dotty.tools.dotc.core.Types$CachedRefinedType.<init>(Types.scala:3260)
	dotty.tools.dotc.core.Types$RefinedType$.apply(Types.scala:3269)
	dotty.tools.dotc.core.Types$ClassInfo.refineSelfType$1(Types.scala:5577)
	dotty.tools.dotc.core.Types$ClassInfo.integrateOpaqueMembers$$anonfun$1(Types.scala:5581)
	scala.collection.LinearSeqOps.foldLeft(LinearSeq.scala:183)
	scala.collection.LinearSeqOps.foldLeft$(LinearSeq.scala:179)
	scala.collection.immutable.List.foldLeft(List.scala:79)
	dotty.tools.dotc.core.Types$ClassInfo.integrateOpaqueMembers(Types.scala:5561)
	dotty.tools.dotc.typer.Namer$ClassCompleter.completeConstructor(Namer.scala:1581)
	dotty.tools.dotc.typer.Namer$ClassCompleter.completeInCreationContext(Namer.scala:1731)
	dotty.tools.dotc.typer.Namer$Completer.complete(Namer.scala:874)
	dotty.tools.dotc.core.SymDenotations$SymDenotation.completeFrom(SymDenotations.scala:175)
	dotty.tools.dotc.core.Denotations$Denotation.completeInfo$1(Denotations.scala:190)
	dotty.tools.dotc.core.Denotations$Denotation.info(Denotations.scala:192)
	dotty.tools.dotc.core.Denotations$SingleDenotation.computeAsSeenFrom(Denotations.scala:1134)
	dotty.tools.dotc.core.Denotations$SingleDenotation.computeAsSeenFrom(Denotations.scala:1087)
	dotty.tools.dotc.core.Denotations$PreDenotation.asSeenFrom(Denotations.scala:137)
	dotty.tools.dotc.core.SymDenotations$ClassDenotation.findMember(SymDenotations.scala:2216)
	dotty.tools.dotc.core.Types$Type.go$1(Types.scala:843)
	dotty.tools.dotc.core.Types$Type.findMember(Types.scala:1000)
	dotty.tools.dotc.core.Types$Type.memberBasedOnFlags(Types.scala:784)
	dotty.tools.dotc.core.Types$Type.member(Types.scala:768)
	dotty.tools.dotc.typer.Checking.checkNoModuleClash(Checking.scala:1119)
	dotty.tools.dotc.typer.Checking.checkNoModuleClash$(Checking.scala:945)
	dotty.tools.dotc.typer.Typer.checkNoModuleClash(Typer.scala:155)
	dotty.tools.dotc.typer.Typer.typedValDef(Typer.scala:2925)
	dotty.tools.dotc.typer.Typer.typedNamed$1(Typer.scala:3625)
	dotty.tools.dotc.typer.Typer.typedUnadapted(Typer.scala:3733)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3811)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3816)
	dotty.tools.dotc.typer.Typer.traverse$1(Typer.scala:3838)
	dotty.tools.dotc.typer.Typer.typedStats(Typer.scala:3884)
	dotty.tools.dotc.typer.Typer.typedClassDef(Typer.scala:3303)
	dotty.tools.dotc.typer.Typer.typedTypeOrClassDef$1(Typer.scala:3634)
	dotty.tools.dotc.typer.Typer.typedNamed$1(Typer.scala:3638)
	dotty.tools.dotc.typer.Typer.typedUnadapted(Typer.scala:3733)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3811)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3816)
	dotty.tools.dotc.typer.Typer.traverse$1(Typer.scala:3838)
	dotty.tools.dotc.typer.Typer.typedStats(Typer.scala:3884)
	dotty.tools.dotc.typer.Typer.typedPackageDef(Typer.scala:3436)
	dotty.tools.dotc.typer.Typer.typedUnnamed$1(Typer.scala:3680)
	dotty.tools.dotc.typer.Typer.typedUnadapted(Typer.scala:3734)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3811)
	dotty.tools.dotc.typer.Typer.typed(Typer.scala:3816)
	dotty.tools.dotc.typer.Typer.typedExpr(Typer.scala:3927)
	dotty.tools.dotc.typer.TyperPhase.typeCheck$$anonfun$1(TyperPhase.scala:47)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:15)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:10)
	dotty.tools.dotc.core.Phases$Phase.monitor(Phases.scala:510)
	dotty.tools.dotc.typer.TyperPhase.typeCheck(TyperPhase.scala:53)
	dotty.tools.dotc.typer.TyperPhase.$anonfun$4(TyperPhase.scala:99)
	scala.collection.Iterator$$anon$6.hasNext(Iterator.scala:479)
	scala.collection.Iterator$$anon$9.hasNext(Iterator.scala:583)
	scala.collection.immutable.List.prependedAll(List.scala:152)
	scala.collection.immutable.List$.from(List.scala:685)
	scala.collection.immutable.List$.from(List.scala:682)
	scala.collection.IterableOps$WithFilter.map(Iterable.scala:900)
	dotty.tools.dotc.typer.TyperPhase.runOn(TyperPhase.scala:98)
	dotty.tools.dotc.Run.runPhases$1$$anonfun$1(Run.scala:368)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:15)
	scala.runtime.function.JProcedure1.apply(JProcedure1.java:10)
	scala.collection.ArrayOps$.foreach$extension(ArrayOps.scala:1324)
	dotty.tools.dotc.Run.runPhases$1(Run.scala:361)
	dotty.tools.dotc.Run.compileUnits$$anonfun$1$$anonfun$2(Run.scala:408)
	dotty.tools.dotc.Run.compileUnits$$anonfun$1$$anonfun$adapted$1(Run.scala:408)
	scala.Function0.apply$mcV$sp(Function0.scala:42)
	dotty.tools.dotc.Run.showProgress(Run.scala:470)
	dotty.tools.dotc.Run.compileUnits$$anonfun$1(Run.scala:408)
	dotty.tools.dotc.Run.compileUnits$$anonfun$adapted$1(Run.scala:420)
	dotty.tools.dotc.util.Stats$.maybeMonitored(Stats.scala:69)
	dotty.tools.dotc.Run.compileUnits(Run.scala:420)
	dotty.tools.dotc.Run.compileSources(Run.scala:307)
	dotty.tools.dotc.interactive.InteractiveDriver.run(InteractiveDriver.scala:161)
	dotty.tools.pc.CachingDriver.run(CachingDriver.scala:45)
	dotty.tools.pc.WithCompilationUnit.<init>(WithCompilationUnit.scala:31)
	dotty.tools.pc.SimpleCollector.<init>(PcCollector.scala:357)
	dotty.tools.pc.PcSemanticTokensProvider$Collector$.<init>(PcSemanticTokensProvider.scala:63)
	dotty.tools.pc.PcSemanticTokensProvider.Collector$lzyINIT1(PcSemanticTokensProvider.scala:63)
	dotty.tools.pc.PcSemanticTokensProvider.Collector(PcSemanticTokensProvider.scala:63)
	dotty.tools.pc.PcSemanticTokensProvider.provide(PcSemanticTokensProvider.scala:88)
	dotty.tools.pc.ScalaPresentationCompiler.semanticTokens$$anonfun$1(ScalaPresentationCompiler.scala:155)
```
#### Short summary: 

java.lang.AssertionError: assertion failed