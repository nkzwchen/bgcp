package hadoop;
import java.io.IOException;
import java.util.*;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
class Map extends MapReduceBase implements Mapper<LongWritable, Text, Text, DoubleWritable> {
   private Text word = new Text();
   public void map(LongWritable key,
               Text value,
               OutputCollector<Text, DoubleWritable> output,
               Reporter reporter)
         throws IOException {
      String line = value.toString();
      String arr[] = line.split("\\s+");
      word.set(arr[0] + " " + arr[1]);
      Double values = Double.valueOf(arr[2]);
      output.collect(word, new DoubleWritable(values));
    }
}
class Reduce extends MapReduceBase implements Reducer<Text, DoubleWritable, Text, DoubleWritable> {
   public void reduce(Text key,
                  Iterator<DoubleWritable> values,
                  OutputCollector<Text, DoubleWritable> output,
                  Reporter reporter)
         throws IOException {
      Double sum = 0.0;
      int count = 0;
      while (values.hasNext()) {
         sum += values.next().get();
         count++;
      }
      double avg = sum/count;
      output.collect(key, new DoubleWritable(avg));
   }
}
public class Avg {
   public static void main(String[] args) throws Exception {
      JobConf conf = new JobConf(Avg.class);
      conf.setJobName("Avg");
      conf.setOutputKeyClass(Text.class);
      conf.setOutputValueClass(DoubleWritable.class);
      conf.setMapperClass(Map.class);
      conf.setCombinerClass(Reduce.class);
      conf.setReducerClass(Reduce.class);
      conf.setInputFormat(TextInputFormat.class);
      conf.setOutputFormat(TextOutputFormat.class);
      FileInputFormat.setInputPaths(conf, new Path(args[0]));
      FileOutputFormat.setOutputPath(conf, new Path(args[1]));
      JobClient.runJob(conf);
   }
}
