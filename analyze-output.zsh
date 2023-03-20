# 2023-03-20
# analyze OpenAI query output:
#  - what documents in the repo contain terms in the query output?

for line in "${(@f)"$(<query-output-list.txt)"}"
{
echo $line
rg -l "$line" ~/Documents/myWikis/myMassiveTestWiki
}
