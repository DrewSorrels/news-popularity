from plotly import tools

import pandas as pd
import plotly as py
import plotly.graph_objs as go

import sys

N = 1000

df = pd.read_csv(sys.argv[1], sep = ', ', header = 0)

# DATA CHANNEL ANALYSIS
# Filter by data channel
lifestyle = df[df.data_channel_is_lifestyle == 1]
entertainment = df[df.data_channel_is_entertainment == 1]
bus = df[df.data_channel_is_bus == 1]
socmed = df[df.data_channel_is_socmed == 1]
tech = df[df.data_channel_is_tech == 1]
world = df[df.data_channel_is_world == 1]

# Plot median for each type
trace1 = go.Bar(
	x = ['lifestyle', 'entertainment', 'bus', 'socmed', 'tech', 'world'],
	y = [
		lifestyle.shares.median(),
		entertainment.shares.median(),
		bus.shares.median(),
		socmed.shares.median(),
		tech.shares.median(),
		world.shares.median()]
)

data = [trace1]


# WORDS ANALYSIS
trace1 = go.Scatter(x = df.kw_min_max, y = df.shares, mode = 'markers', name = '# words in body vs shares')
trace2 = go.Scatter(x = df.kw_max_max, y = df.shares, mode = 'markers', name = 'imgs vs shares')
trace3 = go.Scatter(x = df.kw_avg_max, y = df.shares, mode = 'markers', name = '# words in title vs shares')
trace4 = go.Scatter(x = df.num_videos, y = df.shares, mode = 'markers', name = 'videos vs shares')

fig = tools.make_subplots(rows=2, cols=2)
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 2, 2)
py.offline.plot(fig, filename='basic-scatter')

# WEEK ANALYSIS
# Filter by day
monday = df[df.weekday_is_monday == 1]
tuesday = df[df.weekday_is_tuesday == 1]
wednesday = df[df.weekday_is_wednesday == 1]
thursday = df[df.weekday_is_thursday == 1]
friday = df[df.weekday_is_friday == 1]
saturday = df[df.weekday_is_saturday == 1]
sunday = df[df.weekday_is_sunday == 1]
weekend = df[df.is_weekend == 1]
weekday = df[df.is_weekend == 0]

trace1_1 = go.Bar(
	x = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],
	y = [
		monday[monday.data_channel_is_lifestyle == 1].shares.median(),
		tuesday[tuesday.data_channel_is_lifestyle == 1].shares.median(),
		wednesday[wednesday.data_channel_is_lifestyle == 1].shares.median(),
		thursday[thursday.data_channel_is_lifestyle == 1].shares.median(),
		friday[friday.data_channel_is_lifestyle == 1].shares.median(),
		saturday[saturday.data_channel_is_lifestyle == 1].shares.median(),
		sunday[sunday.data_channel_is_lifestyle == 1].shares.median()],
	name = 'lifestyle'
)

trace1_2 = go.Bar(
	x = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],
	y = [
		monday[monday.data_channel_is_entertainment == 1].shares.median(),
		tuesday[tuesday.data_channel_is_entertainment == 1].shares.median(),
		wednesday[wednesday.data_channel_is_entertainment == 1].shares.median(),
		thursday[thursday.data_channel_is_entertainment == 1].shares.median(),
		friday[friday.data_channel_is_entertainment == 1].shares.median(),
		saturday[saturday.data_channel_is_entertainment == 1].shares.median(),
		sunday[sunday.data_channel_is_entertainment == 1].shares.median()],
	name = 'entertainment'
)

trace1_3 = go.Bar(
	x = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],
	y = [
		monday[monday.data_channel_is_bus == 1].shares.median(),
		tuesday[tuesday.data_channel_is_bus == 1].shares.median(),
		wednesday[wednesday.data_channel_is_bus == 1].shares.median(),
		thursday[thursday.data_channel_is_bus == 1].shares.median(),
		friday[friday.data_channel_is_bus == 1].shares.median(),
		saturday[saturday.data_channel_is_bus == 1].shares.median(),
		sunday[sunday.data_channel_is_bus == 1].shares.median()],
	name = 'business'
)

trace1_4 = go.Bar(
	x = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],
	y = [
		monday[monday.data_channel_is_socmed == 1].shares.median(),
		tuesday[tuesday.data_channel_is_socmed == 1].shares.median(),
		wednesday[wednesday.data_channel_is_socmed == 1].shares.median(),
		thursday[thursday.data_channel_is_socmed == 1].shares.median(),
		friday[friday.data_channel_is_socmed == 1].shares.median(),
		saturday[saturday.data_channel_is_socmed == 1].shares.median(),
		sunday[sunday.data_channel_is_socmed == 1].shares.median()],
	name = 'socmed'
)

trace1_5 = go.Bar(
	x = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],
	y = [
		monday[monday.data_channel_is_tech == 1].shares.median(),
		tuesday[tuesday.data_channel_is_tech == 1].shares.median(),
		wednesday[wednesday.data_channel_is_tech == 1].shares.median(),
		thursday[thursday.data_channel_is_tech == 1].shares.median(),
		friday[friday.data_channel_is_tech == 1].shares.median(),
		saturday[saturday.data_channel_is_tech == 1].shares.median(),
		sunday[sunday.data_channel_is_tech == 1].shares.median()],
	name = 'tech'
)

trace1_6 = go.Bar(
	x = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],
	y = [
		monday[monday.data_channel_is_world == 1].shares.median(),
		tuesday[tuesday.data_channel_is_world == 1].shares.median(),
		wednesday[wednesday.data_channel_is_world == 1].shares.median(),
		thursday[thursday.data_channel_is_world == 1].shares.median(),
		friday[friday.data_channel_is_world == 1].shares.median(),
		saturday[saturday.data_channel_is_world == 1].shares.median(),
		sunday[sunday.data_channel_is_world == 1].shares.median()],
	name = 'world'
)

trace2 = go.Box(
	y = weekend.shares,
	name = 'Weekend shares',
	boxpoints = 'all',
	jitter=0.3)
trace3 = go.Box(
	y = weekday.shares,
	name = 'Weekday shares',
	boxpoints = 'all',
	jitter=0.3)

fig = tools.make_subplots(rows=2, cols=1)
fig.append_trace(trace1_1, 1, 1)
fig.append_trace(trace1_2, 1, 1)
fig.append_trace(trace1_3, 1, 1)
fig.append_trace(trace1_4, 1, 1)
fig.append_trace(trace1_5, 1, 1)
fig.append_trace(trace1_6, 1, 1)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 2, 1)


py.offline.plot(fig, filename='basic-scatter')