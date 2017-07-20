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
PHhtbCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PGJsb2NrIHR5cGU9InN5c3RlbV91bnRpbGtleXByZXNzIiBpZD0iMy83Uzo9NylvZytvaGkwc05mSVgiIHg9IjExNiIgeT0iMjIiPjxzdGF0ZW1lbnQgbmFtZT0iZnVuYyI+PGJsb2NrIHR5cGU9InNjcmVlbl9kcmF3Y2lyY2xlIiBpZD0iQz9GK3t4R3EuQC9lKms2aX1AW24iPjxmaWVsZCBuYW1lPSJDT0xPUiI+I2ZmMDAwMDwvZmllbGQ+PGZpZWxkIG5hbWU9IkRJU1BMQVkiPlRSVUU8L2ZpZWxkPjx2YWx1ZSBuYW1lPSJ4Ij48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0ifj9sLGJqZXFBUHJHNH1OJWBzL3EiPjxmaWVsZCBuYW1lPSJOVU0iPjEwPC9maWVsZD48L3NoYWRvdz48YmxvY2sgdHlwZT0ibWF0aF9yYW5kb21faW50IiBpZD0iMjJud2ZGc00tZ2tLTFQ9Wk59RnUiIGNvbGxhcHNlZD0idHJ1ZSI+PHZhbHVlIG5hbWU9IkZST00iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJ0eE14bjJyZHp2UnYjNlt4ZihhfSI+PGZpZWxkIG5hbWU9Ik5VTSI+MzA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PHZhbHVlIG5hbWU9IlRPIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iTj99VT1ndiVQend7T2hMUH1+eFAiPjxmaWVsZCBuYW1lPSJOVU0iPjIwMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PHZhbHVlIG5hbWU9InkiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJtUn1zeVdxb1Y/eXxzQkJKXTZ4RiI+PGZpZWxkIG5hbWU9Ik5VTSI+MTA8L2ZpZWxkPjwvc2hhZG93PjxibG9jayB0eXBlPSJtYXRoX3JhbmRvbV9pbnQiIGlkPSJabC97V3AodVk9bH4sXSk4dDtrOCIgY29sbGFwc2VkPSJ0cnVlIj48dmFsdWUgbmFtZT0iRlJPTSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IkwrQHg2byhJeF5SOztWM3YuQztsIj48ZmllbGQgbmFtZT0iTlVNIj4zMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0iVE8iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSIxM15qLmR6TmxdNX0oMk9gWU1VSyI+PGZpZWxkIG5hbWU9Ik5VTSI+MjAwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC92YWx1ZT48dmFsdWUgbmFtZT0icmFkaXVzIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iRnRkbnxzWnZ2ZjVMeipVLjZbNz8iPjxmaWVsZCBuYW1lPSJOVU0iPjI1PC9maWVsZD48L3NoYWRvdz48YmxvY2sgdHlwZT0ibWF0aF9yYW5kb21faW50IiBpZD0iSH47XklyPypeeGpoW0Rufi86YywiIGNvbGxhcHNlZD0idHJ1ZSI+PHZhbHVlIG5hbWU9IkZST00iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJGZU9jKlRpcFMoY3RqI08wa2heMSI+PGZpZWxkIG5hbWU9Ik5VTSI+MzA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PHZhbHVlIG5hbWU9IlRPIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iN28heGBGfTRuMX1qNl4rI2N9dDAiPjxmaWVsZCBuYW1lPSJOVU0iPjc1PC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC92YWx1ZT48bmV4dD48YmxvY2sgdHlwZT0ic2NyZWVuX2RyYXdjaXJjbGUiIGlkPSJJVTlaI1pdOkxhSmdQZ3VweyNedSI+PGZpZWxkIG5hbWU9IkNPTE9SIj4jZmZmZjAwPC9maWVsZD48ZmllbGQgbmFtZT0iRElTUExBWSI+VFJVRTwvZmllbGQ+PHZhbHVlIG5hbWU9IngiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJ+P2wsYmplcUFQckc0fU4lYHMvcSI+PGZpZWxkIG5hbWU9Ik5VTSI+MTA8L2ZpZWxkPjwvc2hhZG93PjxibG9jayB0eXBlPSJtYXRoX3JhbmRvbV9pbnQiIGlkPSI9OmRsRVNRYnotWS1SNip4ZUg/MiIgY29sbGFwc2VkPSJ0cnVlIj48dmFsdWUgbmFtZT0iRlJPTSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9Imw9fTlITkQlUnstV0RORmhJS0A2Ij48ZmllbGQgbmFtZT0iTlVNIj4zMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0iVE8iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJmOW9jPz1CZ2BHR3dhMn4oUzIvZCI+PGZpZWxkIG5hbWU9Ik5VTSI+MjUwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC92YWx1ZT48dmFsdWUgbmFtZT0ieSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9Im1SfXN5V3FvVj95fHNCQkpdNnhGIj48ZmllbGQgbmFtZT0iTlVNIj4xMDwvZmllbGQ+PC9zaGFkb3c+PGJsb2NrIHR5cGU9Im1hdGhfcmFuZG9tX2ludCIgaWQ9Ijt6bX5aM3VJISwzcVg4fmd4Mys9IiBjb2xsYXBzZWQ9InRydWUiPjx2YWx1ZSBuYW1lPSJGUk9NIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0idEYlZytpOmoxI2R2N31WP2d9flsiPjxmaWVsZCBuYW1lPSJOVU0iPjMwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJUTyI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IlUjLkhbVnlrdTcrcy58Y2BpX2xSIj48ZmllbGQgbmFtZT0iTlVNIj4yNTA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PC9ibG9jaz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJyYWRpdXMiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJGdGRufHNadnZmNUx6KlUuNls3PyI+PGZpZWxkIG5hbWU9Ik5VTSI+MjU8L2ZpZWxkPjwvc2hhZG93PjxibG9jayB0eXBlPSJtYXRoX3JhbmRvbV9pbnQiIGlkPSIweDRoeUs/T14tKU1aZ2hDMil0fiIgY29sbGFwc2VkPSJ0cnVlIj48dmFsdWUgbmFtZT0iRlJPTSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IltCNll3eng0M0N9TUlLYn46Vjo4Ij48ZmllbGQgbmFtZT0iTlVNIj4zMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0iVE8iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJubjQ6L0VpYz9uTypiSz12a2ZzWCI+PGZpZWxkIG5hbWU9Ik5VTSI+MTAwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC92YWx1ZT48bmV4dD48YmxvY2sgdHlwZT0ic2NyZWVuX2RyYXdjaXJjbGUiIGlkPSJad3szfng3NzNJaEwyW1dtUnhLaiI+PGZpZWxkIG5hbWU9IkNPTE9SIj4jMzNmZjMzPC9maWVsZD48ZmllbGQgbmFtZT0iRElTUExBWSI+VFJVRTwvZmllbGQ+PHZhbHVlIG5hbWU9IngiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJ+P2wsYmplcUFQckc0fU4lYHMvcSI+PGZpZWxkIG5hbWU9Ik5VTSI+MTA8L2ZpZWxkPjwvc2hhZG93PjxibG9jayB0eXBlPSJtYXRoX3JhbmRvbV9pbnQiIGlkPSJNOS1xXWNBMGRCLDdJd2UtblMvayIgY29sbGFwc2VkPSJ0cnVlIj48dmFsdWUgbmFtZT0iRlJPTSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9Im1DXTFLZko7ZEcjKDg7UDFwU3pnIj48ZmllbGQgbmFtZT0iTlVNIj4zMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0iVE8iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJEfHZISUM/KGhuLHpxOkNOfmR7MiI+PGZpZWxkIG5hbWU9Ik5VTSI+MzAwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjwvYmxvY2s+PC92YWx1ZT48dmFsdWUgbmFtZT0ieSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9Im1SfXN5V3FvVj95fHNCQkpdNnhGIj48ZmllbGQgbmFtZT0iTlVNIj4xMDwvZmllbGQ+PC9zaGFkb3c+PGJsb2NrIHR5cGU9Im1hdGhfcmFuZG9tX2ludCIgaWQ9Il4re0tkTnhIQHN5eEtKX1UjUmA5IiBjb2xsYXBzZWQ9InRydWUiPjx2YWx1ZSBuYW1lPSJGUk9NIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iSEBaS24yckNKSVExM2Q6XlA6MEciPjxmaWVsZCBuYW1lPSJOVU0iPjMwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJUTyI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IjVLUzdxMERdfnBYOnp8K2ZfMzUoIj48ZmllbGQgbmFtZT0iTlVNIj4zMDA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PC9ibG9jaz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJyYWRpdXMiPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJGdGRufHNadnZmNUx6KlUuNls3PyI+PGZpZWxkIG5hbWU9Ik5VTSI+MjU8L2ZpZWxkPjwvc2hhZG93PjxibG9jayB0eXBlPSJtYXRoX3JhbmRvbV9pbnQiIGlkPSJxVkBdRGY1NSFhOjB2cisxck9xSCIgY29sbGFwc2VkPSJ0cnVlIj48dmFsdWUgbmFtZT0iRlJPTSI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9Iitmb083LyhEfi1WJSVVSzk5UkVvIj48ZmllbGQgbmFtZT0iTlVNIj4zMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48dmFsdWUgbmFtZT0iVE8iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSIjYC5jMTZ9e0JedWlOT3Fmck9FWCI+PGZpZWxkIG5hbWU9Ik5VTSI+NjA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PC9ibG9jaz48L3ZhbHVlPjxuZXh0PjxibG9jayB0eXBlPSJzY3JlZW5fZHJhd2NpcmNsZSIgaWQ9InhuLG5IUHJrVyVlZEJTYTZQc0UsIj48ZmllbGQgbmFtZT0iQ09MT1IiPiMzM2NjZmY8L2ZpZWxkPjxmaWVsZCBuYW1lPSJESVNQTEFZIj5UUlVFPC9maWVsZD48dmFsdWUgbmFtZT0ieCI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9In4/bCxiamVxQVByRzR9TiVgcy9xIj48ZmllbGQgbmFtZT0iTlVNIj4xMDwvZmllbGQ+PC9zaGFkb3c+PGJsb2NrIHR5cGU9Im1hdGhfcmFuZG9tX2ludCIgaWQ9Ii5hfWw9YjpKcG5FJSsuTGRTUFJNIiBjb2xsYXBzZWQ9InRydWUiPjx2YWx1ZSBuYW1lPSJGUk9NIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iQiNIYFBYWk5AKFc0N00hUHByPzEiPjxmaWVsZCBuYW1lPSJOVU0iPjgwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJUTyI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IlVfRjF8XT1UVntfLzpNZltaXmR1Ij48ZmllbGQgbmFtZT0iTlVNIj4zMDA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PC9ibG9jaz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJ5Ij48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0ibVJ9c3lXcW9WP3l8c0JCSl02eEYiPjxmaWVsZCBuYW1lPSJOVU0iPjEwPC9maWVsZD48L3NoYWRvdz48YmxvY2sgdHlwZT0ibWF0aF9yYW5kb21faW50IiBpZD0idV5EakJvSlhWMVpLXm1jaCpue3MiIGNvbGxhcHNlZD0idHJ1ZSI+PHZhbHVlIG5hbWU9IkZST00iPjxzaGFkb3cgdHlwZT0ibWF0aF9udW1iZXIiIGlkPSJzZTRuP2suNk8wYGtjZVMlT11mTyI+PGZpZWxkIG5hbWU9Ik5VTSI+NzA8L2ZpZWxkPjwvc2hhZG93PjwvdmFsdWU+PHZhbHVlIG5hbWU9IlRPIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0ifG5ya044WzEhVll8R0ReViwxQDIiPjxmaWVsZCBuYW1lPSJOVU0iPjMwMDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PHZhbHVlIG5hbWU9InJhZGl1cyI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IkZ0ZG58c1p2dmY1THoqVS42Wzc/Ij48ZmllbGQgbmFtZT0iTlVNIj4yNTwvZmllbGQ+PC9zaGFkb3c+PGJsb2NrIHR5cGU9Im1hdGhfcmFuZG9tX2ludCIgaWQ9IkZuOnVQeS8/LV5SRVdWdXglSTYxIiBjb2xsYXBzZWQ9InRydWUiPjx2YWx1ZSBuYW1lPSJGUk9NIj48c2hhZG93IHR5cGU9Im1hdGhfbnVtYmVyIiBpZD0iIz9pWUkrTyFuKS96fjlNdihnM0IiPjxmaWVsZCBuYW1lPSJOVU0iPjUwPC9maWVsZD48L3NoYWRvdz48L3ZhbHVlPjx2YWx1ZSBuYW1lPSJUTyI+PHNoYWRvdyB0eXBlPSJtYXRoX251bWJlciIgaWQ9IlQ2XX46cFllanVbNlEpWFlCW2A9Ij48ZmllbGQgbmFtZT0iTlVNIj45MDwvZmllbGQ+PC9zaGFkb3c+PC92YWx1ZT48L2Jsb2NrPjwvdmFsdWU+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L25leHQ+PC9ibG9jaz48L3N0YXRlbWVudD48L2Jsb2NrPjwveG1sPg==
6ef37548816e7b3fe50fe4fb79ed26b2a3579dc3e8cec4803419e22d6449ee76
--END BLOCKS--
"""


import random
from PiStorms import PiStorms
from PiStorms_GRX import PiStorms_GRX

psm = PiStorms()

grx = PiStorms_GRX()


def leCUI8hutHZI4480Dc():
  psm.screen.fillCircle((random.randint(30, 200)), (random.randint(30, 200)), (random.randint(30, 75)), (255, 0, 0), display = True)
  psm.screen.fillCircle((random.randint(30, 250)), (random.randint(30, 250)), (random.randint(30, 100)), (255, 255, 0), display = True)
  psm.screen.fillCircle((random.randint(30, 300)), (random.randint(30, 300)), (random.randint(30, 60)), (51, 255, 51), display = True)
  psm.screen.fillCircle((random.randint(80, 300)), (random.randint(70, 300)), (random.randint(50, 90)), (51, 204, 255), display = True)
grx.untilKeyPress(leCUI8hutHZI4480Dc)
