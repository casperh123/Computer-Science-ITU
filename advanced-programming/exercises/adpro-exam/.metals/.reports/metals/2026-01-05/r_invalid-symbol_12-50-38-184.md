error id: 23016EE710C3B88BB1C6C959C0DEDC1C
### scala.meta.internal.mtags.IndexingExceptions$InvalidSymbolException: _empty_/#

Symbol: _empty_/#

#### Error stacktrace:

```
scala.meta.internal.mtags.OnDemandSymbolIndex.definitions(OnDemandSymbolIndex.scala:61)
	scala.meta.internal.metals.DestinationProvider.definition(DefinitionProvider.scala:469)
	scala.meta.internal.metals.DestinationProvider.fromSymbol(DefinitionProvider.scala:507)
	scala.meta.internal.metals.DestinationProvider.fromSymbol(DefinitionProvider.scala:550)
	scala.meta.internal.metals.DefinitionProvider.fromSymbol(DefinitionProvider.scala:186)
	scala.meta.internal.metals.StacktraceAnalyzer.findLocationForSymbol$1(StacktraceAnalyzer.scala:81)
	scala.meta.internal.metals.StacktraceAnalyzer.$anonfun$fileLocationFromLine$2(StacktraceAnalyzer.scala:89)
	scala.PartialFunction$Unlifted.applyOrElse(PartialFunction.scala:358)
	scala.collection.IterableOnceOps.collectFirst(IterableOnce.scala:1279)
	scala.collection.IterableOnceOps.collectFirst$(IterableOnce.scala:1271)
	scala.collection.AbstractIterable.collectFirst(Iterable.scala:936)
	scala.meta.internal.metals.StacktraceAnalyzer.$anonfun$fileLocationFromLine$1(StacktraceAnalyzer.scala:89)
	scala.Option.flatMap(Option.scala:283)
	scala.meta.internal.metals.StacktraceAnalyzer.fileLocationFromLine(StacktraceAnalyzer.scala:87)
	scala.meta.internal.metals.StacktraceAnalyzer.workspaceFileLocationFromLine(StacktraceAnalyzer.scala:73)
	scala.meta.internal.metals.debug.DebugProxy.$anonfun$modifyLocationInTests$3(DebugProxy.scala:316)
	scala.collection.Iterator$$anon$10.nextCur(Iterator.scala:604)
	scala.collection.Iterator$$anon$10.hasNext(Iterator.scala:618)
	scala.collection.Iterator$$anon$10.hasNext(Iterator.scala:610)
	scala.meta.internal.mtags.MtagsEnrichments$XtensionIteratorCollection.headOption(MtagsEnrichments.scala:32)
	scala.meta.internal.metals.debug.DebugProxy.$anonfun$modifyLocationInTests$1(DebugProxy.scala:320)
	scala.collection.StrictOptimizedIterableOps.map(StrictOptimizedIterableOps.scala:100)
	scala.collection.StrictOptimizedIterableOps.map$(StrictOptimizedIterableOps.scala:87)
	scala.collection.convert.JavaCollectionWrappers$JListWrapper.map(JavaCollectionWrappers.scala:138)
	scala.meta.internal.metals.debug.DebugProxy.modifyLocationInTests(DebugProxy.scala:308)
	scala.meta.internal.metals.debug.DebugProxy.$anonfun$handleServerMessage$1(DebugProxy.scala:284)
	scala.meta.internal.metals.debug.DebugProxy.$anonfun$handleServerMessage$1$adapted(DebugProxy.scala:241)
	scala.meta.internal.metals.debug.ServerAdapter.$anonfun$onReceived$1(ServerAdapter.scala:25)
	scala.meta.internal.metals.debug.MessageIdAdapter.$anonfun$listen$1(MessageIdAdapter.scala:57)
	org.eclipse.lsp4j.jsonrpc.json.StreamMessageProducer.handleMessage(StreamMessageProducer.java:185)
	org.eclipse.lsp4j.jsonrpc.json.StreamMessageProducer.listen(StreamMessageProducer.java:97)
	scala.meta.internal.metals.debug.SocketEndpoint.listen(SocketEndpoint.scala:38)
	scala.meta.internal.metals.debug.MessageIdAdapter.listen(MessageIdAdapter.scala:47)
	scala.meta.internal.metals.debug.ServerAdapter.onReceived(ServerAdapter.scala:18)
	scala.meta.internal.metals.debug.DebugProxy.$anonfun$listenToServer$1(DebugProxy.scala:92)
	scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.scala:18)
	scala.concurrent.Future$.$anonfun$apply$1(Future.scala:691)
	scala.concurrent.impl.Promise$Transformation.run(Promise.scala:500)
	java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144)
	java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642)
	java.base/java.lang.Thread.run(Thread.java:1583)
```
#### Short summary: 

scala.meta.internal.mtags.IndexingExceptions$InvalidSymbolException: _empty_/#