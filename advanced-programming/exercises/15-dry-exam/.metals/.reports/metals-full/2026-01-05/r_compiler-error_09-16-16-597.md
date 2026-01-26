error id: 353F150696CC78FF50EB1AD548CDEBB9
file://<WORKSPACE>/Main.scala
### java.lang.AssertionError: assertion failed: asTerm called on not-a-Term val <none>

occurred in the presentation compiler.



action parameters:
offset: 9
uri: file://<WORKSPACE>/Main.scala
text:
```scala
object Ma@@

```


presentation compiler configuration:
Scala version: 3.7.2-bin-nonbootstrapped
Classpath:
<WORKSPACE>/.scala-build/15-dry-exam_53a8141c8c/classes/test [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala3-library_3/3.7.2/scala3-library_3-3.7.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scalacheck/scalacheck_3/1.19.0/scalacheck_3-1.19.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scalactic/scalactic_3/3.2.19/scalactic_3-3.2.19.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/typelevel/spire_3/0.18.0/spire_3-0.18.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/dev/optics/monocle-core_3/3.3.0/monocle-core_3-3.3.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/dev/optics/monocle-macro_3/3.3.0/monocle-macro_3-3.3.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.16/scala-library-2.13.16.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-sbt/test-interface/1.0/test-interface-1.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/typelevel/spire-macros_3/0.18.0/spire-macros_3-0.18.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/typelevel/spire-platform_3/0.18.0/spire-platform_3-0.18.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/typelevel/spire-util_3/0.18.0/spire-util_3-0.18.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/typelevel/algebra_3/2.8.0/algebra_3-2.8.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/typelevel/cats-core_3/2.12.0/cats-core_3-2.12.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/typelevel/cats-free_3/2.12.0/cats-free_3-2.12.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/typelevel/cats-kernel_3/2.12.0/cats-kernel_3-2.12.0.jar [exists ], <WORKSPACE>/.scala-build/15-dry-exam_53a8141c8c/classes/main [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/sourcegraph/semanticdb-javac/0.10.0/semanticdb-javac-0.10.0.jar [exists ], <WORKSPACE>/.scala-build/15-dry-exam_53a8141c8c/classes/main/META-INF/best-effort [missing ], <WORKSPACE>/.scala-build/15-dry-exam_53a8141c8c/classes/test/META-INF/best-effort [missing ]
Options:
-Xfatal-warnings -deprecation -feature -source:future -language:adhocExtensions -Xsemanticdb -sourceroot <WORKSPACE> -release 11 -Ywith-best-effort-tasty




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