# generate zone lookup table with center points
insert into gare_st_lazare.zone_lookup select distinct(concat('bottom_', cast("id" as integer) )), geom, ST_Centroid(geom), 'bottom' from gare_st_lazare.lazare_bottom_floor_zone

# get all duplicated rows in survey
select distinct(survey_code), 'you have uploaded multiple duplicated questionnaires' as Reject
from gare_st_lazare.survey a
  join ( select point0, point1
           from gare_st_lazare.survey 
          group by point0, point1 
         having count(*) > 1 ) b
    on a.point0 = b.point0
   and a.point1 = b.point1

# import into excel, four arguements, 1. insert column, 2. area to look for 3. which column in (2 4.false means exact match
=VLOOKUP(AB7, $AF$1:$AG$25, 1, 0)

# Then delete
delete from gare_st_lazare.survey
where survey_code in 

(select distinct(survey_code) as Reject
from gare_st_lazare.survey a
  join ( select point0, point1
           from gare_st_lazare.survey 
          group by point0, point1 
         having count(*) > 1 ) b
    on a.point0 = b.point0
   and a.point1 = b.point1)

