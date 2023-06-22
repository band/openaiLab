#! /usr/bin/env python

from transformers import pipeline

summarizer = pipeline(task="summarization")

text = "We tend to think of Christian nationalism, the political ideology based on the belief that the country's authentic identity lies in its Christian roots and in the perpetuation of Christian privilege, as having burst upon the scene to accompany and facilitate the rise of Donald Trump. But as Philip Gorski and Samuel Perry explain in *The Flag and the Cross*, Christian nationalism -- white Christian nationalism, to be more accurate, since the ideology has no place for nonwhites -- is \"one of the oldest and most powerful currents in American politics.\" They trace it back to the New England Puritans' wars against the indigenous groups who dared to stand in the way of the claim by self-described chosen people to their new Promised Land, and follow it through the Lost Cause of a post-Civil War South destined to \"rise again\" -- a Christological narrative of crucifixion and redemption \"crucial to understanding contemporary claims of Christian victimhood and vengeance among white Christian nationalists.\" The drive for western expansion, aptly known as Manifest Destiny, was widely understood as part of a divine plan handed to those who would \"civilize\" an entire continent."

summary = summarizer(text)

print(summary)
