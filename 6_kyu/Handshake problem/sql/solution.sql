--# write your SQL statement here:
-- you are given a table 'participants' with column 'n' (number of handshakes).
-- return a table with this column and your result in a column named 'res'.

-- n = res*(res-1)/ 2 -> res = (1 + sqrt(8*n + 1))/2
select n,
  case
    when n = 0 then 0
    when n = 1 then 2
    when n = 2 then 3
    else cast(ceiling((1 + sqrt(8*n + 1))/2) as int)
  end as res
from participants