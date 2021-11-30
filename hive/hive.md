```sql
create database Metric;

use Metric;

create table if not exists metric(D string,K string, V double)  
row format delimited fields terminated by '\t'  
lines terminated by '\n';

load data inpath '/data/metric.txt' into table metric;


insert overwrite directory "/hiveout"
row format delimited fields terminated by "\t"
SELECT D,K,percentile_approx(V,0.25), percentile_approx(V,0.5), percentile_approx(V,0.75)from metric group by D,K;
```
