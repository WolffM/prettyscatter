oneSegment = 0.36
twoSegment = 0.72

colorscale = [[0, '#87CEEB'], [1, '#00008B']]

def addBackgroundGradient(fig):
    fig.update_layout(plot_bgcolor='white')
    fig.update_layout(
        shapes=[
            # 1st highlight during Feb 4th - Feb 6th
            dict(
                type="rect",
                # x-reference is assigned to the x-values
                xref="x",
                # y-reference is assigned to the plot paper [0,1]
                yref="y",
                x0=-.04,
                y0=-.04,
                x1=oneSegment,
                y1=1.04,
                fillcolor=colorscale,
                opacity=0.2,
                layer="below",
                line_width=0,
            ),
            # 2nd highlight during Feb 7th - Feb 10th
            dict(
                type="rect",
                xref="x",
                yref="y",
                x0=twoSegment,
                y0=-.04,
                x1=1.04,
                y1=1.04,
                fillcolor="orange",
                opacity=0.2,
                layer="below",
                line_width=0,
            ),
            # 3rd highlight during Feb 10th - Feb 14th
            dict(
                type="rect",
                xref="x",
                yref="y",
                x0=-.04,
                y0=-.04,
                x1=1.04,
                y1=oneSegment,
                fillcolor="red",
                opacity=0.2,
                layer="below",
                line_width=0,
            ),
            # 4th highlight during Feb 15th - Feb 20th
            dict(
                type="rect",
                xref="x",
                yref="y",
                x0=-.04,
                x1=1.04,
                y0=twoSegment,
                y1=1.04,
                fillcolor="green",
                opacity=0.2,
                layer="below",
                line_width=0,
            ),
        ]
    )
    return fig

def addBackgroundGradient2(fig):
    lineWidth=12
    interval=65
    opaci=.5
    fig.update_layout(plot_bgcolor='whitesmoke')

    #GREEN
    for i in range(interval):
        opac = (i/interval)
        fig.add_shape(
            type='line',
            xref="x",
            yref="y",
            opacity=opaci,
            layer="below",
            x0=-.04,
            x1=1.04,
            y0=i*((oneSegment)/interval)+twoSegment,
            y1=i*((oneSegment)/interval)+twoSegment,
            line=dict(color='rgba({}, {}, {}, {})'.format((76),(255),(109),(opac)),
                    width=lineWidth,))
    #RED
    for i in range(interval):
        opac = 1-(i/interval)
        fig.add_shape(
            type='line',
            xref="x",
            yref="y",
            opacity=opaci,
            layer="below",
            x0=-.04,
            x1=1.04,
            y0=i*((oneSegment)/interval)-0.04,
            y1=i*((oneSegment)/interval)-0.04,
            line=dict(color='rgba({}, {}, {}, {})'.format((222),(84),(108),(opac)),
                    width=lineWidth,))
    #BLUE
    for i in range(interval):
        opac = 1-(i/interval)
        fig.add_shape(
            type='line',
            xref="x",
            yref="y",
            opacity=opaci*0.9,
            layer="below",
            x0=i*(oneSegment/interval)-0.04,
            x1=i*(oneSegment/interval)-0.04,
            y0=-.04,
            y1=1.04,
            line=dict(color='rgba({}, {}, {}, {})'.format((56),(94),(255),(opac)),
                    width=lineWidth,))
    #ORANGE
    for i in range(interval):
        opac = (i/interval)
        fig.add_shape(
            type='line',
            xref="x",
            yref="y",
            opacity=opaci*0.8,
            layer="below",
            x0=i*((oneSegment)/interval)+twoSegment,
            x1=i*((oneSegment)/interval)+twoSegment,
            y0=-.04,
            y1=1.04,
            line=dict(color='rgba({}, {}, {}, {})'.format((245),(180),(105),(opac)),
                    width=lineWidth,))
    return fig