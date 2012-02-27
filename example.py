from matplotlib.pylab import gca, figure, plot, subplot, title, xlabel, ylabel, xlim,show
from matplotlib.lines import Line2D
import segment
import fit

def draw_plot(data,plot_title):
    plot(range(len(data)),data,alpha=0.8,color='red')
    title(plot_title)
    xlabel("Samples")
    ylabel("Signal")
    xlim((0,len(data)-1))

def draw_segments(segments):
    ax = gca()
    for segment in segments:
        line = Line2D((segment[0],segment[2]),(segment[1],segment[3]))
        ax.add_line(line)

with open("example_data/16265-normalecg.txt") as f:
    file_lines = f.readlines()

data = [float(x.split("\t")[2].strip()) for x in file_lines[100:320]]

max_error = 0.005

#sliding window with regression
figure()
segments = segment.slidingwindowsegment(data, fit.regression, fit.sumsquared_error, max_error)
draw_plot(data,"Sliding window with regression")
draw_segments(segments)

#bottom-up with regression
figure()
segments = segment.bottomupsegment(data, fit.regression, fit.sumsquared_error, max_error)
draw_plot(data,"Bottom-up with regression")
draw_segments(segments)

#top-down with regression
figure()
segments = segment.topdownsegment(data, fit.regression, fit.sumsquared_error, max_error)
draw_plot(data,"Top-down with regression")
draw_segments(segments)



#sliding window with simple interpolation
figure()
segments = segment.slidingwindowsegment(data, fit.interpolate, fit.sumsquared_error, max_error)
draw_plot(data,"Sliding window with simple interpolation")
draw_segments(segments)

#bottom-up with  simple interpolation
figure()
segments = segment.bottomupsegment(data, fit.interpolate, fit.sumsquared_error, max_error)
draw_plot(data,"Bottom-up with simple interpolation")
draw_segments(segments)

#top-down with  simple interpolation
figure()
segments = segment.topdownsegment(data, fit.interpolate, fit.sumsquared_error, max_error)
draw_plot(data,"Top-down with simple interpolation")
draw_segments(segments)


show()

