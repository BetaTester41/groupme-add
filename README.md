# GroupMe Bulk Add
Useful for clubs that use GroupMe for communications, or just for SMS broadcasting...

## Getting your "Access Token"
1. Head to the [developer page](https://dev.groupme.com/).
2. Login to the account that owns the group you want to automate.
3. Click the "Access Token" button next to the your name.
4. There is no step 4.

## Getting you Group ID
1. Fire up that terminal!
2. Fetch all your group info with this command:<br>
`curl https://api.groupme.com/v3/groups?token=YOUR_TOKEN`<br>
(please remember to replace YOUR_TOKEN)
3. Find the group you want, and copy the "id" value
4. Easy right?

## PRs?
Yes please! If you have any cool stuff to add, send me a PR (or 2)!