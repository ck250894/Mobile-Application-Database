# Mobile-Application-Database
This repository contains the python scripts and database design used to implement the database.

### Description of Python scripts:

create_table.py - Creating the table <br/>
bulk_load_table.py - Loading json data in bulk to the table <br/>
add_inverted_index.py - Creating inverted secondary index for different types of queries <br/>
delete_table.py - Deleting the table from DynamoDB <br/>
fetch_photo_and_reactions.py - Find photos and reactions on those photos for a particular user at a particular time <br/>
find_following_for_user.py - Find users following a particular user <br/>
find_and_enrich_following_for_user.py - It is similar to find_following_for_user.py but uses inverted index for querying <br/>
add_reaction.py - Adds reaction to a photo <br/>
follow_user.py - Uses two usernames where one is following the other <br/>
entities.py - Specifies metadata of the entities <br/>
fetch_user_and_photos.py - Finds photos for a specific user <br/>
