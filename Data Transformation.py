import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node artist
artist_node1715858163462 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-spotify-sabarish/staging/artists.csv"], "recurse": True}, transformation_ctx="artist_node1715858163462")

# Script generated for node album
album_node1715858202590 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-spotify-sabarish/staging/albums.csv"], "recurse": True}, transformation_ctx="album_node1715858202590")

# Script generated for node tracks
tracks_node1715858236656 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-spotify-sabarish/staging/track.csv"], "recurse": True}, transformation_ctx="tracks_node1715858236656")

# Script generated for node Join Album & Artist
JoinAlbumArtist_node1715858262972 = Join.apply(frame1=album_node1715858202590, frame2=artist_node1715858163462, keys1=["artist_id"], keys2=["id"], transformation_ctx="JoinAlbumArtist_node1715858262972")

# Script generated for node Join with tracks
Joinwithtracks_node1715858333717 = Join.apply(frame1=tracks_node1715858236656, frame2=JoinAlbumArtist_node1715858262972, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Joinwithtracks_node1715858333717")

# Script generated for node Drop Fields
DropFields_node1715858418754 = DropFields.apply(frame=Joinwithtracks_node1715858333717, paths=["`.track_id`", "id"], transformation_ctx="DropFields_node1715858418754")

# Script generated for node Amazon S3
AmazonS3_node1715858947473 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1715858418754, connection_type="s3", format="glueparquet", connection_options={"path": "s3://project-spotify-sabarish/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1715858947473")

job.commit()
