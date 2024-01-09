import swimClub
import hfpy_utils

CHARTS = "charts/"

def produceBarChart(fn):

    swimmer,age,distance,stroke,times, average, alltimes = swimClub.swim_data(fn)  

    title = swimmer + "(Under " + age + ") " + distance + " " + stroke

    header = f"""
    <html><head>
            <title>
                {title}
            </title>
        </head>
        <body>
            <h3>{title}</h3>
            """
    body = ""

    for n,t in enumerate(times):
        bar_width = hfpy_utils.convert2range(alltimes[n], 0, max(alltimes), 0, 350)
        body = body + f"""
            <svg height="30" width="400">
                <rect height="30" width={bar_width} style="fill:rgb(0, 0, 255);"></rect>
            </svg>{t}<br/>"""

    footer = f"""
        <p> Average time: {average}</p>
        </body>
        </html>
        """

    page = header+body+footer

    save_to = f"{CHARTS}{fn.removesuffix('.txt')}.html"

    with open(save_to, "w") as sf:
        print(page, file=sf)

    return save_to



