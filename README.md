# Random-Movie-Selector
*well i guess i'm bored*
<br>
Sadly it's a bit slow with all the request ...

## Usage
- Get your api key at https://www.themoviedb.org/settings/api
- See avalaible providers https://api.themoviedb.org/3/watch/providers/movie?language={lang}&watch_region={region}&api_key={key} *might do a tool for that*
- Make a providers list: Disney_Plus-Amazon_Prime_Video-Sixplay-France_TV-Arte-TF1-Amazon_Video <br>
`py main.py <key> <providers> <has_personnal_movie> <lang> [log]`

### Notes
has_personnal_movie: true or false, depend if you have movies on our computer, if on true please put all the movies in the same folder has the script
lang: FR, EN, DE ... use to filter movies in your region
log: send feedback of want the program is doing
