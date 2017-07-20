#!/usr/bin/env python

# ATTENTION!
# Please do not manually edit the contents of this file
# Only use the web interface for editing
# Otherwise, the file may no longer be editable using the web interface, or you changes may be lost

# Copyright (c) 2017 mindsensors.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com

"""
--BLOCKLY FILE--
--START BLOCKS--
PHhtbCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PGJsb2NrIHR5cGU9InNjcmVlbl9kcmF3Y2lyY2xlIiBpZD0ibUlNa0FWKX17Yik6YjQ5My9pNDkiIHg9Ii03IiB5PSItMzgxIj48ZmllbGQgbmFtZT0iQ09MT1IiPiNmZmNjMDA8L2ZpZWxkPjxmaWVsZCBuYW1lPSJESVNQTEFZIj5UUlVFPC9maWVsZD48dmFsdWUgbmFtZT0ieCI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IntifHE4UVNuKk47cEkuaTMoLklFIj48ZmllbGQgbmFtZT0iTlVNIj40MDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0ieSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IkpgM0hvSiEzNlhKVE02Q2d4TS50Ij48ZmllbGQgbmFtZT0iTlVNIj40MDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0icmFkaXVzIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0ieGtIQl5yOl9VX0V2UWBgNW9+Wm0iPjxmaWVsZCBuYW1lPSJOVU0iPjI1PC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjxuZXh0PjxibG9jayB0eXBlPSJjb250cm9sc19mb3IiIGlkPSI6WDVwQU5pRS5seXNhazFiYz1ydSI+PGZpZWxkIG5hbWU9IlZBUiI+aTwvZmllbGQ+PHZhbHVlIG5hbWU9IkZST00iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJPZ3ZuNEUhTUE0altrWFlSc2w4RCI+PGZpZWxkIG5hbWU9Ik5VTSI+MDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0iVE8iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJbcmZdSH4qMTdSYGtDfGBXR2swdiI+PGZpZWxkIG5hbWU9Ik5VTSI+MTI8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PHZhbHVlIG5hbWU9IkJZIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iZUsyYkJjV1pMVHBwLj1EcDlBZEIiPjxmaWVsZCBuYW1lPSJOVU0iPjE8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PHN0YXRlbWVudCBuYW1lPSJETyI+PGJsb2NrIHR5cGU9InRleHRfcHJpbnQiIGlkPSJoIUlxKHNZWmtXJUJwbEFyfTVRSCI+PHZhbHVlIG5hbWU9IlRFWFQiPjxzaGFkb3cgdHlwZT0idGV4dCIgaWQ9IkMoJTg6LWFiMVc2NE4zezgvfjt2Ij48ZmllbGQgbmFtZT0iVEVYVCI+YWJjPC9maWVsZD48L3NoYWRvdz48YmxvY2sgdHlwZT0idGV4dF9qb2luIiBpZD0iQFhTYmwrU0dGbFdCd3BGL3kjbWgiIGlubGluZT0idHJ1ZSI+PG11dGF0aW9uIGl0ZW1zPSIzIj48L211dGF0aW9uPjx2YWx1ZSBuYW1lPSJBREQwIj48YmxvY2sgdHlwZT0idmFyaWFibGVzX2dldCIgaWQ9InFVUiVuc1owNHQtOUgyPUYrWytZIj48ZmllbGQgbmFtZT0iVkFSIj5pPC9maWVsZD48L2Jsb2NrPjwvdmFsdWU+PHZhbHVlIG5hbWU9IkFERDEiPjxibG9jayB0eXBlPSJ0ZXh0IiBpZD0iWmxUMCxyUkJvQm5oblhGMV1rQmYiPjxmaWVsZCBuYW1lPSJURVhUIj46IDwvZmllbGQ+PC9ibG9jaz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJBREQyIj48YmxvY2sgdHlwZT0icHJvY2VkdXJlc19jYWxscmV0dXJuIiBpZD0iKighRE9lelNpN2pzcTtZTm94YUMiIGlubGluZT0idHJ1ZSI+PG11dGF0aW9uIG5hbWU9ImZpYm9uYWNjaSI+PGFyZyBuYW1lPSJ4Ij48L2FyZz48L211dGF0aW9uPjx2YWx1ZSBuYW1lPSJBUkcwIj48YmxvY2sgdHlwZT0idmFyaWFibGVzX2dldCIgaWQ9IlJTUWR4N3E4aF5TYDJwPTt1Iy9NIj48ZmllbGQgbmFtZT0iVkFSIj5pPC9maWVsZD48L2Jsb2NrPjwvdmFsdWU+PC9ibG9jaz48L3ZhbHVlPjwvYmxvY2s+PC92YWx1ZT48bmV4dD48YmxvY2sgdHlwZT0ic2NyZWVuX2RyYXdjaXJjbGUiIGlkPSJCRCssXzQ3NyVQMU0oSy1PMCx0NSI+PGZpZWxkIG5hbWU9IkNPTE9SIj4jZmYwMDAwPC9maWVsZD48ZmllbGQgbmFtZT0iRElTUExBWSI+VFJVRTwvZmllbGQ+PHZhbHVlIG5hbWU9IngiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJydU9ndXwsLWsobTluTk5YKTdKTSI+PGZpZWxkIG5hbWU9Ik5VTSI+MTA8L2ZpZWxkPjwvc2hhZG93PjxibG9jayB0eXBlPSJwcm9jZWR1cmVzX2NhbGxyZXR1cm4iIGlkPSJMdHQ3cSE/S1VjdzJxN0lsa3J9eiIgaW5saW5lPSJ0cnVlIj48bXV0YXRpb24gbmFtZT0iZmlib25hY2NpIj48YXJnIG5hbWU9IngiPjwvYXJnPjwvbXV0YXRpb24+PHZhbHVlIG5hbWU9IkFSRzAiPjxibG9jayB0eXBlPSJ2YXJpYWJsZXNfZ2V0IiBpZD0iVUcqVik1Qyp1XU8lczFhZyEudVsiPjxmaWVsZCBuYW1lPSJWQVIiPmk8L2ZpZWxkPjwvYmxvY2s+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PHZhbHVlIG5hbWU9InkiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJqeyNoLTgydVFUOFpAaCFNb1VDbSI+PGZpZWxkIG5hbWU9Ik5VTSI+MTA8L2ZpZWxkPjwvc2hhZG93PjxibG9jayB0eXBlPSJwcm9jZWR1cmVzX2NhbGxyZXR1cm4iIGlkPSJjVn1lXnZNP2ZHd019NDhEfSkhRCIgaW5saW5lPSJ0cnVlIj48bXV0YXRpb24gbmFtZT0iZmlib25hY2NpIj48YXJnIG5hbWU9IngiPjwvYXJnPjwvbXV0YXRpb24+PHZhbHVlIG5hbWU9IkFSRzAiPjxibG9jayB0eXBlPSJ2YXJpYWJsZXNfZ2V0IiBpZD0ia2d4fSlvPyNlZyVLUHtTNV47I1siPjxmaWVsZCBuYW1lPSJWQVIiPmk8L2ZpZWxkPjwvYmxvY2s+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PHZhbHVlIG5hbWU9InJhZGl1cyI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9Ino/dUN4Y0BVRykrKzBoW1tIPX5bIj48ZmllbGQgbmFtZT0iTlVNIj41PC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC9uZXh0PjwvYmxvY2s+PC9zdGF0ZW1lbnQ+PG5leHQ+PGJsb2NrIHR5cGU9InN5c3RlbV93YWl0Zm9ya2V5cHJlc3MiIGlkPSI5LStTSHhlM1dBQTBicEV4d2ZgLCI+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48YmxvY2sgdHlwZT0icHJvY2VkdXJlc19kZWZyZXR1cm4iIGlkPSJHbCh2ZG4qX0Q3QD1tNkhtcHpBayIgeD0iLTkiIHk9IjE0MiI+PG11dGF0aW9uPjxhcmcgbmFtZT0ieCI+PC9hcmc+PC9tdXRhdGlvbj48ZmllbGQgbmFtZT0iTkFNRSI+Zmlib25hY2NpPC9maWVsZD48Y29tbWVudCBwaW5uZWQ9ImZhbHNlIiBoPSI4MCIgdz0iMTYwIj5EZXNjcmliZSB0aGlzIGZ1bmN0aW9uLi4uPC9jb21tZW50PjxzdGF0ZW1lbnQgbmFtZT0iU1RBQ0siPjxibG9jayB0eXBlPSJwcm9jZWR1cmVzX2lmcmV0dXJuIiBpZD0iYD19LWdHb187RHUrWkV3JUA6RzoiPjxtdXRhdGlvbiB2YWx1ZT0iMSI+PC9tdXRhdGlvbj48dmFsdWUgbmFtZT0iQ09ORElUSU9OIj48YmxvY2sgdHlwZT0ibG9naWNfY29tcGFyZSIgaWQ9IltxU1dOIyoyJWBHRy1IVUNQVGE5Ij48ZmllbGQgbmFtZT0iT1AiPkxURTwvZmllbGQ+PHZhbHVlIG5hbWU9IkEiPjxibG9jayB0eXBlPSJ2YXJpYWJsZXNfZ2V0IiBpZD0iX1l4IXpeMj9UJVo2YWoteFRRVW0iPjxmaWVsZCBuYW1lPSJWQVIiPng8L2ZpZWxkPjwvYmxvY2s+PC92YWx1ZT48dmFsdWUgbmFtZT0iQiI+PGJsb2NrIHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iXXJkcHhbUSksTVt1czdaTGd6XW4iPjxmaWVsZCBuYW1lPSJOVU0iPjE8L2ZpZWxkPjwvYmxvY2s+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PHZhbHVlIG5hbWU9IlZBTFVFIj48YmxvY2sgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJ8bD9PZEJEeHlQcj9LSGl3K1tgVSI+PGZpZWxkIG5hbWU9Ik5VTSI+MTwvZmllbGQ+PC9ibG9jaz48L3ZhbHVlPjwvYmxvY2s+PC9zdGF0ZW1lbnQ+PHZhbHVlIG5hbWU9IlJFVFVSTiI+PGJsb2NrIHR5cGU9Im1hdGhfYXJpdGhtZXRpYyIgaWQ9ImJYb0xpNj0yIU9mS3tHZ3M6QilLIiBpbmxpbmU9ImZhbHNlIj48ZmllbGQgbmFtZT0iT1AiPkFERDwvZmllbGQ+PHZhbHVlIG5hbWU9IkEiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJeOXU0bkE0Xl5id1dCOylfUWhbViI+PGZpZWxkIG5hbWU9Ik5VTSI+MTwvZmllbGQ+PC9zaGFkb3c+PGJsb2NrIHR5cGU9InByb2NlZHVyZXNfY2FsbHJldHVybiIgaWQ9IiFaWkolczZrU1J4Uzd3bzRubXslIiBpbmxpbmU9InRydWUiPjxtdXRhdGlvbiBuYW1lPSJmaWJvbmFjY2kiPjxhcmcgbmFtZT0ieCI+PC9hcmc+PC9tdXRhdGlvbj48dmFsdWUgbmFtZT0iQVJHMCI+PGJsb2NrIHR5cGU9Im1hdGhfYXJpdGhtZXRpYyIgaWQ9IlJeLldwQEtZWyVYKEA7MlM3a01aIj48ZmllbGQgbmFtZT0iT1AiPk1JTlVTPC9maWVsZD48dmFsdWUgbmFtZT0iQSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IlNqVCo1Zi9BTkJhV313V2E4WFI7Ij48ZmllbGQgbmFtZT0iTlVNIj4xPC9maWVsZD48L3NoYWRvdz48YmxvY2sgdHlwZT0idmFyaWFibGVzX2dldCIgaWQ9Int1OXFga2E1Zz9VOmUvVzZaYFJHIj48ZmllbGQgbmFtZT0iVkFSIj54PC9maWVsZD48L2Jsb2NrPjwvdmFsdWU+PHZhbHVlIG5hbWU9IkIiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSIpP0hZU3g6dkglOGhJKkEveioxMyI+PGZpZWxkIG5hbWU9Ik5VTSI+MjwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PC9ibG9jaz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJCIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iaTMxUktobXx9MW1tI1JEZWBNflUiPjxmaWVsZCBuYW1lPSJOVU0iPjE8L2ZpZWxkPjwvc2hhZG93PjxibG9jayB0eXBlPSJwcm9jZWR1cmVzX2NhbGxyZXR1cm4iIGlkPSIyS0lXUH1GNWY1ck0wdnJ6RURmdSIgaW5saW5lPSJ0cnVlIj48bXV0YXRpb24gbmFtZT0iZmlib25hY2NpIj48YXJnIG5hbWU9IngiPjwvYXJnPjwvbXV0YXRpb24+PHZhbHVlIG5hbWU9IkFSRzAiPjxibG9jayB0eXBlPSJtYXRoX2FyaXRobWV0aWMiIGlkPSJFODMtW09FaHl4OFtJSXA0LTY5SyI+PGZpZWxkIG5hbWU9Ik9QIj5NSU5VUzwvZmllbGQ+PHZhbHVlIG5hbWU9IkEiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJTalQqNWYvQU5CYVd9d1dhOFhSOyI+PGZpZWxkIG5hbWU9Ik5VTSI+MTwvZmllbGQ+PC9zaGFkb3c+PGJsb2NrIHR5cGU9InZhcmlhYmxlc19nZXQiIGlkPSI0dXBGeno4THdJQyw7R2J4LG4uMyI+PGZpZWxkIG5hbWU9IlZBUiI+eDwvZmllbGQ+PC9ibG9jaz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJCIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iQUtQYHgweWI5a3IzUTtsdn5aczUiPjxmaWVsZCBuYW1lPSJOVU0iPjE8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PC9ibG9jaz48L3ZhbHVlPjwvYmxvY2s+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PC9ibG9jaz48L3htbD4=
5df5a51910ea114a4edd737793179a6bb4e4a3a9e24aa1cf40da97e23a38e0d6
--END BLOCKS--
"""


from PiStorms import PiStorms
from PiStorms_GRX import PiStorms_GRX

x = None
i = None

psm = PiStorms()

grx = PiStorms_GRX()

"""Describe this function...
"""
def fibonacci(x):
  if x <= 1:
    return 1
  return fibonacci(x - 2) + fibonacci(x - 1)


psm.screen.fillCircle(40, 40, 25, (255, 204, 0), display = True)
for i in range(13):
  print(''.join([str(x2) for x2 in [i, ': ', fibonacci(i)]]))
  psm.screen.fillCircle((fibonacci(i)), (fibonacci(i)), 5, (255, 0, 0), display = True)
grx.waitForKeyPress()
