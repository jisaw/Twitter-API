<h1>Twitter-API</h1>
===========

Experiments using the twitter API
<h3>Syntax</h3>
<p>
Command line args should be as follows:<br><br><code>[python twit_search.py -q 'searches for these terms "and this as a phrase"' -l 100 --file nameOfMyFile -xml --method streaming]</code><br><br>
<h5>The -q Flag</h5> 
<p>This flag denotes the query to search twitter for. If it is a single word like 'iPhone' it can be passed without quotation marks. If it has more than one word it needs to be sorrounded with ''. If you want to search for an exact phrase you need to wrap that phrase in double quotes with single quotes around them. Ex. '"Searches phrase"'. If you want to use any special search characters like the :) or ? then the whole search needs to be in quotes. Ex. 'iphone 6 :)'.</p>
<br>
<h5>The -l Flag</h5>
<p>This flag lets us know the number of tweets you want returned. Ex. -l 100 will return 100 tweets.</p>
<br>
<h5>The --file Flag</h5>
<p>This flag gives a custom name to the output file. You do not need to include the filetype ending (.json or .xml), these are handled by the program.</p>
<br>
<h5>The -xml/-json Flag</h5>
<p>This is the flag that will determine the output file type. There are no args following this flag just use the flag as is. Ex. -xml.</p>
<br>
<h5>The --method Flag</h5>
<p>This is the flag the denotes wether the data will be collected from the twitter streaming API or the REST API. The two controls are '--method streaming' and '--method rest'.</p>
</p>
<h3>Dependancies</h3>
<ul>
<li>dicttoxml</li>
<li>Tweepy</li>
<li>json</li>
</ul>


