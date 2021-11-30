```scala
val file = sc.textFile("hdfs://nn:9000/data/")
var result = sc.makeRDD(file.map(_.split("\\s+"))
                        .map(word => (word(0) + "  " + word(1), word(2).toDouble))
                        .groupByKey()
                      .map( x => {  
                        var max = 0.0
                        var min = 0.0
                          for(num <- x._2){
                              if(num > max)
                                  max = num
                              }
                          (x._1, max, min)
                      }).collect()).toDF()
result.coalesce(1).write.option("delimiter", "\t").format("csv").save("hdfs://nn:9000/MAXoutput/")
```
