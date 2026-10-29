## The solution

### Backend

For the backend functionality, I added sources with the link, a favicon for each link and  redacted the names, emails and phone numbers. 

With the link I replaced the ref tag with a href tag with the source link and the source name as the text to display for the link.

For the favicon I used a computed field and propery value to add the favicon url to the class object of source to use it in the content.tsx file.

I used regex for the phone numbers I checked all sets of numbers in 3 or less chunks. For the email I just replaced all words with the @ character in the list. This could be made more robust as there are a few edge cases where someone mistypes a @ symbol so maybe a regex to check for a .com or something similar maybe be better.

For the redacting of the names I hardcoded all the names into a list, so the question can check for names to redact this information going from full names first then to first and second. However I would have liked to not hardcode this information as in a real world application this creates a lot of effort, but maybe this information maybe stored in a database given peoples login or using the context to see if its a name.

### Frontend

Retrieved all needed information from the backend such as links, favicons and the redacted information.

Looped through each source to add its link and favicon. Added the links in bold and italic so it would stand out. Also added converted the href given in a string to actual html tag using `dangerouslySetInnerHTML={{ __html: content }}` to render the string of the href link.

Changed the css colour to a lighter colour so the favicons will show for the citizens advice website link.