# generate zone lookup table with center points
insert into gare_st_lazare.zone_lookup select distinct(concat('bottom_', cast("id" as integer) )), geom, ST_Centroid(geom), 'bottom' from gare_st_lazare.lazare_bottom_floor_zone
